import json, math
from mapgen import Map
from PIL import Image, ImageDraw
OUT = {}
START = {}

def n1():
    m = Map(30, 30, 11); m.rect(1, 1, 28, 28)
    m.block(6, 7, 6, 4, '2'); m.block(19, 6, 4, 6, '2'); m.block(20, 18, 6, 4, '2'); m.block(6, 14, 4, 6, '2')
    m.block(13, 13, 4, 4, '3')
    keep = [(1, 21, 9, 28)]
    m.scatter(12, [(1, 1)], ['3'], 3, keep=keep)
    m.scatter(5, [(2, 2), (3, 2)], ['2'], 3, keep=keep)
    m.finalize((3.5, 26.5)); START['n1'] = (3.5, 26.5, -0.78); return m

def n2():
    m = Map(36, 24, 22); m.rect(1, 1, 34, 22)
    for x in range(7, 30, 6):
        if 14 <= x <= 21: continue
        m.block(x, 4, 2, 2, '2'); m.block(x, 17, 2, 2, '2')
    m.block(6, 9, 3, 6, '3'); m.block(27, 9, 3, 6, '3')
    m.block(16, 10, 4, 4, '2')
    keep = [(1, 8, 5, 15)]
    m.scatter(8, [(1, 1), (2, 1)], ['3'], 3, keep=keep)
    m.finalize((3.5, 11.5)); START['n2'] = (3.5, 11.5, 0.0); return m

def n3():
    m = Map(32, 32, 33)
    m.rect(10, 2, 21, 29); m.rect(2, 5, 8, 26); m.rect(23, 5, 29, 26); m.rect(2, 12, 29, 19)
    m.circ(16, 5.5, 6.5)
    for x in (9, 22):
        m.rect(x, 5, x, 26)
        for a, b in ((5, 6), (10, 11), (20, 21), (25, 26)):
            m.rect(x, a, x, b, '3')
    m.block(14, 3, 4, 2, '3')
    keep = [(10, 24, 21, 29)]
    m.scatter(8, [(3, 1)], ['2'], 2, region=(10, 7, 21, 22), keep=keep)
    m.scatter(6, [(1, 1)], ['3'], 3, region=(2, 5, 8, 26))
    m.scatter(6, [(1, 1)], ['3'], 3, region=(23, 5, 29, 26))
    m.finalize((15.5, 27.5)); START['n3'] = (15.5, 27.5, -1.5708); return m

def n4():
    m = Map(34, 34, 44)
    m.circ(17, 17, 16.2)
    m.ring(17, 17, 8.5, 10.6, '2')
    m.rect(15, 5, 18, 13); m.rect(15, 21, 18, 28); m.rect(5, 15, 13, 18); m.rect(21, 15, 28, 18)
    m.circ(17, 17, 3.2, '3')
    keep = [(11, 28, 23, 33)]
    m.scatter(10, [(1, 1), (2, 2)], ['3', '2'], 3, keep=keep)
    m.finalize((16.5, 31.0)); START['n4'] = (16.5, 31.0, -1.5708); return m

def n5():
    m = Map(36, 28, 55); m.rect(1, 1, 34, 26)
    m.block(14, 2, 8, 3, '2'); m.block(10, 2, 1, 3, '3'); m.block(25, 2, 1, 3, '3')
    keep = [(1, 20, 8, 26)]
    m.scatter(14, [(2, 2), (3, 2), (2, 3)], ['2', '3'], 3, keep=keep)
    m.scatter(10, [(1, 1)], ['3'], 3, keep=keep)
    m.finalize((3.5, 23.5)); START['n5'] = (3.5, 23.5, -0.5); return m

def n7():
    W = H = 42
    m = Map(W, H, 77, '.')
    for bx in (7, 21, 35):
        for by in (7, 21, 35):
            t = m.r.choice(['1', '2', '4'])
            m.block(bx, by, 8, 8, t)
    # plaza central
    m.rect(20, 20, 29, 29, '.'); m.block(24, 24, 2, 2, '6')
    m.block(7, 21, 8, 8, '.'); m.block(10, 24, 2, 2, '3')
    m.border('2')
    keep = [(1, 33, 8, 40)]
    m.scatter(16, [(2, 1), (1, 2)], ['3'], 3, keep=keep, region=(1, 1, W-2, H-2), tries=3000)
    m.scatter(6, [(3, 1), (1, 3)], ['6'], 3, keep=keep, tries=3000)
    m.finalize((3.5, 38.5), wall='1'); START['n7'] = (3.5, 38.5, -0.78); return m

