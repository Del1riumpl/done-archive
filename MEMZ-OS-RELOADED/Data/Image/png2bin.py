import sys, math
import struct, os
from PIL import Image
import glob

doscolors = [
    (0x00, 0x00, 0x00), # 0
    (0x00, 0x00, 0xa8), # 1
    (0x00, 0xa8, 0x00), # 2
    (0x00, 0xa8, 0xa8), # 3
    (0xa8, 0x00, 0x00), # 4
    (0xa8, 0x00, 0xa8), # 5
    (0xa8, 0xa8, 0x00), # 6
    (0xa8, 0xa8, 0xa8), # 7

    (0x54, 0x54, 0x54), # 8
    (0x54, 0x54, 0xff), # 9
    (0x54, 0xff, 0x54), # 10
    (0x54, 0xff, 0xff), # 11
    (0xff, 0x54, 0x54), # 12
    (0xff, 0x54, 0xff), # 13
    (0xff, 0xff, 0x54), # 14
    (0xff, 0xff, 0xff), # 15
]

def color_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

def nearest_color(color):
    nearest = 0

    for i in range(len(doscolors)):
        if color_distance(color, doscolors[i]) < color_distance(color, doscolors[nearest]):
            nearest = i

    return nearest

buf = b""

for imgf in glob.glob(sys.argv[1]):  # Use glob to expand the wildcard
    img = Image.open(imgf).convert("RGB")
    w, h = img.size

    for y in range(0, h, 2):
        for x in range(w):
            b = (nearest_color(img.getpixel((x, y))) << 4) | nearest_color(img.getpixel((x, y+1)))
            buf += bytes([b])

    img.close()

with open(sys.argv[2], "wb") as out:
    out.write(buf)
