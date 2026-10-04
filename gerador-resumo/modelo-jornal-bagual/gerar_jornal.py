# -*- coding: utf-8 -*-
"""Gerador do Jornal Bagual (Lógica Psicológica).
Uso:  python3 gerar_jornal.py edicao.json saida.pdf
Gera o PDF A4 (capa + uma página por matéria) e uma prévia PNG de cada página."""
import base64, re, sys, os, html as H
from bs4 import BeautifulSoup, NavigableString
import pyphen
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))
FS = AQUI + "/fontes/"
HY = pyphen.Pyphen(lang="pt_BR")

def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()

def fonte(fam, arq, peso, estilo="normal"):
    return "@font-face{font-family:%s;src:url(data:font/woff2;base64,%s);font-weight:%s;font-style:%s}" % (fam, b64(FS + arq), peso, estilo)

FONTES = "".join([
    fonte("Gotica", "unifrakturmaguntia-latin-400-normal.woff2", 400),
    fonte("Manchete", "playfair-display-latin-700-normal.woff2", 700),
    fonte("Manchete", "playfair-display-latin-900-normal.woff2", 900),
    fonte("Manchete", "playfair-display-latin-400-italic.woff2", 400, "italic"),
    fonte("Manchete", "playfair-display-latin-700-italic.woff2", 700, "italic"),
    fonte("Texto", "pt-serif-latin-400-normal.woff2", 400),
    fonte("Texto", "pt-serif-latin-700-normal.woff2", 700),
    fonte("Texto", "pt-serif-latin-400-italic.woff2", 400, "italic"),
    fonte("Antiga", "old-standard-tt-latin-400-normal.woff2", 400),
    fonte("Antiga", "old-standard-tt-latin-700-normal.woff2", 700),
    fonte("Antiga", "old-standard-tt-latin-400-italic.woff2", 400, "italic"),
    fonte("Marca", "dm-serif-display-latin-400-normal.woff2", 400),
    fonte("Marca", "dm-serif-display-latin-400-italic.woff2", 400, "italic"),
    fonte("Jak", "plus-jakarta-sans-latin-500-normal.woff2", 500),
    fonte("Jak", "plus-jakarta-sans-latin-700-normal.woff2", 700),
    fonte("Jak", "plus-jakarta-sans-latin-800-normal.woff2", 800),
    fonte("Fonte", "source-serif-4-latin-400-normal.woff2", 400),
    fonte("Fonte", "source-serif-4-latin-600-normal.woff2", 600),
    fonte("Fonte", "source-serif-4-latin-700-normal.woff2", 700),
    fonte("Fonte", "source-serif-4-latin-400-italic.woff2", 400, "italic"),
])
TEMA = "a"
JULIO = AQUI + "/assets/julio.jpg"

def hifenizar(txt):
    txt = txt.replace(" \u2014 ", ", ").replace("\u2014", ", ")
    return re.sub(r"[A-Za-zÀ-ÿ]{7,}", lambda m: HY.inserted(m.group(0), hyphen="­"), txt)

def interno(tag):
    """HTML interno do elemento, com hifenização nos textos e sem links."""
    if tag is None:
        return ""
    t = BeautifulSoup(str(tag), "html.parser")
    for a in t.find_all("a"):
        a.decompose()
    for s in list(t.find_all(string=True)):
        if isinstance(s, NavigableString) and s.strip():
            s.replace_with(NavigableString(hifenizar(str(s))))
    raiz = t.find()
    return "".join(str(c) for c in raiz.contents).strip()

