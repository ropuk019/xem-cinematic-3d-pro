#!/usr/bin/env python3
import argparse, json, shutil, subprocess
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument("video"); a=p.parse_args()
f=Path(a.video).resolve()
if not f.exists() or not f.stat().st_size: raise SystemExit("Missing or empty output: "+str(f))
probe=shutil.which("ffprobe")
if not probe:
    print(f"Exists: {f} ({f.stat().st_size} bytes). ffprobe unavailable; metadata not verified.")
else:
    r=subprocess.run([probe,"-v","error","-show_streams","-show_format","-of","json",str(f)],check=True,capture_output=True,text=True)
    d=json.loads(r.stdout)
    print(json.dumps({"path":str(f),"bytes":f.stat().st_size,"format":d.get("format"),"streams":d.get("streams")},indent=2))
