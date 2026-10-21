import sys,os;sys.path.insert(0,'.')
import gd,palettes
ALIAS={'sergeant.glb':'soldier.glb','chaingunner.glb':'soldier.glb','hellknight.glb':'baron.glb','specter.glb':'pinky.glb'}
_pf=gd.palette_for
gd.palette_for=lambda n:_pf(ALIAS.get(n,n))
def build_sergeant():
    b=gd.build_soldier();b.name='sergeant'
    # escopeta de dos cañones + hombreras anchas
    b.cyl([0.12,1.00,.74],[0.12,1.00,1.06],.04,.035,'rifle','metal',8);b.cyl([0.20,1.00,.74],[0.20,1.00,1.06],.04,.035,'rifle','metal',8)
    b.box([0.16,.94,.55],[0.16,.07,.34],'rifle','dark')
    for sx,sd in((-1,'L'),(1,'R')):
        b.sphere([sx*.40,1.38,0],[.17,.10,.20],f'upper_arm_{sd}','armor',8,5)
    b.box([0,1.52,-.2],[.5,.2,.1],'chest','metal')
    return b
def build_chaingunner():
    b=gd.build_soldier();b.name='chaingunner'
    # minigun de 4 cañones y mochila de municion
    for ox,oy in((.06,.06),(-.06,.06),(.06,-.06),(-.06,-.06)):
        b.cyl([0.16+ox,1.00+oy,.74],[0.16+ox,1.00+oy,1.18],.028,.024,'rifle','metal',6)
    b.cyl([0.16,1.00,.96],[0.16,1.00,1.02],.12,.12,'rifle','dark',8)
    b.box([0,1.30,-.34],[.50,.55,.26],'chest','metal');b.box([0,1.30,-.50],[.36,.18,.08],'chest','dark')
    for sx,sd in((-1,'L'),(1,'R')):
        b.sphere([sx*.42,1.38,0],[.20,.13,.22],f'upper_arm_{sd}','armor',8,5)
    b.sphere([0,1.74,0.0],[.28,.12,.26],'head','armor',9,5)
    return b
def build_hellknight():
    b=gd.build_baron();b.name='hellknight'
    # cuernos laterales y placas en los hombros
    for sx in(-1,1):
        b.tube([[sx*.28,2.40,.05],[sx*.62,2.46,.08],[sx*.86,2.66,.10]],[.10,.08,.015],'head','bone',8)
        b.sphere([sx*.62,1.98,0],[.26,.14,.26],'spine','bone',9,5)
    b.box([0,2.10,.30],[.52,.40,.08],'spine','dark')
    return b
def build_specter():
    b=gd.build_pinky();b.name='specter'
    for sx in(-1,1):b.cone([sx*.42,1.0,.92],[sx*.62,1.20,1.04],.07,'head','bone',6)
    return b
gd.BUILDERS.clear();gd.BUILDERS.update({'sergeant.glb':build_sergeant,'chaingunner.glb':build_chaingunner,'hellknight.glb':build_hellknight,'specter.glb':build_specter})
gd.OUT='/tmp/gd2';os.makedirs(gd.OUT,exist_ok=True)
for fn,bf in gd.BUILDERS.items():
    print(fn,gd.write_glb(bf(),fn))
