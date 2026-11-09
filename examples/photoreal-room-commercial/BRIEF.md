# Photorealistic room / product commercial

**Goal:** a 15-second code-generated cinematic commercial with a warm late-afternoon interior, real Venetian-blind shadows and a macro product reveal.

**Reference language:** natural live-action product cinematography, warm wood, controlled highlights, soft room bounce, shallow but readable depth of field.

**Procedural requirements:** construct room shell, desk, window, blinds, laptop, keyboard, screen typography, coffee cup, notebook and hero lens with Blender Python. No stock footage or downloaded scene models.

**Shot beats:** wide room/desk establishing view; slow push toward the desk; transition to macro lens details; final lens hero frame.

**Lighting:** directional Sun through actual slat geometry, warm bounce, restrained cool fill and a shaped rim strip on the lens.

**Render:** Cycles; preview at 45% resolution / 24 samples; final at 100% / 96–128 samples with denoising as hardware allows.

**Starter implementation:** `../../blender/scenes/venetian_lens_commercial.py`.
