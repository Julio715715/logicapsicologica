# -*- coding: utf-8 -*-
"""PDF da Edição 2: uma página A4, direção editorial, mesmo molde de edicao.py."""
import io, os, shutil, subprocess, time, random
import pymupdf
from playwright.sync_api import sync_playwright
from jornal import fontes, ativos, SITE
from edicao import CSS, WORK, PORT, TINTA, OLIVA, GILT, SAGE, MUDO, TERRA

PASTA = '2026-09-17'


def graf_treta():
    J = "font-family='Jak,sans-serif'"
    return u"""<svg viewBox='0 0 300 124' xmlns='http://www.w3.org/2000/svg'>
<rect x='0' y='4' width='144' height='74' rx='5' fill='#EFE9DA'/>
<text x='10' y='20' %(J)s font-size='6.6' font-weight='800' letter-spacing='.8' fill='%(G)s'>O QUE A DECLARAÇÃO DIZ</text>
<text x='10' y='36' %(J)s font-size='7.2' fill='%(T)s'>Claude e ChatGPT para edição</text>
<text x='10' y='48' %(J)s font-size='7.2' fill='%(T)s'>de rotina, figuras e destaques.</text>
<text x='10' y='66' %(J)s font-size='6.6' font-style='italic' fill='%(M)s'>Os autores assumem o conteúdo.</text>
<rect x='156' y='4' width='144' height='74' rx='5' fill='#FFFDF7' stroke='%(O)s' stroke-width='.8'/>
<text x='166' y='20' %(J)s font-size='6.6' font-weight='800' letter-spacing='.8' fill='%(O)s'>O QUE O ARTIGO DEFENDE</text>
<text x='166' y='36' %(J)s font-size='7.2' fill='%(T)s'>A média de grupo não descreve</text>
<text x='166' y='48' %(J)s font-size='7.2' fill='%(T)s'>a pessoa. Comece pelo caso.</text>
<text x='166' y='66' %(J)s font-size='6.2' font-style='italic' fill='%(M)s'>Um modelo de linguagem é média em texto.</text>
<rect x='30' y='90' width='240' height='28' rx='4' fill='%(O)s'/>
<text x='150' y='102' text-anchor='middle' %(J)s font-size='7' font-weight='800' fill='#F0EDE0'>A pergunta da semana</text>
<text x='150' y='113' text-anchor='middle' %(J)s font-size='6.8' fill='%(S)s'>editar com IA e pensar com IA são a mesma coisa?</text>
</svg>""" % dict(J=J, G=GILT, T=TINTA, M=MUDO, O=OLIVA, S=SAGE)


GRAF = graf_treta()

def caixa(x, n, l1, l2, cor='#EFE9DA', tcor='#43441F'):
    return (u"<rect x='%d' y='6' width='68' height='96' rx='5' fill='%s'/>"
            u"<text x='%d' y='50' text-anchor='middle' font-family='News,serif' font-size='22' font-weight='800' fill='%s'>%s</text>"
            u"<text x='%d' y='70' text-anchor='middle' font-family='Jak,sans-serif' font-size='6.6' fill='#2F2E24'>%s</text>"
            u"<text x='%d' y='82' text-anchor='middle' font-family='Jak,sans-serif' font-size='6.6' fill='#2F2E24'>%s</text>"
            % (x, cor, x + 34, tcor, n, x + 34, l1, x + 34, l2))

FIG2 = (u"<svg viewBox='0 0 300 118' xmlns='http://www.w3.org/2000/svg'>"
        + caixa(0, '19%', 'pediram conselho', 'a um chatbot')
        + caixa(77, '43%', 'desses, ao menos', 'uma vez por mês')
        + caixa(154, '92%', 'acharam', 'útil')
        + caixa(231, '63%', 'não contaram', 'a ninguém', '#F7EDE7', '#A05A3C')
        + u"<text x='150' y='114' text-anchor='middle' font-family='Jak,sans-serif' font-size='6.6' fill='#6C6A55'>1.009 jovens de 12 a 21 anos, Estados Unidos, novembro de 2025</text></svg>")

