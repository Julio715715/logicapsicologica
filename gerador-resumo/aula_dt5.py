# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 5: Transtorno do jogo (introdução). Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

NECESS = u"""<figure class='dg'><div class='dg-t'>Duas necessidades antigas, um transtorno novo</div>
<svg viewBox='0 0 720 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Duas caixas, previsão e ganhos externos, com setas convergindo para o jogo patológico'>
<defs><marker id='nc' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='14' width='250' height='76' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='16' y='38' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>PREVIS&Atilde;O</text>
<text x='16' y='58' %(F)s font-size='11.5' fill='#2f2e24'>sensação de controle, evitar perigos,</text>
<text x='16' y='76' %(F)s font-size='11.5' fill='#2f2e24'>garantir ganhos antes que aconteçam</text>
<rect x='0' y='110' width='250' height='76' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='16' y='134' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>GANHOS EXTERNOS</text>
<text x='16' y='154' %(F)s font-size='11.5' fill='#2f2e24'>poder de compra, status,</text>
<text x='16' y='172' %(F)s font-size='11.5' fill='#2f2e24'>segurança, autonomia</text>
<path d='M254 52 C 330 52, 340 100, 400 100' fill='none' stroke='#8d876f' stroke-width='2' marker-end='url(#nc)'/>
<path d='M254 148 C 330 148, 340 100, 400 100' fill='none' stroke='#8d876f' stroke-width='2' marker-end='url(#nc)'/>
<rect x='408' y='58' width='312' height='84' rx='11' fill='#43441f'/>
<text x='564' y='88' text-anchor='middle' %(F)s font-size='13' font-weight='800' fill='#f0ede0'>jogo patológico</text>
<text x='564' y='108' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>as duas necessidades numa só aposta:</text>
<text x='564' y='124' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>prever o resultado e ganhar com ele</text>
</svg>
<figcaption>O apostador não inventou nada. Ele está usando duas necessidades que a evolução deixou, prever e ganhar, num ambiente em que a previsão não funciona.</figcaption></figure>""" % dict(F=F)

