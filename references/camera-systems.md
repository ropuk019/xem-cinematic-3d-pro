# Camera systems

## Perspective camera
Use a perspective camera for dimensionality. Establish subject scale and framing before animation. Keep the camera target stable unless the shot explicitly requires a moving target.

## Animation
Use frame-derived values. For a normalized progress `p`, use smoothstep `p*p*(3-2*p)` or Remotion `interpolate` with easing. Clamp progress to avoid unintended extrapolation.

## Safe framing
Check the full animation range, not only frame zero. Account for overshoot, orbit, and moving props. Use a wider framing for vertical output when the subject has lateral movement.

## Depth of field
DOF can improve macro/product shots but can also hide important details. Use it selectively; verify the focal plane across the shot. Avoid extreme blur on small mobile screens.
