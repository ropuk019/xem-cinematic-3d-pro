#!/usr/bin/env python3
"""Render a procedural Blender scene and encode its PNG sequence to H.264 MP4."""
import argparse, os, shutil, subprocess, sys
from pathlib import Path

def run(cmd):
    print('+', ' '.join(map(str, cmd)), flush=True)
    subprocess.run(cmd, check=True)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scene', required=True, help='Python scene file; it must build the scene when executed')
    p.add_argument('--output', required=True, help='Output MP4 path')
    p.add_argument('--engine', choices=['CYCLES','BLENDER_EEVEE_NEXT'], default='CYCLES')
    p.add_argument('--device', choices=['CPU','GPU'], default='CPU', help='GPU must already be enabled in Blender preferences')
    p.add_argument('--samples', type=int, default=96)
    p.add_argument('--resolution', default='1920x1080')
    p.add_argument('--scale', type=int, default=100, help='Render resolution percentage; use 35-50 for previews')
    p.add_argument('--fps', type=int, default=30)
    p.add_argument('--duration', type=float, default=8)
    p.add_argument('--no-denoise', action='store_true')
    p.add_argument('--blender', default=os.environ.get('BLENDER','blender'))
    p.add_argument('--keep-frames', action='store_true')
    p.add_argument('--crf', type=int, default=17, help='H.264 quality; lower is higher quality')
    a=p.parse_args()
    blender=shutil.which(a.blender) or (a.blender if Path(a.blender).exists() else None)
    ffmpeg=shutil.which('ffmpeg')
    if not blender: sys.exit('Blender not found; install it or set BLENDER=/path/to/blender')
    if not ffmpeg: sys.exit('FFmpeg not found; install it and add it to PATH')
    try: w,h=map(int,a.resolution.lower().split('x'))
    except ValueError: sys.exit('--resolution must be WIDTHxHEIGHT, e.g. 1920x1080')
    if min(w,h,a.fps,a.samples,a.scale)<=0 or a.duration<=0: sys.exit('Resolution, fps, samples, scale and duration must be positive')
    scene_path=Path(a.scene).resolve()
    if not scene_path.is_file(): sys.exit(f'Scene file not found: {scene_path}')
    output=Path(a.output).resolve(); output.parent.mkdir(parents=True,exist_ok=True)
    frames=output.parent/(output.stem+'_frames'); frames.mkdir(parents=True,exist_ok=True)
    blend=frames/'scene.blend'; prefix=frames/'frame_'; end=max(1,round(a.duration*a.fps))
    setup=frames/'setup.py'
    setup.write_text(f'''\nimport bpy, runpy\nrunpy.run_path(r"{scene_path.as_posix()}",run_name="__main__")\ns=bpy.context.scene\ns.render.engine="{a.engine}"\ns.render.resolution_x={w}; s.render.resolution_y={h}; s.render.resolution_percentage={a.scale}\ns.render.fps={a.fps}; s.frame_start=1; s.frame_end={end}\ns.render.image_settings.file_format="PNG"; s.render.filepath=r"{prefix.as_posix()}"\nif "{a.engine}"=="CYCLES":\n s.cycles.samples={a.samples}; s.cycles.use_denoising={not a.no_denoise!r}; s.cycles.device="{a.device}"\n if "{a.device}"=="GPU":\n  prefs=bpy.context.preferences.addons.get("cycles")\n  if prefs:\n   try:\n    prefs.preferences.get_devices()\n    for device in prefs.preferences.devices: device.use=True\n   except Exception as exc: print("GPU preference check:",exc)\nbpy.ops.wm.save_as_mainfile(filepath=r"{blend.as_posix()}")\n''',encoding='utf-8')
    try:
        run([blender,'-b','--python',str(setup)])
        run([blender,'-b',str(blend),'-a'])
        run([ffmpeg,'-y','-framerate',str(a.fps),'-i',str(frames/'frame_%04d.png'),'-c:v','libx264','-preset','medium','-crf',str(a.crf),'-pix_fmt','yuv420p','-movflags','+faststart',str(output)])
    except subprocess.CalledProcessError as exc:
        sys.exit(f'RENDER FAILED: command exited with status {exc.returncode}. Frames retained at {frames}')
    if not output.exists() or output.stat().st_size==0: sys.exit('Output missing or empty after render')
    print(f'SUCCESS {output} ({output.stat().st_size} bytes)')
    if not a.keep_frames: shutil.rmtree(frames,ignore_errors=True)

if __name__=='__main__': main()
