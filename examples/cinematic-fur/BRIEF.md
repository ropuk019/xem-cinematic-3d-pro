# Example 03 — Procedural fur study

**Intent:** a tactile fuzzy object with a readable silhouette.

**Implementation approach:** use instanced short tapered fibers attached to a base mesh, with deterministic seeded placement. For high counts, use a custom shader or Blender-generated asset. Avoid one React component per fiber.

**QC:** inspect silhouette aliasing, fiber density, shadow noise, and render time.
