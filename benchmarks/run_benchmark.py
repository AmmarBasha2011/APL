#!/usr/bin/env python3
"""مقارنة قابلة لإعادة التشغيل بين APL وPython العادي، بلا مكتبات خارجية."""

from __future__ import annotations

import argparse
import json
import math
import os
import platform
import random
import statistics
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
APL_FILE = ROOT / "benchmarks" / "workload.apl"
PYTHON_FILE = ROOT / "benchmarks" / "workload_python.py"
APL_ENTRY_MARKER = "# تشغيل مباشر"
PYTHON_ENTRY_MARKER = "# تشغيل مباشر"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.apl_runner.main import transpile  # noqa: E402


def positive_int(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("يجب أن يكون العدد أكبر من صفر")
    return number


def percentile(values: List[float], quantile: float) -> float:
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil(quantile * len(ordered)) - 1))
    return ordered[index]


def summarize(samples_ms: List[float]) -> Dict[str, object]:
    return {
        "median_ms": round(statistics.median(samples_ms), 6),
        "mean_ms": round(statistics.mean(samples_ms), 6),
        "min_ms": round(min(samples_ms), 6),
        "max_ms": round(max(samples_ms), 6),
        "p95_ms": round(percentile(samples_ms, 0.95), 6),
        "stdev_ms": round(statistics.stdev(samples_ms), 6) if len(samples_ms) > 1 else 0.0,
        "samples_ms": [round(sample, 6) for sample in samples_ms],
    }


def split_sources() -> Tuple[str, str]:
    apl_source = APL_FILE.read_text(encoding="utf-8")
    python_source = PYTHON_FILE.read_text(encoding="utf-8")
    if APL_ENTRY_MARKER not in apl_source:
        raise RuntimeError("تعذّر العثور على علامة التشغيل في ملف APL")
    if PYTHON_ENTRY_MARKER not in python_source:
        raise RuntimeError("تعذّر العثور على علامة التشغيل في ملف Python")
    apl_definition = apl_source.split(APL_ENTRY_MARKER, 1)[0].rstrip() + "\n"
    python_definition = python_source.split(PYTHON_ENTRY_MARKER, 1)[0].rstrip() + "\n"
    return apl_definition, python_definition


def load_workload_functions(
    apl_definition: str, python_definition: str
) -> Tuple[Callable[[int], int], Callable[[int], int]]:
    generated = transpile(apl_definition)
    apl_namespace: Dict[str, object] = {"__name__": "apl_benchmark"}
    exec(compile(generated, str(APL_FILE), "exec"), apl_namespace)
    apl_function = apl_namespace.get("احسب")
    if not callable(apl_function):
        raise RuntimeError("لم ينتج المترجم دالة احسب في برنامج APL")

    python_namespace: Dict[str, object] = {"__name__": "python_benchmark"}
    exec(compile(python_definition, str(PYTHON_FILE), "exec"), python_namespace)
    python_function = python_namespace.get("calculate")
    if not callable(python_function):
        raise RuntimeError("لم تُعرّف دالة calculate في برنامج Python")
    return apl_function, python_function


def benchmark_execution(
    apl_function: Callable[[int], int],
    python_function: Callable[[int], int],
    iterations: int,
    runs: int,
    warmups: int,
    seed: int,
) -> Tuple[Dict[str, object], Dict[str, int]]:
    expected = python_function(iterations)
    apl_checksum = apl_function(iterations)
    if apl_checksum != expected:
        raise RuntimeError(
            "فشل التحقق: نتيجة APL لا تطابق نتيجة Python "
            f"({apl_checksum!r} != {expected!r})"
        )

    for _ in range(warmups):
        apl_function(iterations)
        python_function(iterations)

    samples: Dict[str, List[float]] = {"apl": [], "python": []}
    rng = random.Random(seed)
    for _ in range(runs):
        order = ["apl", "python"]
        rng.shuffle(order)
        for name in order:
            function = apl_function if name == "apl" else python_function
            started = time.perf_counter_ns()
            checksum = function(iterations)
            elapsed_ms = (time.perf_counter_ns() - started) / 1_000_000
            if checksum != expected:
                raise RuntimeError(f"تغيّرت نتيجة {name} أثناء القياس")
            samples[name].append(elapsed_ms)

    apl_stats = summarize(samples["apl"])
    python_stats = summarize(samples["python"])
    python_median = float(python_stats["median_ms"])
    return (
        {
            "unit": "ms",
            "runs_per_language": runs,
            "warmups_per_language": warmups,
            "apl": apl_stats,
            "python": python_stats,
            "apl_over_python": round(float(apl_stats["median_ms"]) / python_median, 6),
        },
        {"apl": int(apl_checksum), "python": int(expected)},
    )


