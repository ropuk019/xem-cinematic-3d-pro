import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {Canvas} from '@react-three/fiber';
import {ContactShadows} from '@react-three/drei';
import * as THREE from 'three';

export const SceneCanvas: React.FC<{children: React.ReactNode; cameraZ?: number}> = ({children, cameraZ = 6}) => (
  <AbsoluteFill>
    <Canvas
      shadows
      dpr={[1, 1.5]}
      gl={{antialias: true, alpha: false, toneMapping: THREE.ACESFilmicToneMapping}}
      camera={{position: [0, 0.2, cameraZ], fov: 38, near: 0.1, far: 100}}
      onCreated={({gl}) => {
        gl.shadowMap.enabled = true;
        gl.shadowMap.type = THREE.PCFSoftShadowMap;
      }}
    >
      {children}
      <ContactShadows position={[0, -1.52, 0]} opacity={0.42} scale={9} blur={2.5} far={4} resolution={512}/>
    </Canvas>
  </AbsoluteFill>
);

export const useProgress = (duration: number, start = 0) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  return interpolate(frame, [start, start + duration], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
};

export const StudioLights: React.FC = () => (
  <>
    <ambientLight intensity={0.3} />
    <directionalLight
      castShadow
      position={[4, 7, 5]}
      intensity={2.6}
      shadow-mapSize-width={2048}
      shadow-mapSize-height={2048}
      shadow-camera-near={0.1}
      shadow-camera-far={30}
      shadow-camera-left={-6}
      shadow-camera-right={6}
      shadow-camera-top={6}
      shadow-camera-bottom={-6}
      shadow-bias={-0.00015}
      shadow-normalBias={0.025}
    />
    <spotLight castShadow position={[-4, 4, 2]} angle={0.55} penumbra={0.8} intensity={42} color="#78baff"/>
    <pointLight position={[3, 1, -3]} intensity={24} color="#ff8a54"/>
  </>
);
