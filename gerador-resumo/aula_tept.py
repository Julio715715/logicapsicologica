# -*- coding: utf-8 -*-
"""Aula livre: Tratando o TEPT complexo (Andressa Juliana, 27/04/2026).
Fonte: anotações automáticas da reunião e chat dos participantes; não havia
transcrição integral. Gera página e PDF."""
import io, re, sys
sys.path.insert(0, '/home/claude')
from figs_tept import REDE, FASES, TIPOS
import sup_common, gen_resumo

C = 'comentario'
K = 'criterios'

TEPT = {
    'slug': 'tept-complexo',
    'titulo_txt': 'Tratando o TEPT complexo',
    'titulo_html': 'Tratando o TEPT complexo',
    'data': '27 de abril de 2026',
    'meta': 'Apresentação de Andressa Juliana · Mediação de Prof. Júlio Gonçalves · Aula livre',
    'meta_capa': '27/04/2026 &middot; APRESENTA&Ccedil;&Atilde;O DE ANDRESSA JULIANA<br>'
                 'MEDIA&Ccedil;&Atilde;O DE PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AULA LIVRE',
    'header_dir': 'TEPT COMPLEXO &middot; AULA LIVRE',
    'chave': 'mat-Aula-TEPT-',
    'arquivo': 'Aula-TEPT-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>. A aula apresenta um protocolo que exige "
              u"formação formal, time de consultoria e supervisão; o texto descreve o modelo para que o clínico reconheça "
              u"o quadro e saiba o que o tratamento envolve, e não para que o aplique a partir daqui.</p>"
              u"<p>Perguntas de participantes aparecem sem identificação nominal. Não há caso clínico. Os recursos "
              u"sensoriais de ancoragem citados em aula estão descritos de forma genérica, pelo motivo explicado na nota "
              u"de método. Este resumo foi escrito a partir das anotações da reunião e do chat, e não de transcrição "
              u"integral, o que também está registrado na nota.</p></div>"),
    'tema': 'O que o TEPT complexo acrescenta ao TEPT clássico, por que a evitação da memória é o problema central, '
            'e como o DBT-PTSD organiza exposição, invalidação traumática e mente sábia num mesmo tratamento.',
    'essencial': [
        ('A memória traumática é uma rede, e o gatilho acende a rede inteira.',
         'Fragmentos sensoriais, cognitivos, emocionais e corporais ligados entre si, sem começo, meio e fim. Por isso a pessoa revive em vez de lembrar.'),
        ('Evitar custa caro e não segura.',
         'Quanto mais a memória é suprimida, mais intensa ela volta. Tratar só o comportamento de risco deixa o problema central no lugar.'),
        ('A invalidação é um segundo trauma.',
         'Tentar contar e não ser acreditado, ser punido, ou nunca ter contado a ninguém. No DBT-PTSD isso recebe exposição própria.'),
        ('Mente sábia vem antes da exposição, e é o que a torna suportável.',
         'Bondade, compaixão, alegria solidária e equanimidade são treinadas na preparação. Depois, é o adulto em mente sábia que revisita a cena.'),
        ('TEPT complexo e borderline se sobrepõem demais para não serem rastreados juntos.',
         'Num quadro, rastrear o outro. A diferença mais útil está na função do comportamento impulsivo, e não na sua forma.'),
    ],
    'secoes': [
        ('s0', 'Por que o trauma complexo virou assunto de todo clínico', 'Por que o trauma complexo virou assunto de todo clínico', u"""
<p>A aula abriu com uma observação sobre o campo: o trauma complexo vem ganhando espaço próprio em congressos, e quem trabalha com transtornos da personalidade, em especial com o <em>borderline</em>, esbarra nele o tempo todo. Uma parte considerável do que se lê como personalidade foi construída em volta de experiências repetidas de violência.</p>
<p>Dois pontos do enquadramento inicial valem guardar. O primeiro é que trauma não é só o evento violento e visível; o trauma complexo afeta os modelos de funcionamento da pessoa, o jeito como ela se vê, se relaciona e regula o que sente. O segundo é que o próprio formato social pode retraumatizar: a família que não acredita, a instituição que não age, o consultório que trata o relato como exagero. É aqui que a discussão encontra a dimensão sociocultural da Terapia Baseada em Processos: o ambiente que invalida faz parte da rede, e não do pano de fundo.</p>
<div class='callout note'><div class='co-t'>O que a aula se propôs</div>Apresentar o modelo do TEPT, a diferença entre TEPT clássico e TEPT complexo, e a lógica do DBT-PTSD, um protocolo <strong>altamente especializado</strong>, que exige formação formal, participação em time de consultoria e supervisão. O objetivo declarado foi que o clínico reconheça a necessidade de um trabalho específico para esses pacientes, e não que saia aplicando o protocolo.</div>
"""),
        ('s1', 'O DBT-PTSD: para quem, de onde veio, o que sustenta', 'O DBT-PTSD: para quem, de onde veio, o que sustenta', u"""
<h3>Para quem</h3>
<p>O protocolo foi desenvolvido para <strong>adultos que sofreram violência interpessoal na infância e na adolescência</strong>, sobretudo sexual, em geral recorrente e repetida. É um público bem delimitado. A aula registrou que o tratamento não foi desenhado para violência que ocorre apenas na vida adulta.</p>
<h3>De onde veio</h3>
<p>O desenvolvimento é de Martin Bohus, na Alemanha, em contexto de internação, com pacientes que ficavam até três meses no hospital. Bohus questionou uma premissa consolidada: a de que pacientes com padrão <em>borderline</em> e TEPT não deveriam passar por exposição no estágio um do tratamento, antes de estabilizar os comportamentos de risco. Os estudos dele mostraram que os pacientes não aumentavam comportamentos de risco durante a exposição, e que processar a memória traumática era justamente o que os diminuía.</p>
<h3>De que ele é feito</h3>
<p>A estrutura é a da Terapia Comportamental Dialética. O núcleo da exposição vem dos protocolos cognitivo-comportamentais para TEPT. E o tratamento incorporou ferramentas da Terapia de Aceitação e Compromisso e da Terapia Focada na Compaixão, o que aparece com força na prática de mente sábia.</p>
<h3>O que sustenta</h3>
<ul class='key'><li><b>2013</b>: ensaio randomizado em regime residencial, comparando DBT-PTSD com lista de espera e tratamento usual, em mulheres com TEPT após abuso sexual na infância, com e sem transtorno da personalidade <em>borderline</em>.</li><li><b>2020</b>: ensaio com <strong>193 mulheres</strong>, comparando DBT-PTSD com terapia de processamento cognitivo. O DBT-PTSD teve resultado melhor no desfecho primário, com mais remissão sintomática e menos abandono precoce.</li><li><b>2024</b>: metanálise das variantes de DBT para TEPT, com 13 estudos e <strong>663 participantes</strong>, encontrando efeito moderado na gravidade dos sintomas em relação ao controle, com melhora também em depressão, dissociação, sintomas <em>borderline</em> e autolesão.</li></ul>
<p>Os resultados foram consistentes entre o tratamento intensivo em internação e o ambulatorial.</p>
<div class='obs'><h4>Uma moderação de leitura</h4><p>A aula falou em <em>superioridade significativa</em> do DBT-PTSD sobre a terapia de processamento cognitivo. É verdade, e a diferença foi estatisticamente significativa no desfecho primário. Mas a diferença média entre os grupos na escala clínica foi modesta, e a terapia de processamento cognitivo também produziu ganho grande. A leitura defensável é que o DBT-PTSD foi <strong>melhor num quadro em que já se esperava que exposição funcionasse</strong>, e com menos abandono, o que para essa população pesa tanto quanto o tamanho do efeito. Nada disso enfraquece a mensagem central da aula: exposição em pacientes com desregulação grave é viável e ajuda.</p></div>
"""),
        ('s2', 'TEPT clássico, TEPT complexo e o borderline', 'TEPT clássico, TEPT complexo e o borderline', u"""
<h3>Os dois quadros</h3>
<p>O <strong>TEPT clássico</strong> tem três eixos: revivência (intrusões, <em>flashbacks</em>, pesadelos), evitação de lembranças e hipervigilância. O <strong>TEPT complexo</strong>, descrito na CID-11, tem esses três eixos e mais três, que aparecem depois de exposição prolongada e repetida: problemas de regulação do afeto, autoconceito predominantemente negativo (culpa, vergonha, sentir-se estragado) e relacionamentos perturbados. A formulação da aula é precisa: nesses casos a <strong>personalidade foi construída ao redor do trauma</strong>.</p>
<h3>A sobreposição com o borderline</h3>
<p>Existe uma sobreposição enorme entre TEPT complexo e transtorno da personalidade <em>borderline</em>, e o diagnóstico diferencial é difícil. A aula ofereceu duas pistas.</p>
<ul class='key'><li><b>A função do comportamento impulsivo.</b> No TEPT complexo, a impulsividade está a serviço do enfrentamento das memórias traumáticas: a pessoa faz para não lembrar, para não sentir o que a lembrança traz. Isso é o que o clínico consegue investigar em sessão, e é a pista mais útil.</li><li><b>A relação com a solidão.</b> Como observação clínica da apresentadora, pacientes com TEPT complexo tendem a tolerar e até preferir ficar sozinhos, enquanto pacientes com padrão <em>borderline</em> demandam validação social e sofrem mais ao ficar sós.</li></ul>
<div class='callout note'><div class='co-t'>Implicação direta</div>Rastrear ativamente TEPT complexo em pacientes com diagnóstico de <em>borderline</em>, e vice-versa. A segunda pista é observação clínica, e não critério; serve para levantar hipótese, e não para fechar diagnóstico.</div>
"""),
        ('s3', 'A rede de memória traumática e o custo da evitação', 'A rede de memória traumática e o custo da evitação', u"""
<p>Este é o pedaço da aula que mais organiza o resto. Pela repetição das experiências, o trauma se organiza em <strong>redes</strong>. A memória não fica guardada de forma linear, com começo, meio e fim, mas fragmentada e descontextualizada, em elementos ligados entre si: sensoriais (sufocamento, náusea), cognitivos (cognições de culpa), emocionais (medo, vergonha) e corporais.</p>
{{REDE}}
<p>Quando um gatilho ativa um elemento, a rede inteira pode acender, e a pessoa <strong>revive a experiência no presente</strong>. É isso que justifica a exposição: não há como contextualizar a memória sem acessá-la.</p>
<h3>O que a evitação faz</h3>
<p>O paciente com trauma complexo evita as lembranças, e isso demanda uma energia que não se sustenta o tempo inteiro. Quanto mais a memória é suprimida, mais intensa ela volta, em inundações emocionais que puxam comportamentos de risco mais intensos: uso de substâncias, autolesão. Daí a conclusão da aula, que vale como regra de formulação: <strong>tratar só o comportamento de risco tende a ser ineficaz</strong>, porque o problema central, a memória traumática, continua lá.</p>
<h3>As emoções que mais aparecem, e a função de cada uma</h3>
<ul class='key'><li><b>Vergonha</b>: ligada à tentativa de evitar exclusão, e com frequência uma resposta secundária à culpa.</li><li><b>Culpa</b>: pode servir para proteger a única relação que a criança tinha, ou para explicar o evento como algo que ela fez. Culpa dá a sensação de controle onde havia impotência.</li><li><b>Nojo</b>: emoção protetora que, na infância, sem diferenciação clara entre corpo e self, passa a ser vivida como se a pessoa inteira fosse nojenta.</li><li><b>Impotência</b>: o pano de fundo das outras três.</li></ul>
<p>Ler essas emoções pela função é o que permite, mais adiante, reprocessar o sentido delas em vez de discutir se são justificadas.</p>
"""),
        ('s4', 'As quatro fases e o time de consultoria', 'As quatro fases e o time de consultoria', u"""
{{FASES}}
<h3>Preparação</h3>
<p>A primeira fase reúne psicoeducação, acordos (entre eles o compromisso de não suicídio), prática de mente sábia, construção do plano de crise e o mapeamento de valores e metas, na estratégia chamada de <strong>caminho antigo e caminho novo</strong>: o que a vida tem sido, e o que ela pode ser se o trauma deixar de organizá-la.</p>
<p>O treino de habilidades pode ser conduzido pelo próprio terapeuta, individualmente; o protocolo não exige grupo de habilidades separado. O foco é o que a exposição vai pedir: noções básicas de regulação emocional e <strong>habilidades antidissociativas</strong>.</p>
<h3>Critérios para começar a expor</h3>
<p>Os critérios apresentados são relativamente simples: um período de quatro semanas sem comportamentos de risco à vida e abstinência de autolesão. A prontidão, porém, não é decisão solitária do terapeuta: é decidida em <strong>reunião com o time de consultoria</strong>, na qual o paciente apresenta o próprio modelo do trauma, o que por si já é parte do tratamento.</p>
<div class='callout note'><div class='co-t'>O time não é opcional</div>O DBT-PTSD exige participação em time de consultoria específico. A função é dupla: identificar pontos cegos do terapeuta e prevenir o esgotamento de quem trabalha com esse material todos os dias. A aula tratou o time como parte estrutural do tratamento, e não como apoio.</div>
"""),
        ('s5', 'Exposição: como funciona e os três formatos', 'Exposição: como funciona e os três formatos', u"""
<h3>O mecanismo</h3>
<p>A exposição funciona por <strong>aprendizagem inibitória</strong>: cria-se uma nova rede, mais segura, que passa a ser ativada no lugar da rede traumática original. O paciente revive emoções e sensações do trauma sem interpretar que a morte ou o perigo são iminentes, e a memória pode ser contextualizada e integrada como algo do passado.</p>
<p>Há um segundo efeito, que a aula destacou: a exposição cria a experiência de ser acolhido por alguém que não julga. Isso reduz a vergonha, permite reavaliar as cognições do trauma com recursos de adulto e abre caminho para a aceitação radical do que aconteceu.</p>
<h3>Por onde começar</h3>
<p>Paradoxalmente, pela memória que gera <strong>mais angústia e mais intrusões</strong>. A razão é a própria rede: memórias de menor intensidade tendiam a ativar a pior memória de qualquer jeito, pelos elementos interligados. Começar pela pior é começar pelo nó que puxa os outros.</p>
{{TIPOS}}
<h3>A exposição in vivo</h3>
<p>O paciente narra a memória de olhos fechados, no presente. O terapeuta <strong>bloqueia as estratégias de evitação</strong> (rir, mudar de assunto, resumir) e a dissociação, para que a memória seja confrontada como ela é. A sessão é gravada e o paciente ouve a gravação em casa, por cerca de trinta minutos ao dia. Para manter o paciente ancorado, o protocolo usa recursos como assento instável ou contato de mãos com o terapeuta, sempre combinados antes.</p>
<p>O que interrompe a exposição é a queda da ativação emocional junto com a redução dos sintomas de revivência: quando as intrusões e os <em>flashbacks</em> deixam de aparecer com a mesma frequência.</p>
"""),
        ('s6', 'A invalidação traumática como segundo trauma', 'A invalidação traumática como segundo trauma', u"""
<p>Este foi o ponto que mais rendeu perguntas. O trauma complexo costuma ser uma <strong>dupla questão</strong>: a violência interpessoal e o ambiente que invalida a criança. A invalidação pode ser a tentativa de contar e ser punida, desacreditada ou culpada; pode ser o adulto que acredita e não faz nada; pode ser a família que mantém o contato com o agressor e trata o ocorrido como se não fosse nada; e pode ser nunca ter contado a ninguém.</p>
<p>Uma participante perguntou se o adulto que acredita mas <em>coloca debaixo do tapete</em> configura invalidação. A resposta foi que sim: não denunciar, não proteger, seguir a vida como se nada tivesse acontecido é invalidação, mesmo sem uma palavra de descrédito.</p>
<h3>Como se faz</h3>
<p>O paciente escreve previamente a experiência de invalidação, que muitas vezes é mais de uma. Em sessão, narra de olhos fechados, primeiro o evento completo e depois só os pontos críticos, os que mais o ativam. O terapeuta ajuda a acessar todos os elementos: as reações dos outros, o que o paciente sentiu e pensou naquele momento. E intercala a narrativa com perguntas sobre o presente, para sustentar a <strong>dupla consciência</strong>: a pessoa é observadora da memória, e não está de novo dentro dela.</p>
<h3>Para quê</h3>
<p>O objetivo é atualizar a memória: permitir que o paciente veja o evento como <strong>falha do ambiente, e não dele</strong>, e acesse a emoção primária do episódio, quase sempre a tristeza, em vez da secundária, quase sempre a raiva. A exposição é interrompida quando a ativação cai e a revivência rareia.</p>
<div class='callout note'><div class='co-t'>Implicação de formulação</div>A invalidação traumática é tratada como trauma separado, com exposição própria. Na rede do caso, isso significa dois nós, e não um: o evento e a resposta do ambiente ao evento. Muitas vezes é o segundo que sustenta a vergonha.</div>
"""),
        ('s7', 'Mente sábia estendida e a exposição na cadeira vazia', 'Mente sábia estendida e a exposição na cadeira vazia', u"""
<p>O DBT-PTSD tem uma prática de mente sábia própria, mais completa do que a dos manuais padrão de DBT, e o paciente a pratica extensivamente antes de qualquer exposição. Ela é adaptada com uma <strong>cadeira vazia</strong>, que paciente e terapeuta observam, e que representa o lugar da prática.</p>
<h3>Os quatro elementos</h3>
<ul class='key'><li><b>Bondade amorosa</b>: treinar uma visão menos hostil de si.</li><li><b>Compaixão</b>: cuidar da própria dor com coragem.</li><li><b>Alegria solidária</b>: reconhecer pequenos sinais positivos.</li><li><b>Equanimidade e sabedoria</b>: ver a realidade como ela é sem ser destruído por ela.</li></ul>
<p>A prática usa visualizações guiadas, como regar uma planta frágil ou a imagem da árvore e das raízes. E é <strong>personalizada</strong>: o paciente descreve uma experiência própria, de filme ou de livro, que o conecta a cada elemento, e o terapeuta grava uma segunda prática guiada incluindo essas referências.</p>
<h3>A exposição à mente sábia</h3>
<p>É o formato que trabalha o que o TEPT complexo tem de específico: o autoconceito negativo e a autoaversão. Com a mente sábia ativada, o adulto observa a cena na cadeira vazia e responde a perguntas do terapeuta sobre o evento. Reprocessa os significados: de quem era a responsabilidade, se a culpa pertence a ele, se a culpa foi uma tentativa de dar sentido à impotência.</p>
<p>Diferente da exposição in vivo, esta não termina por métrica de intrusão. Termina quando o terapeuta avalia que o paciente reprocessou e consegue olhar a situação com compaixão, aceitação e sem culpa.</p>
<p>Uma participante observou no chat que o procedimento lembra a terapia do esquema. A semelhança existe, e a diferença está no lugar de onde se olha: aqui, quem revisita a cena é o adulto em mente sábia, treinado para isso durante semanas, e não uma parte que o terapeuta convoca.</p>
"""),
        ('s8', 'Antidissociação e ancoragem, inclusive online', 'Antidissociação e ancoragem, inclusive online', u"""
<p>Dissociar durante a exposição anula a exposição. Por isso o terapeuta guia o paciente de volta ao presente com habilidades antidissociativas simples: perguntar a hora, o dia, onde estão; pedir que descreva o ambiente; interagir diretamente, pedindo que olhe para o terapeuta. É o mesmo repertório de tolerância ao mal-estar da DBT, usado com precisão dentro da sessão.</p>
<ul class='key'><li><b>Descrição do presente</b>: local, data, o que se vê e se ouve.</li><li><b>Corpo</b>: movimentar-se, pressionar os pés no chão, contrair e relaxar músculos.</li><li><b>Estímulos sensoriais intensos</b>: usados como âncora, com escolha combinada previamente com o paciente.</li><li><b>Encorajamento interpessoal</b>: o terapeuta traz o paciente de volta pela relação.</li></ul>
<p>Os pacientes montam um <strong>kit de sobrevivência à crise</strong>, com objetos que possam carregar consigo e que funcionem como âncora fora da sessão.</p>
<h3>Online</h3>
<p>Perguntaram como fazer a exposição à mente sábia à distância. A resposta foi que dá para adaptar: a cadeira vazia funciona na tela, e um objeto na mão do paciente pode cumprir a função de ancoragem. A ressalva é importante: em casos difíceis, com dissociação intensa, o encaminhamento para exposição presencial pode ser necessário. Uma participante lembrou que a prática depende de <em>mindfulness</em> bem conduzido, tanto por quem guia quanto por quem pratica, e que isso não é para todo paciente em qualquer momento.</p>
<p>Perguntaram também sobre a relação com o EMDR. A apresentadora respondeu que não conhecia o método o suficiente para comparar, e a pergunta ficou em aberto, o que é a resposta honesta quando se ensina um protocolo específico.</p>
"""),
        ('s9', 'Vida de valor, despedida, e o que a conversa final levantou', 'Vida de valor, despedida, e o que a conversa final levantou', u"""
<h3>Depois da exposição</h3>
<p>A terceira fase constrói uma vida de valor: trabalha a percepção corporal e a sexualidade, frequentemente afetadas, define metas futuras e trabalha a prevenção de a pessoa se colocar em novas situações de violência. Na despedida, o paciente escreve e lê em sessão uma <strong>carta a si mesmo</strong>, com a mente sábia ativada, resumindo a jornada. Seguem sessões de reforço e prevenção de recaída.</p>
<h3>Adesão, cultura e postura</h3>
<p>A conversa final entre apresentadora e mediador tocou em três coisas que não estão no manual.</p>
<p>A primeira é a <strong>adesão</strong>. O protocolo é relativamente novo no Brasil, e a exposição começa pela pior memória, o que soa como inundação. A ponderação foi que o modelo é mais compassivo do que parece, justamente porque a mente sábia entra desde o início. Ainda assim, a adesão de pacientes brasileiros a tratamentos longos e exigentes é baixa, e a fidelidade ao protocolo vai precisar de alguma flexibilidade e adaptação cultural.</p>
<p>A segunda é a <strong>capacidade cognitiva</strong>. Um modelo assim pede que o paciente acompanhe um racional complexo. Nem todos conseguem, e isso precisa entrar na avaliação de prontidão.</p>
<p>A terceira é a <strong>postura do terapeuta</strong>. O mediador defendeu uma postura mais firme, próxima da médica, para sustentar o engajamento: em alguns momentos o terapeuta trabalha por convencimento, e não só pela motivação que o paciente traz, sobretudo para que a prática de mente sábia aconteça de fato entre as sessões.</p>
<h3>Materiais</h3>
<p>Há pouca coisa em português além dos artigos de Bohus, e o manual completo é restrito a quem passa pelo treinamento. Foi mencionada a possibilidade de um novo treinamento no Brasil, com foco em exposição à invalidação traumática. A conclusão da noite foi que o tema tem material para uma semana de aulas, e que tratar trauma, mesmo sem ser o foco de todo clínico, é inevitável com pacientes mais crônicos.</p>
"""),
    ],
    'checklist': [
        'Rastreei TEPT complexo em pacientes com diagnóstico de borderline, e o inverso.',
        'Investiguei a função do comportamento impulsivo: ele serve para não lembrar, para não sentir?',
        'Mapeei a rede da memória traumática do paciente, incluindo os elementos sensoriais e corporais.',
        'Identifiquei a invalidação traumática como nó próprio, separado do evento.',
        'Distingui, com o paciente, a emoção primária do episódio da emoção secundária que aparece no relato.',
        'Li a culpa e a vergonha pela função que cumpriram, antes de discutir se são justificadas.',
        'Avaliei se tratar só o comportamento de risco está deixando o problema central intocado.',
        'Verifiquei minha própria prontidão para exposição: formação, time de consultoria, supervisão.',
        'Combinei com o paciente âncoras antidissociativas antes de qualquer trabalho com a memória.',
        'Encaminhei para tratamento especializado quando o caso pediu, em vez de improvisar exposição.',
    ],
    'questoes': [
        'O que o TEPT complexo acrescenta ao TEPT clássico, segundo a CID-11? Por que isso muda o alvo do tratamento?',
        'Explique a rede de memória traumática. Por que ela justifica a exposição e por que a evitação falha?',
        'Que pista a aula ofereceu para diferenciar TEPT complexo de padrão borderline a partir do comportamento impulsivo?',
        'Por que a exposição começa pela pior memória, e não pela mais leve?',
        'O que é invalidação traumática e por que ela recebe exposição própria?',
        'Pense num paciente seu com história de violência repetida. Onde você localizaria a invalidação na rede dele?',
        'Como você combinaria com um paciente as âncoras antidissociativas antes de qualquer trabalho com a memória?',
        'Qual é a sua posição sobre a postura firme, de convencimento, defendida na conversa final? Em que caso ela ajudaria e em que caso atrapalharia?',
    ],
    'gabarito': {
     0: (C, u"Aos três eixos do TEPT clássico (revivência, evitação e hipervigilância) a CID-11 acrescenta três perturbações da auto-organização: <b>desregulação do afeto</b>, <b>autoconceito negativo</b> (culpa, vergonha, sentir-se estragado) e <b>relacionamentos perturbados</b>. O alvo muda porque a memória do evento não é o único problema: a personalidade foi construída em volta do trauma, e por isso o DBT-PTSD tem exposição própria para o autoconceito (mente sábia) e para o ambiente que invalidou (invalidação traumática)."),
     1: (C, u"A memória traumática não fica guardada como história, mas como <b>elementos interligados</b>: sensoriais, cognitivos, emocionais e corporais. Um gatilho toca um elemento e a rede inteira acende, e a pessoa revive em vez de lembrar. A exposição é justificada porque só acessando a rede é possível contextualizá-la e criar uma rede nova, mais segura, por aprendizagem inibitória. A evitação falha porque custa energia que não se sustenta, e porque a memória suprimida volta mais intensa, puxando comportamentos de risco."),
     2: (C, u"A <b>função</b> do comportamento impulsivo: no TEPT complexo ele está a serviço do enfrentamento das memórias, a pessoa faz para não lembrar ou não sentir o que a lembrança traz. A aula ofereceu uma segunda pista, como observação clínica e não critério: a tolerância ou preferência por ficar só no TEPT complexo, contra a demanda de validação social no padrão borderline. A primeira pista é a que se investiga em sessão; a segunda levanta hipótese."),
     3: (C, u"Porque, pela lógica da rede, memórias de menor intensidade tendiam a ativar a pior memória de qualquer forma, pelos elementos interligados. Começar pela mais leve não poupava o paciente; só adiava. Começar pela pior é começar pelo nó que puxa os outros. O que torna isso suportável é a preparação: mente sábia, plano de crise e âncoras antidissociativas vêm antes."),
     4: (C, u"É a resposta do ambiente ao trauma: tentar contar e ser punido, desacreditado ou culpado; o adulto que acredita e não age; a família que mantém o contato com o agressor; ou nunca ter contado a ninguém. Recebe exposição própria porque é um <b>segundo trauma</b>, com rede própria, e muitas vezes é ele que sustenta a vergonha. O objetivo dessa exposição é atualizar a memória como falha do ambiente, e não da pessoa, e acessar a emoção primária, quase sempre a tristeza, no lugar da raiva."),
     5: (K, u"Não há resposta certa. Uma boa resposta localiza a invalidação como <b>nó separado</b> do evento, com suas próprias ligações: para a vergonha, para a desconfiança de que alguém vá acreditar de novo, para o silêncio em sessão. Vale reconhecer que o nunca ter contado também é invalidação, e que ela pode estar ativa no presente, na família que segue tratando o assunto como inexistente. O erro comum é tratar a invalidação como contexto do trauma, e não como parte da rede."),
     6: (K, u"Não há resposta certa. Uma boa resposta combina as âncoras <b>antes</b>, com o paciente escolhendo o que funciona para ele: descrição do presente, movimento do corpo, um objeto na mão, o contato pela relação. Inclui um sinal combinado para quando a dissociação começar, e um acordo sobre o que o terapeuta vai fazer nesse momento. O erro comum é escolher a âncora no meio da crise, ou impor um recurso que o paciente não testou."),
     7: (K, u"Não há resposta certa, e é a pergunta que mais divide. Uma boa resposta reconhece os dois lados: a postura firme sustenta engajamento em tratamentos exigentes, em que a motivação do paciente oscila e a prática entre sessões decide o resultado; e a mesma postura pode reproduzir invalidação num paciente cuja história é de adultos que decidiam por ele. O critério é a função: firmeza a serviço do que o paciente disse querer no caminho novo, e não a serviço do protocolo. O erro comum é escolher um lado sem olhar para o paciente à frente."),
    },
    'referencias': [
        "Bohus, M., Dyer, A. S., Priebe, K., Kr&uuml;ger, A., Kleindienst, N., Schmahl, C., Niedtfeld, I., &amp; Steil, R. (2013). Dialectical behaviour therapy for post-traumatic stress disorder after childhood sexual abuse in patients with and without borderline personality disorder: A randomised controlled trial. <em>Psychotherapy and Psychosomatics, 82</em>(4), 221–233.",
        "Bohus, M., Kleindienst, N., Hahn, C., M&uuml;ller-Engelmann, M., Ludäscher, P., Steil, R., Fydrich, T., Kuehner, C., Resick, P. A., Stiglmayr, C., Schmahl, C., &amp; Priebe, K. (2020). Dialectical behavior therapy for posttraumatic stress disorder (DBT-PTSD) compared with cognitive processing therapy (CPT) in complex presentations of PTSD in women survivors of childhood abuse: A randomized clinical trial. <em>JAMA Psychiatry, 77</em>(12), 1235–1245.",
        "Bohus, M., Schmahl, C., Fydrich, T., Steil, R., M&uuml;ller-Engelmann, M., Herzog, J., Ludäscher, P., Kleindienst, N., &amp; Priebe, K. (2019). A research programme to evaluate DBT-PTSD, a modular treatment approach for complex PTSD after childhood abuse. <em>Borderline Personality Disorder and Emotion Dysregulation, 6</em>, 7.",
        "Brewin, C. R., Cloitre, M., Hyland, P., et al. (2017). A review of current evidence regarding the ICD-11 proposals for diagnosing PTSD and complex PTSD. <em>Clinical Psychology Review, 58</em>, 1–15.",
        "Craske, M. G., Treanor, M., Conway, C. C., Zbozinek, T., &amp; Vervliet, B. (2014). Maximizing exposure therapy: An inhibitory learning approach. <em>Behaviour Research and Therapy, 58</em>, 10–23.",
        "Ford, J. D., &amp; Courtois, C. A. (2014). Complex PTSD, affect dysregulation, and borderline personality disorder. <em>Borderline Personality Disorder and Emotion Dysregulation, 1</em>, 9.",
        "Hayes, S. C., Hofmann, S. G., &amp; Ciarrochi, J. (2020). A process-based approach to psychological diagnosis and treatment. <em>Clinical Psychology Review, 82</em>, 101908.",
        "Linehan, M. M. (2015). <em>DBT skills training manual</em> (2ª ed.). Guilford Press.",
        "Organização Mundial da Saúde. (2019). <em>Classificação Internacional de Doenças, 11ª revisão (CID-11)</em>: transtorno de estresse pós-traumático complexo (6B41).",
        "Prillinger, K., Goreis, A., Macura, S., Hajek Gross, C., Lozar, A., Fanninger, S., Mayer, A., Oppenauer, C., Plener, P. L., &amp; Kothgassner, O. D. (2024). A systematic review and meta-analysis on the efficacy of dialectical behavior therapy variants for the treatment of post-traumatic stress disorder. <em>European Journal of Psychotraumatology, 15</em>(1), 2406662.",
        "Steil, R., Dittmann, C., M&uuml;ller-Engelmann, M., Dyer, A., Maasch, A.-M., &amp; Priebe, K. (2018). Dialectical behaviour therapy for posttraumatic stress disorder related to childhood sexual abuse: A pilot study in an outpatient treatment setting. <em>European Journal of Psychotraumatology, 9</em>(1), 1423832.",
    ],
    'nota': u"""Material dirigido a psicólogos. Descreve um protocolo que exige formação formal, time de consultoria e supervisão; não habilita ninguém a aplicá-lo.<br><br><strong>Fonte deste resumo.</strong> Diferente dos demais materiais do acervo, este foi escrito a partir das <b>anotações automáticas da reunião</b> e do chat dos participantes, e não de transcrição integral, porque a transcrição não estava disponível. As anotações são detalhadas, mas resumem falas; onde havia dúvida sobre a formulação exata da apresentadora, o texto preferiu a versão mais cautelosa. Se a transcrição aparecer, o material pode ser revisado contra ela.<br><br><strong>Artefatos corrigidos.</strong> As anotações registram o autor do protocolo como <em>Borros</em>; trata-se de Martin Bohus. O nome do instituto que traria o autor ao Brasil aparece nas anotações de forma incerta e foi omitido.<br><br><strong>Uma moderação empírica, sinalizada no texto.</strong> A superioridade do DBT-PTSD sobre a terapia de processamento cognitivo no ensaio de 2020 é real e significativa, mas a diferença média entre os grupos foi modesta, e o comparador também produziu ganho grande; o texto registra as duas coisas. A metanálise citada em aula com 663 participantes corresponde a Prillinger et al. (2024), que encontrou efeito moderado contra controle.<br><br><strong>Uma omissão de segurança.</strong> Os recursos sensoriais de ancoragem citados em aula, entre eles sabor ardido e temperatura, estão descritos de forma genérica, como em outros materiais deste acervo: existem dentro de protocolos estruturados, com triagem e treinamento, e não como lista aberta. As estratégias de descrição do presente, corpo e relação foram integralmente mantidas. Os critérios de prontidão para exposição estão reproduzidos como apresentados em aula e devem ser conferidos no manual por quem for aplicá-los.<br><br><strong>Acréscimos.</strong> As referências foram acrescentadas para dar respaldo formal ao que foi dito sem citação explícita: os ensaios de 2013 e 2020, o programa de pesquisa de 2019, a metanálise de 2024, a descrição do TEPT complexo na CID-11 e a base da aprendizagem inibitória. Nenhuma citação foi construída para preencher lacuna. A observação sobre a semelhança com a terapia do esquema veio do chat e foi comentada no texto; a pergunta sobre EMDR ficou em aberto, como ficou na aula.""",
}

_FIGS = {'REDE': REDE, 'FASES': FASES, 'TIPOS': TIPOS}
TEPT['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in TEPT['secoes']]


def pagina_aula(spec, base):
    h = sup_common.pagina(spec, base)
    h = (h.replace("href='/supervisoes/' title='Voltar para Supervisões'", "href='/aulas/' title='Voltar para Aulas Livres'")
          .replace("<div class='tag'>Supervisão Clínica</div>", "<div class='tag'>Aulas Livres</div>")
          .replace("<a class='home' href='/supervisoes/'>&#8592; Supervisões</a>", "<a class='home' href='/aulas/'>&#8592; Aulas</a>")
          .replace("<div class='kick'>Supervisão clínica · Lógica Psicológica</div>", "<div class='kick'>Resumo de aula · Aula livre</div>"))
    return h


if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/aulas/transdiagnostico-substancias/index.html', encoding='utf-8').read()
    dest = SITE + '/aulas/' + TEPT['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_aula(TEPT, base))
    c = sup_common.pdf(TEPT)
    c['kicker'] = 'RESUMO DE AULA &middot; AULA LIVRE'
    c['gabarito'] = TEPT['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