QUATRO_C = u"""<figure class='dg'><div class='dg-t'>Os quatro C's</div>
<svg viewBox='0 0 720 236' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Quatro blocos em sequência: controle, coping, conflito e chasing, com a linha perigosa marcada antes do último'>
<defs><marker id='qc' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='10' width='166' height='150' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='14' y='36' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>Control</text>
<text x='14' y='52' %(F)s font-size='9.5' fill='#a8894f' font-weight='800' letter-spacing='1'>CONTROLE</text>
<text x='14' y='78' %(F)s font-size='10.5' fill='#6c6a55'>não modula mais</text>
<text x='14' y='94' %(F)s font-size='10.5' fill='#6c6a55'>frequência, duração</text>
<text x='14' y='110' %(F)s font-size='10.5' fill='#6c6a55'>e valor; continua</text>
<text x='14' y='126' %(F)s font-size='10.5' fill='#6c6a55'>com prejuízo evidente</text>
<path d='M170 85 L184 85' stroke='#8d876f' stroke-width='2' marker-end='url(#qc)'/>
<rect x='186' y='10' width='166' height='150' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='200' y='36' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>Coping</text>
<text x='200' y='52' %(F)s font-size='9.5' fill='#a8894f' font-weight='800' letter-spacing='1'>REGULA&Ccedil;&Atilde;O</text>
<text x='200' y='78' %(F)s font-size='10.5' fill='#6c6a55'>o jogo vira estratégia</text>
<text x='200' y='94' %(F)s font-size='10.5' fill='#6c6a55'>de regulação: mais</text>
<text x='200' y='110' %(F)s font-size='10.5' fill='#6c6a55'>afeto negativo ou</text>
<text x='200' y='126' %(F)s font-size='10.5' fill='#6c6a55'>menos afeto positivo</text>
<path d='M356 85 L370 85' stroke='#8d876f' stroke-width='2' marker-end='url(#qc)'/>
<rect x='372' y='10' width='166' height='150' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='386' y='36' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>Conflict</text>
<text x='386' y='52' %(F)s font-size='9.5' fill='#a8894f' font-weight='800' letter-spacing='1'>CONFLITO DE VALORES</text>
<text x='386' y='78' %(F)s font-size='10.5' fill='#6c6a55'>reescalona prioridades;</text>
<text x='386' y='94' %(F)s font-size='10.5' fill='#6c6a55'>o jogo entra em choque</text>
<text x='386' y='110' %(F)s font-size='10.5' fill='#6c6a55'>com valores e</text>
<text x='386' y='126' %(F)s font-size='10.5' fill='#6c6a55'>responsabilidades</text>
<path d='M542 85 L556 85' stroke='#a05a3c' stroke-width='2.4' marker-end='url(#qc)'/>
<rect x='558' y='10' width='162' height='150' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.6'/>
<text x='572' y='36' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>Chasing</text>
<text x='572' y='52' %(F)s font-size='9.5' fill='#a05a3c' font-weight='800' letter-spacing='1'>CA&Ccedil;A DO RESULTADO</text>
<text x='572' y='78' %(F)s font-size='10.5' fill='#6c6a55'>joga para reverter</text>
<text x='572' y='94' %(F)s font-size='10.5' fill='#6c6a55'>o prejuízo, movido</text>
<text x='572' y='110' %(F)s font-size='10.5' fill='#6c6a55'>por desespero ou</text>
<text x='572' y='126' %(F)s font-size='10.5' fill='#6c6a55'>ilusão de compensação</text>
<line x1='549' y1='170' x2='549' y2='222' stroke='#a05a3c' stroke-width='1.4' stroke-dasharray='4 3'/>
<text x='540' y='200' text-anchor='end' %(F)s font-size='10.5' font-style='italic' fill='#a05a3c'>lazer, hábito, alívio</text>
<text x='558' y='200' %(F)s font-size='10.5' font-style='italic' font-weight='800' fill='#a05a3c'>a linha perigosa: tentativa de reverter</text>
</svg>
<figcaption>A ordem dos slides é didática, e não uma sequência obrigatória. O que muda de categoria é o último C: quando a pessoa joga para recuperar o que perdeu, a justificativa de brincadeira ou alívio se rompeu.</figcaption></figure>""" % dict(F=F)

