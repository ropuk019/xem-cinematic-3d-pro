import fs from 'node:fs';
import path from 'node:path';
const src = path.resolve('node_modules/three/examples/fonts/helvetiker_bold.typeface.json');
if (!fs.existsSync(src)) {
  console.warn('Three.js example typeface not found. Text3D sample will need a local font JSON.');
  process.exit(0);
}
fs.mkdirSync(path.resolve('public/fonts'), {recursive: true});
fs.copyFileSync(src, path.resolve('public/fonts/helvetiker_bold.typeface.json'));
console.log('Installed local Text3D typeface.');
