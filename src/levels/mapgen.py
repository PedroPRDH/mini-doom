import random, math
class Map:
    def __init__(s, w, h, seed=1, fill='1'):
        s.w, s.h = w, h
        s.g = [[fill]*w for _ in range(h)]
        s.r = random.Random(seed)
    def rect(s, x0, y0, x1, y1, c='.'):
        for y in range(max(0,y0), min(s.h,y1+1)):
            for x in range(max(0,x0), min(s.w,x1+1)):
                s.g[y][x] = c
    def block(s, x, y, w, h, c): s.rect(x, y, x+w-1, y+h-1, c)
    def circ(s, cx, cy, r, c='.'):
        for y in range(s.h):
            for x in range(s.w):
                if math.hypot(x+.5-cx, y+.5-cy) <= r: s.g[y][x] = c
    def ring(s, cx, cy, r0, r1, c):
        for y in range(s.h):
            for x in range(s.w):
                d = math.hypot(x+.5-cx, y+.5-cy)
                if r0 <= d <= r1: s.g[y][x] = c
    def border(s, c='1'):
        for x in range(s.w): s.g[0][x] = s.g[s.h-1][x] = c
        for y in range(s.h): s.g[y][0] = s.g[y][s.w-1] = c
    def freebox(s, x0, y0, x1, y1):
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                if not (0 <= x < s.w and 0 <= y < s.h) or s.g[y][x] != '.': return False
        return True
    def scatter(s, n, sizes, types, clear=3, region=None, keep=None, tries=800):
        x0, y0, x1, y1 = region or (1, 1, s.w-2, s.h-2)
        placed = 0
        for _ in range(tries):
            if placed >= n: break
            bw, bh = s.r.choice(sizes)
            x = s.r.randint(x0, x1-bw+1); y = s.r.randint(y0, y1-bh+1)
            if keep and any(kx0 <= x+bw-1+clear and x-clear <= kx1 and ky0 <= y+bh-1+clear and y-clear <= ky1 for kx0, ky0, kx1, ky1 in keep): continue
            if not s.freebox(x-clear, y-clear, x+bw-1+clear, y+bh-1+clear): continue
            s.block(x, y, bw, bh, s.r.choice(types)); placed += 1
        return placed
    def finalize(s, start, wall='1'):
        W, H = s.w, s.h
        for x in range(W):
            for y in (0, H-1):
                if s.g[y][x] == '.': s.g[y][x] = wall
        for y in range(H):
            for x in (0, W-1):
                if s.g[y][x] == '.': s.g[y][x] = wall
        fat = set()
        for y in range(1, H-1):
            for x in range(1, W-1):
                if all(s.g[y+j][x+i] == '.' for j in (-1,0,1) for i in (-1,0,1)): fat.add((x, y))
        sx, sy = int(start[0]), int(start[1])
        near = [p for p in fat if abs(p[0]-sx) <= 2 and abs(p[1]-sy) <= 2]
        assert near, 'inicio sin zona ancha'
        comp = {near[0]}; st = [near[0]]
        while st:
            x, y = st.pop()
            for j in (-1,0,1):
                for i in (-1,0,1):
                    q = (x+i, y+j)
                    if q in fat and q not in comp: comp.add(q); st.append(q)
        keep = set()
        for (x, y) in comp:
            for j in (-1,0,1):
                for i in (-1,0,1): keep.add((x+i, y+j))
        for y in range(H):
            for x in range(W):
                if s.g[y][x] == '.' and (x, y) not in keep: s.g[y][x] = wall
        return s
    def rows(s): return [''.join(r) for r in s.g]
    def stats(s):
        fr = sum(r.count('.') for r in s.rows()); return fr, fr/(s.w*s.h)
