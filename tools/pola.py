# Gambar ulang songket piksel Narendang (deck hlm 50) jadi SVG grid, petak tegas
def rects(cells,color,c=1):
    # gabung petak sebaris jadi rect panjang -> path
    rows={}
    for x,y in cells: rows.setdefault(y,set()).add(x)
    d=[]
    for y,xs in sorted(rows.items()):
        xs=sorted(xs);s=p=xs[0]
        for x in xs[1:]+[None]:
            if x==p+1: p=x;continue
            d.append(f'M{s*c} {y*c}h{(p-s+1)*c}v{c}h-{(p-s+1)*c}z')
            if x is not None: s=p=x
    return f'<path fill="{color}" d="{"".join(d)}"/>'

def pita(merah='#B71C26',emas='#F2A23A',krem='#F3E9DA'):
    W,H=20,12;o=[];e=[];k=[]
    for x in range(W): o.append((x,0)); o.append((x,6))
    for y in range(1,6):
        for x in range(W):
            for cx,isi in((10,1),(0,0),(20,0)):
                dx,dy=abs(x-cx),abs(y-3)
                if dx+dy==2: e.append((x,y))
                if isi and dx+dy==0: k.append((x,y))
    for y in range(7,12):
        for x in range(W):
            dy=y-9
            for cx in (5,):
                if abs(x-cx)==abs(dy): k.append((x,y))
            for cx in (15,):
                if abs(x-cx)<=y-7: e.append((x,y))
    body=f'<rect width="{W}" height="{H}" fill="{merah}"/>'+rects(set(o)|set(e),emas)+rects(set(k),krem)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*2}" height="{H*2}" shape-rendering="crispEdges">{body}</svg>'

def songket(latar,motif):
    # ubin 24x24: belah ketupat bertangga + salib tengah, spiral kunci di sudut
    N=24;c=set();m=12
    for y in range(N):
        for x in range(N):
            d=abs(x-m)+abs(y-m)
            if d in(9,5) or (d<=2 and (x==m or y==m)): c.add((x,y))
    sp=['#####','....#','###.#','#...#','#####']
    for j,r in enumerate(sp):
        for i,ch in enumerate(r):
            if ch=='#':
                for X,Y in((i,j),(N-1-i,j),(i,N-1-j),(N-1-i,N-1-j)): c.add((X,Y))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {N} {N}" width="{N*6}" height="{N*6}" shape-rendering="crispEdges"><rect width="{N}" height="{N}" fill="{latar}"/>{rects(c,motif)}</svg>'

if __name__=='__main__':
    open('public/assets/pita.svg','w').write(pita())
    open('public/assets/songket-merah.svg','w').write(songket('#E32B33','#CF2530'))
    open('public/assets/songket-kalio.svg','w').write(songket('#2E1712','#3A1F18'))
    import os;[print(f,os.path.getsize('public/assets/'+f)) for f in os.listdir('public/assets')]
