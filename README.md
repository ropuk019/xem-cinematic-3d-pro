# XEM CINEMATIC 3D

A self-authored, cross-platform cinematic 3D skill pack for **Claude Code + OpenCode**. It combines a reusable agent workflow with a working Remotion + React Three Fiber starter.

This is an independent implementation inspired by publicly described cinematic 3D workflows. It is **not** the seller's paid source code and does not contain proprietary assets.

## What is included

- `SKILL.md`: end-to-end art direction, scene construction, rendering, and QC workflow.
- `references/`: practical cinematography, camera, lighting, material, animation, typography, rendering, and QC notes.
- `starter/`: runnable Remotion + React Three Fiber project.
- `scripts/`: environment checks, project bootstrap, preview-frame extraction, and render helpers.
- `examples/`: five scene briefs with implementation notes.
- `PROMPTS.md`: 30 production prompts.

## Requirements

- Node.js 20 LTS or newer (Node 22 LTS is also suitable).
- npm 10+.
- Windows 10/11, macOS, or Linux.
- A Chromium-compatible browser installed by Remotion (the CLI can download its supported browser).
- For GPU acceleration, a working graphics driver. Software rendering may work but can be slow.

No paid API key is required. Rendering is local. Three-dimensional scenes run in Chromium/WebGL; performance depends on the device and driver.

## Quick start

```bash
# 1. Enter the starter
cd starter

# 2. Install dependencies
npm install

# 3. Open Remotion Studio
npm run studio

# 4. Render sample videos
npm run render:product
npm run render:jelly
npm run render:vertical
```

Output files are written to `starter/out/`.

If Remotion asks to install its browser, allow it. On Linux, if Chromium reports missing system libraries, install the packages requested by the error message. On Ubuntu/Debian, common dependencies include `libnss3`, `libatk1.0-0`, `libatk-bridge2.0-0`, `libx11-xcb1`, `libxcomposite1`, `libxdamage1`, `libxrandr2`, `libgbm1`, `libasound2`, and `libgtk-3-0` (package names can vary by release).

## Use as a Claude Code skill

Copy this directory into your user skills directory:

```bash
# Common Claude Code location
mkdir -p ~/.claude/skills
cp -r xem-cinematic-3d ~/.claude/skills/
```

Or place it inside a project's `.claude/skills/` directory. Restart/reopen Claude Code if the skill does not appear.

## Use with OpenCode

OpenCode skill discovery depends on its installed version and configuration. A portable approach is:

1. Keep this folder in your repository, for example `.opencode/skills/xem-cinematic-3d/`.
2. Add a project instruction telling the agent to read `.opencode/skills/xem-cinematic-3d/SKILL.md` for 3D/video tasks.
3. If your OpenCode version supports the Agent Skills convention, put the folder in its configured skills directory.

Do not assume a Claude-specific skill path is automatically scanned by OpenCode.

## Generate a new project

From the pack root:

```bash
node scripts/create-project.js ../my-cinematic-project
```

This copies the starter to the target path. Then:

```bash
cd ../my-cinematic-project
npm install
npm run studio
```

## Render commands

```bash
npm run render:product
npm run render:jelly
npm run render:vertical
npm run still:product
```

You can also call Remotion directly:

```bash
npx remotion render src/index.ts ProductFilm out/product.mp4
```

For a custom composition, change the composition ID to the one registered in `starter/src/Root.tsx`.

## Project structure

```text
xem-cinematic-3d/
├── SKILL.md
├── PROMPTS.md
├── references/
├── examples/
├── scripts/
└── starter/
    ├── src/
    │   ├── Root.tsx
    │   ├── index.ts
    │   ├── scenes/
    │   └── styles/
    ├── package.json
    └── remotion.config.ts
```

## Troubleshooting

- **Node cannot load a shared library:** use a supported Node build for your OS and install the missing system library. On Ubuntu, `libatomic1` may be required by some Node distributions.
- **Black WebGL canvas:** update GPU drivers; try a normal desktop session; check Chromium WebGL support. Headless GPU availability varies by machine.
- **Slow renders:** lower `width`, `height`, `fps`, geometry detail, shadow map size, and particle count for previews.
- **Font/text differences:** bundle a licensed local font and use the same font in preview and render environments.
- **OpenCode does not discover the skill:** explicitly reference `SKILL.md` in project instructions or configure the skill directory supported by your OpenCode version.

## License

The authored code and documentation in this pack are provided under the MIT License. Third-party dependencies retain their own licenses. Any models, fonts, textures, audio, or images you add must be appropriately licensed.
