#!/usr/bin/env python3
import argparse, shutil, subprocess
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument("video"); p.add_argument("--output",default="preview-frames"); p.add_argument("--fps",default="1/2"); a=p.parse_args()
ff=shutil.which("ffmpeg")
if not ff: raise SystemExit("ffmpeg not found")
out=Path(a.output); out.mkdir(parents=True,exist_ok=True)
subprocess.run([ff,"-y","-i",a.video,"-vf",f"fps={a.fps},scale=960:-1",str(out/"frame-%03d.jpg")],check=True)
print("Frames:",out.resolve())