def tinta(svg):
    def cor(m):
        h = m.group(1)
        if len(h) == 3: h = "".join(c*2 for c in h)
        r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
        L = 0.3*r + 0.59*g + 0.11*b
        L = L if L > 0.8 else L ** 1.9
        v = lambda base: int(max(0, min(255, L * base)))
        return "#%02x%02x%02x" % (v(239), v(232), v(214)) if L > 0.8 else "#%02x%02x%02x" % (int(28 + L*190), int(26 + L*186), int(21 + L*170))
    svg = re.sub(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", cor, svg)
    return re.sub(r"font-family=.[^'\"]*sans-serif.", "font-family='Antiga,serif'", svg).replace("Jak,sans-serif", "Antiga,serif").replace("News,serif", "Manchete,serif")

def ler(caminho):
    s = BeautifulSoup(open(caminho, encoding="utf-8").read(), "html.parser")
    d = {"tema": interno(s.select_one("p.tema")), "itens": []}
    for art in s.select("article.nw"):
        it = {
            "k": art.select_one(".nw-k").get_text(" ", strip=True),
            "h": art.select_one("h3").get_text(" ", strip=True),
            "r": interno(art.select_one("p.nw-r")),
            "ficha": [(c.b.get_text(strip=True), c.get_text(" ", strip=True)[len(c.b.get_text(strip=True)):].strip()) for c in art.select(".ficha .chip")],
            "svg": (tinta if TEMA == "classico" else str)(str(art.select_one("figure svg") or "")),
            "cap": interno(art.select_one("figcaption")),
            "muda": [interno(li) for li in art.select(".nw-c:not(.lim) li")],
            "nao": [interno(li) for li in art.select(".nw-c.lim li")],
            "acao": interno(art.select_one("p.ac")),
            "perg": "",
            "ref": interno(art.select_one(".nw-f")),
        }
        pg = art.select_one("p.pg")
        if pg:
            pg.b.decompose()
            it["perg"] = pg.get_text(" ", strip=True)
        d["itens"].append(it)
    mt = s.find(string=re.compile("Nota de método"))
    d["metodo"] = ""
    if mt:
        bloco = mt.find_parent("div")
        if bloco is not None:
            txt = bloco.get_text(" ", strip=True).replace("Nota de método", "", 1).strip()
            d["metodo"] = hifenizar(H.escape(txt))
    return d

CSS = FONTES + r"""
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box}
html,body{margin:0;background:#efe8d6}
body{color:#1c1a15;font-family:Texto,serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pag{width:210mm;height:297mm;padding:11mm 12mm 9mm;position:relative;overflow:hidden;display:flex;flex-direction:column;page-break-after:always;
  background:#efe8d6 radial-gradient(ellipse at 30% 20%,rgba(255,250,235,.55),rgba(0,0,0,0) 60%)}
.pag:last-child{page-break-after:auto}
/* topo da capa */
.linha-topo{display:flex;justify-content:space-between;font-family:Antiga,serif;font-size:7.6pt;letter-spacing:.06em;text-transform:uppercase;border-top:.6pt solid #1c1a15;border-bottom:.6pt solid #1c1a15;padding:1.3mm 0}
.cabeca{text-align:center;padding:2.5mm 0 1.2mm}
.cabeca .nome{font-family:Gotica,serif;font-size:58pt;line-height:1;letter-spacing:.01em}
.lema{display:flex;justify-content:space-between;align-items:center;font-family:Antiga,serif;font-style:italic;font-size:8.4pt;border-top:2.2pt solid #1c1a15;border-bottom:.6pt solid #1c1a15;padding:1.2mm 0;margin-bottom:1mm}
.lema b{font-style:normal;font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:7.4pt}
.fio2{height:2.6pt;border-top:.6pt solid #1c1a15;border-bottom:.6pt solid #1c1a15;margin:0 0 3mm}
/* topo das páginas internas */
.topo-int{display:flex;justify-content:space-between;align-items:baseline;border-bottom:.6pt solid #1c1a15;padding-bottom:1.2mm;margin-bottom:.8mm;font-family:Antiga,serif;font-size:8pt;letter-spacing:.05em;text-transform:uppercase}
.topo-int .n{font-family:Gotica,serif;font-size:15pt;text-transform:none;letter-spacing:0}
.topo-int+.fio2{margin-bottom:4mm}
/* índice e editorial */
.abre{display:grid;grid-template-columns:1fr 2.1fr;gap:5mm;border-bottom:.6pt solid #1c1a15;padding-bottom:3mm;margin-bottom:3.5mm}
.indice{border-right:.6pt solid #1c1a15;padding-right:4mm}
.rot{font-family:Antiga,serif;font-weight:700;font-size:7.4pt;letter-spacing:.14em;text-transform:uppercase;margin-bottom:1.4mm}
.indice ol{margin:0;padding:0;list-style:none;counter-reset:i}
.indice li{counter-increment:i;font-family:Manchete,serif;font-weight:700;font-size:9.6pt;line-height:1.15;padding:1.2mm 0;border-top:.4pt dotted #6b6656}
.indice li::before{content:counter(i) ". ";font-family:Antiga,serif;font-weight:400}
.indice li span{display:block;font-family:Antiga,serif;font-weight:400;font-size:7.4pt;color:#4a463a;margin-top:.5mm}
.editorial p{margin:0;font-family:Texto,serif;font-style:italic;font-size:10pt;line-height:1.38;text-align:justify;hyphens:manual}
.editorial p::first-letter{font-family:Manchete,serif;font-style:normal;font-weight:900;float:left;font-size:31pt;line-height:.86;padding:1mm 1.6mm 0 0}
/* matéria */
.materia{flex:1;display:flex;flex-direction:column;min-height:0}
.retranca{font-family:Antiga,serif;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;display:flex;align-items:center;gap:2.5mm;margin-bottom:1.4mm}
.retranca::after{content:"";flex:1;border-top:.6pt solid #1c1a15}
h2{font-family:Manchete,serif;font-weight:900;font-size:var(--hs,30pt);line-height:1.02;letter-spacing:-.012em;margin:0 0 2mm}
.linha-fina{font-family:Manchete,serif;font-style:italic;font-weight:400;font-size:11.4pt;line-height:1.3;margin:0 0 2mm;color:#2b2820}
.assina{font-family:Antiga,serif;font-size:7.8pt;letter-spacing:.04em;margin-bottom:2.6mm}
.assina b{font-weight:700}
.corpo{flex:1;min-height:0;column-count:var(--col,3);column-gap:4.6mm;column-rule:.4pt solid #8c8672;column-fill:balance;font-size:var(--fs,9.4pt);line-height:1.36}
.corpo p{margin:0 0 .5em;text-align:justify;hyphens:manual;orphans:2;widows:2}
.corpo .abertura::first-letter{font-family:Manchete,serif;font-weight:900;float:left;font-size:3.35em;line-height:.82;padding:.08em .08em 0 0}
.corpo h4{font-family:Antiga,serif;font-weight:700;font-size:.82em;letter-spacing:.14em;text-transform:uppercase;margin:.9em 0 .35em;padding-top:.35em;border-top:.6pt solid #1c1a15;break-after:avoid}
.corpo .item{text-indent:1.1em}
.corpo .item:first-of-type{text-indent:0}
.ficha{border:.6pt solid #1c1a15;padding:1.6mm 2mm;margin:0 0 .7em;break-inside:avoid;font-size:.86em;line-height:1.3}
.ficha .t{font-family:Antiga,serif;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:.86em;text-align:center;border-bottom:.4pt solid #1c1a15;padding-bottom:1mm;margin-bottom:1mm}
.ficha div{padding:.5mm 0;border-bottom:.4pt dotted #8c8672}
.ficha div:last-child{border-bottom:0}
.ficha b{font-family:Antiga,serif;font-weight:700;font-size:.92em;text-transform:uppercase;letter-spacing:.06em;margin-right:1mm}
.nao{background:#e4dcc6;border-top:2pt solid #1c1a15;border-bottom:.6pt solid #1c1a15;padding:1.8mm 2.2mm;margin:.8em 0;break-inside:avoid}
.nao .t{font-family:Antiga,serif;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:.8em;margin-bottom:1mm}
.nao p{font-size:.94em;margin:0 0 .45em}
.nao p:last-child{margin:0}
.nao p::before{content:"■ ";font-size:.7em;vertical-align:.12em}
.olho{break-inside:avoid;margin:.7em 0 .9em;padding:2mm 0;border-top:1.6pt solid #1c1a15;border-bottom:.6pt solid #1c1a15;text-align:center}
.olho .t{font-family:Antiga,serif;font-size:.74em;letter-spacing:.16em;text-transform:uppercase;margin-bottom:1mm}
.olho q{display:block;font-family:Manchete,serif;font-style:italic;font-weight:700;font-size:1.22em;line-height:1.22;quotes:"“" "”"}
.ref{font-size:.76em;line-height:1.3;color:#3e3a30;border-top:.4pt solid #8c8672;padding-top:1mm;margin-top:.6em;text-align:left!important}
figure{margin:0 0 .8em;break-inside:avoid}
figure.foto{column-span:none}
.foto img{width:100%;display:block;filter:grayscale(1) sepia(.28) contrast(1.08) brightness(.98);border:.4pt solid #1c1a15}
figure svg{width:100%;height:auto;display:block;filter:grayscale(1) contrast(1.15);border-top:.6pt solid #1c1a15;border-bottom:.6pt solid #1c1a15;padding:1mm 0;background:#f5f0e2}
figcaption{font-family:Antiga,serif;font-style:italic;font-size:.8em;line-height:1.26;margin-top:1mm;text-align:justify;hyphens:manual}
figcaption b{font-style:normal}
.destaque{display:grid;grid-template-columns:1fr 1fr;gap:4.6mm;margin-bottom:3mm}
.destaque .foto img{height:62mm;object-fit:cover}
.capa-grade{display:grid;grid-template-columns:2fr 1fr;gap:5mm;border-bottom:2.2pt solid #1c1a15;padding-bottom:3mm}
.principal{display:flex;flex-direction:column;min-height:0}
.h-capa{font-size:31pt;line-height:1}
.principal .foto{margin:0 0 2.5mm}
.principal .foto img{height:74mm;object-fit:cover}
.capa-lf{font-size:12.4pt;text-align:justify;hyphens:manual}
.vai{font-family:Antiga,serif;font-weight:700;font-size:7.6pt;letter-spacing:.14em;text-transform:uppercase;margin-top:1.5mm}
.vai::before{content:"► "}
.lateral{border-left:.6pt solid #1c1a15;padding-left:4.5mm;display:flex;flex-direction:column;gap:4mm}
.lateral .editorial p{font-size:9.2pt}
.lateral .indice{border:0;padding:0;border-top:1.6pt solid #1c1a15;padding-top:2mm}
.chamadas{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:5mm;padding-top:3mm}
.chamada+.chamada{border-left:.6pt solid #1c1a15;padding-left:5mm}
.chamada h3{font-family:Manchete,serif;font-weight:900;font-size:17pt;line-height:1.05;margin:0 0 1.6mm}
.chamada p{margin:0;font-size:9.2pt;line-height:1.36;text-align:justify;hyphens:manual}
.grafico{margin:0 0 3mm}
.grafico svg{height:50mm;width:auto;max-width:100%;margin:0 auto;border:0;background:none}
.grafico{border-top:.6pt solid #1c1a15;border-bottom:.6pt solid #1c1a15;background:#f5f0e2;padding:1.5mm 0 0}
.grafico figcaption{padding:1mm 1.5mm;background:#efe8d6}
.grafico figcaption{font-size:7.8pt}
.destaque .foto{margin:0}
/* rodapé */
.rodape{display:flex;justify-content:space-between;border-top:.6pt solid #1c1a15;margin-top:2.4mm;padding-top:1.3mm;font-family:Antiga,serif;font-size:7.2pt;letter-spacing:.05em;text-transform:uppercase}
/* nota final e anúncio */
.fim{display:grid;grid-template-columns:1.35fr 1fr;gap:4.6mm;margin-top:3mm;padding-top:3mm;border-top:2.2pt solid #1c1a15}
.editor{display:grid;grid-template-columns:20mm 1fr;gap:3mm;font-size:8.2pt;line-height:1.34;text-align:justify}
.editor img{width:20mm;height:24mm;object-fit:cover;filter:grayscale(1) sepia(.25) contrast(1.1);border:.4pt solid #1c1a15}
.editor p{margin:0;hyphens:manual}
.anuncio{display:block;color:inherit;text-decoration:none;border:3pt double #1c1a15;padding:2.4mm 3mm;text-align:center}
.anuncio .a1{font-family:Antiga,serif;font-size:7pt;letter-spacing:.2em;text-transform:uppercase}
.anuncio .a2{font-family:Manchete,serif;font-weight:900;font-size:15pt;line-height:1.05;margin:1mm 0}
.anuncio p{font-family:Antiga,serif;font-size:8.2pt;line-height:1.3;margin:0 0 1.2mm}
.anuncio .a3{font-family:Antiga,serif;font-weight:700;font-size:8.4pt;letter-spacing:.06em;border-top:.4pt solid #1c1a15;padding-top:1.2mm}
"""

MODERNO = r"""
html,body,.pag{background:#fbf9f3}
body{color:#23251a;font-family:Fonte,serif}
.pag{background:#fbf9f3}
.linha-topo,.topo-int,.rodape,.lema b,.rot,.retranca,.vai,.corpo h4,.ficha .t,.ficha b,.nao .t,.olho .t,.assina,.anuncio .a1,.indice li span{font-family:Jak,sans-serif;font-weight:700;letter-spacing:.12em}
.linha-topo,.rodape{font-size:6.8pt;color:#55573f;border-color:#c9c2a8}
.lema{font-family:Fonte,serif;border-top:0;border-bottom:.6pt solid #c9c2a8}
.cabeca .nome,.topo-int .n{font-family:Marca,serif;color:#3d411f;letter-spacing:-.01em}
.cabeca .nome{font-size:60pt}
.topo-int .n{font-size:17pt}
.fio2{border-color:#3d411f}
h2,.chamada h3,.indice li{font-family:Marca,serif;font-weight:400;letter-spacing:-.005em;color:#23251a}
.indice li::before{font-family:Jak,sans-serif;font-weight:800;color:#bcae56}
.linha-fina{font-family:Fonte,serif;font-style:normal;color:#45473a}
.linha-fina b,.linha-fina strong{color:#3d411f}
.retranca{color:#8a7a2e;font-size:7pt}
.retranca::after{border-color:#d9d1b4}
.rot,.vai,.corpo h4,.nao .t,.olho .t{color:#3d411f;font-size:6.9pt}
.vai::before{content:"→ "}
.corpo h4{border-top:1.6pt solid #bcae56}
.corpo{column-rule-color:#e1dac2}
.corpo .abertura::first-letter,.editorial p::first-letter{font-family:Marca,serif;font-weight:400;color:#3d411f}
.editorial p{font-family:Fonte,serif}
.ficha{border:0;background:#f1ede0;border-radius:2mm}
.ficha .t{border-color:#d9d1b4;text-align:left}
.ficha b{color:#3d411f;font-size:.78em}
.nao{background:#f6ece5;border-top:2pt solid #a05a3c;border-bottom:0;border-radius:0 0 2mm 2mm}
.nao .t{color:#a05a3c}
.nao p::before{content:"";display:inline-block;width:1.4mm;height:1.4mm;border-radius:50%;background:#a05a3c;margin-right:1.4mm;vertical-align:.15em}
.olho{border-top:2pt solid #bcae56;border-bottom:.6pt solid #d9d1b4}
.olho q{font-family:Marca,serif;font-weight:400;color:#3d411f;font-size:1.32em}
.foto img,.editor img{filter:none;border:0;border-radius:2mm}
figure svg{filter:none;background:#fff;border:0}
.grafico{background:#fff;border-color:#d9d1b4;border-radius:2mm;overflow:hidden}
.grafico figcaption,figcaption{font-family:Fonte,serif;color:#55573f}
.grafico figcaption{background:#fbf9f3}
.anuncio{border:0;background:#3d411f;color:#f1ead0;border-radius:2mm}
.anuncio .a1{color:#bcae56}.anuncio .a2{font-family:Marca,serif;font-weight:400;color:#f1ead0}
.anuncio p{font-family:Fonte,serif;color:#d9d4b8}.anuncio .a3{font-family:Jak,sans-serif;border-color:#6b6f45;color:#e3d48a}
.lateral,.indice,.chamada+.chamada{border-color:#d9d1b4}
.capa-grade{border-bottom:2pt solid #3d411f}
.lateral .indice{border-top:2pt solid #bcae56}
.indice li{border-top-color:#d9d1b4}
.fim{border-top:2pt solid #3d411f}
.lema{gap:4mm}
.lema b.ql{font-family:Marca,serif;font-weight:400;font-style:normal;text-transform:none;letter-spacing:0;font-size:10pt;color:#3d411f}
.fim .anuncio p{display:none}
.fim .anuncio .a3{font-size:6.6pt;letter-spacing:.04em}
.fim .editor{font-size:7.8pt}
.principal .foto img{height:64mm}
.capa-lf{font-size:11.4pt}
"""
TEMAS = {"classico": "", "a": MODERNO, "b": MODERNO + r"""
.cabeca{background:#2f3218;margin:0 -12mm;padding:5mm 12mm 4mm;display:flex;align-items:center;justify-content:space-between}
.cabeca .nome{color:#f1ead0;font-size:50pt}
.cabeca img{height:15mm}
.linha-topo{border:0;padding:0 0 2mm}
.lema{border-top:0;margin-top:0;padding:1.6mm 0}
.topo-int{background:#2f3218;margin:-11mm -12mm 0;padding:4mm 12mm 3mm;color:#d9d4b8;border:0}
.topo-int .n{color:#f1ead0}
.topo-int+.fio2{display:none}
.topo-int{margin-bottom:5mm}
h2,.chamada h3,.indice li{font-family:Jak,sans-serif;font-weight:800;letter-spacing:-.025em}
h2{font-size:calc(var(--hs,30pt) * .92)}
.h-capa{font-size:28pt}
.indice li{font-size:9pt}
.olho q{font-family:Jak,sans-serif;font-weight:800;letter-spacing:-.01em;font-size:1.15em}
"""}

def corpo_materia(it, abrir_com_lead):
    p = []
    if it["ficha"]:
        p.append("<div class='ficha'><div class='t'>Ficha</div>%s</div>" % "".join("<div><b>%s</b>%s</div>" % (H.escape(a), hifenizar(H.escape(b))) for a, b in it["ficha"]))
    p.append("<h4>Muda na clínica</h4>")
    p += ["<p class='item'>%s</p>" % x for x in it["muda"]]
    if it["svg"] and abrir_com_lead:
        p.append("<figure>%s<figcaption>%s</figcaption></figure>" % (it["svg"], it["cap"]))
    if it["nao"]:
        p.append("<div class='nao'><div class='t'>Não autoriza dizer</div>%s</div>" % "".join("<p>%s</p>" % x for x in it["nao"]))
    p.append("<h4>Ação para a clínica</h4><p>%s</p>" % it["acao"])
    if it["perg"]:
        p.append("<div class='olho'><div class='t'>E uma pergunta</div><q>%s</q></div>" % H.escape(it["perg"]))
    p.append("<p class='ref'>%s</p>" % it["ref"])
    return "".join(p)

def resumir(htm, n=2):
    partes = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý<])", htm)
    return " ".join(partes[:n])

