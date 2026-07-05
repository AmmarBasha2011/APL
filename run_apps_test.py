import subprocess
import sys
import os
import tempfile

APL = sys.executable
APL_SCRIPT = os.path.join(os.path.dirname(__file__), "apl.py")
APPS_DIR = os.path.dirname(__file__)

tests = {
    "fibonacci": {
        "file": "fibonacci.apl",
        "input": "10\n",
        "expected": ["0, 1, 1, 2, 3, 5, 8, 13, 21, 34"],
    },
    "temperature": {
        "file": "temperature.apl",
        "input": "1\n100\n3\n",
        "expected": ["212.0"],
    },
    "stats": {
        "file": "stats.apl",
        "input": "10\n20\n30\nq\n",
        "expected": ["المتوسط:", "20.0", "الانحراف المعياري:"],
    },
    "guess": {
        "file": "guess.apl",
        "input": "50\n",
        "expected": ["تخمينك:"],
        "timeout": 5,
    },
    "todo": {
        "file": "todo.apl",
        "input": "1\n5\n",
        "expected": ["مدير المهام"],
        "timeout": 5,
    },
    "example": {
        "file": "example.apl",
        "input": "",
        "expected": ["الآلة الحاسبة"],
        "timeout": 5,
    },
}

all_pass = True

for name, cfg in tests.items():
    filepath = os.path.join(APPS_DIR, cfg["file"])
    if not os.path.exists(filepath):
        print(f"  SKIP  {name}: file not found")
        continue
    
    print(f"  TEST  {name}...", end=" ")
    try:
        proc = subprocess.run(
            [APL, APL_SCRIPT, filepath],
            input=cfg["input"].encode("utf-8"),
            capture_output=True,
            timeout=cfg.get("timeout", 10),
        )
        output = (proc.stdout + proc.stderr).decode("utf-8", errors="replace")
        ok = True
        for kw in cfg["expected"]:
            if kw not in output:
                ok = False
                break
        logpath = os.path.join(APPS_DIR, f"test_{name}.log")
        with open(logpath, "w", encoding="utf-8") as lf:
            lf.write(output)
        if ok:
            print("PASS")
        else:
            print("FAIL")
            all_pass = False
    except subprocess.TimeoutExpired:
        print("FAIL (timeout)")
        all_pass = False
    except Exception as e:
        print(f"FAIL (exception)")
        all_pass = False

print()
if all_pass:
    print("All applications passed!")
else:
    print("Some tests failed.")
    sys.exit(1)
