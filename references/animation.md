# Animation

## Timing
A good short film has anticipation, action, settle, and hold. Do not animate every object at once. Establish a hierarchy between primary motion and secondary motion.

## Frame determinism
For Remotion, derive time from `useCurrentFrame()` and `useVideoConfig().fps`. Do not use `Date.now()`, `Math.random()` without a fixed seed, or uncontrolled physics simulation.

## Easing
- Linear: mechanical constant velocity.
- Smoothstep: soft start and stop.
- Cubic/quintic ease: stronger acceleration/deceleration.
- Spring: organic overshoot and settle; configure damping to avoid perpetual wobble.

## Secondary motion
Use small amplitude and phase offsets. Secondary motion should support the hero action rather than compete with it.
