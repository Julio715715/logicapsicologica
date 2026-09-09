# -*- coding: utf-8 -*-
"""Menu lateral em telas baixas (desktop com menos de 680 px de altura):
em vez de esconder a foto e o logo, o menu passa a rolar. Roda em todas as
páginas do site; é idempotente."""
import io, glob

SITE = '/home/claude/site'
ANTIGO = ".side .sig img{display:none;} .side .brand{display:none;}"
NOVO = ".side .brand img{max-width:110px;}"

n = 0
for f in glob.glob(SITE + '/**/index.html', recursive=True):
    h = io.open(f, encoding='utf-8').read()
    if ANTIGO in h:
        io.open(f, 'w', encoding='utf-8').write(h.replace(ANTIGO, NOVO))
        n += 1
print('menu lateral ajustado em %d páginas' % n)
