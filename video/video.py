#!/usr/bin/env python3
r"""
Create a slideshow video from all JPG images in:
C:\Users\Susan\Downloads\multilingual-political-website\video

Requires:
  pip install moviepy pillow

Run:
  python video.py
"""

import re
from pathlib import Path

from PIL import Image
from moviepy.editor import ImageClip, concatenate_videoclips


INPUT_DIR = Path(r"D:\Projects\agno\video")
OUTPUT_FILE = INPUT_DIR / "slideshow.mp4"

DURATION_PER_IMAGE_SEC = 3.0
FPS = 30
RESOLUTION = (1920, 1080)  # (width, height)
CROSSFADE_SEC = 0.0        # set to 0.5 for a smooth crossfade, or 0 to disable


def natural_key(s: str):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def fit_to_resolution(img_path: Path, resolution: tuple[int, int]) -> Path:
    """Resize + letterbox to exact resolution (no cropping). Returns temp jpg path."""
    w, h = resolution
    img = Image.open(img_path).convert("RGB")
    img.thumbnail((w, h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (w, h), (0, 0, 0))
    x = (w - img.width) // 2
    y = (h - img.height) // 2
    canvas.paste(img, (x, y))

    tmp_dir = INPUT_DIR / ".slideshow_tmp"
    tmp_dir.mkdir(exist_ok=True)
    out_path = tmp_dir / f"{img_path.stem}_{w}x{h}.jpg"
    canvas.save(out_path, quality=95)
    return out_path


def main():
    if not INPUT_DIR.is_dir():
        raise SystemExit(f"Folder not found: {INPUT_DIR}")

    images = sorted(INPUT_DIR.glob("*.jpg"), key=lambda p: natural_key(p.name))
    if not images:
        raise SystemExit(f"No .jpg files found in: {INPUT_DIR}")

    clips = []
    for p in images:
        fitted = fit_to_resolution(p, RESOLUTION)
        clips.append(ImageClip(str(fitted)).set_duration(DURATION_PER_IMAGE_SEC))

    if CROSSFADE_SEC > 0:
        for i in range(1, len(clips)):
            clips[i] = clips[i].crossfadein(CROSSFADE_SEC)
        video = concatenate_videoclips(clips, method="compose", padding=-CROSSFADE_SEC)
    else:
        video = concatenate_videoclips(clips, method="compose")

    video.write_videofile(
        str(OUTPUT_FILE),
        fps=FPS,
        codec="libx264",
        audio=False,
        threads=4,
    )

    # cleanup temp
    tmp_dir = INPUT_DIR / ".slideshow_tmp"
    if tmp_dir.exists():
        for f in tmp_dir.iterdir():
            try:
                f.unlink()
            except Exception:
                pass
        try:
            tmp_dir.rmdir()
        except Exception:
            pass

    print(f"Done: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
