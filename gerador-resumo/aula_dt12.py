# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 12: Fase da preparação. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

GAS = u"""<figure class='dg'><div class='dg-t'>Níveis de alcance da meta</div>
<svg viewBox='0 0 720 190' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Escala de menos dois a mais dois: mais de três horas, entre duas e três, até duas horas que é a meta, até uma hora, zero horas com substituição por atividades saudáveis'>
<line x1='60' y1='40' x2='660' y2='40' stroke='#9ca575' stroke-width='2'/>
<g %(F)s font-size='11' fill='#2f2e24' text-anchor='middle'>
<circle cx='90' cy='40' r='9' fill='#a05a3c'/><text x='90' y='44' font-size='10' font-weight='800' fill='#fff'>&minus;2</text>
<text x='90' y='72'>mais de 3 h</text><text x='90' y='87'>no dia</text>
<circle cx='225' cy='40' r='9' fill='#c9a48c'/><text x='225' y='44' font-size='10' font-weight='800' fill='#fff'>&minus;1</text>
<text x='225' y='72'>entre 2 e 3 h</text>
<circle cx='360' cy='40' r='12' fill='#43441f'/><text x='360' y='44' font-size='10' font-weight='800' fill='#fff'>0</text>
<text x='360' y='72' font-weight='800'>até 2 h no dia</text><text x='360' y='87' font-size='10' fill='#6c6a55'>meta alcançada</text>
<circle cx='495' cy='40' r='9' fill='#9ca575'/><text x='495' y='44' font-size='10' font-weight='800' fill='#fff'>+1</text>
<text x='495' y='72'>até 1 h</text>
<circle cx='630' cy='40' r='9' fill='#43441f'/><text x='630' y='44' font-size='10' font-weight='800' fill='#fff'>+2</text>
<text x='630' y='72'>0 h e substituiu</text><text x='630' y='87'>por atividade saudável</text>
</g>
<rect x='120' y='118' width='480' height='58' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='360' y='142' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>a meta está no meio, e não no topo</text>
<text x='360' y='161' text-anchor='middle' %(F)s font-size='10' fill='#6c6a55'>o dia em que ele jogou 2h30 é um &minus;1, e não um fracasso; o dia sem jogo só vale +2 se algo entrou no lugar</text>
</svg>
<figcaption>A escala dos slides para a meta de duas horas nos dias de semana. Cinco níveis em vez de dois (cumpriu, não cumpriu) mudam o que o paciente registra e o que o terapeuta consegue ver.</figcaption></figure>""" % dict(F=F)