def benchmark_setup(
    apl_definition: str, python_definition: str, runs: int, seed: int
) -> Dict[str, object]:
    """قياس ترجمة APL مع compile مقابل compile لشفرة Python مباشرة."""

    def prepare_apl() -> None:
        translated = transpile(apl_definition)
        compile(translated, str(APL_FILE), "exec")

    def prepare_python() -> None:
        compile(python_definition, str(PYTHON_FILE), "exec")

    # أول مرور يحمّل أنماط المكتبات المطلوبة؛ القياس هنا لمحرك دافئ.
    prepare_apl()
    prepare_python()
    samples: Dict[str, List[float]] = {"apl": [], "python": []}
    rng = random.Random(seed + 1)
    for _ in range(runs):
        order = ["apl", "python"]
        rng.shuffle(order)
        for name in order:
            prepare = prepare_apl if name == "apl" else prepare_python
            started = time.perf_counter_ns()
            prepare()
            samples[name].append((time.perf_counter_ns() - started) / 1_000_000)

    apl_stats = summarize(samples["apl"])
    python_stats = summarize(samples["python"])
    return {
        "unit": "ms",
        "runs_per_language": runs,
        "description": "APL transpile + Python compile مقابل Python compile فقط؛ محرك دافئ",
        "apl": apl_stats,
        "python": python_stats,
        "apl_over_python": round(
            float(apl_stats["median_ms"]) / float(python_stats["median_ms"]), 6
        ),
    }


def run_child(command: List[str], env: Dict[str, str], expected: int) -> None:
    completed = subprocess.run(
        command,
        cwd=str(ROOT),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "فشل أمر فرعي:\n"
            + " ".join(command)
            + "\n"
            + completed.stderr[-3000:]
        )
    lines = [line.strip().replace("\u202b", "").replace("\u202c", "")
             for line in completed.stdout.splitlines() if line.strip()]
    if not lines or lines[-1] != str(expected):
        raise RuntimeError(
            "لم يطبع البرنامج النتيجة المتوقعة. "
            f"المتوقع={expected!r}، stdout={completed.stdout[-1000:]!r}، "
            f"stderr={completed.stderr[-1000:]!r}"
        )


def benchmark_processes(
    apl_definition: str,
    python_definition: str,
    iterations: int,
    runs: int,
    expected: int,
    seed: int,
) -> Dict[str, object]:
    """قياس تشغيل الملفات من الصدفة، متضمناً بدء المفسّر ومكوّنات APL."""
    apl_source = apl_definition + "\nاطبع احسب(" + str(iterations) + ")\n"
    python_source = (
        python_definition
        + "\nif __name__ == \"__main__\":\n"
        + "    print(calculate(" + str(iterations) + "))\n"
    )
    python_executable = sys.executable
    samples: Dict[str, List[float]] = {
        "python": [],
        "apl_uncached": [],
        "apl_cached": [],
    }

    with tempfile.TemporaryDirectory(prefix="apl-benchmark-") as directory:
        temp_dir = Path(directory)
        apl_path = temp_dir / "workload.apl"
        python_path = temp_dir / "workload.py"
        apl_path.write_text(apl_source, encoding="utf-8")
        python_path.write_text(python_source, encoding="utf-8")
        commands = {
            "python": [python_executable, str(python_path)],
            "apl_uncached": [python_executable, str(ROOT / "apl.py"), str(apl_path)],
            "apl_cached": [python_executable, str(ROOT / "apl.py"), str(apl_path)],
        }

        base_env = os.environ.copy()
        base_env["PYTHONHASHSEED"] = "0"
        base_env["PYTHONIOENCODING"] = "utf-8"

        warm_env = base_env.copy()
        warm_env.pop("APL_NO_CACHE", None)
        # تهيئة الذاكرة خارج التوقيت كي تمثل القياسات اللاحقة التشغيل الدافئ.
        run_child(commands["apl_cached"], warm_env, expected)

        rng = random.Random(seed + 2)
        order = ["python", "apl_uncached", "apl_cached"]
        for _ in range(runs):
            rng.shuffle(order)
            for name in order:
                env = base_env.copy()
                if name == "apl_uncached":
                    env["APL_NO_CACHE"] = "1"
                else:
                    env.pop("APL_NO_CACHE", None)
                started = time.perf_counter_ns()
                run_child(commands[name], env, expected)
                samples[name].append((time.perf_counter_ns() - started) / 1_000_000)

    python_stats = summarize(samples["python"])
    uncached_stats = summarize(samples["apl_uncached"])
    cached_stats = summarize(samples["apl_cached"])
    python_median = float(python_stats["median_ms"])
    return {
        "unit": "ms",
        "runs_per_mode": runs,
        "description": "زمن العملية كاملة: بدء Python + تحميل البرنامج + تنفيذه",
        "python": python_stats,
        "apl_uncached": uncached_stats,
        "apl_cached": cached_stats,
        "apl_uncached_over_python": round(
            float(uncached_stats["median_ms"]) / python_median, 6
        ),
        "apl_cached_over_python": round(
            float(cached_stats["median_ms"]) / python_median, 6
        ),
    }