HTML = u"""<!doctype html><meta charset='utf-8'><style>@FONTES@""" + CSS + u"""</style><div class='pg'>

<div class='top'><img src='/a/logo.png' alt='Lógica Psicológica'>
<div class='e'>Edição 02 &middot; Publicada em setembro de 2026</div></div>

<div class='abre'>
<div>
<h1>Tchê, essa semana a treta foi grande com o Hayes e colaboradores</h1>
<p class='sf'>Um artigo que diz que a média não descreve ninguém veio com a declaração de que Claude e ChatGPT ajudaram no manuscrito. Ao lado, um em cada cinco jovens já pediu conselho de saúde mental a um chatbot, e o ensaio do Therabot mostra efeito grande contra lista de espera, com 28 intervenções humanas no meio.</p>
</div>
<div class='retrato'><img src='/a/julio.jpg' alt='Prof. Júlio Gonçalves'>
<div class='tarja'><b>Seleção e comentário</b><span>Prof. Júlio Gonçalves &middot; CRP 12/17614</span></div></div>
</div>

<div class='duas'>
<div><div class='n'>A notícia da capa</div>
<h2>O artigo, a declaração e a treta</h2>
<div class='fig'>@GRAF@</div>
<p>Hayes, Ciarrochi, Sahdra, Hofmann, Ong e Hernández pedem que a clínica pare de aplicar a média de grupo a pessoas particulares: com 151 pessoas, um efeito médio perto de zero escondia 20 efeitos negativos e 38 positivos. No fim do texto, a declaração obrigatória diz que Claude e ChatGPT foram usados na edição. Lapidar o texto com IA é escolha de ofício; chegar ao argumento com IA seria outra coisa.</p>
<div class='lim'>Não autoriza dizer que o artigo foi escrito por IA, nem que usar IA invalida a tese: o erro ergódico se sustenta ou cai pela matemática, e não pelo processo de edição.</div></div>
<div><div class='n'>A segunda notícia</div>
<h2>Um em cada cinco jovens já perguntou ao chatbot</h2>
<div class='fig'>@FIG2@</div>
<p>Levantamento nacional da RAND e de Harvard na JAMA Pediatrics: 19% dos jovens de 12 a 21 anos já pediram conselho de saúde mental a uma IA, e 63% não contaram a ninguém. Quem já conversava com um médico usou quase o dobro: a IA se soma ao pedido de ajuda, e o silêncio é dado clínico.</p>
<div class='lim'>Não autoriza dizer que o conselho foi bom (a qualidade não foi avaliada) nem que os números valem para o Brasil.</div></div>
</div>

<div class='tres'>
<div><div class='n'>Também nesta edição</div><h2>Therabot: efeito grande, 28 intervenções humanas</h2>
<p>Contra lista de espera, d entre 0,63 e 0,90 em depressão, ansiedade e risco alimentar, e aliança relatada na faixa de pacientes presenciais. Em 8 semanas, a equipe interveio 15 vezes por risco e 13 para corrigir respostas. Nunca foi comparado com terapeuta.</p></div>
<div><div class='n'>Ação para a clínica</div><h2>Separe o que é média do que é particular</h2>
<p>Escreva numa linha para que você usa IA na clínica (transcrição, resumo, revisão de texto) e para que não usa (formulação, escolha de alvo, o que diz ao paciente). Se a segunda lista estiver vazia, a treta se aplica a você.</p></div>
<div><div class='n'>E uma pergunta</div><h2>O que a IA move, e o que só a relação move?</h2>
<p>Para o seu caso mais difícil, liste o que um chatbot conseguiria mover e o que depende de uma pessoa que reage ao que o paciente faz. Use a IA de propósito na primeira lista e proteja a sessão para a segunda.</p></div>
</div>

<div class='foot'>
<span><b>Ação da edição.</b> Pergunte a todo paciente o que ele usa quando está mal e o que faz com a resposta. E decida por escrito onde a IA edita o seu trabalho e onde ela não entra.</span>
<span style='text-align:right;white-space:nowrap'><b>Comunidade Lógica Psicológica</b><br>Edição completa no portal de resumos</span></div>
</div>"""


def gerar(destino):
    prev = WORK + '/prev'
    if os.path.exists(prev):
        shutil.rmtree(prev)
    os.makedirs(prev)
    f = fontes(prev)
    ativos(prev)
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
    dest = SITE + '/newsletter/%s/edicao-02.pdf' % PASTA
    n, m = gerar(dest)
    print('páginas: %d | folga: %d px | %.0f KB' % (n, m['p'] - m['c'], os.path.getsize(dest) / 1024))
