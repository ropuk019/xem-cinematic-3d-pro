# 30 XEM CINEMATIC 3D production prompts

Use these as briefs. Replace bracketed details with the user's actual product, logo, copy, colors, and delivery specs. Do not invent brand claims.

## Product films
1. **Luxury hero turntable:** Create a 10-second premium studio film of [product]. Begin in silhouette, reveal the product with a soft moving key, perform a controlled 180-degree camera orbit, and finish on a clean hero frame. 16:9, 30 fps.
2. **Macro material study:** Show three macro passes across [product], emphasizing [material]. Use shallow depth of field, slow dolly motion, and restrained specular highlights.
3. **Floating assembly:** Separate [product] into 4–6 components, hold each component in a clean exploded arrangement, then reassemble with precise easing. Preserve believable alignment.
4. **Monochrome campaign:** Render [product] and set in a single-color studio environment. Use tonal separation, one rim light, and a restrained shadow.
5. **Liquid reveal:** Reveal [product] through a stylized liquid-metal or translucent-fluid transition. Keep the product itself readable and avoid simulating unsafe real-world behavior.

## 3D typography
6. **Inflated wordmark:** Create the word “[TEXT]” as rounded, inflated 3D lettering with soft reflections, controlled highlights, and a slow camera push. Keep spelling exact.
7. **Chrome title:** Extruded chrome typography on a dark studio stage, with a moving strip light reflected across the letters.
8. **Soft clay lettering:** Rounded clay-like letters, pastel palette, broad soft shadows, gentle bounce, and a minimal background.
9. **Kinetic type sequence:** Animate [TEXT] in three typographic beats: assemble, hero hold, and resolve. Maintain legibility at mobile scale.
10. **Glass title:** Create translucent glass lettering with realistic edge highlights and a contrasting matte backdrop. Avoid low-contrast text.

## Materials and procedural effects
11. **Fuzzy object:** Build a stylized fuzzy [OBJECT] using instanced short fibers or a shader. Cap fiber count and preserve the silhouette.
12. **Iridescent shell:** Use a physically plausible base material with subtle angle-dependent color variation. Avoid rainbow overload.
13. **Ceramic product:** Soft satin ceramic, broad reflections, clean contact shadow, and slow turntable.
14. **Anodized metal:** Brushed/anodized metal with directional highlights and a close camera move.
15. **Translucent resin:** Colored translucent resin with thickness cues, internal color depth, and a bright edge light.

## Environments and atmosphere
16. **Golden-hour room:** A minimal interior with warm directional sunlight, long soft-edged shadows, and a slow camera drift.
17. **Night showroom:** A dark architectural showroom with a single hero pool of light and subtle reflective floor.
18. **Hazy sunbeam:** Create visible volumetric-style light shafts using layered transparent geometry or a supported volumetric effect. Keep the effect subtle.
19. **Minimal cyclorama:** Seamless studio floor and background, soft gradient lighting, and a single hero object.
20. **Architectural reveal:** Reveal [space] with a measured dolly-in, parallax, and carefully composed light/shadow rhythm.

## Motion design and transitions
21. **Spring entrance:** Bring [object] into frame with a damped spring, slight overshoot, and a clear settle.
22. **Precision orbit:** Orbit the camera around [object] by 90 degrees over [duration], with eased acceleration and deceleration.
23. **Match-cut transition:** Transition between [scene A] and [scene B] using a shared silhouette or aligned camera move.
24. **Particle accent:** Add a small number of particles that support the subject's motion. Do not obscure the focal point.
25. **Logo end card:** Reveal the supplied logo without altering its geometry or spelling. Finish with clear brand-safe margins.

## Social and campaign outputs
26. **Vertical product ad:** 9:16 composition with UI-safe margins, product in upper-middle region, one headline, and a short end card.
27. **Square campaign tile:** 1:1 art-directed hero frame, bold but legible type, strong silhouette, and restrained graphic accents.
28. **Fashion accessory film:** Macro detail, controlled reflections, slow orbit, and tactile surface response. No invented endorsements.
29. **Tech launch teaser:** Dark-to-light reveal, precise geometric motion, cyan/white accent palette, and a clean final product lockup.
30. **Seven-shot campaign system:** Produce seven genuinely distinct shots with different camera angles, lighting setups, visual actions, and compositions. Do not count minor recolors or crops as distinct concepts.

## Required response from the agent

For each prompt, provide:
- concise shot plan;
- scene/component plan;
- dependencies and asset assumptions;
- implementation;
- preview and render commands;
- QC findings;
- final output path only after verifying it exists.

## Code-first photorealistic commercial prompts

### Warm interior / Venetian blinds
Create a 15-second photorealistic CGI commercial entirely from procedural Blender Python. Build a believable lived-in desk environment, laptop, keyboard, ceramic coffee cup, notebook and a detailed optical product lens. Model real Venetian-blind slats and use a directional late-afternoon Sun so the shadows physically fall across the desk and product. Use warm wood bounce, controlled cool fill, shaped rim reflections, realistic PBR materials and a deliberate wide-to-macro camera progression with a focus pull. No stock footage or downloaded scene models. Render a low-sample preview, inspect frames, fix defects, then produce the final Cycles render and MP4.

### Premium macro product reveal
Create a 12-second product film with three distinct shots: contextual wide shot, slow macro orbit and extreme-detail hero close-up. Model the product as an assembly with real seams, fasteners, machined bevels, layered glass and fine surface detail. Use large area lights as shaped reflection cards, negative fill for contrast, controlled depth of field and a final held hero composition. All scene geometry, materials, lighting and animation must be generated by code. Render and inspect before final export.
