# Materials

## Principled starting points
| Look | Metalness | Roughness |
|---|---:|---:|
| Matte plastic | 0 | 0.45–0.65 |
| Gloss plastic | 0 | 0.18–0.32 |
| Satin | 0 | 0.35–0.55 |
| Polished metal | 0.85–1 | 0.12–0.28 |
| Rubber | 0 | 0.7–0.9 |

These are artistic starting points. Environment and lighting strongly affect perceived material.

## Procedural methods
- Noise: subtle roughness/color variation, not arbitrary dirt.
- Fresnel: edge response for stylized rim effects.
- Instancing: repeated fibers, dots, or particles.
- Geometry: bevels and rounded edges often create more believable highlights than extreme material settings.

## Glass
Opacity alone does not create glass. Use transmission/refraction support where available, thickness cues, edge highlights, and a contrasting environment. Validate performance and rendering support.