def foto_html(foto, classe, legenda):
    if not foto:
        return ""
    return "<figure class='foto %s'><img src='data:image/%s;base64,%s'>%s</figure>" % (classe, foto[1], b64(foto[0]), ("<figcaption>%s</figcaption>" % legenda) if legenda else "")

def montar(d, foto, num, mes, julio, destaque=0, foto_item=None, legenda="", ano_romano="I"):
    it = d["itens"]
    if foto_item is None:
        foto_item = destaque
    retrato = False
    if foto:
        from PIL import Image
        w, h = Image.open(foto[0]).size
        retrato = w / h < 1.35
    topo = "<div class='linha-topo'><span>Ano %s · Nº %s</span><span>Itajaí, %s</span><span>Lógica Psicológica</span></div>" % (ano_romano, num, mes)
    cab = ("<div class='cabeca'><div class='nome'>Jornal Bagual</div></div>"
           "<div class='lema'><span><b class='ql'>O que vale ler</b> · achados recentes da psicologia, com o que sustentam e o que não autorizam dizer</span><b>Seleção e comentário: Prof. Júlio Gonçalves</b></div>")
    indice = "".join("<li>%s<span>Página %d</span></li>" % (H.escape(x["h"]), n + 2) for n, x in enumerate(it))
    a = it[destaque]
    def chamada(n, x):
        f = foto_html(foto, "mini", "") if (foto and n == foto_item) else ""
        return "<div class='chamada'><div class='retranca'>%s</div><h3>%s</h3>%s<p>%s</p><div class='vai'>Página %d</div></div>" % (H.escape(x["k"]), H.escape(x["h"]), f, resumir(x["r"]), n + 2)
    chamadas = "".join(chamada(n, x) for n, x in enumerate(it) if n != destaque)
    if foto and foto_item == destaque:
        visual = foto_html(foto, "retrato" if retrato else "", legenda)
    elif a["svg"]:
        visual = "<figure class='grafico capa-graf'>%s</figure>" % a["svg"]
    else:
        visual = ""
    lf = "<p class='linha-fina capa-lf'>%s</p>" % resumir(a["r"], 3)
    corpo_principal = ("<div class='lado-a-lado'>%s<div>%s<div class='vai'>Matéria completa na página %d</div></div></div>" % (visual, lf, destaque + 2)) if (foto and foto_item == destaque and retrato) else (visual + lf + "<div class='vai'>Matéria completa na página %d</div>" % (destaque + 2))
    pag1 = ("<section class='pag'>" + topo + cab +
            "<div class='capa-grade'><div class='principal'><div class='retranca'>%s</div><h2 class='h-capa'>%s</h2>" % (H.escape(a["k"]), H.escape(a["h"])) +
            corpo_principal + "</div>" +
            "<aside class='lateral'><div class='editorial'><div class='rot'>Ao leitor</div><p>%s</p></div>" % d["tema"] +
            "<div class='indice'><div class='rot'>Nesta edição</div><ol>%s</ol></div>" % indice +
            "<a class='anuncio' style='margin-top:auto' href='https://psicojulio.com/comunidade-logica-psicologica/'><div class='a1'>Para quem atende</div><div class='a2'>Comunidade Lógica Psicológica</div><p>Cada edição chega antes lá dentro, com a discussão dos colegas.</p></a></aside></div>" +
            "<div class='chamadas'>%s</div>" % chamadas +
            "<div class='rodape'><span>psicojulio.com</span><span>Jornal Bagual · Edição %s</span><span>Página 1</span></div></section>" % num)
    pags = [pag1]
    for n, x in enumerate(it, start=2):
        ultimo = n == len(it) + 1
        fim = ""
        if ultimo:
            fim = ("<div class='fim'><div class='editor'><img src='data:image/jpeg;base64,%s'><p><b>Nota de método.</b> %s</p></div>" % (b64(julio), d["metodo"]) +
                   "<a class='anuncio' href='https://psicojulio.com/comunidade-logica-psicologica/'><div class='a1'>Para quem atende</div><div class='a2'>Comunidade Lógica Psicológica</div>"
                   "<div class='a3'>psicojulio.com/comunidade-logica-psicologica</div></a></div>")
        pags.append("<section class='pag'><div class='topo-int'><span>Edição %s · %s</span><span class='n'>Jornal Bagual</span><span>Página %d</span></div><div class='fio2'></div>" % (num, mes, n) +
                    "<div class='materia'><div class='retranca'>%s</div><h2>%s</h2><p class='linha-fina'>%s</p><div class='assina'>Por <b>Júlio Gonçalves</b></div>" % (H.escape(x["k"]), H.escape(x["h"]), x["r"]) +
                    ("<figure class='grafico'>%s<figcaption>%s</figcaption></figure>" % (x["svg"], x["cap"]) if x["svg"] else "") +
                    "<div class='corpo'>%s</div></div>%s" % (corpo_materia(x, False), fim) +
                    "<div class='rodape'><span>psicojulio.com</span><span>Jornal Bagual · Edição %s</span><span>Página %d</span></div></section>" % (num, n))
    extra = r"""
.lado-a-lado{display:grid;grid-template-columns:44% 1fr;gap:4mm;align-items:start}
.lado-a-lado .foto img{height:auto;max-height:92mm;object-fit:cover}
.lado-a-lado .capa-lf{margin-top:0}
.foto.mini{float:right;width:30mm;margin:0 0 1.5mm 3mm}
.foto.mini img{height:30mm;object-fit:cover;object-position:top}
.capa-graf{margin:0 0 2.5mm}
.h-capa{font-size:calc(31pt * var(--k,1))}
.capa-lf{font-size:calc(11.4pt * (0.5 + 0.5 * var(--k,1)))}
.chamada h3{font-size:calc(17pt * var(--k,1))}
.chamada p{font-size:calc(9.2pt * (0.4 + 0.6 * var(--k,1)))}
.principal .foto:not(.mini) img{height:calc(64mm * var(--k,1))}
.lado-a-lado .foto img{max-height:none;height:auto;object-fit:contain}
.lema>b{white-space:nowrap;font-size:6.6pt}
.lema>span{font-size:8pt}
.capa-graf svg{height:calc(58mm * var(--k,1))}
.chamadas{min-height:0;overflow:hidden}
.grafico svg{height:var(--g,50mm)!important}
.fim{grid-template-columns:1.6fr 1fr}
.fim .editor{grid-template-columns:15mm 1fr;font-size:7.3pt;line-height:1.3}
.fim .editor img{width:15mm;height:19mm}
.fim .anuncio{padding:2mm 3mm;display:flex;flex-direction:column;justify-content:center}
.fim .anuncio .a2{font-size:13pt}
.capa-graf svg{height:58mm}
.indice li span{letter-spacing:.06em}
"""
    return "<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (CSS + TEMAS[TEMA] + extra, "".join(pags))

