import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {ProductFilm} from './ProductFilm';

export const VerticalAd: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 18, 210, 239], [0, 1, 1, 0.9], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{backgroundColor: '#10131b'}}>
      <ProductFilm />
      <AbsoluteFill style={{justifyContent: 'flex-start', alignItems: 'center', paddingTop: 150, opacity}}>
        <div style={{fontFamily: 'Arial, sans-serif', fontWeight: 800, fontSize: 76, color: '#f7f8fb', letterSpacing: 5, textAlign: 'center'}}>FORM / FUNCTION</div>
        <div style={{fontFamily: 'Arial, sans-serif', fontSize: 27, color: '#aab6c8', marginTop: 18, letterSpacing: 8}}>DESIGNED TO STAND OUT</div>
      </AbsoluteFill>
      <AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 150, opacity}}>
        <div style={{fontFamily: 'Arial, sans-serif', fontSize: 28, color: '#ffffff', letterSpacing: 6}}>DISCOVER THE NEW STANDARD</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
