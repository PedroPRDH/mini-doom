import json,random
from collections import deque
class G:
    def __init__(s,w,h):
        s.w,s.h=w,h;s.W=[[0]*w for _ in range(h)];s.H=[[0]*w for _ in range(h)]
        for x in range(w):s.W[0][x]=s.W[h-1][x]=1
        for y in range(h):s.W[y][0]=s.W[y][w-1]=1
    def wall(s,x,y,w,h,t):
        for j in range(y,y+h):
            for i in range(x,x+w):
                if 0<=i<s.w and 0<=j<s.h:s.W[j][i]=t;s.H[j][i]=0
    def plat(s,x,y,w,h,l):
        for j in range(y,y+h):
            for i in range(x,x+w):
                if 1<=i<s.w-1 and 1<=j<s.h-1 and not s.W[j][i]:s.H[j][i]=l
    def stairs(s,x,y,w,n,d,start=1):  # d: 'N','S','E','W' direction of ascent; n steps; each +1 level
        for k in range(n):
            l=start+k
            if d=='N':s.plat(x,y-k,w,1,l)
            if d=='S':s.plat(x,y+k,w,1,l)
            if d=='E':s.plat(x+k,y,1,w,l)
            if d=='W':s.plat(x-k,y,1,w,l)
    def finish(s,start):
        # seal pockets unreachable from start
        sx,sy=int(start[0]),int(start[1]);seen={(sx,sy)};q=deque([(sx,sy)])
        while q:
            x,y=q.popleft()
            for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                a,b=x+dx,y+dy
                if 0<=a<s.w and 0<=b<s.h and not s.W[b][a] and (a,b) not in seen:seen.add((a,b));q.append((a,b))
        for y in range(s.h):
            for x in range(s.w):
                if not s.W[y][x] and (x,y) not in seen:s.W[y][x]=1;s.H[y][x]=0
        free=sum(1 for y in range(s.h) for x in range(s.w) if not s.W[y][x])
        return free
    def rows(s):
        return [''.join('.' if not c else str(c) for c in r) for r in s.W],[''.join(str(min(9,c)) for c in r) for r in s.H]
    def png(s,name):
        from PIL import Image
        im=Image.new('RGB',(s.w*10,s.h*10))
        for y in range(s.h):
            for x in range(s.w):
                if s.W[y][x]:c=(40,40,60) if s.W[y][x]==1 else [(0,0,0),(0,0,0),(150,60,40),(190,120,30),(60,100,170),(40,130,50),(170,170,60)][s.W[y][x]]
                else:v=60+s.H[y][x]*30;c=(v,v,v)
                for a in range(10):
                    for b in range(10):im.putpixel((x*10+a,y*10+b),c)
        im.save(name)

def e7():  # CALLES EN LLAMAS 44x44
    g=G(44,44)
    # fachadas en L en las 4 esquinas (paredes largas deslizables)
    g.wall(5,5,10,2,2);g.wall(5,5,2,10,2)
    g.wall(29,5,10,2,3);g.wall(37,5,2,10,3)
    g.wall(29,37,10,2,4);g.wall(37,29,2,10,4)
    g.wall(5,37,10,2,2);g.wall(5,29,2,10,2)
    # zigurat central con escaleras N y S
    g.plat(14,14,16,16,2);g.plat(17,17,10,10,4);g.plat(20,20,4,4,6)
    g.stairs(20,13,4,1,'N',1);g.stairs(20,30,4,1,'S',1)
    g.stairs(21,16,2,1,'N',3) ;g.stairs(21,27,2,1,'S',3)
    # cañones de salto de pared (dos paredes paralelas) hacia azoteas
    g.wall(9,21,3,1,5);g.wall(9,24,3,1,5);g.plat(2,19,7,7,5)
    g.wall(32,21,3,1,6);g.wall(32,24,3,1,6);g.plat(35,19,7,7,5)
    g.wall(21,8,1,3,3);g.wall(24,8,1,3,3);g.plat(19,2,7,6,5)
    g.wall(21,33,1,3,4);g.wall(24,33,1,3,4);g.plat(19,36,7,6,5)
    # puentes elevados (2m) desde las tierras altas al zigurat
    pass
    g.plat(35,21,0,0,0)
    # piedras de salto (pasos 0.5-1m) en las esquinas libres
    for (x,y,l) in [(10,10,2),(13,9,3),(16,11,4),(11,14,3),(8,12,5)]:g.plat(x,y,2,2,l)
    for (x,y,l) in [(31,11,2),(34,9,3),(36,12,4),(32,14,3)]:g.plat(x,y,2,2,l)
    for (x,y,l) in [(31,32,2),(34,34,3),(30,35,4),(33,30,3)]:g.plat(x,y,2,2,l)
    for (x,y,l) in [(9,33,2),(12,35,3),(10,30,4),(13,31,3)]:g.plat(x,y,2,2,l)
    # medios muros bajos tipo barricada con setos y barreras (reemplazan columnas)
    g.plat(3,3,4,2,2);g.plat(37,3,4,2,2);g.plat(3,39,4,2,2);g.plat(37,39,4,2,2)
    g.plat(15,3,4,3,2);g.plat(26,3,4,3,2);g.plat(15,38,4,3,2);g.plat(26,38,4,3,2)
    return g,(3.5,38.5,-0.78)
