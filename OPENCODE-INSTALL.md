# OpenCode install and configure

After pushing this repository to GitHub, give OpenCode the following instruction (replace the username):

```text
Clone https://github.com/YOUR_GITHUB_USERNAME/xem-cinematic-3d-pro into ~/tools/xem-cinematic-3d-pro.
Read OPENCODE-INSTALL.md and SKILL.md completely.
Inspect my OS, CPU, RAM, Node, npm, Python, Blender, FFmpeg, GPU, VRAM and render support.
Do not overwrite existing configs, projects or skill directories.
Configure this skill using the Agent Skills discovery method supported by my installed OpenCode version. If native discovery is unavailable, add a project-level instruction that explicitly reads ~/tools/xem-cinematic-3d-pro/SKILL.md for all 3D/video tasks.
Install only required dependencies. Read references/code-first-photorealism.md. Run the environment checks and a low-quality Cycles preview of blender/scenes/venetian_lens_commercial.py. Extract and visually inspect representative frames; fix actual defects and rerender. Do not attempt a 4K/full-sample render until the preview is approved.
Inspect representative output frames and report exact paths, renderer, settings and any missing capabilities.
Do not say installation or testing succeeded unless the skill is discoverable/readable and the sample render is verified.
```

## Portable fallback
Keep this repository in a stable path, then add project instructions:

```text
For all 3D scene, product-film, motion-graphics and video requests:
1. Read ~/tools/xem-cinematic-3d-pro/SKILL.md.
2. Read relevant files under references/.
3. Choose Blender Cycles/EEVEE, Remotion Three.js or hybrid mode.
4. Use the included Blender scene and render scripts where suitable.
5. Default to code-generated Blender scenes and Cycles for photorealistic CGI; use Three.js/Remotion for web-native 3D, titles and composition.
5. Render a low-quality preview, inspect it, fix defects and render final.
6. Verify the output file before reporting success.
```

## Linux
Ubuntu/Debian:
```bash
sudo apt update
sudo apt install -y ffmpeg python3
```
Install Blender 4.x or newer from a trusted source and ensure `blender` is on PATH. Install Node.js 20+ and npm 10+. If Node reports `libatomic.so.1` missing, install `libatomic1`.

## Windows
Install Blender, Node.js LTS and FFmpeg. Add their executable folders to PATH, reopen the terminal, then verify `blender --version`, `node --version`, `npm --version`, `ffmpeg -version`.

## macOS
Install Blender, Node LTS and FFmpeg. Verify CLI paths. On Apple Silicon, test the Metal backend with a real render.

## GPU warning
A GPU existing in the computer does not mean Cycles GPU rendering is configured. Check Blender Preferences > System, choose a supported backend, and run a test render. CPU rendering remains a fallback but may be slow.