AJUSTE = r"""() => {
  const out = [];
  const estoura = (el) => el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1;
  for (const pg of document.querySelectorAll('.pag')) {
    const c = pg.querySelector('.corpo');
    if (!c) {
      // capa: encolhe manchetes e textos até as chamadas caberem
      const ch = pg.querySelector('.chamadas');
      let k = 1;
      while ((estoura(ch) || estoura(pg)) && k > 0.62) { k = Math.round((k - 0.02) * 100) / 100; pg.style.setProperty('--k', k); }
      out.push('capa ' + k); continue;
    }
    let fs = 10.2, g = 50;
    c.style.columnFill = 'auto';
    const set = () => { c.style.setProperty('--fs', fs + 'pt'); pg.style.setProperty('--g', g + 'mm'); };
    set();
    while (estoura(c) && fs > 8.6) { fs = Math.round((fs - 0.1) * 10) / 10; set(); }
    while (estoura(c) && g > 38) { g -= 2; set(); }
    while (estoura(c) && fs > 7.8) { fs = Math.round((fs - 0.1) * 10) / 10; set(); }
    while (estoura(c) && g > 28) { g -= 2; set(); }
    while (estoura(c) && fs > 7.2) { fs = Math.round((fs - 0.1) * 10) / 10; set(); }
    out.push(fs + '/' + g + (estoura(c) ? ' ESTOURA' : ''));
  }
  return out;
}"""

