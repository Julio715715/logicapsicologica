# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 3: O que é a dependência tecnológica?
Fonte: slides da aula (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

VENN = u"""<figure class='dg'><div class='dg-t'>CID-11 e DSM-5-TR: o que cada um pede</div>
<svg viewBox='0 0 720 250' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Dois círculos sobrepostos: critérios só da CID-11, critérios comuns e critérios só do DSM-5-TR'>
<circle cx='260' cy='130' r='112' fill='#f1ece0' fill-opacity='.9' stroke='#9ca575' stroke-width='1.6'/>
<circle cx='460' cy='130' r='112' fill='#fffdf7' fill-opacity='.85' stroke='#a05a3c' stroke-width='1.6'/>
<text x='170' y='36' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a8894f'>CID-11 · 6C51</text>
<text x='560' y='36' text-anchor='end' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>DSM-5-TR · IGD (seção III)</text>
<text x='196' y='120' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>padrão persistente</text>
<text x='196' y='138' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>ou recorrente,</text>
<text x='196' y='156' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>em geral 12 meses</text>
<text x='360' y='96' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>perda de controle</text>
<text x='360' y='118' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>prioridade crescente</text>
<text x='360' y='140' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>continuar apesar</text>
<text x='360' y='158' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>das consequências</text>
<text x='360' y='180' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>prejuízo funcional</text>
<text x='524' y='92' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>abstinência</text>
<text x='524' y='110' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>tolerância</text>
<text x='524' y='128' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>mentir sobre o uso</text>
<text x='524' y='146' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>perda de interesse</text>
<text x='524' y='164' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>usar para escapar</text>
<text x='524' y='182' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>5 de 9, em 12 meses</text>
<text x='360' y='238' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#8d876f'>comorbidades que cercam os dois: ansiedade, depressão, TOC, TDAH</text>
</svg>
<figcaption>O núcleo comum é funcional: controle, prioridade, continuidade apesar do custo, prejuízo. O DSM acrescenta critérios emprestados das substâncias, e é aí que a discussão pega.</figcaption></figure>""" % dict(F=F)

GRAD = u"""<figure class='dg'><div class='dg-t'>Do uso intenso ao transtorno</div>
<svg viewBox='0 0 720 140' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Gradiente em três faixas: uso intenso, uso problemático e transtorno, com o que distingue cada passagem'>
<rect x='0' y='30' width='226' height='60' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='113' y='55' text-anchor='middle' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>uso intenso</text>
<text x='113' y='76' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>muitas horas, sem prejuízo</text>
<rect x='247' y='30' width='226' height='60' rx='10' fill='#fffdf7' stroke='#a8894f' stroke-width='1.4'/>
<text x='360' y='55' text-anchor='middle' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>uso problemático</text>
<text x='360' y='76' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>prejuízo em alguma área, controle oscilante</text>
<rect x='494' y='30' width='226' height='60' rx='10' fill='#43441f'/>
<text x='607' y='55' text-anchor='middle' %(F)s font-size='12.5' font-weight='800' fill='#f0ede0'>transtorno</text>
<text x='607' y='76' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>os critérios, por 12 meses, com prejuízo grave</text>
<text x='236' y='118' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#a05a3c'>o que separa: prejuízo</text>
<text x='484' y='118' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#a05a3c'>o que separa: perda de controle + tempo</text>
</svg>
<figcaption>Tempo de tela sozinho não coloca ninguém em faixa nenhuma. É o prejuízo e a perda de controle que movem a pessoa para a direita.</figcaption></figure>""" % dict(F=F)

DT3 = {
    'slug': 'aula3',
    'titulo_txt': 'O que é a dependência tecnológica? Formas, CID-11 e DSM-5-TR',
    'titulo_html': 'O que &eacute; a depend&ecirc;ncia tecnol&oacute;gica? Formas, CID-11 e DSM-5-TR',
    'data': 'Vídeo 3',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 3',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 3 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 3',
    'chave': 'mat-Aula-DT3-',
    'arquivo': 'Aula-DT3-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do terceiro vídeo da "
              u"disciplina, que faz o alinhamento conceitual: o que é dependência tecnológica, que formas assume e como os dois "
              u"sistemas classificatórios a tratam. Não havia transcrição.</p>"
              u"<p>Os critérios diagnósticos estão parafraseados dos manuais, e não transcritos. Três moderações estão sinalizadas "
              u"no corpo do texto, com a justificativa.</p></div>"),
    'tema': 'Uma definição de trabalho, seis formas em que o problema aparece, e o que a CID-11 e o DSM-5-TR reconhecem, deixam de fora '
            'e discordam entre si. O alinhamento que a avaliação dos próximos vídeos vai exigir.',
    'essencial': [
        ('A definição é funcional, e não de tempo.',
         'Uso excessivo e descontrolado a ponto de causar prejuízo significativo na vida pessoal, social, acadêmica ou profissional. Horas não entram na definição.'),
        ('A CID-11 reconhece o jogo; o resto entra por aproximação.',
         'O transtorno devido a jogos eletrônicos (6C51) tem critérios próprios. Redes, streaming e smartphone cabem numa categoria residual, e não numa entidade.'),
        ('O DSM-5-TR ainda não reconhece.',
         'O transtorno de jogo pela internet está na seção III, como condição para estudo, com nove critérios emprestados das substâncias.'),
        ('O núcleo comum aos dois é o mesmo dos transtornos aditivos.',
         'Perda de controle, prioridade crescente, continuidade apesar das consequências e prejuízo funcional, sustentados por cerca de doze meses.'),
        ('Ansiedade, depressão, TOC e TDAH cercam o quadro.',
         'Comorbidade é regra, e frequentemente a direção é da comorbidade para o uso, e não o contrário. Avaliar um sem o outro erra o alvo.'),
    ],
    'secoes': [
        ('s0', 'Uma definição de trabalho', 'Uma definição de trabalho', u"""
<p>Os dois primeiros vídeos explicaram por que a tela prende. Este alinha o vocabulário antes de entrar em avaliação. A definição adotada pela aula: dependência tecnológica, também chamada de <strong>transtorno de dependência de internet</strong> (TAI), é o <strong>uso excessivo e descontrolado</strong> de recursos tecnológicos (internet, jogos eletrônicos, smartphones, redes sociais) <strong>a ponto de causar prejuízos significativos</strong> na vida pessoal, social, acadêmica ou profissional.</p>
<p>Repare no que a definição faz e no que não faz. Ela exige três coisas: excesso, descontrole e prejuízo. E não exige nenhuma quantidade de horas. Isso importa porque a queixa costuma chegar em horas ("ele fica o dia inteiro no celular"), e horas sozinhas não dizem nada sem as outras duas.</p>
{{GRAD}}
<div class='obs'><h4>Uma moderação sobre o termo</h4><p>"Dependência de internet" é um rótulo de 1998 que a literatura vem questionando, não porque o sofrimento não exista, mas porque a internet é meio e não objeto: ninguém é dependente do cabo. As formas da seção seguinte mostram isso, e a própria CID-11 escolheu nomear o objeto (jogos) e não o meio. A aula usa "dependência tecnológica" como termo guarda-chuva, e o texto mantém, com esta ressalva.</p></div>
"""),
        ('s1', 'As formas que o problema assume', 'As formas que o problema assume', u"""
<p>A dependência tecnológica pode assumir várias formas, e o slide lista seis.</p>
<ul class='key'><li><b>Internet em geral</b>: navegação e consumo de informação sem fim.</li><li><b>Redes sociais</b>: uso compulsivo de Instagram, TikTok, Facebook.</li><li><b>Smartphone</b>: uso constante, checagem automática, a chamada "nomofobia".</li><li><b>Videogames</b>: jogos online, sobretudo os de mundo persistente com muitos jogadores (MMORPGs).</li><li><b>Streaming e pornografia online</b>.</li><li><b>Compras e apostas digitais</b>.</li></ul>
<p>A lista serve para uma coisa: lembrar que o objeto muda o mecanismo. As apostas seguem o esquema de reforço variável quase puro (vídeo 2, gancho 1); as redes sociais apoiam-se na comparação e no status (ganchos 2 e 5); o smartphone como objeto é sobretudo hábito e estímulo preparado (ganchos 4 e 6). Avaliar "uso de tecnologia" sem dizer qual é avaliar nada.</p>
<div class='callout note'><div class='co-t'>Sobre "nomofobia"</div>O termo aparece no slide entre aspas, e as aspas estão certas: não é diagnóstico em nenhum manual. Descreve o desconforto de ficar sem o aparelho e serve como queixa de entrada, não como categoria.</div>
"""),
        ('s2', 'O que a CID-11 reconhece', 'O que a CID-11 reconhece', u"""
<p>A CID-11 criou um agrupamento de <strong>transtornos devidos a comportamentos aditivos</strong>, ao lado dos transtornos por uso de substâncias. É a primeira vez que um sistema classificatório reconhece dependência sem substância como categoria própria, e a dependência tecnológica pode ser analisada por aproximação com dois códigos.</p>
<ul class='key'><li><b>6C51, transtorno devido a jogos eletrônicos</b> (<em>gaming disorder</em>): padrão persistente ou recorrente de comportamento de jogo, digital ou por vídeo, caracterizado por perda de controle sobre o jogar, prioridade crescente dada ao jogo em detrimento de outros interesses e atividades, e continuidade ou escalada apesar de consequências negativas. O padrão é grave o bastante para causar prejuízo significativo e em geral é evidente por pelo menos doze meses.</li><li><b>6C5Y, outros transtornos especificados devidos a comportamentos aditivos</b>: categoria residual que pode abrigar quadros não relacionados a jogos, como redes sociais, streaming e smartphone.</li></ul>
<p>Além disso, a CID-11 permite codificar o uso de risco como condição relevante à saúde mesmo sem critérios de transtorno.</p>
<div class='obs'><h4>Uma moderação de precisão</h4><p>O slide fala em "problemas associados ao uso de internet" como condição codificável. O que a CID-11 tem, no capítulo de fatores que influenciam o estado de saúde, é o código de <strong>jogo de risco</strong> (QE22, <em>hazardous gaming</em>): padrão de jogo que aumenta o risco de dano sem preencher critérios de transtorno. Não há código equivalente para "uso de internet" em geral. O sentido do slide se mantém, a codificação é mais estreita do que ele sugere.</p></div>
"""),
        ('s3', 'O que o DSM-5-TR reconhece, e o que não', 'O que o DSM-5-TR reconhece, e o que não', u"""
<p>O DSM não reconhece a dependência tecnológica como diagnóstico oficial. Menciona três coisas correlatas.</p>
<ul class='key'><li><b>Transtorno de jogo pela internet</b> (<em>Internet Gaming Disorder</em>, IGD): está na seção III do DSM-5-TR, entre as condições para estudos adicionais. Os critérios propostos são nove, e cinco precisam estar presentes em doze meses: preocupação com o jogo, sintomas de abstinência, tolerância, tentativas fracassadas de controlar, perda de interesse por outras atividades, continuidade apesar dos problemas, mentir sobre o uso, jogar para escapar de humor negativo, e prejuízo ou perda de relação, emprego ou estudo.</li><li><b>Transtornos do controle de impulsos</b>: alguns casos de uso problemático têm sido discutidos nessa chave, como já ocorreu com o jogo patológico antes de ele migrar para os transtornos aditivos.</li><li><b>Transtornos relacionados a substâncias e transtornos aditivos</b>: a dependência tecnológica não está listada, mas há debate sobre inclusão futura como transtorno aditivo sem substância, ao lado do jogo de azar.</li></ul>
<p>O detalhe que interessa é a origem dos nove critérios: foram transpostos dos transtornos por substâncias e do jogo de azar. É por isso que aparecem abstinência e tolerância, que a CID-11 não exige.</p>
"""),
        ('s4', 'Onde os dois convergem e onde divergem', 'Onde os dois convergem e onde divergem', u"""
{{VENN}}
<p>O núcleo comum é o que define transtorno aditivo em qualquer objeto: <strong>perda de controle, prioridade excessiva, continuidade apesar das consequências e prejuízo funcional</strong>. Isso é o que os dois sistemas concordam e é o que a avaliação precisa procurar primeiro.</p>
<p>O DSM acrescenta <strong>abstinência, tolerância, mentir, perda de interesse e uso para escapar de emoções negativas</strong>. Os três últimos são clinicamente úteis. Os dois primeiros são os mais discutidos, porque foram criados para substâncias: "tolerância" a um jogo e "abstinência" de uma rede social são conceitos que a pesquisa ainda não conseguiu medir com a mesma clareza.</p>
<div class='obs'><h4>Uma moderação sobre o tempo</h4><p>O slide coloca os doze meses só do lado da CID-11. Os dois sistemas trabalham com essa janela: a CID-11 diz que o padrão é "normalmente evidente por pelo menos doze meses" (e admite encurtar se os critérios forem todos graves), e o DSM-5-TR exige os cinco critérios "num período de doze meses". A diferença real entre eles não está no tempo, e sim nos critérios emprestados das substâncias.</p></div>
<h3>As comorbidades</h3>
<p>Ansiedade, depressão, TOC e TDAH cercam o quadro nos dois sistemas. A relação costuma ser de mão dupla, e com frequência a direção principal é da comorbidade para o uso: a pessoa usa para regular o que a ansiedade ou o vazio depressivo produzem. Isso ecoa a hipótese do uso compensatório e conversa direto com o critério "usar para escapar de emoções negativas". Avaliar a tela sem avaliar o que ela está regulando erra o alvo.</p>
"""),
        ('s5', 'O que levar para a avaliação', 'O que levar para a avaliação', u"""
<p>Três consequências práticas deste alinhamento, antes dos vídeos sobre avaliação.</p>
<p>Primeira: <strong>nomear o objeto</strong>. Jogo, rede, aposta, pornografia, smartphone como hábito. O mecanismo e a intervenção mudam com o objeto, e só o jogo tem categoria própria.</p>
<p>Segunda: <strong>procurar o núcleo funcional antes dos critérios emprestados</strong>. Controle, prioridade, continuidade apesar do custo, prejuízo. Abstinência e tolerância entram depois, e com cautela.</p>
<p>Terceira: <strong>avaliar a comorbidade como parte do quadro</strong>, e não como achado incidental. Muitas vezes é ela que organiza a rede do caso, e a tela é a saída barata que o vídeo 2 descreveu.</p>
<div class='callout note'><div class='co-t'>Leitura em processos</div>Os critérios são descrições de topografia. O que a formulação precisa é a função: o que a pessoa obtém e de que ela sai quando usa. Os dois sistemas ajudam a decidir se há transtorno; nenhum dos dois diz o que tratar. A lista de critérios responde à primeira pergunta; a rede do caso, à segunda.</div>
<h3>O que vem no próximo vídeo</h3>
<p>Os impactos da dependência tecnológica na saúde de modo geral.</p>
"""),
    ],
    'checklist': [
        'Nomeei o objeto do uso (jogo, rede, aposta, pornografia, smartphone) antes de falar em dependência.',
        'Avaliei excesso, descontrole e prejuízo, e não só horas de uso.',
        'Procurei primeiro o núcleo comum: controle, prioridade, continuidade apesar do custo, prejuízo.',
        'Tratei abstinência e tolerância com cautela, como critérios emprestados das substâncias.',
        'Verifiquei a janela de doze meses antes de falar em transtorno.',
        'Avaliei ansiedade, depressão, TOC e TDAH como parte do quadro, e perguntei o que a tela regula.',
        'Distingui, no registro, uso intenso, uso problemático e transtorno.',
    ],
    'questoes': [
        'Enuncie a definição de trabalho da aula e diga o que ela exige e o que ela não exige.',
        'O que a CID-11 reconhece como entidade própria e o que entra por aproximação? Que código cobre redes e streaming?',
        'Por que abstinência e tolerância aparecem no DSM-5-TR e não na CID-11, e por que isso é discutido?',
        'Qual é o núcleo comum aos dois sistemas, e por que a avaliação deveria começar por ele?',
        'Pense num paciente teu que usa muito. Em que faixa tu o colocaria (uso intenso, problemático, transtorno) e com base em quê?',
        'Como tu explicaria a uma família que "o dia inteiro no celular" não é, por si, diagnóstico, sem minimizar a preocupação dela?',
    ],
    'gabarito': {
     0: (C, u"Uso excessivo e descontrolado de recursos tecnológicos a ponto de causar prejuízo significativo na vida pessoal, social, acadêmica ou profissional. Exige <b>excesso, descontrole e prejuízo</b>; não exige quantidade de horas nem um objeto específico. Horas sem prejuízo e sem perda de controle são uso intenso, e não dependência."),
     1: (C, u"Entidade própria: o <b>transtorno devido a jogos eletrônicos</b> (6C51), com perda de controle, prioridade crescente e continuidade apesar das consequências, em geral por doze meses. Redes sociais, streaming e smartphone entram por aproximação na categoria residual <b>6C5Y</b>, outros transtornos especificados devidos a comportamentos aditivos. Uso de risco sem transtorno pode ser codificado como jogo de risco (QE22)."),
     2: (C, u"Porque os nove critérios do transtorno de jogo pela internet foram transpostos dos transtornos por substâncias e do jogo de azar, e abstinência e tolerância fazem parte desse pacote. A CID-11 preferiu um núcleo funcional (controle, prioridade, continuidade) sem eles. A discussão existe porque tolerância a um jogo e abstinência de uma rede são difíceis de definir e de medir, e há risco de patologizar uso intenso comum."),
     3: (C, u"Perda de controle, prioridade excessiva, continuidade apesar das consequências e prejuízo funcional. A avaliação deveria começar por ele porque é o que os dois sistemas concordam, é o que define transtorno aditivo em qualquer objeto, e é o que separa uso intenso de transtorno. Os critérios emprestados entram depois, com cautela."),
     4: (K, u"Não há resposta certa. Uma boa resposta escolhe a faixa a partir de prejuízo e controle, e não de horas: há prejuízo em alguma área? Há tentativas fracassadas de reduzir? Há doze meses de padrão? Cita o objeto (jogo, rede, aposta) e a comorbidade que pode estar organizando o uso. O erro comum é colocar na faixa pelo tempo de tela."),
     5: (K, u"Não há resposta certa. Uma boa resposta valida a preocupação (a família está vendo algo real) e reorienta a pergunta para o que o uso está custando e se a pessoa consegue parar quando precisa. Explica que os manuais definem transtorno por controle, prioridade e prejuízo, e propõe observar isso junto. O erro comum é corrigir a família sobre o diagnóstico e deixar a preocupação sem lugar."),
    },
    'referencias': [
        "American Psychiatric Association. (2022). <em>Manual diagnóstico e estatístico de transtornos mentais: DSM-5-TR</em> (5ª ed., texto revisado). Artmed.",
        "Billieux, J., Schimmenti, A., Khazaal, Y., Maurage, P., &amp; Heeren, A. (2015). Are we overpathologizing everyday life? A tenable blueprint for behavioral addiction research. <em>Journal of Behavioral Addictions, 4</em>(3), 119–123.",
        "Brand, M., Wegmann, E., Stark, R., M&uuml;ller, A., W&ouml;lfling, K., Robbins, T. W., &amp; Potenza, M. N. (2019). The Interaction of Person-Affect-Cognition-Execution (I-PACE) model for addictive behaviors: Update, generalization to addictive behaviors beyond internet-use disorders, and specification of the process character of addictive behaviors. <em>Neuroscience &amp; Biobehavioral Reviews, 104</em>, 1–10.",
        "Kardefelt-Winther, D. (2014). A conceptual and methodological critique of internet addiction research: Towards a model of compensatory internet use. <em>Computers in Human Behavior, 31</em>, 351–354.",
        "King, D. L., &amp; Delfabbro, P. H. (2019). <em>Internet gaming disorder: Theory, assessment, treatment, and prevention.</em> Academic Press.",
        "Lutfian, L., Rizanti, A. P., &amp; Chandra, I. N. (2023). The use of cognitive behaviour therapy as a treatment of internet addiction disorder in adolescents: Literature review. <em>Journal of Public Health Research and Community Health Development, 6</em>(2). https://doi.org/10.20473/jphrecode.v6i2.31158",
        "Organização Mundial da Saúde. (2019). <em>Classificação Internacional de Doenças, 11ª revisão (CID-11)</em>: 6C51 transtorno devido a jogos eletrônicos; 6C5Y outros transtornos especificados devidos a comportamentos aditivos; QE22 jogo de risco.",
        "Internet and video game addictions: A cognitive behavioral approach. (2014). <em>Revista de Psiquiatria Clínica, 41</em>(3). https://doi.org/10.1590/0101-60830000000016",
        "Young, K. S. (1998). Internet addiction: The emergence of a new clinical disorder. <em>CyberPsychology &amp; Behavior, 1</em>(3), 237–244.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o terceiro vídeo de uma disciplina de pós-graduação e faz o alinhamento conceitual; avaliação e intervenção vêm depois.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. Os critérios diagnósticos foram conferidos nos manuais e aparecem parafraseados; a ligação entre as formas do problema e os ganchos do vídeo 2, e a seção final sobre avaliação, foram desenvolvidas pelo autor do material a partir da lógica da disciplina.<br><br><strong>Três moderações, sinalizadas no texto.</strong> Primeira: o rótulo "dependência de internet" é questionado na literatura por tomar o meio pelo objeto; o texto mantém o termo guarda-chuva da aula com a ressalva. Segunda: a CID-11 não tem código para "problemas associados ao uso de internet" em geral; o que existe é o jogo de risco (QE22), e o texto corrige a codificação sem mudar o sentido. Terceira: a janela de doze meses vale para os dois sistemas, e não só para a CID-11; a diferença real está nos critérios emprestados das substâncias.<br><br><strong>Referências dos slides.</strong> Os dois artigos mostrados nos slides foram incluídos: a revisão de Lutfian et al. (2023) e o artigo de 2014 da Revista de Psiquiatria Clínica, este citado pelo título e DOI porque a autoria não pôde ser conferida no momento da escrita. As demais referências foram acrescentadas para dar respaldo formal ao que os slides afirmam sem citação: os manuais, a origem do termo, a crítica à patologização do cotidiano, o modelo do uso compensatório e o modelo I-PACE. Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'VENN': VENN, 'GRAD': GRAD}
DT3['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DT3['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT3['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT3, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT3)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT3['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
