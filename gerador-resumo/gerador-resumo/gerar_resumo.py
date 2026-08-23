#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador do "Resumo de aula" da Jornada da Leitura — Lógica Psicológica.

Reproduz o padrão dos capítulos 1 a 3:
  capa · página da Comunidade · conteúdo com cabeçalho corrido e rodapé Ψ · N ·
  referências + nota de método + contato · duas fichas de trabalho preenchíveis.

Uso:  python3 gerar_resumo.py conteudo/cap4.json saida/resumo.pdf
"""

import base64, json, os, subprocess, sys, tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
FONTES = BASE / "fontes"
ASSETS = BASE / "assets"
DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# ---------------------------------------------------------------- utilidades

def b64(caminho):
    return base64.b64encode(Path(caminho).read_bytes()).decode()

def face(arquivo, peso, estilo="normal"):
    return (f"@font-face{{font-family:'Jak';font-style:{estilo};font-weight:{peso};"
            f"font-display:block;src:url(data:font/woff2;base64,{b64(FONTES/arquivo)}) "
            f"format('woff2');}}")

FONT_CSS = "".join([
    face("plus-jakarta-sans-latin-400-normal.woff2", 400),
    face("plus-jakarta-sans-latin-500-normal.woff2", 500),
    face("plus-jakarta-sans-latin-700-normal.woff2", 700),
    face("plus-jakarta-sans-latin-800-normal.woff2", 800),
    face("plus-jakarta-sans-latin-400-italic.woff2", 400, "italic"),
    face("plus-jakarta-sans-latin-500-italic.woff2", 500, "italic"),
])

CORES = """
:root{--olive:#5b5c2a;--olive-dk:#43441f;--sage:#9ca575;--sage-dk:#7c8054;
--cream:#f8f3e6;--cream-dp:#efe7d3;--gilt:#a8894f;--gilt-lt:#c3a468;
--ink:#2f2e24;--muted:#6c6a55;--card:#fffdf7;--linha:#e2d9c2;}
"""

BASE_CSS = CORES + """
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
html,body{margin:0;padding:0;}
body{font-family:'Jak',sans-serif;color:var(--ink);background:#fff;
 font-size:10.6pt;line-height:1.56;font-weight:400;}
b,strong{font-weight:800;color:var(--olive-dk);}
i,em{font-style:italic;}
.psi{font-family:'DejaVu Sans',sans-serif;font-weight:700;}
.nota{color:var(--muted);font-size:9.4pt;}
"""

# ------------------------------------------------------------------- páginas

def html_capa(d):
    return f"""<!DOCTYPE html><meta charset="utf-8"><style>{FONT_CSS}{BASE_CSS}
@page{{size:A4;margin:0;}}
.capa{{width:210mm;height:297mm;position:relative;overflow:hidden;
 background:linear-gradient(150deg,#6a6b33 0%,#5b5c2a 42%,#43441f 100%);
 display:flex;flex-direction:column;align-items:center;justify-content:flex-start;}}
.logo{{width:50mm;margin-top:26mm;}}
.selo{{margin-top:12mm;width:15mm;height:15mm;border-radius:50%;
 border:1px solid var(--gilt-lt);display:flex;align-items:center;justify-content:center;}}
.selo span{{color:var(--gilt-lt);font-size:16pt;}}
.sobrancelha{{margin-top:11mm;color:var(--gilt-lt);font-size:8pt;font-weight:700;
 letter-spacing:.34em;text-transform:uppercase;}}
h1{{margin:5mm 22mm 0;font-size:34pt;line-height:1.06;font-weight:800;
 color:var(--cream);text-align:center;letter-spacing:-.01em;}}
.cap{{margin-top:6mm;color:var(--sage);font-size:10pt;font-weight:700;letter-spacing:.34em;}}
.regua{{margin-top:5mm;width:22mm;height:1.4pt;background:var(--gilt-lt);}}
.sub{{margin:6mm 34mm 0;color:#e9e3ce;font-size:11.5pt;line-height:1.5;
 font-style:italic;text-align:center;}}
.pe{{position:absolute;left:14mm;right:14mm;bottom:16mm;color:var(--gilt-lt);
 font-size:7.4pt;font-weight:700;letter-spacing:.2em;text-align:center;line-height:1.8;}}
.pe i{{font-weight:500;}}
</style>
<div class="capa">
  <img class="logo" src="data:image/png;base64,{b64(ASSETS/'logo-creme.png')}">
  <div class="selo"><span class="psi">&#936;</span></div>
  <div class="sobrancelha">Resumo de aula · Jornada da Leitura</div>
  <h1>{d['titulo']}</h1>
  <div class="cap">CAPÍTULO {d['numero']}</div>
  <div class="regua"></div>
  <div class="sub">{d['subtitulo']}</div>
  <div class="pe">{d['meta_capa']}</div>
</div>"""


def html_comunidade(d):
    bullets = "".join(
        f'<li><span class="psi">&#936;</span><div>{t}</div></li>' for t in [
            "<b>Aprofundar o raciocínio clínico</b> com conteúdos que unem ciência, processos e análise funcional.",
            "<b>Estruturar uma prática ética e coerente</b>, com pensamento crítico e evidências atualizadas.",
            "<b>Desenvolver o self clínico</b> por meio de supervisão, leituras guiadas e construção em rede.",
        ])
    return f"""<!DOCTYPE html><meta charset="utf-8"><style>{FONT_CSS}{BASE_CSS}
@page{{size:A4;margin:0;}}
.pg{{width:210mm;height:297mm;display:flex;background:var(--cream);}}
.esq{{width:62%;padding:24mm 12mm 18mm 20mm;}}
.dir{{width:38%;background:url(data:image/jpeg;base64,{b64(ASSETS/'julio.jpg')}) center/cover;}}
.logo{{width:44mm;}}
.rot{{margin-top:14mm;color:var(--olive);font-size:8pt;font-weight:800;
 letter-spacing:.26em;text-transform:uppercase;}}
.nome{{font-size:20pt;font-weight:800;color:var(--ink);margin-top:1mm;}}
.crp{{color:var(--muted);font-size:9.6pt;}}
.chamada{{margin-top:10mm;font-style:italic;color:var(--muted);font-size:11pt;}}
.marca{{font-size:19pt;font-weight:800;color:var(--olive-dk);line-height:1.25;
 background:linear-gradient(transparent 62%,var(--sage) 62%);display:inline;}}
.para{{margin-top:9mm;font-weight:800;color:var(--ink);}}
ul{{list-style:none;margin:4mm 0 0;padding:0;}}
li{{display:flex;gap:3mm;margin-bottom:4.5mm;line-height:1.5;}}
li .psi{{color:var(--gilt);}}
.cta{{display:inline-block;margin-top:9mm;background:var(--olive);color:var(--cream);
 padding:4mm 8mm;border-radius:3mm;font-weight:800;font-size:10.5pt;}}
</style>
<div class="pg"><div class="esq">
  <img class="logo" src="data:image/png;base64,{b64(ASSETS/'logo.png')}">
  <div class="rot">Professor e psicólogo clínico</div>
  <div class="nome">Júlio Gonçalves</div>
  <div class="crp">MSc · CRP 12/17614</div>
  <div class="chamada">Aprenda muito mais na</div>
  <div><span class="marca">Comunidade Lógica Psicológica</span></div>
  <div class="para">Uma comunidade para quem quer:</div>
  <ul>{bullets}</ul>
  <div class="cta">Clique aqui e saiba mais</div>
</div><div class="dir"></div></div>"""


def bloco_html(b):
    t = b["t"]
    if t == "h2":
        return f'<h2>{b["v"]}</h2>'
    if t == "h3":
        return f'<h3>{b["v"]}</h3>'
    if t == "p":
        return f'<p>{b["v"]}</p>'
    if t == "lista":
        itens = "".join(f'<li><span class="psi">&#936;</span><div>{x}</div></li>' for x in b["v"])
        return f'<ul class="psilista">{itens}</ul>'
    if t == "callout":
        return (f'<div class="callout"><div class="rot">{b["rotulo"]}</div>'
                f'<p>{b["v"]}</p></div>')
    if t == "cards":
        cs = "".join(f'<div class="card"><div class="rot">{c["rotulo"]}</div>'
                     f'<p>{c["texto"]}</p></div>' for c in b["v"])
        return f'<div class="cards">{cs}</div>'
    if t == "fluxo":
        passos = []
        for i, p in enumerate(b["v"]):
            if i:
                passos.append('<div class="seta">&#8594;</div>')
            passos.append(f'<div class="passo"><div class="rot">{p["rotulo"]}</div>'
                          f'<p>{p["texto"]}</p></div>')
        return (f'<div class="fluxo"><div class="rot-x">{b["rotulo"]}</div>'
                f'<div class="linha-fluxo">{"".join(passos)}</div>'
                f'<div class="legenda">{b["legenda"]}</div></div>')
    raise ValueError(t)


def html_conteudo(d):
    ess = "".join(f'<li><span class="psi">&#936;</span><div>{x}</div></li>' for x in d["essencial"])
    corpo = "".join(bloco_html(b) for b in d["blocos"])
    refs = "".join(f"<li>{r}</li>" for r in d["referencias"])
    return f"""<!DOCTYPE html><meta charset="utf-8"><style>{FONT_CSS}{BASE_CSS}
@page{{size:A4;margin:26.6mm 22mm 19mm 22mm;}}
h2{{font-size:15pt;font-weight:800;margin:9mm 0 3mm;line-height:1.2;
 break-after:avoid;color:var(--ink);}}
h2+p,h3+p,h2+.cards,h2+ul{{break-before:avoid;}}
h3{{font-size:11.6pt;font-weight:800;margin:6mm 0 2mm;color:var(--olive);break-after:avoid;}}
p{{margin:0 0 3.4mm;}}
ul.psilista{{list-style:none;margin:0 0 4mm;padding:0;}}
ul.psilista>li{{display:flex;gap:3.4mm;margin-bottom:3.2mm;break-inside:avoid;}}
ul.psilista>li>.psi{{color:var(--gilt);flex:0 0 auto;}}
.essencial{{background:var(--card);border:.7pt solid var(--cream-dp);border-radius:3mm;
 padding:6mm 7mm 3mm;margin-bottom:9mm;break-inside:avoid;}}
.essencial>.rot{{color:var(--gilt);font-size:7.6pt;font-weight:800;
 letter-spacing:.26em;margin-bottom:4mm;}}
.callout{{background:var(--card);border-left:2.4pt solid var(--gilt);
 border-radius:0 2.4mm 2.4mm 0;padding:5mm 6mm 2.2mm;margin:5mm 0 6mm;break-inside:avoid;}}
.callout>.rot{{color:var(--gilt);font-size:7.6pt;font-weight:800;
 letter-spacing:.26em;margin-bottom:2.6mm;}}
.cards{{display:flex;gap:4mm;margin:4mm 0 6mm;break-inside:avoid;}}
.card{{flex:1;background:var(--cream);border:.7pt solid var(--cream-dp);
 border-radius:2.6mm;padding:4.5mm;}}
.card>.rot{{color:var(--olive-dk);font-size:8pt;font-weight:800;
 letter-spacing:.19em;margin-bottom:2.4mm;}}
.card p{{color:var(--muted);font-size:9.8pt;line-height:1.45;margin:0;}}
.fluxo{{background:var(--card);border:.7pt solid var(--cream-dp);border-radius:3mm;
 padding:5mm;margin:5mm 0 6mm;break-inside:avoid;}}
.fluxo>.rot-x{{color:var(--gilt);font-size:7.6pt;font-weight:800;
 letter-spacing:.26em;text-align:center;margin-bottom:4mm;}}
.linha-fluxo{{display:flex;align-items:stretch;gap:2.5mm;}}
.passo{{flex:1;border:.7pt solid var(--cream-dp);border-radius:2.4mm;
 padding:3.4mm;text-align:center;background:#fff;}}
.passo>.rot{{color:var(--gilt);font-size:7pt;font-weight:800;letter-spacing:.19em;}}
.passo p{{margin:1.6mm 0 0;font-size:9pt;line-height:1.35;}}
.seta{{align-self:center;color:var(--sage-dk);font-size:12pt;}}
.legenda{{margin-top:3.4mm;text-align:center;color:var(--muted);font-size:9.4pt;}}
h2.refs{{font-size:16pt;margin-top:11mm;}}
ol.refs{{padding-left:6mm;margin:0;color:var(--muted);font-size:9.6pt;line-height:1.45;}}
ol.refs li{{margin-bottom:1.8mm;break-inside:avoid;}}
.metodo{{background:var(--cream);border-radius:3mm;padding:5mm 6mm;margin-top:8mm;
 color:var(--muted);font-size:9.4pt;line-height:1.5;}}
.metodo .rot{{color:var(--olive-dk);font-size:7.6pt;font-weight:800;
 letter-spacing:.26em;margin-bottom:2.6mm;}}
.contato{{margin-top:7mm;text-align:center;font-size:9pt;line-height:1.6;break-inside:avoid;}}
.contato .a{{color:var(--gilt);font-weight:700;}}
.contato .b{{color:var(--muted);}}
</style>
<div class="essencial"><div class="rot">O ESSENCIAL</div><ul class="psilista">{ess}</ul></div>
{corpo}
<h2 class="refs">Referências</h2>
<ol class="refs">{refs}</ol>
<div class="metodo"><div class="rot">NOTA DE MÉTODO</div>{d['nota_metodo']}</div>
<div class="contato"><div class="a">contato@psicojulio.com · (47) 99933-8021</div>
<div class="b">Rua Concórdia, 703, São Vicente, Itajaí — 88309-645 · CNPJ 49.649.803/0001-60</div></div>"""


def html_fichas(d):
    chk = "".join(f'<li><span class="cx"></span><div>{x}</div></li>' for x in d["checklist"])
    perg = "".join(f'<li><div class="q">{i+1}. {q}</div><div class="resp"></div></li>'
                   for i, q in enumerate(d["perguntas"]))
    return f"""<!DOCTYPE html><meta charset="utf-8"><style>{FONT_CSS}{BASE_CSS}
@page{{size:A4;margin:26.6mm 22mm 19mm 22mm;}}
h1{{font-size:24pt;font-weight:800;margin:9mm 0 1.5mm;}}
.sub{{font-style:italic;color:var(--muted);margin-bottom:7mm;}}
ul{{list-style:none;margin:0;padding:0;}}
.lista{{background:var(--cream);border-radius:3mm;padding:6mm 7mm;}}
.lista li{{display:flex;gap:4mm;margin-bottom:5.5mm;align-items:flex-start;}}
.lista li:last-child{{margin-bottom:0;}}
.cx{{flex:0 0 auto;width:4.4mm;height:4.4mm;border:.9pt solid var(--sage-dk);
 border-radius:.8mm;margin-top:.6mm;background:#fff;}}
.rot{{color:var(--gilt);font-size:7.6pt;font-weight:800;letter-spacing:.26em;
 margin:9mm 0 2.5mm;}}
.caixa{{border:.7pt solid var(--cream-dp);border-radius:2.4mm;height:78mm;background:var(--card);}}
.perg li{{margin-bottom:4.5mm;break-inside:avoid;}}
.q{{font-weight:500;margin-bottom:2mm;}}
.resp{{border:.7pt solid var(--cream-dp);border-radius:2.4mm;height:18mm;background:var(--card);}}
.quebra{{break-before:page;}}
.quebra+h1{{margin-top:0;}}
</style>
<h1>Levar para a prática</h1>
<div class="sub">Marque conforme experimentar em sessão — e salve o PDF para acompanhar.</div>
<ul class="lista">{chk}</ul>
<div class="rot">MINHAS ANOTAÇÕES — O QUE LEVO PARA A CLÍNICA</div>
<div class="caixa"></div>
<div class="quebra"></div>
<h1>Para revisar — responda</h1>
<div class="sub">Responda com suas palavras. O texto fica salvo no PDF.</div>
<ul class="perg">{perg}</ul>"""


# --------------------------------------------------------------- renderização

def render(html, destino):
    from playwright.sync_api import sync_playwright
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html); caminho = f.name
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file://" + caminho)
        pg.wait_for_timeout(700)
        pg.pdf(path=destino, format="A4", print_background=True, prefer_css_page_size=True)
        b.close()
    os.unlink(caminho)


def montar(json_path, saida):
    import pymupdf
    from pypdf import PdfReader, PdfWriter

    d = json.loads(Path(json_path).read_text(encoding="utf-8"))
    tmp = Path(tempfile.mkdtemp())

    partes = [("capa", html_capa(d)), ("comunidade", html_comunidade(d)),
              ("conteudo", html_conteudo(d)), ("fichas", html_fichas(d))]
    arquivos = {}
    for nome, h in partes:
        arquivos[nome] = str(tmp / f"{nome}.pdf")
        render(h, arquivos[nome])

    n_conteudo = pymupdf.open(arquivos["conteudo"]).page_count
    n_fichas = pymupdf.open(arquivos["fichas"]).page_count

    # 1. junta na ordem do padrão
    w = PdfWriter()
    for nome in ("capa", "comunidade", "conteudo", "fichas"):
        for pg in PdfReader(arquivos[nome]).pages:
            w.add_page(pg)
    bruto = str(tmp / "bruto.pdf")
    with open(bruto, "wb") as fh:
        w.write(fh)

    # 2. carimba o cabeçalho corrido e o rodapé "Ψ · N"
    doc = pymupdf.open(bruto)
    direita = f"{d['titulo_curto']} · TBP · ENC. {d['numero']}"
    for i in range(n_conteudo + n_fichas):
        pg = doc[2 + i]
        cabecalho(pg, "LÓGICA PSICOLÓGICA", direita)
        if i < n_conteudo:
            rodape_psi(pg, i + 1)

    # 3. injeta os campos preenchíveis nas duas fichas finais
    p_chk = doc[2 + n_conteudo]
    alvos = [r for r in localizar_caixas(p_chk)]
    for i, r in enumerate(alvos):
        add_check(p_chk, r, f"chk_{i}")
    add_texto(p_chk, maior_retangulo(p_chk), "notas")

    for j in range(1, n_fichas):
        pg = doc[2 + n_conteudo + j]
        for k, r in enumerate(caixas_resposta(pg)):
            add_texto(pg, r, f"resp_{j-1}_{k}")

    doc.set_metadata({"title": d["titulo"],
                      "author": "Prof. Júlio Gonçalves · CRP 12/17614",
                      "subject": "Lógica Psicológica · Jornada da Leitura"})
    Path(saida).parent.mkdir(parents=True, exist_ok=True)
    doc.save(saida, garbage=3, deflate=True)
    doc.close()
    return saida, n_conteudo


# ------------------------------------------- cabeçalho corrido e rodapé Ψ · N

MARGEM_E, MARGEM_D = 62.4, 532.9      # mesmas margens dos caps 1–3
Y_CABECA, Y_REGUA, Y_RODAPE = 64.5, 71.0, 812.0
GILT = (0.659, 0.537, 0.310)
MUTED = (0.424, 0.416, 0.333)
TTF_BOLD = str(FONTES / "plus-jakarta-sans-latin-800-normal.ttf")


def _largura(txt, fonte, size, tracking):
    return fonte.text_length(txt, fontsize=size) + tracking * max(len(txt) - 1, 0)


def _escreve(page, txt, x, y, size, cor, ttf, nome, tracking=0.0):
    """insere texto com espaçamento entre letras (o tracking da identidade)"""
    import pymupdf
    fonte = pymupdf.Font(fontfile=ttf)
    for ch in txt:
        page.insert_text(pymupdf.Point(x, y), ch, fontsize=size,
                         fontfile=ttf, fontname=nome, color=cor)
        x += fonte.text_length(ch, fontsize=size) + tracking


def cabecalho(page, esquerda, direita, size=6.8, tracking=1.3):
    import pymupdf
    fonte = pymupdf.Font(fontfile=TTF_BOLD)
    _escreve(page, esquerda, MARGEM_E, Y_CABECA, size, GILT, TTF_BOLD, "jak8", tracking)
    x = MARGEM_D - _largura(direita, fonte, size, tracking)
    _escreve(page, direita, x, Y_CABECA, size, GILT, TTF_BOLD, "jak8", tracking)
    page.draw_line(pymupdf.Point(MARGEM_E, Y_REGUA), pymupdf.Point(MARGEM_D, Y_REGUA),
                   color=(0.886, 0.851, 0.761), width=0.7)


def rodape_psi(page, n):
    import pymupdf
    txt = f"\u03a8 · {n}"
    fonte = pymupdf.Font(fontfile=DEJAVU)
    x = page.rect.width / 2 - _largura(txt, fonte, 8, 0.8) / 2
    _escreve(page, txt, x, Y_RODAPE, 8, MUTED, DEJAVU, "dejavu", 0.8)


# ------------------------------------------------- localização das caixas

def _retangulos(page):
    out = []
    for dr in page.get_drawings():
        r = dr["rect"]
        if r.width > 2 and r.height > 2:
            out.append(r)
    return out

def localizar_caixas(page):
    """quadradinhos do checklist: pequenos e quase quadrados"""
    rs = [r for r in _retangulos(page) if 8 < r.width < 20 and abs(r.width - r.height) < 4]
    rs.sort(key=lambda r: r.y0)
    vistos, saida = [], []
    for r in rs:
        if all(abs(r.y0 - v) > 4 for v in vistos):
            vistos.append(r.y0); saida.append(r)
    return saida

def maior_retangulo(page):
    rs = [r for r in _retangulos(page) if r.height > 100]
    return max(rs, key=lambda r: r.height) if rs else None

def caixas_resposta(page):
    rs = [r for r in _retangulos(page) if 45 < r.height < 90 and r.width > 300]
    rs.sort(key=lambda r: r.y0)
    vistos, saida = [], []
    for r in rs:
        if all(abs(r.y0 - v) > 6 for v in vistos):
            vistos.append(r.y0); saida.append(r)
    return saida

def add_check(page, rect, nome):
    import pymupdf
    w = pymupdf.Widget()
    w.field_type = pymupdf.PDF_WIDGET_TYPE_CHECKBOX
    w.field_name = nome
    w.rect = rect
    w.border_color = (0.486, 0.502, 0.329)
    w.fill_color = (1, 1, 1)
    w.border_width = 0.9
    page.add_widget(w)

def add_texto(page, rect, nome):
    import pymupdf
    if rect is None:
        return
    w = pymupdf.Widget()
    w.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
    w.field_name = nome
    w.field_flags = pymupdf.PDF_TX_FIELD_IS_MULTILINE
    w.rect = rect
    w.text_fontsize = 10
    w.text_color = (0.184, 0.180, 0.141)
    w.fill_color = None
    w.border_width = 0
    page.add_widget(w)


if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else "conteudo/cap4.json"
    saida = sys.argv[2] if len(sys.argv) > 2 else "saida/resumo.pdf"
    caminho, n = montar(entrada, saida)
    print(f"gerado: {caminho} ({n} páginas de conteúdo)")
