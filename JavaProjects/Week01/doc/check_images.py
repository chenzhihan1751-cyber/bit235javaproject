from PIL import Image
import os

d = r"D:\JavaDev\JavaProjects\Week01\doc\images"
bad = 0
for f in sorted(os.listdir(d)):
    p = os.path.join(d, f)
    im = Image.open(p).convert("RGB")
    w, h = im.size
    px = im.load()
    bg = px[w - 8, h - 8]
    minx, miny, maxx, maxy = w, h, 0, 0
    for y in range(4, h - 4):
        for x in range(4, w - 4):
            c = px[x, y]
            if abs(c[0]-bg[0]) + abs(c[1]-bg[1]) + abs(c[2]-bg[2]) > 18:
                minx = min(minx, x); miny = min(miny, y)
                maxx = max(maxx, x); maxy = max(maxy, y)
    ok = (maxx < w - 4) and (maxy < h - 4)
    if not ok:
        bad += 1
    flag = "" if ok else "   <-- CLIPPED"
    print("%-20s %dx%d ink=(%d,%d)-(%d,%d) right_gap=%d bottom_gap=%d%s"
          % (f, w, h, minx, miny, maxx, maxy, w - 4 - maxx, h - 4 - maxy, flag))
print("clipped images:", bad)
