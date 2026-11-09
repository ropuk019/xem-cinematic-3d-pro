# Code-first photorealism playbook

## Build rather than fake

If the image depends on a physical interaction, model the cause. Blind shadows require slats and a directional source. A metallic edge highlight requires a shaped reflection source. A convincing glass lens needs layered optical surfaces and dark internal geometry. A cup needs wall thickness, a handle and a liquid surface if the camera can see inside it.

## Procedural modeling hierarchy

1. Primary silhouette and dimensions.
2. Secondary construction: caps, seams, bezels, handles, joints and panel gaps.
3. Tertiary details visible at the chosen focal length: knurling, screws, labels, aperture blades, stitching.
4. Surface breakup: subtle roughness variation, fingerprints, dust or edge wear only where plausible.

Use bevels to catch light. Weighted normals improve hard-surface shading but do not repair bad topology. Apply transforms before bevel operations. Avoid coplanar surfaces and z-fighting.

## Interior light recipe

- Use a real window opening and geometry for blinds.
- A Sun light creates coherent directional shadows; its angular size controls softness.
- The size and distance of the source and blinds determine shadow softness and spacing.
- Add warm bounce from the room and restrained fill to keep shadow detail.
- Do not make every surface equally bright. Protect the highlight roll-off and maintain a readable black level.

## Macro lens recipe

- Use a plausible camera focal length and a large but controlled aperture.
- Model the focus ring, grip, barrel joints, front filter ring, glass stack, aperture and engraved markings.
- Use a dark interior behind glass so reflections read correctly.
- Give the focus target a real object and animate it deliberately; inspect sharpness at the hero frame.
- Avoid extreme DOF that turns the entire product into an indistinct blur.

## Material response

- Metals reflect the environment; metalness alone does not create realism. Design the reflection environment.
- Dielectrics retain a visible diffuse component and Fresnel reflections.
- Roughness should vary subtly, not randomly at high contrast.
- Glass needs thickness, transmission, IOR and reflection. Avoid a single transparent plane for a thick optical element.
- Use bump/displacement at a scale that matches the camera distance and texture type.

## Render iteration

Render low samples and reduced resolution first. Inspect actual images, not just the viewport. Denoising can smear microdetail; compare denoised and raw crops when necessary. Use a frame sequence for long renders so a crash does not destroy completed frames. Only increase samples and output resolution after composition, materials, lighting and animation pass review.
