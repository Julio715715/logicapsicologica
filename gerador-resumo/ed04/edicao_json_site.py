# -*- coding: utf-8 -*-
"""Página do site de uma edição a partir do edicao.json do molde Bagual.

uso: python3 edicao_json_site.py <pasta-da-edicao> <PASTA-no-site YYYY-MM-DD> <nome-do-pdf>
ex.: python3 edicao_json_site.py ed04 2026-10-03 edicao-04.pdf

Reaproveita item()/conferir() de edicao02_site.py e o molde da página da Ed. 1.
Imprime a linha para o bloco da home (span.nres). Idempotente no índice.
"""
import io, os, re, sys, json
from edicao02_site import item, conferir, SITE

pasta_ed, PASTA, PDF = sys.argv[1], sys.argv[2], sys.argv[3]
ED = json.load(io.open(os.path.join(pasta_ed, 'edicao.json'), encoding='utf-8'))
NUM = int(ED['numero']); NUMTXT = u'Edição %d' % NUM
NPAG = 'quatro páginas'


def figura(m):
    svg = io.open(os.path.join(pasta_ed, m['figura_svg']), encoding='utf-8').read().strip()
    return u"<figure class='nwfig'>%s<figcaption>%s</figcaption></figure>" % (svg, m['legenda_figura'])


def url_ref(m):
    # primeiro link http na referência, se houver; senão, sem botão
    u = re.search(r"https?://\S+", m['referencia'])
    return (u.group(0).rstrip('.'), 'Ver a fonte') if u else ('#', '')


ITENS, IDX = [], []
for i, m in enumerate(ED['materias'], 1):
    url, rot = url_ref(m)
    ITENS.append(item(i, m['retranca'], m['titulo'], m['linha_fina'], [tuple(x) for x in m['ficha']], figura(m),
                      m['muda_na_clinica'], m['nao_autoriza_dizer'], m['acao_para_a_clinica'], m['pergunta'],
                      m['referencia'], url, rot))
    IDX.append((i, m['titulo']))
    if not rot:  # sem link: tira a âncora vazia
        ITENS[-1] = ITENS[-1].replace(u"<a href='#' target='_blank' rel='noopener'> &#8599;</a>", '')

TEMA = ED['ao_leitor']
titulos = [m['titulo'] for m in ED['materias']]
curto = lambda t: t.split('.')[0].replace(u'Tchê, ', '')
RESUMO_CARD = u' · '.join(curto(t) for t in titulos)
RESUMO_HOME = u' &middot; '.join(curto(t) for t in titulos) + u" &middot; <b>edição em PDF</b>"

if __name__ == '__main__':
    base = SITE + '/newsletter/2026-09/index.html'
    h = io.open(base, encoding='utf-8').read()
    i = h.index("<article class='nw'"); j = h.rindex("</article>") + len("</article>")
    h = h[:i] + '\n'.join(ITENS) + h[j:]
    a = h.index("<div class='idx'>"); b = h.index("</div>", a) + 6
    h = h[:a] + "<div class='idx'>" + ''.join(u"<a href='#i%d'>%s</a>" % x for x in IDX) + "</div>" + h[b:]
    conferir(u"<div class='sub'>Edição 1</div>" in h, 'número da edição')
    h = h.replace(u"<div class='sub'>Edição 1</div>", u"<div class='sub'>%s</div>" % NUMTXT)
    a = h.index("<p class='tema'>"); b = h.index("</p>", a) + 4
    h = h[:a] + u"<p class='tema'>" + TEMA + u"</p>" + h[b:]
    h = re.sub(r"<title>.*?</title>", u"<title>%s · O que vale ler · Lógica Psicológica</title>" % NUMTXT, h, count=1)
    conferir("href='edicao-01.pdf'" in h, 'botão do pdf')
    h = h.replace("href='edicao-01.pdf'", "href='%s'" % PDF)
    h = re.sub(r'(?i)publicada em setembro de 2026', lambda m: ('Publicada em ' if m.group(0)[0]=='P' else 'publicada em ') + ED['mes'], h)
    h = h.replace(u"&mdash; uma página, para ler e compartilhar", u"&mdash; %s, o Jornal Bagual" % NPAG)
    os.makedirs(SITE + '/newsletter/' + PASTA, exist_ok=True)
    io.open(SITE + '/newsletter/%s/index.html' % PASTA, 'w', encoding='utf-8').write(h)
    print('edição %d: %d itens' % (NUM, h.count("<article class='nw'")))

    f = SITE + '/newsletter/index.html'
    h = io.open(f, encoding='utf-8').read()
    if (u"%s</div>" % NUMTXT) not in h:
        card = (u"<div class='card bydate live'><div class='ct'><span class='dt'>%02d</span></div>"
                u"<div class='tt'>%s</div><div class='pr'>%s</div>"
                u"<div class='acts'><a class='go' href='%s/'>Abrir</a><a class='pdf' href='%s/%s'>PDF</a></div></div>"
                % (NUM, NUMTXT, RESUMO_CARD, PASTA, PASTA, PDF))
        conferir("<div class='cards'>" in h, 'grade de cards')
        h = h.replace("<div class='cards'>", "<div class='cards'>" + card, 1)
        io.open(f, 'w', encoding='utf-8').write(h)
        print('card inserido no índice')
    print('home (span.nres): ' + RESUMO_HOME)
