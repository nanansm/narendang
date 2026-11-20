# Rakit public/index.html (HTML statis, CSS inline) dari data + logo trace
import json,re,html,os,urllib.parse
SITE='https://narendang.com/'
B='../00-brief/'
WA_TEXT='Hi! saya dapat nomor ini dari Instagram, saya mau tanya informasi, Promo dan Pricelist di Narendang Bandung'
if os.path.exists(B+'linktree-sosmed.json'):
    soc=dict(json.load(open(B+'linktree-sosmed.json')));lama=json.load(open(B+'linktree-lama.json'))
    wa_btn=[u for _,u in lama if 'whatsapp' in u][0]
    WA=re.sub(r'\D','',urllib.parse.parse_qs(urllib.parse.urlparse(wa_btn).query)['phone'][0])
    WA_URL='https://wa.me/'+WA+'?text='+urllib.parse.quote(WA_TEXT)
else:  # tanpa folder 00-brief: pakai tautan yang tersimpan di repo
    soc=json.load(open('tools/tautan.json'));WA_URL=soc['WA_URL'];WA=re.sub(r'\D','',WA_URL.split('?')[0])
EMAIL=soc['EMAIL_ADDRESS'].replace('mailto:','')
IG=soc['INSTAGRAM'];TT=soc['TIKTOK'];FB=soc['FACEBOOK']
L=dict(
 paket='https://drive.google.com/file/d/1_N6kEI7wz-DQBLiqoVIXI3FNaNFYAz9z/view',
 gofood='https://gofood.link/a/Htiz8JG',
 shopee='https://shopee.co.id/universal-link/now-food/shop/21195163?deep_and_deferred=1&shareChannel=copy_link',
 maps_kal='https://goo.gl/maps/2MAngdNgNLFF7DMJ8',
 maps_cis='https://maps.app.goo.gl/2pqmeNbjDpwAFavY8',
 menu_kal='#',menu_cis='#')
T=json.load(open('tools/logo-trace.json'))
def logo(k,cls,label):
    t=T[k];return f'<svg class="{cls}" viewBox="0 0 {t["w"]} {t["h"]}" role="img" aria-label="{label}"><g transform="{t["g"]}"><path d="{t["d"]}"/></g></svg>'
GONJ=logo('gonjong','gonjong','')
GONJ_IKON=logo('gonjong','gonjong-ikon','')
BOW=open('tools/mote-bow.svg').read().replace('<svg ','<svg class="bow" role="img" aria-label="MOTE" ',1)
WORD=logo('wordmark','wordmark','Narendang')

ICON={
'wa':'<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.8-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.2-.2-.5-.3z"/>',
'ig':'<path d="M12 7.2A4.8 4.8 0 1 0 16.8 12 4.8 4.8 0 0 0 12 7.2zm0 7.9A3.1 3.1 0 1 1 15.1 12 3.1 3.1 0 0 1 12 15.1zM17 5.9a1.1 1.1 0 1 0 1.1 1.1A1.1 1.1 0 0 0 17 5.9zM21.9 7.1a5.6 5.6 0 0 0-1.5-4 5.6 5.6 0 0 0-4-1.5C14.8 1.5 9.2 1.5 7.6 1.6a5.6 5.6 0 0 0-4 1.5 5.6 5.6 0 0 0-1.5 4c-.1 1.6-.1 7.2 0 8.8a5.6 5.6 0 0 0 1.5 4 5.6 5.6 0 0 0 4 1.5c1.6.1 7.2.1 8.8 0a5.6 5.6 0 0 0 4-1.5 5.6 5.6 0 0 0 1.5-4c.1-1.6.1-7.2 0-8.8zm-2.2 11a3.2 3.2 0 0 1-1.8 1.8c-1.3.5-4.3.4-5.9.4s-4.6.1-5.9-.4a3.2 3.2 0 0 1-1.8-1.8c-.5-1.3-.4-4.3-.4-5.9s-.1-4.6.4-5.9A3.2 3.2 0 0 1 6.1 4.1C7.4 3.6 10.4 3.7 12 3.7s4.6-.1 5.9.4a3.2 3.2 0 0 1 1.8 1.8c.5 1.3.4 4.3.4 5.9s.1 4.6-.4 5.9z"/>',
'tt':'<path d="M19.6 6.7a4.8 4.8 0 0 1-3.8-4.2V2h-3.4v13.4a2.9 2.9 0 1 1-2-2.7V9.2a6.3 6.3 0 1 0 5.4 6.2V8.6a8.2 8.2 0 0 0 4.8 1.5V6.8a4.8 4.8 0 0 1-1-.1z"/>',
'fb':'<path d="M14 8.5V6.7c0-.8.2-1.3 1.4-1.3H17V2.2A21 21 0 0 0 14.6 2C12.2 2 10.6 3.5 10.6 6.1v2.4H8v3.4h2.6V22H14V11.9h2.7l.4-3.4z"/>',
'mail':'<path d="M3 5h18v14H3zm2 2v.5l7 4.6 7-4.6V7zm14 2.9-7 4.6-7-4.6V17h14z"/>',
'panah':'<path d="M7 17 17 7M9 7h8v8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"/>',
'pin':'<path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 14.5 9 2.5 2.5 0 0 1 12 11.5z"/>',
'menu':'<path d="M5 3h11l3 3v15H5zm2 2v14h10V7h-2V5zm2 4h6v1.6H9zm0 3.4h6V14H9zm0 3.4h4v1.6H9z"/>',
}
def ik(k,c='ik'): return f'<svg class="{c}" viewBox="0 0 24 24" aria-hidden="true">{ICON[k]}</svg>'
# bunga piksel (label deck)
BUNGA='<svg class="bunga" viewBox="0 0 7 7" aria-hidden="true" shape-rendering="crispEdges"><path d="M3 0h1v2H3zM0 3h2v1H0zM5 3h2v1H5zM3 5h1v2H3zM2 2h3v3H2z"/></svg>'
def lb(txt,cls=''): return f'<p class="lb {cls}">{BUNGA}{txt}</p>'
GJ=T['gonjong']
LG_KAL=logo('gonjong','lg-kal','Logogram Narendang Jl. Kalimantan')
LG_CIS='<img class="lg-cis" src="/assets/mark-cisangkuy.webp" width="240" height="140" alt="Logogram Narendang Jl. Cisangkuy 58">'

