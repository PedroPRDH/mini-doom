import sys,os,json,glob,base64,struct
import numpy as np
sys.path.insert(0,'.')
import meshoptimizer as mo
SRC=sys.argv[1] if len(sys.argv)>1 else '../out/models2'
def parse(path):
    d=open(path,'rb').read();jl,_=struct.unpack('<II',d[12:20]);j=json.loads(d[20:20+jl]);bo=20+jl+8;binb=d[bo:]
    return j,binb
def acc(j,binb,i):
    a=j['accessors'][i];bv=j['bufferViews'][a['bufferView']];o=bv.get('byteOffset',0)+a.get('byteOffset',0)
    nc={'SCALAR':1,'VEC2':2,'VEC3':3,'VEC4':4}[a['type']];dt={5126:'<f4',5125:'<u4',5123:'<u2',5121:'u1'}[a['componentType']]
    return np.frombuffer(binb,dtype=dt,count=a['count']*nc,offset=o).reshape(-1,nc) if nc>1 else np.frombuffer(binb,dtype=dt,count=a['count'],offset=o)
out={};tot=[0,0,0]
for f in sorted(glob.glob(SRC+'/*.glb')):
    n=os.path.basename(f)[:-4];j,b=parse(f)
    meshes=[]
    for mi,mesh in enumerate(j['meshes']):
        for pr in mesh['primitives']:
            P=acc(j,b,pr['attributes']['POSITION']).astype(np.float32);I=acc(j,b,pr['indices']).astype(np.uint32)
            meshes.append((P,I))
    if len(meshes)!=1 or n in('barrel',):continue
    res=[]
    for P,I in meshes:
        lv=[]
        for ratio,err in((.5,.03),(.2,.09)):
            dst=np.zeros(len(I),dtype=np.uint32)
            nidx=mo.simplify(dst,I,P,target_index_count=max(36,int(len(I)*ratio)),target_error=err)
            lv.append(dst[:nidx].astype('<u2' if len(P)<65536 else '<u4'))
        res.append([x.tobytes() for x in lv]);tot[0]+=len(I)//3;tot[1]+=len(lv[0])//3;tot[2]+=len(lv[1])//3
        print(n,'verts',len(P),'tris',len(I)//3,'->',len(lv[0])//3,len(lv[1])//3)
    out[n]=[[base64.b64encode(x).decode() for x in r] for r in res]
json.dump(out,open('../out/lod.json','w'),separators=(',',':'))
print('total',tot,os.path.getsize('../out/lod.json')//1024,'KB')
