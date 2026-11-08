import React from 'react';
import {Composition} from 'remotion';
import {ProductFilm} from './scenes/ProductFilm';
import {JellyTitle} from './scenes/JellyTitle';
import {VerticalAd} from './scenes/VerticalAd';

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="ProductFilm"
        component={ProductFilm}
        durationInFrames={240}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="JellyTitle"
        component={JellyTitle}
        durationInFrames={210}
        fps={30}
        width={1080}
        height={1080}
      />
      <Composition
        id="VerticalAd"
        component={VerticalAd}
        durationInFrames={240}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
