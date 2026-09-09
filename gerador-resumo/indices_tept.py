# -*- coding: utf-8 -*-
"""Insere a aula 'Tratando o TEPT complexo' nos índices: card em aulas/index.html,
contadores e bloco 'Publicado agora' na home, LEIA-ME. Idempotente."""
import io
SITE = '/home/claude/site'

CARD = (u"<div class='card bydate live'><div class='ct'><span class='dt'>27/04</span></div>"
        u"<div class='tt'>Tratando o TEPT complexo</div><div class='pr'>Andressa Juliana</div>"
        u"<div class='acts'><a class='go' href='tept-complexo/'>Abrir</a>"
        u"<a class='pdf' href='tept-complexo/resumo.pdf'>PDF</a></div></div>")

f = SITE + '/aulas/index.html'
h = io.open(f, encoding='utf-8').read()
if 'tept-complexo/' not in h:
    anc = u"<a class='pdf' href='transtornos-alimentares/resumo.pdf'>PDF</a></div></div>"
    assert anc in h
    h = h.replace(anc, anc + CARD, 1)
    io.open(f, 'w', encoding='utf-8').write(h)
    print('card inserido em aulas/')

f = SITE + '/index.html'
h = io.open(f, encoding='utf-8').read()
if 'tept-complexo/' not in h:
    for a, b in [(u"32 materiais publicados", u"33 materiais publicados"),
                 (u"5 aulas publicadas", u"6 aulas publicadas")]:
        assert a in h, a
        h = h.replace(a, b, 1)
    i = h.index("<a class='novo' href='/aulas/transdiagnostico-substancias/'>")
    j = h.index("</a>", i) + 4
    h = h[:i] + (u"<a class='novo' href='/aulas/tept-complexo/'><div class='nvk'>Publicado agora</div>"
                 u"<div class='nvt'>Tratando o TEPT complexo</div>"
                 u"<div class='nvm'>Aula livre &middot; 27/04/2026 &middot; Andressa Juliana</div>"
                 u"<span class='nva'>Abrir o material &#8594;</span></a>") + h[j:]
    io.open(f, 'w', encoding='utf-8').write(h)
    print('home atualizada')