QUAD = u"""<figure class='dg'><div class='dg-t'>Onde a dependência se instala: os quadrantes do estado</div>
<svg viewBox='0 0 720 250' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Quatro quadrantes cruzando ativo e inativo com contexto desagradável e agradável; os dois quadrantes desagradáveis são onde os comportamentos de dependência se desenvolvem; ao lado, curva de ativação subindo antes do humor'>
<line x1='200' y1='20' x2='200' y2='230' stroke='#2f2e24' stroke-width='1.6'/>
<line x1='40' y1='125' x2='360' y2='125' stroke='#2f2e24' stroke-width='1.6'/>
<text x='200' y='14' text-anchor='middle' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#8d876f'>ATIVO</text>
<text x='200' y='246' text-anchor='middle' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#8d876f'>INATIVO</text>
<text x='36' y='125' text-anchor='end' %(F)s font-size='9' font-weight='800' fill='#a05a3c' transform='rotate(-90 36 125)'>CONTEXTO DESAGRAD&Aacute;VEL</text>
<text x='366' y='125' text-anchor='start' %(F)s font-size='9' font-weight='800' fill='#43441f' transform='rotate(90 366 125)'>CONTEXTO AGRAD&Aacute;VEL</text>
<rect x='44' y='24' width='152' height='97' rx='8' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/>
<text x='120' y='58' text-anchor='middle' %(F)s font-size='10.5' fill='#a05a3c'>irritado, nervoso,</text>
<text x='120' y='74' text-anchor='middle' %(F)s font-size='10.5' fill='#a05a3c'>tenso, ansioso</text>
<rect x='44' y='129' width='152' height='97' rx='8' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/>
<text x='120' y='168' text-anchor='middle' %(F)s font-size='10.5' fill='#a05a3c'>cansado, triste,</text>
<text x='120' y='184' text-anchor='middle' %(F)s font-size='10.5' fill='#a05a3c'>desmotivado, infeliz</text>
<rect x='204' y='24' width='152' height='97' rx='8' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='280' y='58' text-anchor='middle' %(F)s font-size='10.5' fill='#43441f'>esperançoso, motivado,</text>
<text x='280' y='74' text-anchor='middle' %(F)s font-size='10.5' fill='#43441f'>feliz, entusiasmado</text>
<rect x='204' y='129' width='152' height='97' rx='8' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='280' y='168' text-anchor='middle' %(F)s font-size='10.5' fill='#43441f'>calmo, relaxado,</text>
<text x='280' y='184' text-anchor='middle' %(F)s font-size='10.5' fill='#43441f'>tranquilo, pleno</text>
<line x1='430' y1='40' x2='430' y2='210' stroke='#2f2e24' stroke-width='1.4'/>
<line x1='430' y1='210' x2='710' y2='210' stroke='#2f2e24' stroke-width='1.4'/>
<text x='570' y='228' text-anchor='middle' %(F)s font-size='10' fill='#6c6a55'>tempo</text>
<polyline points='450,150 480,145 510,138 540,130 570,120 600,108 630,92 660,70 690,50' fill='none' stroke='#43441f' stroke-width='2.4'/>
<polyline points='450,170 480,178 510,180 540,178 570,168 600,150 630,125 660,95 690,60' fill='none' stroke='#a05a3c' stroke-width='2.4'/>
<text x='452' y='142' %(F)s font-size='10' font-weight='800' fill='#43441f'>ativação</text>
<text x='452' y='195' %(F)s font-size='10' font-weight='800' fill='#a05a3c'>humor</text>
<text x='560' y='60' %(F)s font-size='9.5' font-style='italic' fill='#a05a3c'>fase crítica: pode haver</text>
<text x='560' y='73' %(F)s font-size='9.5' font-style='italic' fill='#a05a3c'>queda no humor no início</text>
</svg>
<figcaption>À esquerda, os dois quadrantes desagradáveis são onde a dependência se desenvolve: a tela é o que a pessoa faz quando está tensa ou quando está desmotivada. À direita, a ativação planejada sobe antes do humor, e o humor pode cair no começo.</figcaption></figure>""" % dict(F=F)

