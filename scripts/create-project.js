#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const packRoot = path.resolve(here, '..');
const source = path.join(packRoot, 'starter');
const targetArg = process.argv[2];

if (!targetArg) {
  console.error('Usage: node scripts/create-project.js <target-directory>');
  process.exit(1);
}
const target = path.resolve(process.cwd(), targetArg);
if (fs.existsSync(target) && fs.readdirSync(target).length > 0) {
  console.error(`Refusing to overwrite non-empty directory: ${target}`);
  process.exit(1);
}
fs.mkdirSync(target, {recursive: true});
fs.cpSync(source, target, {recursive: true});
console.log(`Starter copied to: ${target}`);
console.log('Next: cd into the directory, run npm install, then npm run studio.');
