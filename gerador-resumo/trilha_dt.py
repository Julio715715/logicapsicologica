# -*- coding: utf-8 -*-
"""Trilha 'Dependências tecnológicas' na Jornada da Leitura (disciplina gravada
do Júlio, um vídeo por encontro). Gera o índice da trilha a partir do índice de
Psicoterapeutas Eficazes, registra a trilha no hub da Jornada e ajusta a home.
VIDEOS é a lista que cresce a cada material publicado. Idempotente."""
import io, re

SITE = '/home/claude/site'

# (n, slug ou None, título, tema curto)
VIDEOS = [
    (1, 'aula1', u'Por que brincar é tão bom: bases evolutivas do comportamento lúdico', u'Fundamentos'),
    (2, 'aula2', u'Como os produtos exploram o que a evolução deixou: seis ganchos do design digital', u'Fundamentos'),
    (3, 'aula3', u'O que é a dependência tecnológica? Formas, CID-11 e DSM-5-TR', u'Alinhamento conceitual'),
    (4, 'aula4', u'Impactos na saúde: o que o uso problemático custa e o que ele acompanha', u'Impactos'),
    (5, 'aula5', u'Transtorno do jogo: a aposta, o acaso e os quatro C\'s', u'Transtorno do jogo'),
    (6, 'aula6', u'Critérios diagnósticos do transtorno do jogo: os nove sinais, o ciclo e o que especificar', u'Transtorno do jogo'),
    (7, 'aula7', u'Avaliação diagnóstica: formulação de caso, avaliação ecológica momentânea e as escalas', u'Avaliação'),
    (8, 'aula8', u'Etapas do processo interventivo: fármacos, grupos de apoio, o protocolo STICA e as três fases', u'Intervenção'),
    (9, 'aula9', u'Entrevista motivacional: os estágios de mudança e a pergunta certa para cada um', u'Intervenção'),
    (10, 'aula10', u'Pré-contemplação: o ciclo, as crenças sobre o acaso e o que a neurobiologia diz (e o que não diz)', u'Estágios de mudança'),
    (11, 'aula11', u'Contemplação: a balança de vantagens e desvantagens e a discrepância entre valores e comportamento', u'Estágios de mudança'),
    (12, 'aula12', u'Preparação: metas SMART, escala de alcance, ativação e o manejo do impulso', u'Estágios de mudança'),
]
TOTAL_PREVISTO = None  # None = não anunciar total; a trilha cresce conforme os vídeos chegam


def card(n, slug, titulo, tema):
    if slug:
        return (u"<div class='card live'><div class='ct'><span class='n'>%d</span><span class='dt'>V&iacute;deo %d</span></div>"
                u"<div class='tt'>%s</div><div class='pr'>%s</div><div class='acts'><a class='go' href='%s/'>Abrir</a>"
                u"<a class='pdf' href='%s/resumo.pdf'>PDF</a></div></div>" % (n, n, titulo, tema, slug, slug))
    return (u"<div class='card'><div class='ct'><span class='n'>%d</span><span class='dt'>V&iacute;deo %d</span></div>"
            u"<div class='tt'>%s</div><div class='pr'>%s</div><div class='soon'>em breve</div></div>" % (n, n, titulo, tema))


if __name__ == '__main__':
    import os
    os.makedirs(SITE + '/dependencias-tecnologicas', exist_ok=True)
    h = io.open(SITE + '/psicoterapeutas-eficazes/index.html', encoding='utf-8').read()
    h = re.sub(r"<title>.*?</title>", u"<title>Dependências tecnológicas — Lógica Psicológica</title>", h, count=1)
    a = h.index("<div class='hero'>"); b = h.index("<h2>Encontros</h2>")
    hero = (u"<div class='hero'><div class='kick'>Jornada da Leitura</div><h1>Depend&ecirc;ncias tecnol&oacute;gicas</h1>"
            u"<p>Avaliação e tratamento das dependências tecnológicas: fundamentos evolutivos, transtornos, avaliação e intervenção.</p>"
            u"<div class='divider'></div></div>"
            u"<div class='book'><div class='bk'>Disciplina gravada</div><div class='bt'>Avaliação e tratamento das dependências tecnológicas</div>"
            u"<span style='color:var(--muted);font-size:14px'>Prof. Júlio Gonçalves &middot; um vídeo por encontro, com resumo e PDF</span></div>")
    h = h[:a] + hero + h[b:]
    a = h.index("<div class='cards'>"); b = h.index("</div>", h.rindex("</div></div>", a, h.index("<div class='cta'>"))) if False else None
    # substitui o bloco de cards inteiro (até o CTA)
    a = h.index("<div class='cards'>"); b = h.index("<div class='cta'>")
    cards = ''.join(card(*v) for v in VIDEOS)
    h = h[:a] + "<div class='cards'>" + cards + "</div>" + h[b:]
    io.open(SITE + '/dependencias-tecnologicas/index.html', 'w', encoding='utf-8').write(h)

    pub = sum(1 for v in VIDEOS if v[1])
    tot = TOTAL_PREVISTO or len(VIDEOS)
    tm = (u"%d v&iacute;deos · %d com material publicado &#8594;" % (tot, pub)) if tot > 1 else u"1 v&iacute;deo publicado &#8594;"

    # hub da Jornada
    f = SITE + '/jornada/index.html'; j = io.open(f, encoding='utf-8').read()
    novo = (u"<a class='tema' href='../dependencias-tecnologicas/'><div class='tk'>Prof. Júlio Gonçalves</div>"
            u"<div class='tt'>Dependências tecnológicas</div><div class='td'>Disciplina gravada: avaliação e tratamento, vídeo a vídeo.</div>"
            u"<div class='tm'>%s</div></a>" % tm)
    if 'dependencias-tecnologicas' in j:
        j = re.sub(r"<a class='tema' href='\.\./dependencias-tecnologicas/'>.*?</a>", novo, j, count=1, flags=re.S)
    else:
        j = j.replace("<div class='temas'>", "<div class='temas'>" + novo, 1)
    io.open(f, 'w', encoding='utf-8').write(j)
    print('trilha: %d vídeos, %d publicados' % (len(VIDEOS), pub))
