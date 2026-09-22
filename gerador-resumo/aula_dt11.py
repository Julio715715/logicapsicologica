# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 11: Fase da contemplação. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

CAMINHOS = u"""<figure class='dg'><div class='dg-t'>Os caminhos da vida</div>
<svg viewBox='0 0 720 230' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Uma pessoa à esquerda e dois caminhos que se separam: o caminho sonhado, para cima, com saúde, curso ou trabalho, conexões e dinheiro; e o caminho atual, para baixo, com demandas psicológicas, tempo perdido, isolamento e dívida. No meio, as perguntas: como minha vida está, como pode melhorar'>
<circle cx='44' cy='96' r='12' fill='#43441f'/><rect x='34' y='110' width='20' height='40' rx='6' fill='#43441f'/>
<path d='M70 118 C 200 118, 260 40, 700 40' fill='none' stroke='#9ca575' stroke-width='14' stroke-linecap='round' opacity='0.55'/>
<path d='M70 122 C 200 122, 260 200, 700 200' fill='none' stroke='#a05a3c' stroke-width='14' stroke-linecap='round' opacity='0.45'/>
<text x='140' y='72' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#43441f'>CAMINHO SONHADO</text>
<text x='250' y='58' %(F)s font-size='11' fill='#2f2e24'>saúde</text>
<text x='330' y='48' %(F)s font-size='11' fill='#2f2e24'>curso, trabalho</text>
<text x='450' y='34' %(F)s font-size='11' fill='#2f2e24'>conexões</text>
<text x='560' y='30' %(F)s font-size='11' fill='#2f2e24'>+ R$</text>
<text x='140' y='178' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>CAMINHO ATUAL</text>
<text x='250' y='192' %(F)s font-size='11' fill='#2f2e24'>demandas psi</text>
<text x='350' y='206' %(F)s font-size='11' fill='#2f2e24'>tempo perdido</text>
<text x='460' y='214' %(F)s font-size='11' fill='#2f2e24'>isolamento</text>
<text x='560' y='218' %(F)s font-size='11' fill='#2f2e24'>&minus; R$</text>
<text x='400' y='112' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>Como minha vida está?</text>
<text x='400' y='132' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>Como pode melhorar?</text>
<rect x='690' y='22' width='24' height='36' rx='4' fill='#d9d3c1' stroke='#8d876f'/>
<rect x='690' y='182' width='24' height='36' rx='4' fill='#d9d3c1' stroke='#8d876f'/>
</svg>
<figcaption>O desenho do slide, redesenhado. Os dois caminhos terminam no mesmo lugar; o que muda é o que a pessoa faz no trajeto. A pergunta do meio é a que a contemplação precisa responder.</figcaption></figure>""" % dict(F=F)

AREAS = u"""<figure class='dg'><div class='dg-t'>Oito áreas para a balança</div>
<svg viewBox='0 0 720 190' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Oito áreas da análise de vantagens e desvantagens: emocional, cognitiva, social, saúde, acadêmica, financeira, familiar e lazer offline'>
<rect x='0' y='6' width='172' height='80' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='12' y='28' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Emocional</text>
<text x='12' y='48' %(F)s font-size='9.5' fill='#6c6a55'>ansiedade, estresse, alívio,</text>
<text x='12' y='62' %(F)s font-size='9.5' fill='#6c6a55'>regulação, autoestima</text>
<rect x='182' y='6' width='172' height='80' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='194' y='28' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Cognitiva</text>
<text x='194' y='48' %(F)s font-size='9.5' fill='#6c6a55'>concentração, foco,</text>
<text x='194' y='62' %(F)s font-size='9.5' fill='#6c6a55'>procrastinação, crenças</text>
<rect x='364' y='6' width='172' height='80' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='376' y='28' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Social</text>
<text x='376' y='48' %(F)s font-size='9.5' fill='#6c6a55'>amizades, relações, suporte,</text>
<text x='376' y='62' %(F)s font-size='9.5' fill='#6c6a55'>online e offline</text>
<rect x='546' y='6' width='174' height='80' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='558' y='28' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Saúde</text>
<text x='558' y='48' %(F)s font-size='9.5' fill='#6c6a55'>sono, alimentação, atividade</text>
<text x='558' y='62' %(F)s font-size='9.5' fill='#6c6a55'>física, dores, visão, exaustão</text>
<rect x='0' y='100' width='172' height='80' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='12' y='122' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Acadêmica</text>
<text x='12' y='142' %(F)s font-size='9.5' fill='#6c6a55'>assiduidade, produtividade,</text>
<text x='12' y='156' %(F)s font-size='9.5' fill='#6c6a55'>prazos, notas, motivação</text>
<rect x='182' y='100' width='172' height='80' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='194' y='122' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Financeira</text>
<text x='194' y='142' %(F)s font-size='9.5' fill='#6c6a55'>gastos com jogos, microtransações,</text>
<text x='194' y='156' %(F)s font-size='9.5' fill='#6c6a55'>compras, prejuízo</text>
<rect x='364' y='100' width='172' height='80' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='376' y='122' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Familiar</text>
<text x='376' y='142' %(F)s font-size='9.5' fill='#6c6a55'>regras, limites, convivência,</text>
<text x='376' y='156' %(F)s font-size='9.5' fill='#6c6a55'>conflitos, apoio, expectativas</text>
<rect x='546' y='100' width='174' height='80' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='558' y='122' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Lazer offline</text>
<text x='558' y='142' %(F)s font-size='9.5' fill='#6c6a55'>hobbies, leitura, esporte, arte,</text>
<text x='558' y='156' %(F)s font-size='9.5' fill='#6c6a55'>espiritualidade, metas, planos</text>
</svg>
<figcaption>As oito áreas do slide. A balança feita só em "tempo" sai vazia; feita por área, aparece o que o paciente não tinha ligado ao uso.</figcaption></figure>""" % dict(F=F)

