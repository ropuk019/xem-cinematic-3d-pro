import React, {useRef} from 'react';
import {useCurrentFrame, interpolate, Easing} from 'remotion';
import {useFrame} from '@react-three/fiber';
import {RoundedBox, MeshReflectorMaterial} from '@react-three/drei';
import * as THREE from 'three';
import {SceneCanvas, StudioLights} from './Shared';

const HeroDevice: React.FC<{progress: number}> = ({progress}) => {
  const group = useRef<THREE.Group>(null);
  useFrame(() => {
    if (!group.current) return;
    group.current.rotation.y = -0.22 + progress * 0.85;
    group.current.rotation.x = Math.sin(progress * Math.PI) * 0.025;
  });
  return (
    <group ref={group} position={[0, -0.02, 0]}>
      <RoundedBox args={[2.25, 2.9, 0.72]} radius={0.22} smoothness={8} castShadow receiveShadow>
        <meshPhysicalMaterial color="#343e4c" metalness={0.78} roughness={0.24} clearcoat={0.8} clearcoatRoughness={0.15}/>
      </RoundedBox>
      <RoundedBox args={[2.08, 2.7, 0.12]} radius={0.17} smoothness={8} position={[0, 0, 0.38]} castShadow receiveShadow>
        <meshPhysicalMaterial color="#151d29" metalness={0.52} roughness={0.28}/>
      </RoundedBox>
      <mesh position={[0, 0.35, 0.47]} castShadow>
        <cylinderGeometry args={[0.68, 0.68, 0.09, 96]}/>
        <meshPhysicalMaterial color="#080d16" metalness={0.62} roughness={0.16}/>
      </mesh>
      <mesh position={[0, 0.35, 0.53]}>
        <cylinderGeometry args={[0.55, 0.55, 0.035, 96]}/>
        <meshPhysicalMaterial color="#12618c" metalness={0.48} roughness={0.12} clearcoat={1} emissive="#07304d" emissiveIntensity={0.35}/>
      </mesh>
      <mesh position={[0, 0.35, 0.555]}>
        <torusGeometry args={[0.43, 0.012, 12, 96]}/>
        <meshStandardMaterial color="#a8e7ff" metalness={0.85} roughness={0.16} emissive="#1b8fc7" emissiveIntensity={0.25}/>
      </mesh>
      <RoundedBox args={[0.7, 0.1, 0.045]} radius={0.04} smoothness={5} position={[0, -0.78, 0.43]}>
        <meshStandardMaterial color="#7e8fa4" metalness={0.65} roughness={0.25}/>
      </RoundedBox>
      {[-0.72, -0.48, -0.24].map((y, i) => (
        <mesh key={i} position={[0.76, y, 0.43]}>
          <sphereGeometry args={[0.035, 16, 12]}/>
          <meshBasicMaterial color={i === 0 ? '#4ad7ff' : '#75869a'}/>
        </mesh>
      ))}
    </group>
  );
};

const ProductScene: React.FC<{progress: number}> = ({progress}) => (
  <>
    <color attach="background" args={['#10141d']}/>
    <fog attach="fog" args={['#10141d', 10, 25]}/>
    <StudioLights/>
    <HeroDevice progress={progress}/>
    <mesh rotation={[-Math.PI/2, 0, 0]} position={[0, -1.53, 0]} receiveShadow>
      <planeGeometry args={[200, 200]}/>
      <MeshReflectorMaterial blur={[300, 80]} resolution={512} mixBlur={1} mixStrength={0.22}
        roughness={0.4} metalness={0.22} color="#151b26"/>
    </mesh>
  </>
);

export const ProductFilm: React.FC = () => {
  const frame = useCurrentFrame();
  const progress = interpolate(frame, [0, 239], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.inOut(Easing.cubic)
  });
  return <SceneCanvas cameraZ={7}><ProductScene progress={progress}/></SceneCanvas>;
};
