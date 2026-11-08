# Rendering and performance

## Preview-first
Render low-resolution previews before final quality. Use a short test composition to validate fonts, WebGL, asset loading, and browser support.

## Performance
- Reuse geometry and materials.
- Use instancing for repeated meshes.
- Reduce shadow map resolution for previews.
- Avoid unnecessary transparent layers and overdraw.
- Keep polygon counts appropriate to output resolution.
- Limit post-processing passes.

## Output
Confirm codec, dimensions, fps, duration, and output file size. Remotion's CLI syntax can change; inspect `npx remotion render --help` when needed.
