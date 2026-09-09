# -*- coding: utf-8 -*-
"""PDF da Edição 1 (definitiva): uma página A4, direção editorial, mesmo
molde de edicao.py. Só o conteúdo muda."""
import io, os, shutil, subprocess, time
import pymupdf
from playwright.sync_api import sync_playwright
from jornal import fontes, ativos, SITE
from edicao import CSS, WORK, PORT, TINTA, OLIVA, GILT, SAGE, MUDO, TERRA

GRAF = u"""<svg viewBox='0 0 300 124' xmlns='http://www.w3.org/2000/svg'>
<line x1='30' y1='40' x2='74' y2='92' stroke='#DCD4BB' stroke-width='2'/>
<line x1='30' y1='40' x2='74' y2='30' stroke='#DCD4BB' stroke-width='3.4'/>
<line x1='74' y1='30' x2='74' y2='92' stroke='#DCD4BB' stroke-width='1.6'/>
<circle cx='74' cy='30' r='15' fill='%(O)s'/>
<text x='74' y='33' text-anchor='middle' font-family='Jak,sans-serif' font-size='6.8' font-weight='800' fill='#F0EDE0'>abertura</text>
<circle cx='30' cy='40' r='13.5' fill='#EFE9DA' stroke='%(S)s' stroke-width='1.2'/>
<text x='30' y='42.5' text-anchor='middle' font-family='Jak,sans-serif' font-size='5.8' fill='%(T)s'>atenção</text>
<circle cx='74' cy='92' r='13.5' fill='#FFFDF7' stroke='%(TE)s' stroke-width='1.4'/>
<text x='74' y='94.5' text-anchor='middle' font-family='Jak,sans-serif' font-size='5.8' fill='%(T)s'>engajar</text>
<text x='96' y='26' font-family='Jak,sans-serif' font-size='6.8' font-weight='800' letter-spacing='.6' fill='%(O)s'>MAIS CENTRAL</text>
<text x='96' y='96' font-family='Jak,sans-serif' font-size='6.8' font-weight='800' letter-spacing='.6' fill='%(TE)s'>MENOS CENTRAL</text>
<text x='158' y='28' font-family='Jak,sans-serif' font-size='7' fill='%(M)s'>2 semanas em cada um</text>
<text x='158' y='58' font-family='News,serif' font-size='17' font-weight='800' fill='%(O)s'>sem diferença</text>
<text x='158' y='76' font-family='Jak,sans-serif' font-size='7.2' fill='%(T)s'>4 de 6 melhoraram</text>
<text x='158' y='88' font-family='Jak,sans-serif' font-size='7.2' fill='%(T)s'>nenhuma fase claramente melhor</text>
<text x='158' y='100' font-family='Jak,sans-serif' font-size='7.2' fill='%(T)s'>num caso, o menos central rendeu mais</text>
<text x='158' y='116' font-family='Jak,sans-serif' font-size='7' font-style='italic' fill='%(TE)s'>centralidade instável entre reestimações</text>
</svg>""" % dict(T=TINTA, S=SAGE, O=OLIVA, M=MUDO, TE=TERRA)

FIG2 = u"""<svg viewBox='0 0 300 118' xmlns='http://www.w3.org/2000/svg'>
<rect x='0' y='4' width='88' height='70' rx='6' fill='#F7EDE7'/>
<text x='10' y='22' font-family='Jak,sans-serif' font-size='7.5' font-weight='800' letter-spacing='1' fill='#A05A3C'>DISPARA</text>
<text x='10' y='40' font-family='Jak,sans-serif' font-size='8' fill='#2F2E24'>solidão, tédio</text>
<text x='10' y='54' font-family='Jak,sans-serif' font-size='8' fill='#2F2E24'>incerteza sobre si</text>
<text x='10' y='68' font-family='Jak,sans-serif' font-size='8' fill='#2F2E24'>descontinuidade</text>
<path d='M92 39 L102 39' stroke='#8D876F' stroke-width='1.6'/>
<rect x='106' y='4' width='88' height='70' rx='6' fill='#43441F'/>
<text x='150' y='36' text-anchor='middle' font-family='News,serif' font-size='12' font-weight='800' fill='#F0EDE0'>nostalgia</text>
<text x='150' y='54' text-anchor='middle' font-family='Jak,sans-serif' font-size='7.5' fill='#9CA575'>uma versão de si</text>
<text x='150' y='65' text-anchor='middle' font-family='Jak,sans-serif' font-size='7.5' fill='#9CA575'>com vínculo</text>
<path d='M198 39 L208 39' stroke='#8D876F' stroke-width='1.6'/>
<rect x='212' y='4' width='88' height='70' rx='6' fill='#EFE9DA'/>
<text x='222' y='22' font-family='Jak,sans-serif' font-size='7.5' font-weight='800' letter-spacing='1' fill='#A8894F'>DEVOLVE</text>
<text x='222' y='40' font-family='Jak,sans-serif' font-size='8' fill='#2F2E24'>conexão</text>
<text x='222' y='54' font-family='Jak,sans-serif' font-size='8' fill='#2F2E24'>continuidade</text>
<text x='222' y='68' font-family='Jak,sans-serif' font-size='8' fill='#2F2E24'>sentido</text>
<text x='150' y='96' text-anchor='middle' font-family='Jak,sans-serif' font-size='8' font-weight='800' fill='#43441F'>alimenta ação no presente</text>
<text x='150' y='110' text-anchor='middle' font-family='Jak,sans-serif' font-size='8' font-weight='800' fill='#A05A3C'>ou vira refúgio do presente</text>
</svg>"""

