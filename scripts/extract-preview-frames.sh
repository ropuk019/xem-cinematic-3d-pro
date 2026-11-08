#!/usr/bin/env bash
set -euo pipefail
VIDEO="${1:-starter/out/product-film.mp4}"
OUT="${2:-preview-frames}"
mkdir -p "$OUT"
command -v ffmpeg >/dev/null || { echo "ffmpeg is required"; exit 1; }
ffmpeg -y -i "$VIDEO" -vf "fps=1/2,scale=960:-1" "$OUT/frame-%03d.jpg"
echo "Preview frames written to $OUT"