def baris(logo,judul,ket,url,ikon='panah'):
    return f'<li><a class="baris" href="{html.escape(url)}" target="_blank" rel="noopener"><span class="logo-k">{logo}</span><span class="isi"><b>{judul}</b><small>{ket}</small></span><span class="pnh-k">{ik(ikon,"ik pnh")}</span></a></li>'

def tombol(url,teks,ikon,cls):
    ext='' if url=='#' else ' target="_blank" rel="noopener"'
    return f'<a class="tb {cls}" href="{html.escape(url)}"{ext}>{ik(ikon)}<span>{teks}</span>{ik("panah","ik tb-pnh")}</a>'

ld={"@context":"https://schema.org","@graph":[
 {"@type":"Organization","@id":SITE+"#brand","name":"Narendang","slogan":"Nendang Rasanya!","url":SITE,"logo":SITE+"assets/ikon-512.png","email":EMAIL,"telephone":"+"+WA,"sameAs":[IG,TT,FB]},
 {"@type":"Restaurant","name":"Narendang Jl. Kalimantan","servesCuisine":["Masakan Padang","Rendang"],"parentOrganization":{"@id":SITE+"#brand"},"telephone":"+"+WA,
  "address":{"@type":"PostalAddress","streetAddress":"Jl. Kalimantan","addressLocality":"Bandung","addressRegion":"Jawa Barat","addressCountry":"ID"},
  "geo":{"@type":"GeoCoordinates","latitude":-6.913934,"longitude":107.6151509},"hasMap":L['maps_kal'],"acceptsReservations":True,"image":SITE+"assets/og.jpg"},
 {"@type":"Restaurant","name":"Narendang Jl. Cisangkuy 58","servesCuisine":["Masakan Padang","Rendang"],"parentOrganization":{"@id":SITE+"#brand"},"telephone":"+"+WA,
  "address":{"@type":"PostalAddress","streetAddress":"Jl. Cisangkuy No. 58","addressLocality":"Bandung","addressRegion":"Jawa Barat","addressCountry":"ID"},
  "geo":{"@type":"GeoCoordinates","latitude":-6.9024267,"longitude":107.6217764},"hasMap":L['maps_cis'],"acceptsReservations":True,"image":SITE+"assets/og.jpg"}]}

TITLE='Narendang — Rumah Makan Padang di Bandung · Jl. Kalimantan & Cisangkuy 58'
DESC='Reservasi, Nasi Box, dan Prasmanan Narendang lewat WhatsApp. Dua outlet di Bandung: Jl. Kalimantan dan Jl. Cisangkuy 58. Nendang Rasanya!'
css=open('tools/style.css').read()
css=re.sub(r'/\*.*?\*/','',css,flags=re.S);css=re.sub(r'\s+',' ',css);css=re.sub(r'\s*([{}:;,>])\s*',r'\1',css).replace(';}','}')