DT11 = {
    'slug': 'aula11',
    'titulo_txt': 'Contemplação: a balança de vantagens e desvantagens e a discrepância entre valores e comportamento',
    'titulo_html': 'Contempla&ccedil;&atilde;o: a balan&ccedil;a de vantagens e desvantagens e a discrep&acirc;ncia entre valores e comportamento',
    'data': 'Vídeo 11',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 11',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 11 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 11',
    'chave': 'mat-Aula-DT11-',
    'arquivo': 'Aula-DT11-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo primeiro vídeo da "
              u"disciplina, sobre a fase de contemplação. Não havia transcrição.</p>"
              u"<p>O vídeo tem quatro slides de conteúdo: a ficha do estágio, a tabela de vantagens e desvantagens, as oito áreas e o desenho dos caminhos da vida.</p></div>"),
    'tema': 'O paciente ambivalente: como levantar a balança de vantagens e desvantagens sem inclinar o prato, as oito áreas em que '
            'olhar, e o exercício dos caminhos da vida para trabalhar a discrepância entre o que a pessoa valoriza e o que faz.',
    'essencial': [
        ('Contemplação: "reconheço que pode ser um problema, mas não sei se quero mudar".',
         'O paciente está ambivalente: vê os prejuízos e ainda valoriza os benefícios (distração, prazer, socialização online).'),
        ('A balança se faz com os dois pratos cheios.',
         'Vantagens percebidas de um lado, desvantagens percebidas ou reais do outro, nas palavras do paciente. Uma balança inclinada pelo terapeuta não pesa.'),
        ('Oito áreas, para não fazer a balança só em tempo.',
         'Emocional, cognitiva, social, saúde, acadêmica, financeira, familiar e lazer offline. Cada uma revela uma ligação que o paciente não tinha feito.'),
        ('O trabalho é a discrepância entre valores e comportamento.',
         'Os caminhos da vida: o sonhado e o atual saem do mesmo ponto e chegam ao mesmo lugar. A pergunta é o que a pessoa faz no trajeto.'),
        ('A terceira pergunta abre a preparação.',
         '"O que te impede de mudar esse padrão agora?" transforma ambivalência em obstáculo nomeado, e obstáculo nomeado tem plano.'),
    ],
    'secoes': [
        ('s0', 'A ficha do estágio', 'Contemplação: a ficha do estágio', u"""
<p>O segundo estágio, na frase do paciente: <em>"Eu reconheço que pode ser um problema, mas ainda não tenho certeza se quero mudar."</em></p>
<ul class='key'><li><b>Características</b>: o paciente está ambivalente. Vê prós e contras em continuar como está. Reconhece os prejuízos, mas ainda valoriza os "benefícios": distração, prazer, socialização online.</li><li><b>Perguntas</b>: quais são as coisas boas e as coisas ruins de passar tanto tempo online ou jogando; o que ele acredita que poderia melhorar na vida se usasse menos tecnologia; e uma terceira, nova em relação ao vídeo 9: <strong>o que te impede de mudar esse padrão agora?</strong></li><li><b>Intervenção</b>: aplicar a análise de vantagens e desvantagens; trabalhar a discrepância entre valores e comportamentos.</li></ul>
<p>Repare no que muda em relação à pré-contemplação. Lá, as perguntas abriam a percepção; aqui, a percepção já existe, e as perguntas trabalham a ambivalência. E a terceira pergunta faz uma coisa importante: transforma "não sei se quero" em "o que me impede", que é um obstáculo com nome. Obstáculo com nome tem plano, e o plano é a fase seguinte.</p>
"""),
        ('s1', 'A balança', 'A balança de vantagens e desvantagens', u"""
<p>O slide traz uma tabela de exemplo com duas colunas, <strong>vantagens percebidas</strong> e <strong>desvantagens percebidas ou reais</strong>, em frases de paciente.</p>
<ul class='key'><li><b>Escape da realidade</b>: "consigo esquecer dos meus problemas enquanto estou jogando". Do outro lado, <b>problemas no sono</b>: "vou dormir muito tarde e acordo cansado".</li><li><b>Sensação de competência</b>: "sinto que sou bom em algo quando jogo". Do outro lado, <b>queda no desempenho escolar ou profissional</b>: "tenho deixado de fazer trabalhos e entregas por causa do jogo".</li><li><b>Socialização online</b>: "tenho amigos no jogo com quem falo todos os dias". Do outro lado, <b>isolamento social offline</b>: "quase não saio mais com meus amigos ou familiares".</li><li><b>Prazer imediato</b>: "é divertido e me distrai rapidamente". Do outro lado, <b>culpa e arrependimento</b>: "depois de jogar por horas, fico me sentindo mal comigo mesmo".</li></ul>
<div class='obs'><h4>Três cuidados ao fazer a balança</h4><p>Primeiro: as vantagens são reais, e o terapeuta que as trata como desculpa perde o paciente. "Sinto que sou bom em algo quando jogo" é um dado de formulação: diz que a pessoa não tem outro lugar onde se sinta competente, e esse é o vazio que a intervenção vai precisar preencher. Segundo: a coluna diz "percebidas ou reais" de propósito; o paciente lista o que percebe, e o terapeuta pode acrescentar o que a avaliação mostrou (a EMA do vídeo 7, por exemplo), sem transformar a lista dele na lista do terapeuta. Terceiro: os pares da tabela não são coincidência. Cada vantagem tem a desvantagem correspondente na mesma linha (escapar dos problemas e dormir tarde; amigos no jogo e nenhum fora dele). Mostrar o par é mostrar que o mesmo comportamento produz os dois, o que é o começo da discrepância.</p></div>
"""),
        ('s2', 'As oito áreas', 'As oito áreas da análise', u"""
{{AREAS}}
<p>O slide seguinte lista as áreas que podem ser abordadas na análise. A <strong>emocional</strong>, como a pessoa lida com as emoções e o impacto emocional do comportamento (ansiedade, estresse, tristeza, irritabilidade, alívio, regulação afetiva, autoestima). A <strong>cognitiva</strong>, os processos de pensamento, atenção, memória e decisão (concentração, foco, procrastinação, crenças centrais e autopercepções sobre o comportamento). A <strong>social</strong>, qualidade e quantidade das relações, online e offline (família, amizades, relacionamentos amorosos, suporte social, participação em atividades). A <strong>saúde</strong>, o estado físico e os hábitos de autocuidado (sono, alimentação, atividade física, higiene, dores musculares, visão, exaustão). A <strong>acadêmica</strong>, desempenho e funcionamento no estudo ou trabalho (assiduidade, produtividade, concentração, tarefas, notas, prazos, satisfação, motivação). A <strong>financeira</strong>, como o comportamento afeta os recursos (gastos com jogos, equipamentos, microtransações, compras compulsivas online, planejamento e prejuízo). A <strong>familiar</strong>, dinâmicas e relações no núcleo familiar (regras, limites, convivência, comunicação, conflitos, apoio emocional, expectativas). E o <strong>lazer offline</strong>, envolvimento em atividades de crescimento e lazer fora do digital (hobbies, leitura, esporte, arte, espiritualidade, voluntariado, metas pessoais, planos de vida).</p>
<p>A utilidade da lista é uma só: a balança feita em "tempo de uso" sai vazia dos dois lados, porque tempo não é vantagem nem desvantagem. Feita por área, cada linha revela uma ligação que o paciente não tinha feito, e as últimas duas (familiar e lazer offline) costumam ser as que mais surpreendem.</p>
"""),
        ('s3', 'Os caminhos da vida', 'Os caminhos da vida: valores e comportamento', u"""
{{CAMINHOS}}
<p>O último slide é um desenho à mão, feito em sessão. Uma pessoa, e dois caminhos que saem do mesmo ponto. O <strong>caminho sonhado</strong>, para cima: saúde, curso ou trabalho, conexões, mais dinheiro. O <strong>caminho atual</strong>, para baixo: demandas psicológicas, tempo perdido, isolamento, menos dinheiro. No meio, duas perguntas: <em>como minha vida está? como pode melhorar?</em> E no fim dos dois caminhos, a mesma imagem: uma lápide.</p>
<p>É a intervenção do slide para a "discrepância entre valores e comportamentos". O desenho faz três coisas de uma vez. Coloca os valores da pessoa no papel com as palavras dela (o que está no caminho sonhado é o que ela quer, e não o que a família quer). Coloca o comportamento atual ao lado, na mesma escala. E lembra que os dois caminhos têm o mesmo fim, o que retira a pergunta do plano da culpa e a coloca no plano da escolha: o tempo é o mesmo nos dois; o que muda é o que a pessoa faz com ele.</p>
<div class='callout note'><div class='co-t'>Como usar</div>Desenhar junto, em papel, na sessão. Pedir primeiro o caminho sonhado, e com detalhe: que saúde, que trabalho, que conexões. Só depois o atual, com o que a balança já levantou. E então as duas perguntas do meio, na ordem: como está, como pode melhorar. A lápide não precisa de comentário; quem desenha entende. Para a maioria dos pacientes em contemplação, é o momento em que a ambivalência inclina, e é o material para a pergunta seguinte: o que te impede de ir pelo de cima?</div>
"""),
        ('s4', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>A contemplação é o estágio em que a rede está mais visível para o próprio paciente, e as três ferramentas do vídeo trabalham nós diferentes.</p>
<ul class='key'><li><b>A balança trabalha a função.</b> Cada vantagem percebida é uma função que o uso cumpre (escapar, sentir-se competente, pertencer, se distrair). A intervenção vai precisar repor cada uma; a balança é o inventário.</li><li><b>As oito áreas trabalham a discriminação.</b> Ligam o uso a consequências que o paciente não tinha conectado, o que é o mesmo movimento do ciclo no vídeo 10, agora por domínio de vida.</li><li><b>Os caminhos da vida trabalham valores e self.</b> É a intervenção de discrepância: a pessoa se vê fazendo o oposto do que quer, sem que ninguém tenha dito isso a ela.</li><li><b>A terceira pergunta trabalha a barreira.</b> "O que te impede" converte ambivalência difusa em obstáculo específico, e obstáculo específico é o que a preparação resolve.</li></ul>
<p>Na prática: balança por área, desenho dos caminhos, e a pergunta do que impede. Nessa ordem, numa ou duas sessões, sem pressa para chegar à meta.</p>
"""),
    ],
    'checklist': [
        'Perguntei as coisas boas antes das ruins, e levei as boas a sério como dados de formulação.',
        'Fiz a balança por área, e não só em tempo de uso.',
        'Deixei o paciente escrever as frases dele; acrescentei dados da avaliação sem substituir a lista dele.',
        'Mostrei os pares (a vantagem e a desvantagem que o mesmo comportamento produz).',
        'Desenhei os caminhos da vida junto com o paciente, com o caminho sonhado nas palavras dele.',
        'Fiz as duas perguntas do meio na ordem: como está, como pode melhorar.',
        'Fechei com "o que te impede de mudar esse padrão agora?" e anotei o obstáculo nomeado.',
        'Não propus meta ainda; guardei o obstáculo para a fase de preparação.',
    ],
    'questoes': [
        'Descreva a ficha da contemplação: características, as três perguntas e a intervenção.',
        'Quais são os quatro pares da tabela de vantagens e desvantagens, e o que os pares mostram?',
        'Quais são as oito áreas da análise, e por que a balança feita só em tempo de uso sai vazia?',
        'Descreva o exercício dos caminhos da vida e o que ele faz com a discrepância entre valores e comportamento.',
        'O que a terceira pergunta ("o que te impede de mudar agora?") faz com a ambivalência?',
        'Pense num paciente teu em contemplação. Quais vantagens ele percebe no uso, e que função cada uma cumpre?',
    ],
    'gabarito': {
     0: (C, u"Características: ambivalência; vê prós e contras em continuar como está; reconhece os prejuízos, mas valoriza os benefícios (distração, prazer, socialização online). Perguntas: coisas boas e ruins de passar tanto tempo online; o que poderia melhorar se usasse menos; o que impede de mudar o padrão agora. Intervenção: análise de vantagens e desvantagens e trabalho da discrepância entre valores e comportamentos."),
     1: (C, u"Escape da realidade e problemas no sono; sensação de competência e queda no desempenho; socialização online e isolamento offline; prazer imediato e culpa e arrependimento. Os pares mostram que o mesmo comportamento produz a vantagem e a desvantagem correspondente, o que é o começo da discrepância: não dá para ficar com um lado da linha."),
     2: (C, u"Emocional, cognitiva, social, saúde, acadêmica, financeira, familiar e lazer offline. Tempo de uso não é vantagem nem desvantagem em si; a balança só enche quando cada área revela uma ligação concreta entre o uso e algo que a pessoa ganha ou perde ali, e as áreas familiar e de lazer offline costumam trazer ligações que o paciente não tinha feito."),
     3: (C, u"Desenho em sessão: a pessoa e dois caminhos que saem do mesmo ponto, o sonhado (saúde, curso ou trabalho, conexões, mais dinheiro) e o atual (demandas psicológicas, tempo perdido, isolamento, menos dinheiro), com as perguntas \"como minha vida está? como pode melhorar?\" no meio e o mesmo fim para os dois. Coloca os valores da pessoa nas palavras dela, o comportamento ao lado na mesma escala, e tira a pergunta do plano da culpa para o da escolha: o tempo é o mesmo, o que muda é o que ela faz no trajeto."),
     4: (C, u"Converte a ambivalência difusa (\"não sei se quero\") em obstáculo específico e nomeado (\"o que me impede é X\"). Obstáculo nomeado admite plano, e o plano é a fase de preparação. É a pergunta que faz a ponte entre os dois estágios."),
     5: (K, u"Não há resposta certa. Uma boa resposta lista as vantagens nas palavras do paciente e nomeia a função de cada uma (escapar de um problema específico, sentir-se competente onde não se sente em outro lugar, pertencer a um grupo, preencher tempo vazio), porque esse inventário é o que a intervenção vai precisar repor. O erro comum é listar as vantagens como desculpas a serem desmontadas, o que perde tanto o paciente quanto a formulação."),
    },
    'referencias': [
        "Hayes, S. C., Strosahl, K. D., &amp; Wilson, K. G. (2012). <em>Acceptance and commitment therapy: The process and practice of mindful change</em> (2nd ed.). Guilford Press.",
        "Janis, I. L., &amp; Mann, L. (1977). <em>Decision making: A psychological analysis of conflict, choice, and commitment.</em> Free Press.",
        "Miller, W. R., &amp; Rollnick, S. (2023). <em>Entrevista motivacional: Ajudando pessoas a mudar e crescer</em> (4. ed.). Artmed.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo primeiro vídeo de uma disciplina de pós-graduação; a fase de preparação vem no vídeo 12.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. Os três cuidados ao fazer a balança, o quadro "como usar" dos caminhos da vida e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina. O desenho dos caminhos da vida foi redesenhado a partir do esboço à mão do slide, mantendo os elementos e as palavras.<br><br><strong>Referências.</strong> Os slides não citam fontes. A balança decisional remonta a Janis e Mann (1977) e é ferramenta padrão da entrevista motivacional; o trabalho com discrepância entre valores e comportamento tem formulação na terapia de aceitação e compromisso, e as duas obras estão nas referências como respaldo, não como fonte dos slides.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'CAMINHOS': CAMINHOS, 'AREAS': AREAS}
DT11['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT11['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT11['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT11, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT11)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT11['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
