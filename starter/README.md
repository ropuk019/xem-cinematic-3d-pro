# Starter project notes

The starter intentionally uses simple generated geometry so it runs without downloading models or fonts. The "product" is a fictional generic device, not a real brand. The jelly-title sample uses glossy rounded forms as a dependency-free visual placeholder rather than claiming to be true extruded typography.

To add a real 3D model, place a licensed `.glb` in `public/models/` and load it with `GLTFLoader` or `@react-three/drei`'s `useGLTF`. Bundle fonts locally for reproducible 3D typography.

The `VerticalAd` composition is a layout starter; replace placeholder copy with the user's approved headline and offer. Verify composition framing after changes.
