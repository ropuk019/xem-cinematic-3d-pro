# XEM Reality Engine — production operating guide

## Recommended workflow

1. Start with a shot list and a reference breakdown.
2. Build every scene element with Blender Python unless the brief authorizes specific external assets.
3. Render a contact-sheet preview with low samples and reduced resolution.
4. Inspect composition, lighting, material response, focus, motion and continuity.
5. Correct the scene and render again.
6. Render final frames with Cycles, encode with FFmpeg and verify the file.

## First test command

```bash
python scripts/render_blender.py \
  --scene blender/scenes/venetian_lens_commercial.py \
  --output out/venetian-preview.mp4 \
  --engine CYCLES --device CPU --samples 16 \
  --resolution 1280x720 --scale 50 --fps 24 --duration 15 \
  --keep-frames
```

This is a pipeline smoke test, not a final quality setting. It requires Blender and FFmpeg on PATH. The included renderer renders the full requested frame range; on a slow machine, reduce `--duration`, `--fps`, `--samples` and `--scale` for the first test.

## GPU setup

GPU rendering is not automatic merely because a GPU exists. In Blender, open Preferences → System, select the supported backend for the installed GPU and enable the device. Run a small Cycles test render. Then use `--device GPU`. If the backend is unavailable or unstable, use CPU. Keep final render settings realistic for the device's VRAM.

## Troubleshooting

- **Blender not found:** install Blender and add its executable to PATH, or set `BLENDER=/absolute/path/to/blender`.
- **FFmpeg not found:** install FFmpeg and add it to PATH.
- **GPU render fails:** use Blender Preferences to enable a supported backend; retry with CPU to isolate the issue.
- **Out of memory:** lower resolution, samples, texture sizes and subdivision; render shots separately.
- **Slow preview:** use EEVEE Next for blocking or Cycles at 25–50% resolution and 8–24 samples.
- **Black or flat glass:** check material transmission, IOR, thickness, light/reflection environment and dark internal geometry.
- **Weak blind shadows:** check actual slat geometry, Sun direction, angular size and object-to-receiver spacing.
- **Soft hero object:** inspect camera focus target, focal length, aperture and focus distance at the intended hero frame.
- **Flicker:** remove unseeded randomness, stabilize temporal effects and inspect the rendered frame sequence.

## Output honesty

The agent must distinguish among source-code validity, successful scene setup, preview render, visually inspected render and verified final export. Never report a later stage as complete when only an earlier stage has passed.