HTML = u"""<!doctype html><meta charset='utf-8'><style>@FONTES@""" + CSS + u"""</style><div class='pg'>

<div class='top'><img src='/a/logo.png' alt='Lógica Psicológica'>
<div class='e'>Edição 01 &middot; Publicada em setembro de 2026</div></div>

<div class='abre'>
<div>
<h1>Um estudo que não confirmou a aposta, e um feed cheio de anos 80</h1>
<p class='sf'>A rede idiográfica foi posta à prova na escolha do alvo e a hipótese da centralidade não se sustentou. Ao lado, a trend das fotos anos 80 lida pela pesquisa sobre nostalgia. E, em outubro, sete nomes da psicoterapia mundial em São Paulo. Cada item com o que sustenta e o que não autoriza dizer.</p>
</div>
<div class='retrato'><img src='/a/julio.jpg' alt='Prof. Júlio Gonçalves'>
<div class='tarja'><b>Seleção e comentário</b><span>Prof. Júlio Gonçalves &middot; CRP 12/17614</span></div></div>
</div>

<div class='duas'>
<div><div class='n'>A notícia da capa</div>
<h2>Intervir no nó mais central não rendeu mais</h2>
<div class='fig'>@GRAF@</div>
<p>Seis pessoas com dor crônica, cinco medidas por dia, uma rede de inflexibilidade psicológica para cada uma. Tratar primeiro o processo mais central deveria mover mais a rede inteira. Quatro melhoraram, mas sem fase claramente melhor, e a centralidade mudou entre reestimações.</p>
<div class='lim'>Não autoriza dizer que redes idiográficas não servem: o próprio grupo achou sinal em outro modelo, em análise exploratória. Seis pessoas, um problema, uma abordagem, quatro semanas.</div></div>
<div><div class='n'>A segunda notícia</div>
<h2>Todo mundo virou anos 80 no feed</h2>
<div class='fig' style='display:flex;gap:4mm;align-items:center'><img src='/a/julio-anos80.jpg' alt='' style='width:22mm;height:33mm;object-fit:cover;border-radius:1.2mm;flex:none'><div style='font-size:8.4pt;line-height:1.5;color:#6C6A55;font-style:italic'>Eu também entrei na trend. Decididamente não me gostei, hehe.</div></div>
<p>Retratos gerados por IA com cabelo armado e grão de filme, inclusive de quem nasceu depois de 1990. Uma revisão de Sedikides e Wildschut na Emotion Review, que reúne duas décadas de estudos experimentais, descreve a nostalgia como resposta a um desconforto: ela devolve conexão, continuidade do self e sentido. O que interessa é o que a pessoa faz na hora seguinte.</p>
<div class='lim'>Não autoriza dizer que a trend é sinal de sofrimento coletivo, nem que nostalgia é sempre boa: a base é de laboratório, com efeito medido logo depois da indução.</div></div>
</div>

<div class='tres'>
<div><div class='n'>Agenda</div><h2>Artmed Experience, 15 a 17 de outubro</h2>
<p>Barlow, Leahy, Hofmann, Tsai, Fonagy, Miller e Luana Marques no Expo Center Norte, com simulações clínicas comentadas. O tema é o que diferencia terapeutas extraordinários: relação, formulação e personalização, o terreno da TBP.</p></div>
<div><div class='n'>Ação para a clínica</div><h2>Registre por que escolheu o alvo</h2>
<p>Centralidade, acesso ou função. Escreva o critério na formulação e volte a ele em quatro semanas para ver qual previu melhor a mudança que aconteceu.</p></div>
<div><div class='n'>E uma pergunta</div><h2>Lembrar leva a quê?</h2>
<p>Com o paciente que idealiza uma época, mapeie a função: o que ele sente logo depois de lembrar e o que faz na hora seguinte. Ligar para alguém é uma coisa; se recolher e comparar é outra.</p></div>
</div>

<div class='foot'>
<span><b>Ação da edição.</b> Trate a centralidade do nó como hipótese a testar, e a nostalgia do paciente como um dado sobre o que o presente não está fornecendo.</span>
<span style='text-align:right;white-space:nowrap'><b>Comunidade Lógica Psicológica</b><br>Edição completa no portal de resumos</span></div>
</div>"""


def gerar(destino):
    prev = WORK + '/prev'
    if os.path.exists(prev):
        shutil.rmtree(prev)
    os.makedirs(prev)
    f = fontes(prev)
    ativos(prev)
    shutil.copy(SITE + '/assets/julio-anos80.jpg', prev + '/a/julio-anos80.jpg')
    io.open(prev + '/e.html', 'w', encoding='utf-8').write(
        HTML.replace('@FONTES@', f).replace('@GRAF@', GRAF).replace('@FIG2@', FIG2))
    srv = subprocess.Popen(['python3', '-m', 'http.server', str(PORT), '-d', prev],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.2)
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(); pg = b.new_page()
            pg.goto('http://localhost:%d/e.html' % PORT, wait_until='load')
            pg.wait_for_timeout(1000)
            m = pg.evaluate("()=>{const e=document.querySelector('.pg');"
                            "return {p:Math.round(e.getBoundingClientRect().height),"
                            "c:Math.round(e.scrollHeight)}}")
            pg.pdf(path=destino, format='A4', print_background=True, prefer_css_page_size=True)
            b.close()
    finally:
        srv.terminate()
    d = pymupdf.open(destino); n = d.page_count
    d[0].get_pixmap(dpi=118).save('/tmp/edicao.png')
    d.close()
    return n, m


if __name__ == '__main__':
    os.makedirs(WORK, exist_ok=True)
    dest = SITE + '/newsletter/2026-09/edicao-01.pdf'
    n, m = gerar(dest)
    print('páginas: %d | folga: %d px | %.0f KB' % (n, m['p'] - m['c'], os.path.getsize(dest) / 1024))
