#!/usr/bin/env node
import {spawnSync} from 'node:child_process';

const run = (cmd, args) => {
  const r = spawnSync(cmd, args, {encoding: 'utf8'});
  return {status: r.status, output: (r.stdout || '') + (r.stderr || '')};
};
const node = run(process.execPath, ['--version']);
const npm = run('npm', ['--version']);
console.log(`Node: ${node.output.trim()}`);
console.log(`npm: ${npm.output.trim()}`);
const major = Number((node.output.match(/v(\d+)/) || [])[1] || 0);
if (major < 20) {
  console.error('Node 20+ is recommended. Upgrade Node before installing the starter.');
  process.exitCode = 1;
} else {
  console.log('Environment version check passed.');
}