def n8():
    m = Map(40, 30, 88); m.rect(1, 1, 38, 28)
    m.block(17, 12, 6, 6, '6')
    m.block(3, 3, 4, 4, '1'); m.block(33, 3, 4, 4, '1'); m.block(33, 23, 4, 4, '1'); m.block(3, 23, 4, 4, '1')
    keep = [(1, 12, 8, 18)]
    m.scatter(12, [(1, 6), (6, 1), (1, 4), (4, 1)], ['5'], 3, keep=keep)
    m.scatter(12, [(2, 2)], ['5'], 3, keep=keep)
    m.scatter(5, [(1, 1)], ['3'], 3, keep=keep)
    m.finalize((3.5, 15.5)); START['n8'] = (3.5, 15.5, 0.0); return m

def n9():
    m = Map(48, 20, 99); m.rect(1, 1, 46, 18)
    for x0 in range(5, 44, 14): m.rect(x0, 9, x0+6, 10, '6')
    for x in range(10, 44, 12): m.block(x, 3, 2, 2, '1'); m.block(x, 15, 2, 2, '1')
    keep = [(1, 6, 6, 14)]
    m.scatter(14, [(2, 1), (1, 2), (3, 1)], ['3'], 3, keep=keep, tries=3000)
    m.scatter(5, [(3, 1)], ['6'], 3, keep=keep, tries=3000)
    m.finalize((2.5, 12.5)); START['n9'] = (2.5, 12.5, 0.0); return m

def n10():
    m = Map(30, 30, 111); m.rect(1, 1, 28, 28)
    m.block(1, 1, 4, 4, '1'); m.block(25, 1, 4, 4, '1')
    m.circ(8, 15, 2.2, '6'); m.circ(22, 15, 2.2, '6')
    keep = [(1, 21, 9, 28)]
    m.scatter(7, [(3, 2), (2, 2)], ['3'], 3, keep=keep)
    m.scatter(6, [(1, 1)], ['2'], 3, keep=keep)
    m.finalize((3.5, 26.0)); START['n10'] = (3.5, 26.0, -0.78); return m

for name, fn in [('n1', n1), ('n2', n2), ('n3', n3), ('n4', n4), ('n5', n5), ('n7', n7), ('n8', n8), ('n9', n9), ('n10', n10)]:
    m = fn(); OUT[name] = m.rows()
    fr, pc = m.stats(); print(name, m.w, m.h, 'libres', fr, '%.0f%%' % (pc*100))
json.dump({'maps': OUT, 'start': START}, open('maps.json', 'w'))
# vista previa
C = {'.': (40, 36, 34), '1': (170, 110, 80), '2': (120, 130, 160), '3': (200, 170, 70), '4': (80, 140, 190), '5': (60, 150, 60), '6': (180, 180, 180)}
S = 8; names = list(OUT); cols = 3
rows = (len(names)+cols-1)//cols
cw = max(len(OUT[n][0]) for n in names)*S+10; ch = max(len(OUT[n]) for n in names)*S+10
im = Image.new('RGB', (cols*cw, rows*ch), (10, 10, 10)); d = ImageDraw.Draw(im)
for i, n in enumerate(names):
    ox, oy = (i % cols)*cw+5, (i//cols)*ch+5
    for y, r in enumerate(OUT[n]):
        for x, c in enumerate(r): d.rectangle([ox+x*S, oy+y*S, ox+x*S+S-1, oy+y*S+S-1], fill=C[c])
    sx, sy, _ = START[n]; d.ellipse([ox+sx*S-5, oy+sy*S-5, ox+sx*S+5, oy+sy*S+5], fill=(255, 50, 50))
im.save('preview.png'); print('ok')