def e8():  # PARQUE CENTRAL 44x36: colinas, lago de plataformas, muros de piedra
    g=G(44,36)
    # colinas escalonadas (terraplenes)
    def hill(cx,cy,r,top):
        for y in range(g.h):
            for x in range(g.w):
                d=max(abs(x-cx),abs(y-cy))
                if d<=r:
                    l=max(1,top-(d*top//(r+1)))
                    if not g.W[y][x] and 1<=x<g.w-1 and 1<=y<g.h-1:g.H[y][x]=max(g.H[y][x],l)
    hill(11,9,6,5);hill(33,26,6,5);hill(32,8,4,4);hill(12,27,4,4);hill(22,18,3,3)
    # muros de piedra del parque (deslizables) formando pasillos
    g.wall(18,3,1,8,5);g.wall(24,3,1,8,5);g.wall(18,25,1,8,5);g.wall(24,25,1,8,5)
    g.wall(2,16,10,1,6);g.wall(2,20,10,1,6);g.wall(32,15,10,1,6);g.wall(32,19,10,1,6)
    g.plat(2,17,10,3,4);g.plat(32,16,10,3,4)
    # lago de piedras (piedras de salto)
    for (x,y,l) in [(19,14,1),(21,13,2),(23,15,3),(25,13,2),(27,15,1),(20,20,2),(22,22,3),(24,20,2),(26,22,1)]:g.plat(x,y,2,2,l)
    # pabellones: plataformas elevadas con escalera
    g.plat(36,29,5,4,3);g.stairs(35,30,2,1,'E',1) if False else None
    g.plat(3,28,6,5,3);g.stairs(9,29,3,2,'E',1)
    g.plat(3,3,5,5,2);g.plat(37,3,5,5,2);g.stairs(3,8,3,1,'S',1) if False else None
    g.plat(14,31,6,3,2);g.plat(28,2,6,3,2)
    return g,(3.5,14.5,0.0)
def e9():  # AUTOPISTA EN RUINAS 52x24: tramos elevados, vigas, rampas
    g=G(52,24)
    # viaducto central elevado (pasos) y rampas en ambos extremos
    g.plat(14,9,24,6,6)
    g.stairs(13,10,4,6,'W',5) if False else None
    for k in range(5):g.plat(13-k,9,1,6,5-k)
    for k in range(5):g.plat(38+k,9,1,6,5-k)
    # carriles laterales a media altura con huecos (saltos)
    for x in range(8,46,8):
        g.plat(x,2,5,3,3);g.plat(x+3,19,5,3,3)
    # muros de contención largos deslizables
    g.wall(8,7,18,1,6);g.wall(26,16,18,1,6)
    g.wall(2,2,1,0,0)
    g.wall(20,1,1,5,5);g.wall(32,18,1,5,5)
    # vallas / camiones volcados como paredes cortas (3x1)
    g.wall(6,11,3,1,3);g.wall(44,12,3,1,3);g.wall(10,14,1,3,2);g.wall(41,6,1,3,2)
    # trampolines (pasos) para subir al viaducto
    for (x,y,l) in [(16,4,1),(20,5,2),(24,5,3),(28,5,4),(32,5,5)]:g.plat(x,y,2,2,l)
    for (x,y,l) in [(36,18,1),(32,17,2),(28,17,3),(24,17,4),(20,17,5)]:g.plat(x,y,2,2,l)
    return g,(2.5,12.5,0.0)
def e10():  # AZOTEA FINAL 36x36: arena multinivel con anillo de cornisas y torres
    g=G(36,36)
    g.plat(8,8,20,20,2);g.plat(11,11,14,14,4);g.plat(14,14,8,8,6)
    g.stairs(16,28,4,1,'S',1) if False else None
    g.plat(16,28,4,1,1);g.plat(16,7,4,1,1);g.plat(28,16,1,4,1);g.plat(7,16,1,4,1)
    g.plat(17,25,2,1,3);g.plat(17,10,2,1,3);g.plat(10,17,1,2,3);g.plat(25,17,1,2,3)
    # torres-muro en las esquinas (4 L)
    for (x,y,sx,sy,t) in [(3,3,1,1,2),(31,3,-1,1,3),(3,31,1,-1,4),(31,31,-1,-1,2)]:
        g.wall(x if sx>0 else x-4,y if sy>0 else y-1,5,2,t)
        g.wall(x if sx>0 else x+1,y if sy>0 else y-4,2,6 if sy>0 else 6,t) if False else None
    # muros paralelos para wall-jump en los laterales
    g.wall(3,12,1,12,5);g.wall(7,12,1,12,5) if False else None
    g.wall(30,10,1,2,1) if False else None
    g.wall(2,11,6,1,5);g.wall(2,24,6,1,5);g.plat(2,12,6,12,3)
    g.wall(28,11,6,1,6);g.wall(28,24,6,1,6);g.plat(28,12,6,12,3)
    for (x,y,l) in [(5,4,2),(11,4,3),(19,3,2),(25,4,3),(5,30,2),(11,31,3),(19,31,2),(25,30,3)]:g.plat(x,y,2,2,l)
    return g,(3.5,26.0,-0.78)
if __name__=='__main__':
    out={'maps':{},'h':{},'start':{}}
    for n,f in (('e7',e7),('e8',e8),('e9',e9),('e10',e10)):
        g,st=f();free=g.finish(st);r,h=g.rows();out['maps'][n]=r;out['h'][n]=h;out['start'][n]=list(st)
        print(n,g.w,g.h,'libres',free);g.png(f'prev_{n}.png')
    json.dump(out,open('maps2.json','w'))
