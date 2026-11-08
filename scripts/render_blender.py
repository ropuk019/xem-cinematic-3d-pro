#!/usr/bin/env python3
import argparse, os, shutil, subprocess, sys
from pathlib import Path

def run(cmd): print("+"," ".join(map(str,cmd)),flush=True); subprocess.run(cmd,check=True)
def main():
    p=argparse.ArgumentParser(description="Render Blender scene and encode MP4")
    p.add_argument("--scene",required=True); p.add_argument("--output",required=True)
    p.add_argument("--engine",choices=["BLENDER_EEVEE_NEXT","CYCLES"],default="BLENDER_EEVEE_NEXT")
    p.add_argument("--samples",type=int,default=64); p.add_argument("--resolution",default="1920x1080")
    p.add_argument("--fps",type=int,default=30); p.add_argument("--duration",type=float,default=8)
    p.add_argument("--denoise",action="store_true"); p.add_argument("--blender",default=os.environ.get("BLENDER","blender"))
    p.add_argument("--keep-frames",action="store_true"); a=p.parse_args()
    blender=shutil.which(a.blender) or (a.blender if Path(a.blender).exists() else None)
    ffmpeg=shutil.which("ffmpeg")
    if not blender: sys.exit("Blender not found; install it or set BLENDER=/path/to/blender")
    if not ffmpeg: sys.exit("FFmpeg not found; install it and add it to PATH")
    try: w,h=map(int,a.resolution.lower().split("x"))
    except: sys.exit("--resolution must be WIDTHxHEIGHT")
    if min(w,h,a.fps)<=0 or a.duration<=0: sys.exit("Resolution, fps and duration must be positive")
    scene_path=Path(a.scene).resolve(); output=Path(a.output).resolve(); output.parent.mkdir(parents=True,exist_ok=True)
    frames=output.parent/(output.stem+"_frames"); frames.mkdir(parents=True,exist_ok=True)
    blend=frames/"scene.blend"; prefix=frames/"frame_"; end=max(1,round(a.duration*a.fps))
    setup=frames/"setup.py"
    setup.write_text(f'''
import bpy, runpy
runpy.run_path(r"{scene_path.as_posix()}",run_name="__main__")
s=bpy.context.scene
s.render.engine="{a.engine}"
s.render.resolution_x={w}; s.render.resolution_y={h}; s.render.resolution_percentage=100
s.render.fps={a.fps}; s.frame_start=1; s.frame_end={end}
s.render.image_settings.file_format="PNG"; s.render.filepath=r"{prefix.as_posix()}"
if "{a.engine}"=="CYCLES":
 s.cycles.samples={a.samples}; s.cycles.use_denoising={str(a.denoise)}
bpy.ops.wm.save_as_mainfile(filepath=r"{blend.as_posix()}")
''',encoding="utf-8")
    run([blender,"-b","--python",str(setup)])
    run([blender,"-b",str(blend),"-a"])
    run([ffmpeg,"-y","-framerate",str(a.fps),"-i",str(frames/"frame_%04d.png"),
         "-c:v","libx264","-pix_fmt","yuv420p","-crf","17","-movflags","+faststart",str(output)])
    if not output.exists() or output.stat().st_size==0: sys.exit("Output missing or empty after render")
    print(f"SUCCESS {output} ({output.stat().st_size} bytes)")
    if not a.keep_frames: shutil.rmtree(frames,ignore_errors=True)
if __name__=="__main__": main()