DT5 = {
    'slug': 'aula5',
    'titulo_txt': 'Transtorno do jogo: a aposta, o acaso e os quatro C\'s',
    'titulo_html': 'Transtorno do jogo: a aposta, o acaso e os quatro C&rsquo;s',
    'data': 'Vídeo 5',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 5',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 5 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 5',
    'chave': 'mat-Aula-DT5-',
    'arquivo': 'Aula-DT5-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do quinto vídeo da "
              u"disciplina, que abre o bloco sobre transtorno do jogo. Não havia transcrição.</p>"
              u"<p>O vídeo é curto e conceitual: define a aposta e o jogo de azar, apresenta os quatro C's e fixa a primeira "
              u"tarefa clínica, desfazer a ideia de sorte e azar. Os critérios diagnósticos ficam para o vídeo 6.</p></div>"),
    'tema': 'Por que o ser humano aposta, o que exatamente é uma aposta, os quatro C\'s que marcam a passagem do lazer ao transtorno, '
            'e a primeira coisa a trabalhar com o paciente: o acaso não tem memória, dono nem aviso.',
    'essencial': [
        ('Apostar usa duas necessidades antigas.',
         'Prever (sentir controle, evitar perigo) e ganhar (poder de compra, status, segurança). O jogo patológico é essas duas necessidades num ambiente onde prever não funciona.'),
        ('A aposta é o elemento central.',
         'Empenhar um valor com base numa previsão de resultado futuro. Se acerta, recebe o valor mais um acréscimo combinado; se erra, a contraparte fica com tudo.'),
        ('Jogo de azar é jogo baseado no acaso, e não em má sorte.',
         'O resultado é determinado parcial ou totalmente por variáveis aleatórias. Por isso nenhuma técnica, ritual ou esforço muda o desfecho.'),
        ('A brincadeira disfarça o risco.',
         'A pessoa está brincando, pela previsão, com coisa séria. O formato lúdico reduz a percepção de risco. É a herança evolutiva do vídeo 1 usada contra ela.'),
        ('Os quatro C\'s: Control, Coping, Conflict, Chasing.',
         'Perda de controle, jogo como regulação emocional, conflito com valores e caça do prejuízo. O último é a linha perigosa.'),
        ('Primeira tarefa clínica: o acaso.',
         'Independente, incontrolável, imprevisível. Antes de qualquer outra coisa, desfazer a ideia de que o jogo depende de sorte ou azar.'),
    ],
    'secoes': [
        ('s0', 'Obcecados por prever e ganhar', 'Obcecados por prever e ganhar', u"""
{{NECESS}}
<p>O vídeo começa onde a disciplina começou: na evolução. Seres humanos são obcecados por duas coisas. A primeira é a <strong>previsão</strong>. Antecipar o que vem dá sensação de controle, permite evitar perigos e garantir ganhos antes que aconteçam. O slide chama isso de necessidade evolutiva, e é: um animal que prevê onde estará o predador e onde estará a comida sobrevive mais.</p>
<p>A segunda são os <strong>ganhos externos</strong>: poder de compra, ganhos materiais, status, segurança, autonomia. Também aqui não há nada de patológico. É o que move a maior parte do trabalho humano.</p>
<p>O jogo patológico fica no cruzamento das duas. A aposta é, ao mesmo tempo, um exercício de previsão e uma promessa de ganho. Ela oferece as duas coisas que a espécie mais quer, e oferece num ambiente em que a primeira delas, a previsão, não tem como funcionar. Esse é o núcleo do vídeo, e tudo o que vem depois desdobra isso.</p>
<div class='callout note'><div class='co-t'>Ligação com os vídeos 1 e 2</div>Nos vídeos 1 e 2, a lógica era a mesma para jogos digitais e redes: o produto explora um mecanismo evolutivo que estava lá antes dele. No jogo de azar o mecanismo explorado é a previsão. A diferença é que aqui a aposta custa dinheiro real, e o dinheiro é a segunda necessidade sendo usada para pagar pela primeira.</div>
"""),
        ('s1', 'O que é uma aposta', 'O que é, exatamente, uma aposta', u"""
<p>O slide dedica um cuidado que vale reproduzir: definir os termos antes de falar do transtorno.</p>
<h3>Jogo de azar não é má sorte</h3>
<p>O termo "jogo de azar" não se refere a má sorte. Refere-se ao <strong>jogo baseado no acaso</strong>, em que o resultado é determinado parcial ou totalmente por variáveis aleatórias. Fica implícito que o jogo de azar envolve ganhos esperados ou reais; ninguém aposta para perder.</p>
<h3>O elemento central: a aposta</h3>
<p>Aposta é o ato de <strong>empenhar um valor</strong>, financeiro ou material, com base numa <strong>previsão de resultado futuro</strong>. A mecânica é simples e vale ter clara, porque o paciente costuma descrevê-la de um jeito bem menos simples:</p>
<ul class='key'><li><b>Se a previsão estiver correta</b>: o apostador recebe o valor apostado de volta, mais um acréscimo pré-estabelecido. Esse acréscimo é o ganho.</li><li><b>Se a previsão estiver incorreta</b>: o apostador perde o valor apostado, que é retido pela contraparte (a banca, a casa de apostas, o cassino).</li></ul>
<h3>Onde o jogo de azar aparece</h3>
<p>Quando esse tipo de aposta ocorre em contextos lúdicos ou recreativos, como jogos, máquinas eletrônicas, cassinos ou apostas esportivas, temos o jogo de azar: <strong>diversão mediada por risco e recompensa</strong>. A definição importa para o Brasil de hoje, em que a aposta esportiva online, as "bets", passou a ser regulamentada e anunciada em escala, com acesso pelo celular a qualquer hora. É o mesmo mecanismo do cassino, com a fricção do deslocamento retirada.</p>
<div class='obs'><h4>Por que a definição importa na clínica</h4><p>O paciente raramente chega dizendo "eu empenho valores com base em previsões que não podem funcionar". Ele diz que joga, que aposta, que "entende de futebol", que tem um método. Reduzir o que ele faz aos dois desfechos acima, acertou e recebeu o combinado, errou e a banca ficou com tudo, já é intervenção. Tira o enredo e deixa a mecânica.</p></div>
"""),
        ('s2', 'Brincando com coisa séria', 'Brincando com coisa séria', u"""
<p>O terceiro movimento do vídeo liga o jogo de azar ao comportamento lúdico do vídeo 1. O indivíduo está <strong>brincando</strong>, por meio da previsão, com <strong>coisa séria</strong>: ganhos ou perdas reais. E ele brinca porque há muita <strong>incerteza</strong>, ou seja, porque há acaso, e o acaso envolve riscos de verdade.</p>
<p>O ponto fino é o seguinte. O comportamento lúdico tem função evolutiva, como o vídeo 1 mostrou: brincar é treinar em ambiente seguro, com o custo do erro reduzido. Quando a aposta se apresenta em formato de brincadeira, com cores, sons, campeonato, palpite entre amigos, ela pega carona nessa marca de segurança. A pessoa está envolvida com risco real, mas <strong>disfarçada</strong> de comportamento lúdico, e por isso a <strong>percepção de risco fica reduzida</strong>. O cérebro lê "jogo" e desliga parte do alarme que ligaria diante de "perda de dinheiro".</p>
<div class='callout note'><div class='co-t'>Em processos</div>A redução da percepção de risco não é um erro de raciocínio isolado. É o formato do estímulo, lúdico, acionando um repertório antigo (brincar é seguro) num contexto em que ele não vale. Na formulação, isso entra como discriminação de contexto falha: o ambiente dá as pistas de brincadeira e retira as pistas de perigo.</div>
"""),
        ('s3', 'Os quatro C\'s', 'Os quatro C\'s', u"""
{{QUATRO_C}}
<p>O slide organiza a passagem do jogo recreativo ao transtorno em quatro marcadores, todos com C em inglês.</p>
<ul class='key'><li><b>Control (controle)</b>: a pessoa já não consegue mais modular a frequência, a duração ou o valor das apostas. Mesmo com prejuízos evidentes, continua jogando.</li><li><b>Coping (confronto das emoções)</b>: o jogo passa a funcionar como estratégia de regulação emocional. Isso pode ocorrer em momentos de aumento de afetos negativos ou de redução de afetos positivos, e vale notar as duas direções: a pessoa joga para fugir do que está sentindo e também para sentir alguma coisa quando não sente nada.</li><li><b>Conflict (conflito de valores)</b>: à medida que o comportamento se torna repetitivo, o indivíduo reescalona suas prioridades. O jogo começa a entrar em conflito com seus próprios valores e responsabilidades. Não é ainda, necessariamente, a perda de emprego ou de casamento; é o momento em que o jogo passa na frente do que a pessoa dizia ser importante.</li><li><b>Chasing (caça do resultado)</b>: aqui a pessoa cruza uma linha perigosa. Deixa de apostar por lazer ou hábito e passa a jogar movida por desespero ou ilusão de compensação. A justificativa se rompe: não é mais uma brincadeira ou um alívio, mas uma tentativa de reverter o prejuízo.</li></ul>
<h3>Por que o chasing é a linha</h3>
<p>Nos três primeiros C's, o jogo ainda tem uma justificativa que a pessoa consegue sustentar: diversão, alívio, hábito. No chasing, a justificativa é a própria perda. A pessoa joga porque perdeu, e a lógica da aposta garante que, na média, ela vai perder de novo. É o único dos quatro que fecha uma alça diretamente sobre si mesmo, e não por acaso "tentar recuperar o que perdeu" é um dos critérios formais do DSM-5-TR para o transtorno do jogo, que o vídeo 6 vai apresentar.</p>
<div class='obs'><h4>Como usar os quatro C's na avaliação</h4><p>São perguntas, e não uma escala. Tu consegue decidir quanto e quando joga? O que tu está sentindo pouco antes de apostar? O que ficou para trás por causa do jogo? Quando perde, o que tu faz em seguida? A quarta resposta é a que mais separa quem precisa de tratamento de quem precisa de orientação.</p></div>
"""),
        ('s4', 'A primeira tarefa: o acaso', 'A primeira tarefa clínica: o acaso', u"""
<p>O último slide de conteúdo fixa o ponto de partida do tratamento. A primeira coisa a trabalhar com o paciente é <strong>desfazer a ideia de que o jogo depende de azar ou de sorte</strong>. O que está em jogo é o acaso, e isso faz toda a diferença.</p>
<p>O acaso é algo que não depende da pessoa, nem dos eventos anteriores, nem dos seus esforços, estratégias ou superstições. Três propriedades, e vale apresentar as três ao paciente, uma a uma:</p>
<ul class='key'><li><b>É independente</b>: não importa o que já aconteceu ou o que a pessoa faça agora, isso não muda o resultado. Cinco vermelhos seguidos na roleta não tornam o preto "devido". A moeda não tem memória.</li><li><b>É incontrolável</b>: não há técnica secreta, ritual, sopro nos dados, nem trazer uma pessoa bonita para dar sorte. Nada disso altera o desfecho.</li><li><b>É imprevisível</b>: justamente porque é aleatório e está fora do controle de qualquer um, o resultado não pode ser antecipado por ninguém, por mais que a pessoa "entenda" do jogo.</li></ul>
<h3>Sorte e azar são a linguagem da ilusão de controle</h3>
<p>Quando o paciente fala em sorte e azar, ele está descrevendo o acaso como se fosse uma força com humor, que pode estar a favor ou contra, que pode virar. É a gramática que sustenta o chasing ("agora vai virar") e a busca de método ("eu já entendi como funciona"). A literatura chama isso de ilusão de controle e de falácia do jogador: a tendência a tratar uma sequência aleatória como se ela se equilibrasse no curto prazo. A terapia cognitiva do jogo, na linha de Ladouceur, começa exatamente por aqui, porque enquanto a pessoa acredita que o resultado pode ser previsto ou influenciado, todo o resto do tratamento é discutido em cima de uma premissa falsa.</p>
<div class='callout note'><div class='co-t'>Como fazer sem virar aula de estatística</div>Não é convencer com números. É pedir que o paciente descreva a última sequência de apostas e, a cada passo, perguntar o que ele achava que ia acontecer e por quê. As três propriedades aparecem sozinhas nas lacunas do relato: onde ele achou que a sorte "tinha que virar", onde acreditou que o ritual ajudou, onde tinha certeza do palpite. Trabalha-se com o material dele, e não com o conceito.</div>
"""),
        ('s5', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>Para quem trabalha com formulação processual, este vídeo já entrega uma rede quase completa, ainda antes dos critérios diagnósticos.</p>
<ul class='key'><li><b>Antecedente distal</b>: duas necessidades evolutivas, prever e ganhar, que o ambiente de aposta ativa ao mesmo tempo.</li><li><b>Contexto</b>: formato lúdico que reduz a percepção de risco, mais acesso permanente pelo celular no caso das apostas online.</li><li><b>Cognição</b>: crença de que o resultado depende de sorte, azar, método ou ritual. É o processo que sustenta os outros, e por isso é o primeiro alvo.</li><li><b>Afeto e função</b>: o jogo como regulação (coping), para baixar afeto negativo ou levantar afeto positivo. Reforço negativo e positivo na mesma resposta.</li><li><b>Self e valores</b>: reescalonamento de prioridades e conflito com o que a pessoa diz que importa (conflict).</li><li><b>Alça de manutenção</b>: perda, desespero ou ilusão de compensação, nova aposta, nova perda (chasing). A alça se fecha sobre si mesma e não precisa de mais nada para continuar.</li></ul>
<p>O ponto de entrada que o vídeo indica é a cognição sobre o acaso, e faz sentido: é o nó que, uma vez desfeito, tira o combustível do chasing e a justificativa do método. Mas a alça de coping permanece, e vai precisar de uma resposta alternativa para a mesma função, o que os vídeos de intervenção devem trazer.</p>
"""),
    ],
    'checklist': [
        'Defini com o paciente, em duas frases, o que é uma aposta: valor empenhado numa previsão, dois desfechos possíveis.',
        'Perguntei sobre os quatro C\'s como perguntas, e não como escala: controle, o que sente antes, o que ficou para trás, o que faz depois de perder.',
        'Identifiquei se há chasing. Se há, tratei como sinal de gravidade, e não como fase.',
        'Registrei a linguagem de sorte, azar, método e ritual que o paciente usa, com as palavras dele.',
        'Apresentei as três propriedades do acaso a partir do relato dele, e não como conceito abstrato.',
        'Notei se o formato do jogo (app, cores, campeonato, palpite entre amigos) está reduzindo a percepção de risco.',
        'Perguntei pelo acesso: onde e quando ele consegue apostar, e se o celular está sempre à mão.',
        'Levantei qual função o jogo cumpre (baixar afeto negativo, levantar afeto positivo) antes de falar em reduzir.',
    ],
    'questoes': [
        'Quais são as duas necessidades evolutivas que o vídeo aponta na base do jogo patológico, e por que a aposta atende às duas ao mesmo tempo?',
        'Defina aposta e jogo de azar nos termos do vídeo, e explique por que "azar" não quer dizer má sorte.',
        'O que significa dizer que o apostador está "brincando com coisa séria", e o que isso faz com a percepção de risco?',
        'Descreva os quatro C\'s e explique por que o chasing é tratado como a linha perigosa.',
        'Quais são as três propriedades do acaso, e por que trabalhar isso vem antes de qualquer outra intervenção?',
        'Pense num paciente teu que aposta. Que frases dele mostram a ideia de sorte, azar ou método, e como tu entraria nisso sem dar aula de estatística?',
    ],
    'gabarito': {
     0: (C, u"A previsão (sensação de controle, evitar perigos, garantir ganhos) e os ganhos externos (poder de compra, status, segurança, autonomia). A aposta é ao mesmo tempo um exercício de previsão e uma promessa de ganho, ou seja, oferece as duas coisas numa só resposta, num ambiente em que a primeira delas não pode funcionar, porque o resultado é aleatório."),
     1: (C, u"Aposta é o ato de empenhar um valor, financeiro ou material, com base numa previsão de resultado futuro; se a previsão acerta, a pessoa recebe o valor de volta mais um acréscimo pré-estabelecido, e se erra, perde o valor para a contraparte. Jogo de azar é a aposta em contexto lúdico ou recreativo, jogo baseado no acaso: o resultado é determinado parcial ou totalmente por variáveis aleatórias. \"Azar\" nomeia o acaso, e não a má sorte."),
     2: (C, u"Que a pessoa está envolvida com ganhos e perdas reais, mas por meio de um formato que se apresenta como brincadeira. Como o comportamento lúdico tem função evolutiva e vem marcado como seguro (o custo do erro é baixo quando se brinca), o formato lúdico da aposta pega carona nessa marca e reduz a percepção de risco: a pessoa lê \"jogo\" onde há perda de dinheiro."),
     3: (C, u"Control: já não modula frequência, duração ou valor, e continua com prejuízo evidente. Coping: o jogo vira estratégia de regulação emocional, diante de mais afeto negativo ou menos afeto positivo. Conflict: reescalona prioridades e o jogo entra em choque com valores e responsabilidades. Chasing: joga para reverter o prejuízo, movida por desespero ou ilusão de compensação. O chasing é a linha porque nele a justificativa de brincadeira ou alívio se rompe; a razão para jogar passa a ser a própria perda, e a alça se fecha sobre si mesma."),
     4: (C, u"Independente (o que já aconteceu e o que a pessoa faz agora não mudam o resultado), incontrolável (nenhuma técnica, ritual ou superstição altera o desfecho) e imprevisível (por ser aleatório, ninguém antecipa o resultado). Vem antes porque a crença em sorte, azar ou método é a premissa que sustenta o chasing e a busca de estratégia; enquanto ela estiver de pé, o resto do tratamento é negociado em cima de uma ideia falsa."),
     5: (K, u"Não há resposta certa. Uma boa resposta traz frases concretas do paciente (\"agora vai virar\", \"eu entendo de futebol\", \"esse site é mais fácil\", \"quando eu vou com fulano eu ganho\") e descreve uma entrada pelo relato: reconstruir a última sequência de apostas e, a cada passo, perguntar o que ele esperava e por quê, deixando as três propriedades do acaso aparecerem nas lacunas. O erro comum é explicar probabilidade em abstrato, o que o paciente costuma aceitar e seguir apostando."),
    },
    'referencias': [
        "American Psychiatric Association. (2022). <em>Manual diagnóstico e estatístico de transtornos mentais: DSM-5-TR</em> (5. ed., texto revisado). Artmed.",
        "Ladouceur, R., Sylvain, C., Boutin, C., &amp; Doucet, C. (2002). <em>Understanding and treating the pathological gambler.</em> Wiley.",
        "Langer, E. J. (1975). The illusion of control. <em>Journal of Personality and Social Psychology, 32</em>(2), 311–328.",
        "Potenza, M. N., Balodis, I. M., Derevensky, J., Grant, J. E., Petry, N. M., Verdejo-Garcia, A., &amp; Yip, S. W. (2019). Gambling disorder. <em>Nature Reviews Disease Primers, 5</em>, 51.",
        "Tversky, A., &amp; Kahneman, D. (1971). Belief in the law of small numbers. <em>Psychological Bulletin, 76</em>(2), 105–110.",
        "World Health Organization. (2019). <em>International classification of diseases, 11th revision (ICD-11)</em>: 6C50 Gambling disorder.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o quinto vídeo de uma disciplina de pós-graduação e abre o bloco sobre transtorno do jogo; os critérios diagnósticos vêm no vídeo 6.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. O vídeo tem quatro slides de conteúdo; as ligações com os vídeos 1 e 2, a seção sobre a linguagem de sorte e azar como ilusão de controle, o quadro de perguntas a partir dos quatro C's e a seção final em processos foram desenvolvidas pelo autor do material a partir da lógica da disciplina e estão sinalizadas como tal.<br><br><strong>Sobre os quatro C's.</strong> Os slides apresentam Control, Coping, Conflict e Chasing como organização didática, sem citar fonte. O material os manteve como estão e não atribuiu autoria. A perda de controle e o chasing correspondem a critérios do DSM-5-TR e da CID-11, o que está indicado no texto. A ordem em que aparecem na figura segue os slides e não deve ser lida como sequência obrigatória.<br><br><strong>Acréscimos.</strong> A menção às apostas esportivas online no Brasil é do autor do material, sem citação, e serve de contexto. As referências sobre ilusão de controle, falácia do jogador, terapia cognitiva do jogo e a revisão do transtorno do jogo foram acrescentadas para dar respaldo ao que os slides afirmam sem citação. Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'NECESS': NECESS, 'QUATRO_C': QUATRO_C}
DT5['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DT5['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT5['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT5, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT5)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT5['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
