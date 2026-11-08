import React, {useRef} from 'react';
import {useFrame} from '@react-three/fiber';
import {Text3D, Center, Float} from '@react-three/drei';
import {useCurrentFrame, interpolate, Easing} from 'remotion';
import * as THREE from 'three';
import {SceneCanvas, StudioLights} from './Shared';

const ExtrudedTitle: React.FC<{progress: number}> = ({progress}) => {
  const group = useRef<THREE.Group>(null);
  useFrame(() => {
    if (!group.current) return;
    group.current.rotation.y = Math.sin(progress * Math.PI * 2) * 0.09;
    group.current.position.y = -0.12 + Math.sin(progress * Math.PI * 2) * 0.05;
  });
  return (
    <group ref={group}>
      <Center>
        <Text3D font="/fonts/helvetiker_bold.typeface.json" size={1.0} height={0.24}
          bevelEnabled bevelThickness={0.1} bevelSize={0.045} bevelSegments={6} curveSegments={16}>
          XEM
          <meshPhysicalMaterial color="#fa78bd" roughness={0.16} metalness={0.06} clearcoat={1} clearcoatRoughness={0.08}/>
        </Text3D>
      </Center>
    </group>
  );
};

export const JellyTitle: React.FC = () => {
  const frame = useCurrentFrame();
  const progress = interpolate(frame, [0, 209], [0, 1], {extrapolateRight: 'clamp', easing: Easing.inOut(Easing.cubic)});
  return (
    <SceneCanvas cameraZ={6.8}>
      <color attach="background" args={['#171225']}/>
      <StudioLights/>
      <pointLight position={[0, 3, 4]} intensity={55} color="#ffc4e5"/>
      <pointLight position={[-4, 0, -2]} intensity={38} color="#7c8dff"/>
      <Float speed={1.1} rotationIntensity={0.05} floatIntensity={0.12}>
        <ExtrudedTitle progress={progress}/>
      </Float>
      <mesh rotation={[-Math.PI/2, 0, 0]} position={[0, -1.1, 0]} receiveShadow>
        <planeGeometry args={[100, 100]}/>
        <meshStandardMaterial color="#211a32" roughness={0.7}/>
      </mesh>
    </SceneCanvas>
  );
};
