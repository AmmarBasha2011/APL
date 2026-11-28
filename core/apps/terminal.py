"""APL Terminal: an ordinary terminal that reads and writes Arabic properly.

It is a plain command terminal, not the APL REPL: whatever you type runs in the
system shell (cmd on Windows, sh on Linux), so `dir`, `ls`, `cd`, `python` and
`عمار شغل برنامج.apl` all work. The window is a local browser page, because a
browser lays out Arabic (shaping and right-to-left) correctly where many
console windows do not. Programs that read input get a line at a time.
Full-screen programs such as vim are not supported.
"""
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

from core.apps import common, web

BODY = """<style>#t{height:70vh;overflow:auto;background:#050d0a;border:1px solid var(--line);border-radius:12px;padding:12px;white-space:pre-wrap;word-break:break-word;direction:ltr;unicode-bidi:plaintext;text-align:start;font-family:Consolas,'Cascadia Code',monospace}
#l{display:flex;gap:8px;margin-top:10px}#c{flex:1;direction:auto;font-family:Consolas,monospace}.p{color:var(--g);direction:ltr;unicode-bidi:isolate}</style>
<div id="t"></div><form id="l"><span class="p" id="cwd"></span><input id="c" autocomplete="off" autofocus placeholder="اكتب أمر واضغط Enter"><button>تشغيل</button></form>"""

SCRIPT = """<script>
const t=document.getElementById('t'),c=document.getElementById('c'),cw=document.getElementById('cwd');
let id=null,hist=[],hp=0;
function add(s){t.textContent+=s;t.scrollTop=t.scrollHeight}
async function api(p,b){const r=await fetch(p,{method:'POST',body:JSON.stringify(b||{})});return r.json()}
async function poll(){if(id===null)return;const d=await api('/api/read',{id});add(d.out);if(d.cwd)cw.textContent=d.cwd+' $';
if(d.done){id=null;add('\\n');}else setTimeout(poll,120)}
document.getElementById('l').onsubmit=async e=>{e.preventDefault();const v=c.value;c.value='';
if(id!==null){add(v+'\\n');await api('/api/send',{id,text:v});return}
hist.push(v);hp=hist.length;add(cw.textContent+' '+v+'\\n');if(!v.trim())return;
if(v.trim()==='clear'||v.trim()==='cls'){t.textContent='';return}
const d=await api('/api/start',{cmd:v});id=d.id;cw.textContent=d.cwd+' $';poll()};
c.onkeydown=e=>{if(e.key==='ArrowUp'&&hp>0){c.value=hist[--hp];e.preventDefault()}else if(e.key==='ArrowDown'&&hp<hist.length){c.value=hist[++hp]||'';e.preventDefault()}};
api('/api/cwd').then(d=>cw.textContent=d.cwd+' $');
</script>"""


class Session:
    def __init__(self):
        self.cwd = os.getcwd()
        self.jobs = {}
        self.counter = 0
        self.lock = threading.Lock()

    def start(self, cmd):
        stripped = cmd.strip()
        self.counter += 1
        job_id = self.counter
        job = {"buf": [], "done": False, "proc": None, "lock": threading.Lock()}
        self.jobs[job_id] = job
        if stripped == "cd" or stripped.startswith("cd ") or stripped.lower().startswith("cd\t"):
            target = stripped[2:].strip().strip('"') or str(Path.home())
            path = Path(os.path.expanduser(target))
            path = path if path.is_absolute() else Path(self.cwd) / path
            if path.is_dir():
                self.cwd = str(path.resolve())
            else:
                job["buf"].append("المجلد مش موجود: %s\n" % target)
            job["done"] = True
            return job_id
        if sys.platform == "win32":
            cmd = "chcp 65001 >nul & " + cmd  # cmd prints Arabic in UTF-8
        try:
            proc = subprocess.Popen(cmd, shell=True, cwd=self.cwd, stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    env=common.child_env())
        except OSError as error:
            job["buf"].append("تعذر التشغيل: %s\n" % error)
            job["done"] = True
            return job_id
        job["proc"] = proc

        def pump():
            import codecs
            decoder = codecs.getincrementaldecoder("utf-8")("replace")
            while True:
                chunk = proc.stdout.read1(4096) if hasattr(proc.stdout, "read1") else proc.stdout.read(1)
                if not chunk:
                    break
                with job["lock"]:
                    job["buf"].append(decoder.decode(chunk))
            proc.wait()
            with job["lock"]:
                if proc.returncode:
                    job["buf"].append("\n[كود الخروج %s]" % proc.returncode)
                job["done"] = True

        threading.Thread(target=pump, daemon=True).start()
        return job_id

    def read(self, job_id):
        job = self.jobs.get(job_id)
        if job is None:
            return {"out": "", "done": True, "cwd": self.cwd}
        with job["lock"]:
            out, job["buf"] = "".join(job["buf"]), []
            done = job["done"]
        if done:
            self.jobs.pop(job_id, None)
        return {"out": out, "done": done, "cwd": self.cwd}

    def send(self, job_id, text):
        job = self.jobs.get(job_id)
        if job and job["proc"] and job["proc"].poll() is None:
            try:
                job["proc"].stdin.write((text + "\n").encode("utf-8"))
                job["proc"].stdin.flush()
            except OSError:
                pass

    def stop(self):
        for job in self.jobs.values():
            if job["proc"] and job["proc"].poll() is None:
                job["proc"].kill()


def run(argv):
    import json
    session = Session()

    def routes(handler, method, path, query, body):
        if path == "/":
            return 200, "text/html; charset=utf-8", web.page("APL Terminal", BODY, "", SCRIPT).encode("utf-8")
        data = json.loads(body.decode("utf-8") or "{}") if body else {}
        if path == "/api/cwd":
            return 200, "application/json", web.json_bytes({"cwd": session.cwd})
        if path == "/api/start":
            job_id = session.start(str(data.get("cmd", "")))
            return 200, "application/json", web.json_bytes({"id": job_id, "cwd": session.cwd})
        if path == "/api/read":
            return 200, "application/json", web.json_bytes(session.read(data.get("id")))
        if path == "/api/send":
            session.send(data.get("id"), str(data.get("text", "")))
            return 200, "application/json", b"{}"
        return 404, "text/plain; charset=utf-8", b"not found"

    _, url = web.serve(routes, "APL Terminal", block=False)
    web.open_browser(url)
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        pass
    finally:
        session.stop()
    return 0
