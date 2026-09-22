# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 16: RPD e reatribuição. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

TORTA = u"""<figure class='dg'><div class='dg-t'>A torta da responsabilidade</div>
<svg viewBox='0 0 720 230' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Gráfico de pizza com cinco fatias: paciente 20 por cento, ausência dos pais 30, amigos que jogam 20, superproteção parental 20, cultura do fazer o que gosta 10; ao lado, a pergunta de reatribuição'>
<g transform='translate(120,115)'>
<path d='M0,0 L0,-90 A90,90 0 0,1 85.6,-27.8 Z' fill='#a05a3c'/>
<path d='M0,0 L85.6,-27.8 A90,90 0 0,1 0,90 Z' fill='#c9c6a8'/>
<path d='M0,0 L0,90 A90,90 0 0,1 -85.6,27.8 Z' fill='#9ca575'/>
<path d='M0,0 L-85.6,27.8 A90,90 0 0,1 -52.9,-72.8 Z' fill='#d9d3c1'/>
<path d='M0,0 L-52.9,-72.8 A90,90 0 0,1 0,-90 Z' fill='#8d876f'/>
</g>
<g %(F)s font-size='10.5' fill='#2f2e24'>
<rect x='250' y='40' width='10' height='10' fill='#a05a3c'/><text x='266' y='49'>paciente · 20%%</text>
<rect x='250' y='62' width='10' height='10' fill='#c9c6a8'/><text x='266' y='71'>ausência dos pais · 30%%</text>
<rect x='250' y='84' width='10' height='10' fill='#9ca575'/><text x='266' y='93'>amigos que jogam · 20%%</text>
<rect x='250' y='106' width='10' height='10' fill='#d9d3c1'/><text x='266' y='115'>superproteção parental · 20%%</text>
<rect x='250' y='128' width='10' height='10' fill='#8d876f'/><text x='266' y='137'>cultura do "fazer o que gosta" · 10%%</text>
</g>
<rect x='450' y='34' width='270' height='150' rx='10' fill='#43441f'/>
<text x='466' y='58' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#9ca575'>EVENTO</text>
<text x='466' y='76' %(F)s font-size='10.5' fill='#f0ede0'>"usei o dinheiro da faculdade</text>
<text x='466' y='92' %(F)s font-size='10.5' fill='#f0ede0'>para investir em jogos"</text>
<text x='466' y='120' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#9ca575'>A PERGUNTA</text>
<text x='466' y='138' %(F)s font-size='10.5' fill='#f0ede0'>tu é 100%% responsável? o que</text>
<text x='466' y='154' %(F)s font-size='10.5' fill='#f0ede0'>essa torta faz com a culpa? o que</text>
<text x='466' y='170' %(F)s font-size='10.5' fill='#f0ede0'>tu pode reparar na tua parte?</text>
</svg>
<figcaption>A torta do exemplo. A fatia do paciente não é zero (ele tem o que reparar), e não é cem (a culpa que paralisa não cabe). Os 20%% são o tamanho da responsabilidade que dá para agir.</figcaption></figure>""" % dict(F=F)