def cpu_name() -> str:
    name = platform.processor().strip()
    if name:
        return name
    if sys.platform.startswith("linux"):
        try:
            for line in Path("/proc/cpuinfo").read_text(encoding="utf-8").splitlines():
                if line.lower().startswith("model name"):
                    return line.split(":", 1)[1].strip()
        except OSError:
            pass
    return platform.machine() or "غير متاح"


def build_report(args: argparse.Namespace) -> Dict[str, object]:
    apl_definition, python_definition = split_sources()
    apl_function, python_function = load_workload_functions(apl_definition, python_definition)

    execution, checksums = benchmark_execution(
        apl_function,
        python_function,
        args.iterations,
        args.runs,
        args.warmups,
        args.seed,
    )
    setup = benchmark_setup(
        apl_definition, python_definition, args.setup_runs, args.seed
    )
    processes = benchmark_processes(
        apl_definition,
        python_definition,
        args.iterations,
        args.process_runs,
        checksums["python"],
        args.seed,
    )

    return {
        "schema_version": 1,
        "project": "APL — Ammar Programming Language",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "environment": {
            "python_version": platform.python_version(),
            "implementation": platform.python_implementation(),
            "operating_system": platform.platform(),
            "cpu": cpu_name(),
            "logical_cores": os.cpu_count(),
        },
        "settings": {
            "iterations_per_sample": args.iterations,
            "execution_runs_per_language": args.runs,
            "warmups_per_language": args.warmups,
            "setup_runs_per_language": args.setup_runs,
            "process_runs_per_mode": args.process_runs,
            "random_seed": args.seed,
            "operation": "sum((i * i) % 97 for i in range(iterations))",
        },
        "validation": {
            "apl_checksum": checksums["apl"],
            "python_checksum": checksums["python"],
            "matches": checksums["apl"] == checksums["python"],
        },
        "results": {
            "execution": execution,
            "setup": setup,
            "process": processes,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="قياس منصف وقابل للتكرار لأداء APL مقابل Python العادي."
    )
    parser.add_argument(
        "--iterations", type=positive_int, default=1_000_000,
        help="عدد دورات الحلقة في كل عينة (الافتراضي: 1000000)",
    )
    parser.add_argument(
        "--runs", type=positive_int, default=100,
        help="عدد عينات تنفيذ الحلقة لكل لغة (الافتراضي: 100)",
    )
    parser.add_argument(
        "--warmups", type=positive_int, default=3,
        help="عدد مرات الإحماء لكل لغة (الافتراضي: 3)",
    )
    parser.add_argument(
        "--setup-runs", type=positive_int, default=25,
        help="عينات قياس الترجمة/التحضير (الافتراضي: 25)",
    )
    parser.add_argument(
        "--process-runs", type=positive_int, default=7,
        help="عينات تشغيل الملف لكل وضع (الافتراضي: 7)",
    )
    parser.add_argument(
        "--seed", type=int, default=20261002,
        help="بذرة ترتيب العينات (الافتراضي: 20261002)",
    )
    parser.add_argument(
        "--output", type=Path,
        help="حفظ التقرير بصيغة JSON في هذا المسار (اختياري)",
    )
    args = parser.parse_args()

    report = build_report(args)
    serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
        print("حُفظ تقرير JSON في: " + str(args.output), file=sys.stderr)
    sys.stdout.write(serialized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