page=f'''<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<meta name="description" content="{html.escape(DESC)}">
<link rel="canonical" href="{SITE}">
<meta name="theme-color" content="#E32B33">
<meta property="og:type" content="website"><meta property="og:site_name" content="Narendang"><meta property="og:locale" content="id_ID">
<meta property="og:title" content="{html.escape(TITLE)}"><meta property="og:description" content="{html.escape(DESC)}">
<meta property="og:url" content="{SITE}"><meta property="og:image" content="{SITE}assets/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/fonts/philosopher-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/barlow-condensed-600.woff2" as="font" type="font/woff2" crossorigin>
<style>{css}</style>
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False,separators=(',',':'))}</script>
</head>
<body>
<div class="pita" aria-hidden="true"></div>
<main class="kol">
<header class="kepala">
{GONJ}
<h1 class="logo">{WORD}<span class="sr">Narendang, rumah makan Padang di Bandung</span></h1>
<p class="tagline"><span>Nendang</span> Rasanya!</p>
<p class="garis-lb">Rumah Makan Padang · Bandung</p>
</header>

<a class="cta" href="{html.escape(WA_URL)}" target="_blank" rel="noopener">
<span class="cta-isi"><b>Reservasi</b><small>Nasi Box · Prasmanan · WhatsApp</small></span>{ik('wa','ik cta-ik')}
</a>

{lb('Dua outlet')}
<div class="outlet">
<section class="kartu krem" aria-labelledby="o1">
<div class="atas"><p class="nomor">Outlet 01</p>{LG_KAL}</div>
<h2 id="o1"><span class="jl">Jl.</span>Kalimantan</h2>
<p class="janji">Sudah&nbsp;terbukti nendang&nbsp;rasanya.</p>
<p class="bukti"><b>4,8</b><span>1.312 ulasan Google</span></p>
{tombol(L['maps_kal'],'Rute','pin','tb-isi')}
<a class="menu-ln" href="{L['menu_kal']}">Lihat menu</a>
</section>
<section class="kartu kalio" aria-labelledby="o2">
<div class="atas"><p class="nomor">Outlet 02</p>{LG_CIS}</div>
<h2 id="o2"><span class="jl">Jl.</span>Cisangkuy&nbsp;58</h2>
<p class="janji">Paling&nbsp;cocok buat&nbsp;rombongan dan&nbsp;keluarga.</p>
<p class="bukti"><b>178</b><span>kursi dan 2 ruang VIP</span></p>
{tombol(L['maps_cis'],'Rute','pin','tb-isi')}
<a class="menu-ln" href="{L['menu_cis']}">Lihat menu</a>
</section>
</div>


{lb('Pesan antar &amp; katering')}
<ul class="daftar">
{baris(GONJ_IKON,'Paket Box &amp; Prasmanan','Daftar paket (PDF)',L['paket'])}
{baris('<img src="/assets/ikon-gofood.svg" alt="" width="30" height="28">','GoFood','Pesan antar',L['gofood'])}
{baris('<img src="/assets/ikon-shopeefood.svg" alt="" width="24" height="27">','ShopeeFood','Pesan antar',L['shopee'])}
</ul>

{lb('Ulas di Google')}
<ul class="daftar">
{baris('<img src="/assets/mark-cisangkuy.webp" alt="" width="34" height="20">','Ulas Jl. Cisangkuy 58','Google Maps · outlet kedua',L['maps_cis'])}
{baris(GONJ_IKON,'Ulas Jl. Kalimantan','Google Maps · outlet pertama',L['maps_kal'])}
</ul>

<nav class="sosmed" aria-label="Media sosial Narendang">
<a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram Narendang">{ik('ig')}</a>
<a href="{TT}" target="_blank" rel="noopener" aria-label="TikTok Narendang">{ik('tt')}</a>
<a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook Narendang">{ik('fb')}</a>
<a href="mailto:{EMAIL}" aria-label="Email Narendang">{ik('mail')}</a>
</nav>
<p class="akun">@narendang_bdg</p>
</main>
<footer class="kaki">
<div class="pita" aria-hidden="true"></div>
<p class="kaki-tag"><span>Nendang</span><br>Rasanya!</p>
<p class="kaki-c">© 2026 Narendang{BOW}Bandung</p>
</footer>
</body>
</html>
'''
open('public/index.html','w').write(page)
open('public/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
open('public/sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE}</loc><changefreq>monthly</changefreq></url></urlset>\n')
open('public/_headers','w').write('/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n/assets/*\n  Cache-Control: public, max-age=2592000\n')
print('index.html',len(page))
