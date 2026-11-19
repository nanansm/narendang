# Aset raster: mark songket, noise kertas, favicon, OG image
import json,random,os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
A='../05-aset-brand/dari-deck/';P='public/assets/'
m=Image.open(A+'mark-songket-krem-lubang.png');m.thumbnail((120,120));m.save(P+'mark-prime-krem.webp',quality=88,method=6)
m2=Image.open(A+'mark-songket-2warna.png');m2.thumbnail((240,240));m2.save(P+'mark-prime.webp',quality=88,method=6)
# noise butir kertas: alpha rendah
random.seed(5);n=Image.new('LA',(160,160))
px=[(random.choice((40,60,90)),random.randint(0,22)) if random.random()<.55 else (0,0) for _ in range(160*160)]
n.putdata(px);n.convert('RGBA').save(P+'butir.webp',lossless=True,quality=100,method=6)
g=Image.open(A+'gonjong-polos-merah.png')
def ikon(s,bg=None,pad=.14):
    c=Image.new('RGBA',(s,s),bg or (0,0,0,0));t=g.copy();t.thumbnail((int(s*(1-2*pad)),int(s*(1-2*pad))),Image.LANCZOS)
    c.alpha_composite(t,((s-t.width)//2,(s-t.height)//2));return c
ikon(32).save(P+'favicon-32.png');ikon(180,(239,231,218,255)).save(P+'apple-touch-icon.png');ikon(512,(239,231,218,255)).save(P+'ikon-512.png')
# OG 1200x630
og=Image.new('RGB',(1200,630),'#EFE7DA')
pita=Image.new('RGB',(1200,48));
import re
sv=open('public/assets/pita.svg').read();pt=Image.new('RGB',(20,12));dd=ImageDraw.Draw(pt)
for fill,d in re.findall(r'fill="([^"]+)"(?: d="([^"]*)")?',sv):
    if not d: dd.rectangle((0,0,19,11),fill=fill);continue
    for x,y,w in re.findall(r'M(\d+) (\d+)h(\d+)',d): dd.rectangle((int(x),int(y),int(x)+int(w)-1,int(y)),fill=fill)
pt=pt.resize((80,48),Image.NEAREST)
for x in range(0,1200,80): og.paste(pt,(x,0)); og.paste(pt,(x,582))
gj=g.copy();gj.thumbnail((250,250),Image.LANCZOS);og.paste(gj,((1200-gj.width)//2,120),gj)
w=Image.open(A+'wordmark-merah.png');w.thumbnail((560,200),Image.LANCZOS);og.paste(w,((1200-w.width)//2,120+gj.height+28),w)
d=ImageDraw.Draw(og);f=ImageFont.truetype(os.environ['TMPDIR']+'/ph700.ttf',54)
t1,t2='Nendang ','Rasanya!';w1=d.textlength(t1,font=f);w2=d.textlength(t2,font=f);x=(1200-w1-w2)/2;y=120+gj.height+28+w.height+30
d.text((x,y),t1,font=f,fill='#2E1712');d.text((x+w1,y),t2,font=f,fill='#E32B33')
og.save(P+'og.jpg',quality=84,optimize=True,progressive=True)
for f in sorted(os.listdir(P)): print(f,os.path.getsize(P+f))