def ler_json(caminho):
    """Lê a edição a partir do JSON (ver exemplo-edicao.json)."""
    import json
    e = json.load(open(caminho, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(caminho))
    def txt(x):   # texto simples, com hifenização
        return hifenizar(H.escape(x or ""))
    def rico(x):  # texto que pode ter <strong>/<em>
        return interno(BeautifulSoup("<p>%s</p>" % (x or ""), "html.parser").p)
    d = {"tema": rico(e["ao_leitor"]), "metodo": txt(e.get("nota_metodo") or METODO), "itens": []}
    for it in e["materias"]:
        svg = it.get("figura_svg") or ""
        if svg and not svg.lstrip().startswith("<svg"):
            svg = open(os.path.join(base, svg), encoding="utf-8").read()
        d["itens"].append({
            "k": it["retranca"], "h": it["titulo"], "r": rico(it["linha_fina"]),
            "ficha": [(a, b) for a, b in it.get("ficha", [])],
            "svg": svg, "cap": rico(it.get("legenda_figura", "")),
            "muda": [rico(x) for x in it["muda_na_clinica"]],
            "nao": [rico(x) for x in it["nao_autoriza_dizer"]],
            "acao": rico(it["acao_para_a_clinica"]), "perg": it.get("pergunta", ""),
            "ref": rico(it.get("referencia", "")),
        })
    foto = e.get("foto_capa")
    if foto:
        foto = os.path.join(base, foto)
    return d, e, foto

METODO = ("A seleção é editorial e não pretende ser exaustiva: privilegia achados com desenho sólido e consequência prática para quem atende. "
          "Cada item é parafraseado a partir do resumo publicado, sem transcrição, e traz o link para a fonte primária, a leitura do original continua sendo "
          "responsabilidade de quem for citar. O campo o que o estudo não autoriza dizer e a ação para a clínica são partes fixas do formato. "
          "A ação é sempre formulada em termos de processos, e não de diagnóstico.")

def gerar(entrada, saida):
    d, e, foto = ler_json(entrada)
    f = (foto, "png" if foto.lower().endswith("png") else "jpeg") if foto else None
    h = montar(d, f, str(e["numero"]), e["mes"], JULIO, int(e.get("destaque", 0)),
               e.get("foto_materia") if e.get("foto_materia") is not None else None, e.get("legenda_foto", ""))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 794, "height": 1123})
        pg.set_content(h, wait_until="load")
        pg.wait_for_timeout(500)
        ajuste = pg.evaluate(AJUSTE)
        pg.pdf(path=saida, width="210mm", height="297mm", print_background=True, prefer_css_page_size=True)
        b.close()
    print("PDF:", saida, "| ajuste por página:", ajuste)
    if any("ESTOURA" in str(a) for a in ajuste):
        print("ATENÇÃO: alguma matéria não coube na página. Encurte o texto dela e gere de novo.")
    try:
        import pymupdf
        doc = pymupdf.open(saida)
        for i, pgn in enumerate(doc):
            pgn.get_pixmap(dpi=90).save(saida.replace(".pdf", "-pagina%d.png" % (i + 1)))
        print("Prévias PNG geradas ao lado do PDF.")
    except ImportError:
        pass

if __name__ == "__main__":
    gerar(sys.argv[1], sys.argv[2])
