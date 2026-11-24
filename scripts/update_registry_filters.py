import ast,base64,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'core/libraries/registry.json';entries=json.loads(p.read_text())
for e in entries:
 if not e['substitute']:continue
 tree=ast.parse((ROOT/'core/libraries'/(e['module']+'.py')).read_text());keys=set()
 for node in tree.body:
  if isinstance(node,ast.Assign) and isinstance(node.value,ast.Dict):
   for k in node.value.keys:
    if isinstance(k,ast.Constant) and isinstance(k.value,str):keys.add(k.value)
 size=max(128,len(keys)*16);size=(size+7)//8*8;bits=bytearray(size//8)
 for key in keys:
  digest=hashlib.blake2b(key.encode(),digest_size=16).digest()
  for off in (0,4,8):
   n=int.from_bytes(digest[off:off+4],'little')%size;bits[n//8]|=1<<(n%8)
 e['token_filter']=base64.b64encode(bits).decode()
text=json.dumps(entries,ensure_ascii=False,indent=2)+'\n'
if '--check' in sys.argv:
 if p.read_text() != text: raise SystemExit('Registry filters are stale')
else:
 p.write_text(text)
