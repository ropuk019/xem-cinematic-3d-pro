import React from 'react';
import {RoundedBox as DreiRoundedBox} from '@react-three/drei';

export const RoundedBox = DreiRoundedBox;
export const Mesh = (props: React.ComponentProps<'mesh'>) => <mesh {...props} />;