DT12 = {
    'slug': 'aula12',
    'titulo_txt': 'Preparação: metas SMART, escala de alcance, ativação e o manejo do impulso',
    'titulo_html': 'Prepara&ccedil;&atilde;o: metas SMART, escala de alcance, ativa&ccedil;&atilde;o e o manejo do impulso',
    'data': 'Vídeo 12',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 12',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 12 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 12',
    'chave': 'mat-Aula-DT12-',
    'arquivo': 'Aula-DT12-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo segundo vídeo da "
              u"disciplina, sobre a fase de preparação. Não havia transcrição.</p>"
              u"<p>É o vídeo mais denso da série de estágios: metas, escala de alcance, quadrantes do estado, ativação, o elefante e o condutor, "
              u"e duas listas de ferramentas para o impulso. Os exercícios de regulação fisiológica estão descritos em termos gerais, sem instruções.</p></div>"),
    'tema': 'O paciente que quer mudar e não sabe como: metas SMART em vez de "parar", uma escala de cinco níveis para medir o alcance, '
            'os quadrantes em que a dependência se instala, a ativação que precede o humor, e o manejo do impulso com o elefante e o condutor.',
    'essencial': [
        ('Preparação: "eu quero mudar, mas não sei bem como".',
         'O paciente está motivado, mas precisa de orientação prática. Pode ter tentado reduzir sem sucesso sustentado.'),
        ('A meta é SMART, e não "parar".',
         '"Usar o computador por no máximo duas horas por dia nos dias de semana, a partir da próxima semana" tem específico, mensurável, atingível, relevante e prazo.'),
        ('Cinco níveis de alcance, com a meta no meio.',
         'De menos dois (mais de três horas) a mais dois (zero horas e substituiu). O dia de duas horas e meia é um menos um, não um fracasso.'),
        ('A dependência se instala nos quadrantes desagradáveis.',
         'Tenso ou desmotivado, a tela é a resposta. Seleção de atividades é o que ocupa esses quadrantes com outra coisa.'),
        ('A ativação vem antes do humor.',
         'Atividades bem planejadas sobem primeiro; o humor pode cair no começo. É a fase crítica, e o paciente precisa saber disso antes.'),
        ('O elefante obedece ao condutor enquanto quiser.',
         'Sistema 1 e sistema 2. Manejo do impulso é arranjar o caminho para o elefante, e não vencer o cabo de guerra.'),
    ],
    'secoes': [
        ('s0', 'A ficha do estágio', 'Preparação: a ficha do estágio', u"""
<p>O terceiro estágio, na frase do paciente: <em>"Eu quero mudar, mas não sei bem como."</em></p>
<ul class='key'><li><b>Características</b>: o paciente está motivado, mas precisa de orientação prática. Pode ter tentado reduzir o uso, mas sem sucesso sustentado.</li><li><b>Perguntas</b>: se já pensou em alguma estratégia para reduzir o tempo de uso; o que acha que precisa para conseguir mudar; quais horários ou situações seriam mais fáceis para começar.</li><li><b>Intervenção</b>: definir metas terapêuticas realistas (SMART) e planejar estratégias específicas: apps de bloqueio, agenda offline, substituições.</li></ul>
<p>A terceira pergunta merece destaque: <strong>onde é mais fácil começar</strong>. Não onde é mais grave. O paciente em preparação já tentou e falhou; a primeira meta tem que ser a que ele consegue cumprir, porque o que está em jogo é a autoeficácia, e não as horas.</p>
"""),
        ('s1', 'Metas SMART', 'Metas SMART: em vez de "parar"', u"""
<p>O slide usa o modelo SMART: <b>S</b> (específica), "reduzir o uso de internet para três horas por dia"; <b>M</b> (mensurável), monitorado por registros diários; <b>A</b> (atingível), baseado no histórico do paciente; <b>R</b> (relevante), vinculada a valores pessoais; <b>T</b> (temporal), prazo definido, "até o final do mês".</p>
<p>E o exemplo que o slide destaca: em vez de simplesmente <strong>"parar de jogar"</strong>, definir como meta <strong>"usar o computador por no máximo duas horas por dia durante os dias de semana"</strong>, a partir da próxima semana. Repare no que essa formulação faz: tem número, tem dias, tem data de início, deixa o fim de semana fora (atingível) e admite uso (funcional). "Parar de jogar" falha em todos os cinco critérios e ainda entrega ao paciente uma meta que ele já não cumpriu sozinho.</p>
<div class='obs'><h4>O R é o que segura os outros quatro</h4><p>"Vinculada a valores pessoais" liga a meta ao caminho sonhado do vídeo 11. Uma meta de duas horas que não está ligada a nada dura até a primeira noite ruim; uma meta de duas horas que existe para o paciente ter tempo de estudar para a prova que ele quer passar dura mais. Ao escrever a meta, vale escrever o para quê ao lado.</p></div>
"""),
        ('s2', 'Escala de alcance', 'A escala de alcance da meta', u"""
{{GAS}}
<p>O slide seguinte apresenta os <strong>níveis de alcance da meta</strong>, uma escala de cinco pontos para a meta de duas horas. <b>+2</b>: jogou zero horas no dia e substituiu o tempo com atividades saudáveis. <b>+1</b>: jogou até uma hora. <b>0</b>: jogou até duas horas, meta alcançada. <b>&minus;1</b>: jogou entre duas e três horas. <b>&minus;2</b>: jogou mais de três horas.</p>
<p>Dois detalhes fazem a escala funcionar. A meta está no <strong>zero</strong>, no meio, e não no topo: cumprir é o esperado, e não o máximo. E o +2 exige <strong>substituição</strong>, e não só abstinência: um dia sem jogar e sem fazer nada no lugar é um +1 no máximo, porque foi um dia em que o quadrante desagradável ficou vazio, e quadrante vazio é onde a recaída começa. Para o paciente, a escala muda o registro: em vez de "falhei" ou "consegui", ele anota um número, e o número de terça (&minus;1) conversa com o de quarta (+1) de um jeito que "falhei" e "consegui" não conversam. Para o terapeuta, é a medida semanal da EMA (vídeo 7) já pronta.</p>
"""),
        ('s3', 'Quadrantes e ativação', 'Os quadrantes do estado e a ativação que precede o humor', u"""
{{QUAD}}
<p>Dois esboços à mão. O primeiro cruza dois eixos: <strong>ativo e inativo</strong>, na vertical; <strong>contexto desagradável e agradável</strong>, na horizontal. Nos quadrantes desagradáveis: ativo (irritado, nervoso, tenso, ansioso) e inativo (cansado, triste, desmotivado, infeliz). Nos agradáveis: ativo (esperançoso, motivado, feliz, entusiasmado) e inativo (calmo, relaxado, tranquilo, pleno). A anotação do slide: <strong>é nos quadrantes desagradáveis que se desenvolvem os comportamentos de dependência</strong>. É a função, de novo: tenso, a tela baixa a ativação; desmotivado, a tela ocupa o vazio. E a meta de duas horas só se sustenta se esses dois quadrantes ganharem outra ocupação.</p>
<p>O segundo esboço é a lógica da ativação comportamental: duas curvas no tempo, <strong>ativação</strong> (atividades bem planejadas) subindo primeiro, e <strong>humor</strong> subindo depois, com uma <strong>fase crítica</strong> no início em que o humor pode cair. Depois, correlação positiva. A anotação: a seleção de atividades é extremamente importante para que essa correlação negativa inicial seja suprimida o máximo possível.</p>
<div class='callout note'><div class='co-t'>O que dizer ao paciente antes de começar</div>Que as primeiras semanas podem ser piores. Que ele vai fazer coisas que ainda não dão prazer, porque o prazer vem atrás da ação, e não na frente. E que a escolha das atividades é o que encurta essa fase: coisas que ele já gostou um dia, com gente, fora de casa, no horário em que ele jogaria. Quem não é avisado lê a queda inicial do humor como prova de que a mudança não funciona, e volta para a tela no terceiro dia.</div>
"""),
        ('s4', 'O elefante e o condutor', 'Manejo da impulsividade: o elefante e o condutor', u"""
<p>Para o manejo do impulso, o vídeo usa a alegoria de Jonathan Haidt: o <strong>cérebro emocional</strong> (sistema 1) é um elefante; o <strong>cérebro racional</strong> (sistema 2) é o condutor. Os dois convivem bem. O animal obedece ao condutor, mas apenas enquanto estiver disposto. Quando concordam, tudo transcorre; e quando divergem? Se o elefante escolhe um caminho pela direita (acreditar em hipóteses) e o condutor quer ir pela esquerda (olhar as evidências), quem tem mais probabilidade de ganhar? No elefante do slide estão escritos os seus componentes: vieses de atenção, condicionamento, crenças, vieses de memória, emoções aprendidas.</p>
<p>O slide seguinte apoia a alegoria em Kahneman, <em>Rápido e devagar</em>. O <strong>sistema 1</strong> é rápido, instintivo e emocional, guiado por experiências passadas e associações: velocidade (reage em milissegundos, útil em perigo), intuição (atalhos mentais e padrões) e erro potencial (vieses e reações impulsivas). O <strong>sistema 2</strong> é lento, deliberado e analítico, entra quando é preciso planejar, decidir com complexidade ou corrigir o sistema 1: raciocínio lógico, autocontrole (freios às respostas automáticas) e esforço cognitivo (consome energia e cansa).</p>
<div class='obs'><h4>O que a alegoria ensina sobre estratégia</h4><p>Se o condutor perde o cabo de guerra, a estratégia não pode ser "ter mais força de vontade". Tem que ser <strong>arranjar o caminho</strong>: tirar a tela de onde o elefante a acha, colocar a atividade onde o elefante passa, e dar ao condutor dez minutos de vantagem. É exatamente a lógica da lista seguinte. E vale lembrar, como o próprio Kahneman lembra, que os dois sistemas são uma metáfora útil, e não duas regiões do cérebro; o que importa para a clínica é a assimetria: o automático é rápido e barato, o deliberado é lento e cansa, e o ambiente decide qual dos dois ganha na maior parte das vezes.</p></div>
"""),
        ('s5', 'Ferramentas para o impulso', 'Ferramentas para o impulso', u"""
<h3>Ideias para o manejo do impulso</h3>
<ul class='key'><li><b>Bloqueio de apps</b>: aplicativos como Forest, StayFocusd ou Freedom, para limitar tempo ou bloquear apps específicos.</li><li><b>Monitoramento de tempo de tela</b>: Screen Time (iOS) ou Bem-estar Digital (Android), para acompanhar e revisar o uso diário.</li><li><b>Atraso voluntário da resposta</b>: ao sentir vontade de usar ou gastar, esperar dez minutos antes de agir; nesse tempo, respirar, andar ou registrar o impulso. É a vantagem do condutor sobre o elefante: o impulso tem pico e queda, e dez minutos costumam bastar para a queda.</li><li><b>Limite de gasto diário</b>: um teto por dia (o slide sugere vinte reais) e registro de cada compra em planilha ou app de finanças.</li><li><b>Registro de impulsos, sentimentos e motivos</b>: anotar o momento do impulso, o gatilho emocional e o contexto num diário de autorregulação. É a EMA (vídeo 7) no nível do episódio.</li><li><b>Ambiente digital limpo</b>: tirar atalhos de apps impulsivos da tela inicial, desativar notificações automáticas e deixar o celular longe ao fazer tarefas. É arranjar o caminho do elefante.</li></ul>
<h3>Exercícios de regulação fisiológica e distrativos</h3>
<p>O último slide traz duas listas para o momento em que o impulso ou a ativação sobem. Na coluna de <strong>regulação fisiológica</strong>: respiração lenta com contagem (inspirar, segurar, expirar mais devagar, repetir); exercício físico regular (corrida, flexões, pular corda); mudança de temperatura; escaneamento corporal (atenção parte a parte, dos pés à cabeça, soltando a tensão); e estímulos sensoriais intensos (sabores fortes, cheiros marcantes, texturas). Na coluna de <strong>exercícios distrativos</strong>: contagens (regressiva de cem, de um em um, ou seguir o ponteiro dos segundos); quebra-cabeças ou jogos que dirijam a atenção para uma tarefa lúdica; vídeos ou programas engraçados (filmes repetidos ajudam, porque a previsibilidade dá sensação de controle); lista de gratidão; e aterramento (foco nos cinco sentidos no momento presente, segurar um objeto físico). O slide fecha: <strong>mindfulness pode ser uma boa pedida</strong>.</p>
<div class='callout note'><div class='co-t'>Duas observações</div>Primeira: as técnicas de regulação fisiológica são as de tolerância ao mal-estar da DBT; servem para atravessar o pico do impulso, e não para tratar o que o produz. Segunda: na coluna distrativa, "jogos e videogames" para quem tem dependência de jogos é a exceção óbvia; a lista é genérica e o terapeuta adapta. O critério para escolher é o quadrante: para o ativo-desagradável (tenso), regulação fisiológica; para o inativo-desagradável (desmotivado), distração ativa e, melhor ainda, a atividade planejada da seção anterior.</div>
"""),
        ('s6', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>A preparação é o estágio em que a formulação vira plano, e o vídeo entrega cada peça do plano ligada a um nó.</p>
<ul class='key'><li><b>A meta SMART</b> é o comportamento-alvo, com o valor ao lado (R). Sem o R, é só um número.</li><li><b>A escala de alcance</b> é a medida, e o +2 com substituição garante que a medida inclua a função, e não só a abstinência.</li><li><b>Os quadrantes</b> são o mapa dos antecedentes: em que estado a tela entra. <b>A ativação</b> é a intervenção sobre o quadrante inativo-desagradável, com o aviso da fase crítica.</li><li><b>O elefante e o condutor</b> são o modelo do controle: o automático ganha do deliberado, e por isso se intervém no ambiente e no tempo (bloqueio, ambiente limpo, atraso de dez minutos), e não na força de vontade.</li><li><b>As técnicas de regulação e distração</b> são a resposta alternativa para o pico do impulso; escolhidas pelo quadrante, e não pela lista.</li></ul>
<p>Na prática: meta com para quê, escala de cinco níveis, atividade planejada no horário da tela, ambiente arranjado contra o elefante, e uma técnica para o pico, ensaiada na sessão antes de ser necessária.</p>
"""),
    ],
    'checklist': [
        'Comecei pela situação em que é mais fácil mudar, e não pela mais grave.',
        'Escrevi a meta em formato SMART, com o para quê (valor) ao lado.',
        'Evitei "parar" como meta; combinei um limite com dias, horários e data de início.',
        'Montei com o paciente a escala de cinco níveis, com a meta no zero e substituição no +2.',
        'Identifiquei em que quadrante do estado a tela entra para este paciente.',
        'Planejei atividades para ocupar esse quadrante no horário em que ele usaria a tela.',
        'Avisei da fase crítica: o humor pode cair antes de subir.',
        'Arranjei o ambiente (bloqueio, notificações, atalhos, distância do celular) em vez de contar com força de vontade.',
        'Ensaiei na sessão uma técnica para o pico do impulso, escolhida pelo quadrante.',
    ],
    'questoes': [
        'Descreva a ficha da preparação: características, perguntas e intervenção.',
        'Reescreva "parar de jogar" como meta SMART e explique o que cada letra acrescenta.',
        'Descreva a escala de alcance da meta e explique por que a meta fica no zero e o +2 exige substituição.',
        'O que os quadrantes do estado mostram sobre onde a dependência se instala, e o que a curva de ativação e humor acrescenta?',
        'Explique a alegoria do elefante e do condutor e o que ela implica para a estratégia de manejo do impulso.',
        'Pense num paciente teu em preparação. Qual seria a primeira meta SMART dele, em que quadrante a tela entra, e o que tu colocaria no lugar?',
    ],
    'gabarito': {
     0: (C, u"Características: motivado, mas precisa de orientação prática; pode ter tentado reduzir sem sucesso sustentado. Perguntas: se já pensou em estratégia para reduzir; o que acha que precisa para conseguir mudar; quais horários ou situações seriam mais fáceis para começar. Intervenção: metas SMART e estratégias específicas (apps de bloqueio, agenda offline, substituições)."),
     1: (C, u"Por exemplo: \"usar o computador por no máximo duas horas por dia nos dias de semana, a partir da próxima semana, para ter tempo de estudar\". S: número e dias, e não \"parar\". M: registro diário e escala de alcance. A: duas horas nos dias de semana, com fim de semana livre, com base no histórico. R: ligada ao valor (o estudo, o caminho sonhado). T: data de início e prazo de revisão."),
     2: (C, u"+2: zero horas e substituiu por atividade saudável; +1: até uma hora; 0: até duas horas, meta alcançada; −1: entre duas e três; −2: mais de três. A meta no zero faz do cumprimento o esperado, e não o máximo, e dá espaço para registrar tanto o dia acima quanto o abaixo sem virar fracasso ou façanha. O +2 exige substituição porque um dia sem tela e sem nada no lugar deixa o quadrante desagradável vazio, que é onde a recaída começa."),
     3: (C, u"Os quadrantes cruzam ativo e inativo com contexto agradável e desagradável; a dependência se desenvolve nos dois desagradáveis (tenso e desmotivado), porque a tela é o que baixa a ativação num e ocupa o vazio no outro. A curva mostra que, com atividades bem planejadas, a ativação sobe antes do humor, e que o humor pode cair no início (fase crítica); a seleção das atividades encurta essa fase, e o paciente precisa ser avisado dela antes."),
     4: (C, u"O cérebro emocional (sistema 1) é o elefante: rápido, automático, feito de vieses de atenção e memória, condicionamento, crenças e emoções aprendidas. O racional (sistema 2) é o condutor: lento, deliberado, cansa. O elefante obedece enquanto quer; num cabo de guerra, ganha. Logo a estratégia não é mais força de vontade, e sim arranjar o caminho: tirar a tela de onde o elefante a encontra, colocar a atividade onde ele passa, e dar ao condutor dez minutos de vantagem (atraso da resposta, bloqueio, ambiente limpo)."),
     5: (K, u"Não há resposta certa. Uma boa resposta escolhe a situação mais fácil (e não a mais grave), escreve a meta com número, dias, data e para quê, identifica o quadrante (tenso ou desmotivado) em que a tela entra para esse paciente e propõe, para o mesmo horário, uma atividade que ele já gostou um dia, de preferência com gente e fora de casa, com o aviso da fase crítica. O erro comum é começar pela redução mais ambiciosa e deixar o horário da tela vazio."),
    },
    'referencias': [
        "Haidt, J. (2006). <em>The happiness hypothesis: Finding modern truth in ancient wisdom.</em> Basic Books.",
        "Kahneman, D. (2012). <em>Rápido e devagar: Duas formas de pensar.</em> Objetiva.",
        "Kiresuk, T. J., &amp; Sherman, R. E. (1968). Goal attainment scaling: A general method for evaluating comprehensive community mental health programs. <em>Community Mental Health Journal, 4</em>(6), 443–453.",
        "Linehan, M. M. (2015). <em>DBT skills training manual</em> (2nd ed.). Guilford Press.",
        "Martell, C. R., Dimidjian, S., &amp; Herman-Dunn, R. (2010). <em>Behavioral activation for depression: A clinician's guide.</em> Guilford Press.",
        "Miller, W. R., &amp; Rollnick, S. (2023). <em>Entrevista motivacional: Ajudando pessoas a mudar e crescer</em> (4. ed.). Artmed.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo segundo vídeo de uma disciplina de pós-graduação; valores e programação de atividades vêm no vídeo 13.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. Os quadros "o R é o que segura os outros quatro", "o que dizer ao paciente antes de começar", "o que a alegoria ensina sobre estratégia", as duas observações sobre as listas de técnicas e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina. Os dois esboços à mão (quadrantes e curvas) foram redesenhados mantendo os elementos e as palavras.<br><br><strong>Sobre as técnicas.</strong> Os exercícios de regulação fisiológica do slide (mudança de temperatura, estímulos sensoriais intensos) estão descritos em termos gerais, sem instruções de aplicação, por escolha editorial deste material; a fonte para o detalhe é o manual de habilidades da DBT, nas referências. A escala de alcance da meta segue a lógica do Goal Attainment Scaling (Kiresuk e Sherman, 1968), citado como respaldo; o slide não cita fonte. A alegoria do elefante é atribuída no slide a Jonathan Haidt, e os dois sistemas a Kahneman, e as duas obras estão nas referências; o material acrescenta a ressalva do próprio Kahneman de que os sistemas são metáfora, e não anatomia.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'GAS': GAS, 'QUAD': QUAD}
DT12['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT12['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT12['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT12, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT12)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT12['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
