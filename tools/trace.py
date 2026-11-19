# Trace logo PNG (dari deck) jadi SVG path satu warna via potrace
import subprocess,sys,re,os
from PIL import Image
A='../05-aset-brand/dari-deck/'
def trace(src,name):
    im=Image.open(A+src);a=im.split()[-1];bb=a.getbbox();a=a.crop(bb)
    bw=a.point(lambda v:0 if v>127 else 255).convert('1')
    p=f'/tmp/{name}.pbm' if not os.environ.get('TMPDIR') else os.environ['TMPDIR']+f'/{name}.pbm'
    bw.save(p)
    out=subprocess.run(['potrace','-s','-o','-','--flat','-t','4','-a','1.0','-O','0.4',p],capture_output=True,text=True).stdout
    vb=re.search(r'viewBox="([^"]+)"',out).group(1);g=re.search(r'<g transform="([^"]+)"',out).group(1)
    paths=re.findall(r' d="([^"]+)"',out)
    print(name,bb,vb,len(''.join(paths)))
    return dict(w=bb[2]-bb[0],h=bb[3]-bb[1],vb=vb,g=g,d=' '.join(paths))
import json
json.dump({'gonjong':trace('gonjong-polos-merah.png','gonjong'),'wordmark':trace('wordmark-merah.png','wordmark')},open('tools/logo-trace.json','w'))