DT16 = {
    'slug': 'aula16',
    'titulo_txt': 'RPD e reatribuição: o pensamento "decepcionei meu pai" e a torta da responsabilidade',
    'titulo_html': 'RPD e reatribui&ccedil;&atilde;o: o pensamento &ldquo;decepcionei meu pai&rdquo; e a torta da responsabilidade',
    'data': 'Vídeo 16',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 16',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 16 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 16',
    'chave': 'mat-Aula-DT16-',
    'arquivo': 'Aula-DT16-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo sexto vídeo da "
              u"disciplina, sobre o registro de pensamentos disfuncionais e a reatribuição, com o mesmo caso do vídeo 15. Não havia transcrição.</p></div>"),
    'tema': 'Duas técnicas cognitivas sobre o mesmo pensamento: o RPD, que testa "decepcionei meu pai" contra as evidências e '
            'produz uma cognição alternativa, e a reatribuição, que divide a responsabilidade pelo dinheiro gasto em jogos numa torta.',
    'essencial': [
        ('O RPD começa pelo precipitante, e não pelo pensamento.',
         'Lembrar que precisa conversar com o pai sobre a dívida. Sem o gatilho, o pensamento parece vir do nada, e não vem.'),
        ('Três pensamentos, um deles quente.',
         '"Decepcionei meu pai", "não sei me controlar", "sou o culpado por tudo isso". O primeiro é o que carrega a emoção, e é o que se testa.'),
        ('Evidências a favor e contra, contadas.',
         'Três de cada lado no exemplo. O empate é o que abre espaço para a alternativa: talvez desapontado com a situação, não decepcionado com a pessoa.'),
        ('A estratégia compensatória é o que mantém.',
         'Esquivar da conversa, inventar desculpa, ruminar. Enquanto ela dura, a crença não é testada, e o RPD só funciona se a conversa acontecer.'),
        ('Reatribuição: a fatia do paciente não é zero nem cem.',
         '20% de responsabilidade no exemplo. É o tamanho que permite reparar sem paralisar.'),
    ],
    'secoes': [
        ('s0', 'O RPD', 'O registro de pensamentos disfuncionais', u"""
<p>O vídeo retoma o caso do vídeo 15 (a matrícula atrasada e o pai que não sabe) e aplica a primeira técnica das intervenções cognitivas: o <strong>registro de pensamentos disfuncionais</strong>, na versão de sete colunas do slide.</p>
<ul class='key'><li><b>Precipitante</b>: lembrar que precisa conversar com o pai sobre a dívida da faculdade.</li><li><b>Pensamentos automáticos</b>: <em>"decepcionei meu pai"</em> (destacado), "não sei me controlar", "sou o culpado por tudo isso".</li><li><b>Quanto acredita</b>: 100%.</li><li><b>Emoções e fisiologia</b>: ansiedade, raiva, frustração.</li><li><b>Intensidade antes</b>: 100%. <b>Depois</b>: a preencher.</li><li><b>Estratégias compensatórias</b>: se esquiva da conversa, inventa desculpa, fica ruminando.</li></ul>
<p>A segunda linha da tabela é o teste. <strong>Evidências a favor</strong> do pensamento: eu menti; ele consideraria isso uma decepção; tenho a sensação de que isso vai acontecer. Total: 3. <strong>O que de pior poderia acontecer, e daqui a cinco anos ainda seria difícil?</strong> Atrasar a formação; talvez difícil no começo, mas provavelmente se resolveria. <strong>O que diria a um amigo</strong>: enfrente o problema, assim se livra de uma vez do sofrimento. <strong>Evidências contra</strong>: meu pai seria compreensivo se eu explicasse o contexto; ele costuma valorizar esforços; ele sabe que não é um curso que gosto e já comentou que eu poderia trancar. Total: 3. <strong>Cognições e comportamentos alternativos</strong>: cognição, "talvez ele fique desapontado com a situação, mas não decepcionado com a minha pessoa, ainda mais se eu explicar o contexto"; comportamento, monitorar o jogo, seguir no tratamento e ser honesto com ele. <strong>Quanto ainda faz sentido acreditar</strong>: a preencher.</p>
<div class='obs'><h4>Três detalhes que fazem o RPD funcionar aqui</h4><p>Primeiro: a coluna do precipitante. O pensamento "decepcionei meu pai" tem hora e gatilho (lembrar da conversa), e é nesse gatilho que a estratégia compensatória entra. Segundo: o pensamento quente. Dos três, "decepcionei meu pai" é o que carrega a emoção; "sou o culpado por tudo" é crença de fundo e vai para a reatribuição. Terceiro: o empate. Três contra três não prova que o pensamento é falso; prova que ele não é a única leitura, e é isso que a cognição alternativa precisa. Repare que ela não nega a decepção; ela a redimensiona: desapontado com a situação, não decepcionado com a pessoa. E a coluna de "comportamento alternativo" é o que impede o RPD de virar exercício de papel: monitorar, seguir, ser honesto. Sem a conversa, a crença nunca é testada de verdade.</p></div>
"""),
        ('s1', 'Reatribuição', 'Reatribuição: a torta da responsabilidade', u"""
{{TORTA}}
<p>A segunda técnica trabalha o pensamento de fundo: "sou o culpado por tudo isso". A ficha de <strong>reatribuição</strong> tem três passos.</p>
<ul class='key'><li><b>1. Evento ou situação negativa</b>: usei o dinheiro da faculdade para investir em jogos.</li><li><b>2. Pessoas e circunstâncias que podem ter contribuído</b>, com porcentagem: paciente, 20; ausência dos pais, 30; amigos que jogam, 20; superproteção parental, 20; cultura do "fazer o que gosta", 10. Soma: 100. E a torta ao lado.</li><li><b>3. A pergunta</b>: você é 100% responsável? como essa torta de responsabilidades afeta seus sentimentos de culpa e vergonha? existe alguma atitude que você pode tomar para reparar a parte pela qual é responsável?</li></ul>
<p>O que a técnica faz é separar <strong>responsabilidade de culpa</strong>. A culpa de 100% paralisa: quem é culpado por tudo não tem por onde começar. A fatia de 20% é agível: é a parte que o paciente pode reparar (a conversa com o pai, o tratamento, o monitoramento), e é exatamente o comportamento alternativo do RPD. As outras fatias não são desculpa; são contexto, e contexto explica sem absolver.</p>
<div class='callout note'><div class='co-t'>Um cuidado</div>A ordem das fatias importa: pedir primeiro todas as outras contribuições e deixar o paciente por último, porque quem começa por si mesmo costuma dar 80 e não sobra torta. E a terceira pergunta é obrigatória: sem "o que tu pode reparar", a reatribuição vira transferência de culpa para os pais, o que não ajuda ninguém e ainda dá ao paciente uma razão nova para não conversar.</div>
"""),
        ('s2', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<ul class='key'><li><b>O precipitante é o antecedente</b>, e a estratégia compensatória (esquivar, desculpa, ruminar) é a evitação que fecha a alça: enquanto a conversa não acontece, a crença fica intacta e a tela tem função.</li><li><b>O RPD trabalha o nó cognitivo</b> "decepcionei" produzindo flexibilidade, e não a crença oposta: a alternativa mantém o desapontamento e muda o alvo (situação, não pessoa).</li><li><b>A reatribuição trabalha o nó de self</b> "sou culpado por tudo", e a fatia de 20% é o tamanho de responsabilidade que permite agir. Culpa total é imobilidade; responsabilidade parcial é plano.</li><li><b>As duas técnicas convergem no mesmo comportamento</b>: a conversa com o pai. É o teste da crença, a reparação da fatia, e o item do plano de ação do vídeo 15. Se ela não acontece, nada do que foi escrito muda a rede.</li></ul>
"""),
    ],
    'checklist': [
        'Comecei o RPD pelo precipitante, e não pelo pensamento.',
        'Identifiquei o pensamento quente entre os automáticos e testei esse, e não o mais fácil.',
        'Contei as evidências dos dois lados e não forcei a balança contra o pensamento.',
        'Escrevi a cognição alternativa redimensionando, e não negando (desapontado com a situação, não com a pessoa).',
        'Anotei a estratégia compensatória e combinei o comportamento alternativo que testa a crença de verdade.',
        'Na reatribuição, pedi as outras contribuições antes da fatia do paciente.',
        'Fiz a terceira pergunta: o que tu pode reparar na tua parte.',
        'Conferi que as duas técnicas apontam para o mesmo comportamento, e marquei quando ele vai acontecer.',
    ],
    'questoes': [
        'Descreva as sete colunas da primeira linha do RPD com o exemplo do slide.',
        'Quais são as evidências a favor e contra "decepcionei meu pai", e o que o empate permite?',
        'Qual é a cognição alternativa do exemplo, e por que ela não nega a decepção?',
        'Descreva os três passos da reatribuição e as fatias da torta do exemplo.',
        'Como a reatribuição separa responsabilidade de culpa, e por que a terceira pergunta é obrigatória?',
        'Pense num paciente teu. Qual é o pensamento quente ligado ao uso, e como tu montaria a torta para a crença de fundo dele?',
    ],
    'gabarito': {
     0: (C, u"Precipitante: lembrar que precisa conversar com o pai sobre a dívida. Pensamentos automáticos: \"decepcionei meu pai\" (quente), \"não sei me controlar\", \"sou o culpado por tudo\". Quanto acredita: 100%. Emoções e fisiologia: ansiedade, raiva, frustração. Intensidade antes: 100%; depois: a preencher. Estratégias compensatórias: esquivar da conversa, inventar desculpa, ruminar."),
     1: (C, u"A favor: eu menti; ele consideraria uma decepção; tenho a sensação de que vai acontecer (3). Contra: ele seria compreensivo com o contexto; valoriza esforços; sabe que não é um curso que gosto e já falou em trancar (3). O empate não prova que o pensamento é falso; prova que não é a única leitura, e é isso que abre espaço para a alternativa."),
     2: (C, u"\"Talvez ele fique desapontado com a situação, mas não decepcionado com a minha pessoa, ainda mais se eu explicar o contexto.\" Ela mantém o desapontamento porque ele é plausível (o paciente mentiu); o que muda é o alvo: situação em vez de pessoa. Alternativa que nega a evidência não convence o paciente e não sobrevive à conversa."),
     3: (C, u"1: evento negativo (usei o dinheiro da faculdade em jogos). 2: pessoas e circunstâncias que contribuíram, com porcentagens: paciente 20, ausência dos pais 30, amigos que jogam 20, superproteção parental 20, cultura do \"fazer o que gosta\" 10. 3: a pergunta: é 100% responsável? como a torta afeta culpa e vergonha? o que pode reparar na sua parte?"),
     4: (C, u"Culpa de 100% paralisa: quem é culpado por tudo não tem por onde começar. A fatia parcial é agível: é o que o paciente pode reparar. As outras fatias explicam sem absolver. A terceira pergunta é obrigatória porque sem \"o que tu pode reparar\" a técnica vira transferência de culpa para os outros, e dá ao paciente uma razão nova para não agir."),
     5: (K, u"Não há resposta certa. Uma boa resposta identifica o pensamento que carrega a emoção no momento do uso (e não o mais genérico), testa esse, e monta a torta para a crença de fundo pedindo as outras fatias antes da do paciente, com a pergunta da reparação no fim. O erro comum é testar \"não sei me controlar\", que é crença de fundo e pede reatribuição ou continuum (vídeo 17), e não RPD."),
    },
    'referencias': [
        "Beck, J. S. (2022). <em>Terapia cognitivo-comportamental: Teoria e prática</em> (3. ed.). Artmed.",
        "Greenberger, D., &amp; Padesky, C. A. (2016). <em>A mente vencendo o humor</em> (2. ed.). Artmed.",
        "Leahy, R. L. (2017). <em>Cognitive therapy techniques: A practitioner's guide</em> (2nd ed.). Guilford Press.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo sexto vídeo de uma disciplina de pós-graduação; o continuum cognitivo vem no vídeo 17.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. A torta foi redesenhada com as porcentagens do slide. Os quadros "três detalhes que fazem o RPD funcionar aqui", "um cuidado" e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina. O caso é a vinheta didática dos vídeos 15 e 16.<br><br><strong>Referências.</strong> Os slides não citam fontes; o RPD de sete colunas e a torta de responsabilidade são técnicas padrão da terapia cognitiva, e os manuais estão nas referências como respaldo.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'TORTA': TORTA}
DT16['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT16['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT16['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT16, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT16)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT16['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
