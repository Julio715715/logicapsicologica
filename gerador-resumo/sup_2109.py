# -*- coding: utf-8 -*-
"""Supervisão de 21/09/2026: aceitação antes da mudança (bipolaridade, identidade, plano de segurança).
Fonte: anotações do encontro + texto de apoio 'Aceitação, mudança e dialética' (aula 5, Descomplicando a DBT)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

REDE = u"""<figure class='dg'><div class='dg-t'>A alça que o erro pequeno dispara</div>
<svg viewBox='0 0 720 250' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Rede do caso: erro pequeno no trabalho ativa a exigência de normalidade, a recusa do diagnóstico e pensamentos de morte, que levam a isolamento e voltam a alimentar a exigência; contexto invalidante e fadiga pelos medicamentos cercam a alça'>
<defs><marker id='rd' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='96' width='150' height='58' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='75' y='120' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>erro pequeno</text>
<text x='75' y='138' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>no trabalho, no dia a dia</text>
<path d='M154 125 L178 125' stroke='#8d876f' stroke-width='2' marker-end='url(#rd)'/>
<rect x='182' y='84' width='170' height='82' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='267' y='108' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>exigência de normalidade</text>
<text x='267' y='126' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>"tenho que render, tenho que</text>
<text x='267' y='141' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>ser normal"; recusa do</text>
<text x='267' y='156' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>diagnóstico, ruminação de identidade</text>
<path d='M356 125 L380 125' stroke='#8d876f' stroke-width='2' marker-end='url(#rd)'/>
<rect x='384' y='96' width='150' height='58' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='459' y='120' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>pensamentos de morte</text>
<text x='459' y='138' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>passageiros, recorrentes</text>
<path d='M538 125 L562 125' stroke='#8d876f' stroke-width='2' marker-end='url(#rd)'/>
<rect x='566' y='96' width='154' height='58' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='643' y='120' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>isolamento</text>
<text x='643' y='138' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>e mais inadequação</text>
<path d='M643 158 L643 190 L267 190 L267 170' fill='none' stroke='#8d876f' stroke-width='2' stroke-dasharray='5 4' marker-end='url(#rd)'/>
<text x='455' y='206' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#8d876f'>quanto mais isolada, mais a exigência de ser normal pesa</text>
<rect x='0' y='10' width='350' height='52' rx='9' fill='#43441f'/>
<text x='14' y='31' %(F)s font-size='10.5' font-weight='800' fill='#f0ede0'>CONTEXTO INVALIDANTE</text>
<text x='14' y='49' %(F)s font-size='10.5' fill='#9ca575'>avó rígida e depreciativa; mãe que descarrega nela; sem rede</text>
<rect x='370' y='10' width='350' height='52' rx='9' fill='#43441f'/>
<text x='384' y='31' %(F)s font-size='10.5' font-weight='800' fill='#f0ede0'>FADIGA BIOFISIOL&Oacute;GICA</text>
<text x='384' y='49' %(F)s font-size='10.5' fill='#9ca575'>cansaço pelos medicamentos, sono, custo de vida sozinha</text>
<path d='M175 66 L175 80' stroke='#8d876f' stroke-width='1.6' marker-end='url(#rd)'/>
<path d='M545 66 L545 80' stroke='#8d876f' stroke-width='1.6' marker-end='url(#rd)'/>
<text x='360' y='240' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>as duas faixas de cima não são pano de fundo: elas abaixam o limiar em que o erro pequeno dispara a alça</text>
</svg>
<figcaption>Mesmo estabilizada, sem hipomania nem depressão, a paciente entra nessa alça por um erro comum de trabalho. O alvo não é o erro; é a exigência que o transforma em veredito.</figcaption></figure>""" % dict(F=F)

ORDEM = u"""<figure class='dg'><div class='dg-t'>O que a supervisão definiu, em ordem de prioridade</div>
<svg viewBox='0 0 720 228' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Quatro prioridades em sequência: plano de segurança, postura de aceitação, contexto em pequenas mudanças, e o que fica para depois'>
<rect x='0' y='8' width='168' height='150' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.5'/>
<text x='14' y='32' %(F)s font-size='22' font-weight='800' fill='#a05a3c'>1</text>
<text x='14' y='56' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Segurança</text>
<text x='14' y='76' %(F)s font-size='10.5' fill='#6c6a55'>refazer o plano para</text>
<text x='14' y='91' %(F)s font-size='10.5' fill='#6c6a55'>qualquer grau de ideação;</text>
<text x='14' y='106' %(F)s font-size='10.5' fill='#6c6a55'>treinar regulação fora</text>
<text x='14' y='121' %(F)s font-size='10.5' fill='#6c6a55'>da crise; caixa de</text>
<text x='14' y='136' %(F)s font-size='10.5' fill='#6c6a55'>regulação emocional</text>
<rect x='184' y='8' width='168' height='150' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='198' y='32' %(F)s font-size='22' font-weight='800' fill='#a8894f'>2</text>
<text x='198' y='56' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Postura</text>
<text x='198' y='76' %(F)s font-size='10.5' fill='#6c6a55'>aceitação e validação</text>
<text x='198' y='91' %(F)s font-size='10.5' fill='#6c6a55'>antes de resolver;</text>
<text x='198' y='106' %(F)s font-size='10.5' fill='#6c6a55'>não argumentar sobre o</text>
<text x='198' y='121' %(F)s font-size='10.5' fill='#6c6a55'>potencial dela; não sugerir</text>
<text x='198' y='136' %(F)s font-size='10.5' fill='#6c6a55'>o que ela já planeja</text>
<rect x='368' y='8' width='168' height='150' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='382' y='32' %(F)s font-size='22' font-weight='800' fill='#a8894f'>3</text>
<text x='382' y='56' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Contexto</text>
<text x='382' y='76' %(F)s font-size='10.5' fill='#6c6a55'>ler o trabalho pelos</text>
<text x='382' y='91' %(F)s font-size='10.5' fill='#6c6a55'>princípios da aceitação;</text>
<text x='382' y='106' %(F)s font-size='10.5' fill='#6c6a55'>mudanças pequenas e</text>
<text x='382' y='121' %(F)s font-size='10.5' fill='#6c6a55'>factíveis; ajustes de</text>
<text x='382' y='136' %(F)s font-size='10.5' fill='#6c6a55'>ambiente e de sono</text>
<rect x='552' y='8' width='168' height='150' rx='10' fill='#f1ece0' stroke='#d9d3c1' stroke-width='1.3' stroke-dasharray='5 4'/>
<text x='566' y='32' %(F)s font-size='22' font-weight='800' fill='#b9b39d'>4</text>
<text x='566' y='56' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Fica para depois</text>
<text x='566' y='76' %(F)s font-size='10.5' fill='#6c6a55'>mudanças comportamentais</text>
<text x='566' y='91' %(F)s font-size='10.5' fill='#6c6a55'>complexas, habilidades</text>
<text x='566' y='106' %(F)s font-size='10.5' fill='#6c6a55'>sociais, "aceitar o</text>
<text x='566' y='121' %(F)s font-size='10.5' fill='#6c6a55'>diagnóstico" como meta:</text>
<text x='566' y='136' %(F)s font-size='10.5' fill='#6c6a55'>quando houver força</text>
<rect x='0' y='176' width='720' height='44' rx='10' fill='#43441f'/>
<text x='360' y='194' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#f0ede0'>a ordem é de prioridade, e não de calendário</text>
<text x='360' y='211' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>1 e 2 acontecem na mesma sessão; 3 entra quando 2 estiver sustentado; 4 espera a paciente, e não a terapeuta</text>
</svg>
<figcaption>A supervisão pediu que os tópicos fossem organizados por prioridade. É esta a ordem.</figcaption></figure>""" % dict(F=F)

SUP_2109 = {
    'slug': 'aceitacao-antes-da-mudanca',
    'titulo_txt': 'Aceitação antes da mudança: diagnóstico recusado, identidade e plano de segurança',
    'titulo_html': 'Aceita&ccedil;&atilde;o antes da mudan&ccedil;a: diagn&oacute;stico recusado, identidade e plano de seguran&ccedil;a',
    'data': '21 de setembro de 2026',
    'meta': 'Supervisão de caso · Mediação de Prof. Júlio Gonçalves · Terapia Baseada em Processos',
    'meta_capa': '21/09/2026 &middot; SUPERVIS&Atilde;O DE CASO &middot; MEDIA&Ccedil;&Atilde;O DE PROF. J&Uacute;LIO GON&Ccedil;ALVES<br>'
                 'COMUNIDADE L&Oacute;GICA PSICOL&Oacute;GICA &middot; MATERIAL DESIDENTIFICADO',
    'header_dir': 'ACEITA&Ccedil;&Atilde;O ANTES DA MUDAN&Ccedil;A &middot; SUPERVIS&Atilde;O',
    'chave': 'mat-Sup-2026-09-21-',
    'arquivo': 'Sup-2026-09-21-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Antes de ler</h4>"
              u"<p>Este material discute o caso de uma <strong>adulta jovem com diagnóstico de transtorno bipolar, história de tentativa de suicídio e pensamentos de morte recorrentes</strong>. "
              u"O caso foi desidentificado: idades, datas, serviço de origem, medicamentos e doses, ocupações e composição familiar foram generalizados ou removidos.</p>"
              u"<p>A supervisão pediu duas coisas: reorganizar a segurança e mudar a postura, de resolver para aceitar. O texto de apoio enviado depois do encontro, "
              u"<strong>Aceitação, mudança e dialética</strong> (aula 5 do Descomplicando a DBT), está incorporado aqui numa seção própria, para que o material fique completo sem depender de outro link.</p></div>"),
    'tema': 'Uma paciente estabilizada que recusa o diagnóstico e transforma cada erro pequeno num veredito sobre quem ela é. '
            'A supervisão reorganizou a segurança e trocou a direção do tratamento: aceitar o contexto antes de tentar mudá-lo.',
    'essencial': [
        ('Segurança primeiro, e para qualquer grau de ideação.',
         'Os pensamentos de morte são passageiros e sem plano, mas recorrentes. O plano de segurança volta a ser refeito, e a regulação se treina fora da crise, não dentro dela.'),
        ('Aceitação antes da mudança.',
         'A paciente ainda não tem força emocional para mudanças complexas. Tentar resolver agora invalida; o tratamento prioriza acolher e validar o contexto.'),
        ('Argumentar sobre o potencial dela é reproduzir a avó.',
         'Insistir que ela é capaz, ou sugerir o que ela já planejava fazer, gera reatância: raiva e rejeição, no mesmo formato da invalidação que ela conhece de casa.'),
        ('O alvo não é o erro; é a exigência.',
         'Sem episódio algum, um erro comum no trabalho reativa pensamentos de morte. O que dispara a alça é a regra de normalidade e de alto rendimento.'),
        ('Impermanência, interexistência e um mundo completo.',
         'Não deixar o estado ruim virar o dia inteiro; cuidar do próprio esgotamento para não invalidar; ler os eventos pelas variáveis que os produziram, e não pela culpa.'),
        ('A regulação emocional ganha um objeto.',
         'Uma caixa com itens sensoriais, cartões terapêuticos e pequenos presentes de autocuidado, feita para o cuidado dela e não para o desempenho dela.'),
    ],
    'secoes': [
        ('s0', 'O caso, em uma página', 'O caso, em uma página', u"""
<p>Adulta jovem, atendida desde a adolescência, inicialmente num serviço público. Chegou com história de conflitos familiares graves: mãe ausente, avó rígida e depreciativa que a criou. Relatou pensamentos de morte e uma tentativa de suicídio anterior. Um psiquiatra fechou o diagnóstico de <strong>transtorno bipolar</strong>; o primeiro estabilizador foi suspenso por ela por causa dos efeitos colaterais.</p>
<h3>Quadro</h3>
<ul class='key'><li><b>Ciclagem</b>: períodos de cerca de uma semana com hipersexualidade, jornadas intensas de trabalho em mais de um lugar e insônia, alternados com fases depressivas.</li><li><b>Estabilização recente</b>, depois de ajuste medicamentoso (antipsicótico atípico e antidepressivo) e de um período difícil de acesso aos remédios e de custo de vida alto, quando saiu da casa da avó.</li><li><b>Recusa do diagnóstico</b>, com ruminação extrema sobre a própria identidade e cobrança rígida por um padrão de normalidade e alta produtividade.</li><li><b>Erros pequenos viram veredito</b>: mesmo estável, sem hipomania nem depressão, um erro cotidiano no trabalho reativa pensamentos de morte e sentimento de inadequação.</li><li><b>Sem rede funcional</b>: a avó invalida, a mãe transfere para ela as próprias sobrecargas.</li><li><b>Fadiga biofisiológica</b> pelos medicamentos, que alimenta o isolamento e o sofrimento atrelado à exigência de desempenho.</li><li><b>Apatia diante dos efeitos colaterais</b>, que a terapeuta trouxe como dúvida.</li></ul>
{{REDE}}
<div class='callout note'><div class='co-t'>Onde está o sofrimento agora</div>Não está nos episódios, que a medicação vem segurando. Está no intervalo entre eles: numa pessoa que se exige ser normal e produtiva, que não aceita o nome do que tem, e para quem qualquer falha comum confirma que ela não é o que deveria ser. O tratamento, neste momento, é sobre o intervalo.</div>
"""),
        ('s1', 'Prioridade 1: risco e plano de segurança', 'Prioridade 1: risco e plano de segurança', u"""
{{ORDEM}}
<p>A avaliação feita na supervisão: os pensamentos de morte ocorrem de forma <strong>passageira, depois de conflitos no trabalho, sem plano ativo estruturado</strong>. O que preocupa é a recorrência, somada à história de tentativa e à ausência de rede. Com esse perfil, a decisão foi consensual e vem antes de qualquer outra coisa.</p>
<ul class='key'><li><b>Refazer o plano de segurança</b> com a paciente, e aplicá-lo para <strong>qualquer grau de ideação</strong>, não só para os momentos de risco alto. O plano existente precisa ser reformulado com foco na regulação de crises.</li><li><b>Treinar habilidades de regulação fora da crise.</b> Um plano só funciona se as habilidades que ele lista já foram praticadas em dia calmo. O momento de aprender a regular não é o momento em que a paciente precisa regular.</li><li><b>Construir uma caixa de regulação emocional</b>: itens táteis, exercícios sensoriais de ancoragem, cartões com frases terapêuticas sobre o transtorno bipolar e pequenos presentes voltados ao autocuidado. O critério de escolha dos itens é explícito: <strong>cuidado, e não desempenho</strong>. Nada na caixa pode virar mais uma tarefa em que ela possa falhar.</li></ul>
<div class='obs'><h4>Por que a caixa importa neste caso</h4><p>Não é um recurso genérico. Para uma paciente cuja história é de invalidação e cujo sofrimento gira em torno de não render o suficiente, um objeto concreto montado pela terapeuta, com itens que dizem "isso é para tu te cuidar", faz duas coisas ao mesmo tempo: entrega uma ferramenta de regulação e modela, fora da fala, a postura de aceitação que a supervisão pediu. Os cartões sobre o transtorno entram como psicoeducação em dose pequena, que ela lê quando quiser, sem ninguém explicando.</p></div>
"""),
        ('s2', 'Prioridade 2: postura, reatância e validação', 'Prioridade 2: a postura, e o que a reatância ensina', u"""
<p>O segundo bloco da supervisão foi sobre a posição da terapeuta. A orientação: <strong>acolhimento compassivo e validação do sofrimento</strong>, evitando tentativas precipitadas de resolução de problemas, que neste caso invalidam.</p>
<h3>Reatância: o que não fazer</h3>
<p>Dois movimentos que parecem apoio e produzem o oposto. O primeiro é <strong>insistir em argumentos racionais sobre o potencial dela</strong> ("tu é capaz, tu tem tanta coisa boa"). O segundo é <strong>sugerir ações que ela já planejava</strong>. Os dois geram raiva e rejeição, e por um motivo preciso: <strong>se assemelham à postura da avó</strong>, que também dizia o que ela devia ser e fazer. A paciente não distingue, no calor, a boa intenção da terapeuta da cobrança de casa. O formato é o mesmo, e é o formato que dói.</p>
<p>O texto de apoio dá o nome: conselho diretivo, dado sem investigar a função do comportamento e sem validação prévia, ameaça a autonomia e ativa o modo opositor, e pesa mais em quem tem histórico de humilhação e invalidação. É exatamente este caso.</p>
<h3>O que fazer no lugar</h3>
<ul class='key'><li><b>Atenção plena no momento presente</b>: ficar com o que ela traz, na sessão, sem correr para o que fazer com aquilo.</li><li><b>Análise detalhada do contexto</b>: reconstruir o que aconteceu, hora a hora, antes de qualquer proposta. É o que revela as contingências reais e evita que a paciente use a resolução de problemas como <strong>esquiva emocional</strong> (planejar para não sentir).</li><li><b>Validar o sofrimento e a busca de apoio</b>, sem validar a regra de normalidade que o produz. O texto de apoio separa bem: valida-se o desejo e a função, o comportamento que serve a eles continua sendo alvo.</li><li><b>Trocar o "mas" pelo "e"</b>. "Entendo que foi difícil, mas..." apaga a validação. "Entendo que foi difícil, e..." preserva as duas coisas.</li></ul>
<div class='callout note'><div class='co-t'>Um teste simples para a sessão</div>Depois de cada fala da terapeuta, perguntar: isso saiu porque a paciente precisava ouvir, ou porque eu precisava dizer? A pressão por mudança rápida, lembra o texto de apoio, costuma vir do medo do terapeuta de ser julgado ou de não estar ajudando. Explicação em excesso funciona como ruminação ativa, só que em voz alta.</div>
"""),
        ('s3', 'Diagnóstico, identidade e dialética', 'Diagnóstico recusado, identidade e a psicoeducação dialética', u"""
<p>A paciente recusa o diagnóstico. A supervisão não tratou isso como problema a resolver, e sim como parte do quadro a acolher. O motivo está no que a recusa protege: se ela aceita "sou bipolar", na leitura dela, aceita que não é normal, e a exigência de normalidade é o eixo em torno do qual a ruminação sobre identidade gira. Confrontar a recusa é mexer nesse eixo sem ter onde apoiar.</p>
<p>O caminho definido foi a <strong>psicoeducação dialética</strong>: não a explicação do transtorno, e sim a apresentação de que <strong>duas coisas podem ser verdadeiras ao mesmo tempo</strong>. Ela pode ter um diagnóstico e ser competente. Pode ter errado no trabalho e não ser uma fraude. Pode estar cansada pelos remédios e ainda assim estar melhor do que há um ano. Nenhuma dessas frases pede que ela escolha um lado, e é isso que a diferencia da cobrança que ela conhece.</p>
<h3>Aceitação não é resignação</h3>
<p>Vale antecipar a leitura que a paciente provavelmente fará de "aceitar": desistir. O texto de apoio distingue: resignação toma o fato como imutável, segue julgando a realidade como errada e fecha o campo de ação; aceitação reconhece o fato e mantém abertura para a mudança possível, respeitando o contexto e as habilidades atuais. O teste não está no que a pessoa sente, e sim no que ela consegue fazer em seguida. Para esta paciente, aceitar o diagnóstico, quando chegar a hora, vai ser o que abre a possibilidade de negociar o trabalho, o sono e o descanso sem que cada um deles seja uma prova de fraqueza.</p>
<div class='obs'><h4>Por enquanto, nem essa palavra</h4><p>A decisão da supervisão foi explícita: neste momento, a terapeuta se abstém de mudanças comportamentais complexas e de treino de habilidades sociais, e prioriza a aceitação do contexto atual. "Aceitar o diagnóstico" não entra como meta. Entra, se entrar, como consequência de uma relação em que ela pôde ser bipolar sem ser diminuída.</p></div>
"""),
        ('s4', 'Os princípios aplicados ao caso', 'Três princípios da aceitação, aplicados ao caso', u"""
<p>A supervisão usou três dos cinco princípios da postura de aceitação que o texto de apoio apresenta (os outros dois, consciência do momento presente e desapego, apareceram na seção anterior).</p>
<h3>Impermanência</h3>
<p>Emoção e contexto mudam sozinhos. No caso, o uso é concreto: <strong>não deixar um estado emocional ruim se generalizar para o dia inteiro ou para a vida inteira</strong>. Quando o erro no trabalho vira "eu sou assim", a terapeuta pode reconstruir com ela as horas seguintes e mostrar, com o material dela, que o pico passou. O medo de que a melhora seja seguida de dor, lembra o texto, leva à resignação; tratar os altos e baixos como lombada evita que ela construa barreiras rígidas de evitação.</p>
<h3>Interexistência</h3>
<p>Comportamento da paciente e reação da terapeuta estão sob contingências mútuas, e a supervisão aplicou o princípio à própria terapeuta: <strong>cuidar para que o esgotamento profissional não gere ranço ou invalidação sutil</strong>. Cansaço, noite mal dormida e agenda inviável produzem impaciência, e a paciente lê impaciência como a avó. Daí a importância de o grupo de supervisão funcionar como consultoria, e de a terapeuta ter autocuidado como parte da conduta, e não como luxo.</p>
<h3>O mundo é completo como ele é</h3>
<p>O princípio mais difícil de transmitir, e a supervisão usou uma analogia trazida pelo grupo: um acidente de trânsito envolvendo uma criança e um caminhão. Ninguém escolheu aquele desfecho; ele resultou da convergência de muitas variáveis contextuais, boa parte delas incontroláveis. "Perfeito" aqui não é bom: é <strong>completo</strong>, totalmente explicado pelas condições que o produziram. Para a paciente, a aplicação é direta: o erro no trabalho, o diagnóstico, a família que ela teve, tudo isso aconteceu por variáveis que se juntaram, e a leitura por contingências <strong>elimina a culpa individual</strong> sem negar que doeu. O texto de apoio separa essa leitura da leitura moral: a negligência que ela viveu não deveria ter acontecido, e, dadas as condições daquele ambiente, aconteceu. O trabalho parte da realidade presente.</p>
"""),
        ('s5', 'Prioridade 3: contexto, trabalho e sono', 'Prioridade 3: contexto, trabalho, sono e efeitos colaterais', u"""
<p>Quando a postura estiver sustentada, entra o contexto, e a orientação foi de escala: <strong>ler o trabalho pelos princípios da aceitação e buscar pequenas mudanças factíveis</strong> que reduzam o sofrimento. Não é reorganizar a vida profissional; é encontrar, com ela, o que pode ficar um pouco menos custoso na semana que vem.</p>
<p>A dúvida da terapeuta sobre a <strong>apatia diante dos efeitos colaterais</strong> teve resposta na mesma escala: testar pequenos ajustes ambientais e de rotina de sono, e observar. Apatia num contexto de fadiga medicamentosa e exigência de rendimento pode ser cansaço, pode ser desesperança, pode ser a única forma de não brigar com mais uma coisa. Mudanças pequenas de ambiente mostram qual das três é, sem precisar perguntar.</p>
<div class='callout note'><div class='co-t'>Rede de apoio: a mesma regra de outras supervisões</div>A avó invalida e a mãe descarrega. A rede disponível não é rede segura, e a terapeuta não deve contar com ela no plano de segurança sem verificar, pessoa a pessoa, como cada uma reage quando a paciente está mal. Enquanto isso, o vínculo terapêutico é a rede, e o grupo da comunidade funciona como consultoria para a terapeuta não carregar isso sozinha.</div>
"""),
        ('s6', 'O texto de apoio', 'O texto de apoio: aceitação, mudança e dialética', u"""
<div class='obs'><h4>Sobre esta seção</h4><p>Resume o material enviado à terapeuta depois do encontro, a aula 5 do curso Descomplicando a DBT, no que ele acrescenta ao caso. Quem já leu o texto pode pular.</p></div>
<h3>A postura vem antes da técnica</h3>
<p>A prática costuma correr para avaliações extensas e intervenções imediatas, e essa pressa gera postura iatrogênica e invalidante. A DBT pede o contrário: postura ancorada no modelo biossocial, com aceitação antes da mudança. A aceitação é base transversal de todos os módulos, e não um módulo a mais. Protocolo aplicado sobre relação frágil produz efeito iatrogênico.</p>
<h3>Como o terapeuta invalida sem perceber</h3>
<p>Argumentação, moralização, desaprovação, estigma do diagnóstico, advertência de cima, ironia, análise na hora errada e a conjunção "mas". Falas afirmativas que julgam ou culpabilizam por faltas travam o avanço; o caminho é a pergunta aberta, que estimula curiosidade e autonomia e revela as contingências reais por trás do comportamento. Dois estilos foram contrastados: o afetuoso, receptivo e democrático, que trabalha por perguntas e devolve autonomia; e o diretivo, moralista e frio, que trabalha por cobrança. Um detalhe contraintuitivo: pacientes controladores costumam procurar terapeutas diretivos, e o arranjo mantém tudo como está.</p>
<h3>Validação</h3>
<p>A base é o silêncio atento e a escuta sem interrupção; relatos que parecem neutros carregam sofrimento implícito, que só aparece se houver espaço. Sobre nomear a emoção pelo paciente: abrir espaço para ele descrever as próprias sensações, e recorrer à formulação prévia só quando o repertório estiver limitado por desregulação forte. O que se valida e o que não se valida: o desejo de anestesiar a dor é legítimo e merece validação; o comportamento que anestesia continua sendo alvo.</p>
<h3>Os cinco princípios da postura</h3>
<ul class='key'><li><b>Consciência do momento presente</b>: atenção plena a cada palavra; o risco é o terapeuta apressar o alívio movido pela própria angústia. Suportar um minuto de sofrimento em ambiente controlado constrói tolerância; validar sem resgatar cedo demais.</li><li><b>Impermanência</b>: emoção e contexto mudam sozinhos; reconstruir a crise hora a hora mostra que o pico passou.</li><li><b>Interexistência</b>: comportamento do paciente e reação do terapeuta sob contingências mútuas; inclui a biofisiologia do terapeuta.</li><li><b>Desapego</b>: apego é exigir que a realidade fosse outra; alimenta ruminação, cansaço e comportamento desadaptado.</li><li><b>O mundo é perfeito como ele é</b>: perfeito no sentido de completo; os eventos ocorreram pela convergência das variáveis daquele contexto.</li></ul>
<h3>Aceitação radical: dois equívocos</h3>
<p>O primeiro é confundir aceitação radical com aprovar comportamento de risco: valida-se o contexto, a emoção e o sofrimento que impulsionam o ato, nunca o ato. O segundo é usar aceitação como autoindulgência ou como passividade diante da mudança. A ferramenta para sair da resignação são os dilemas dialéticos: nomear os dois polos e apostar em mudanças pequenas.</p>
<h3>Hierarquia de alvos e flexibilidade</h3>
<p>Comportamentos que ameaçam a vida vêm antes dos que interferem na terapia, que vêm antes dos que afetam a qualidade de vida, que vêm antes do aumento de habilidades. É essa hierarquia que explica a ordem de prioridades desta supervisão. E se um alvo prioritário reaparece, a solução em curso é interrompida; o tratamento volta para reajustar o compromisso e manejar a crise, e só depois retoma de onde parou.</p>
"""),
        ('s7', 'Lendo em processos', 'Lendo o caso em processos', u"""
<ul class='key'><li><b>Cognição</b>: regra de normalidade e alto rendimento; recusa do diagnóstico como proteção da identidade; ruminação. É o nó que transforma o erro em veredito.</li><li><b>Afeto</b>: pensamentos de morte como resposta a conflito e falha; vergonha e inadequação. Passageiros, mas com história de tentativa: o plano de segurança cobre isso.</li><li><b>Self</b>: "quem eu sou se tenho isso". A dialética (duas coisas verdadeiras) é a intervenção que não pede escolha.</li><li><b>Contexto social</b>: avó invalidante, mãe que descarrega, sem rede. A terapeuta é, por ora, o único contexto validante, e por isso a reatância custa tanto.</li><li><b>Biofisiologia</b>: fadiga medicamentosa, sono, custo de viver sozinha. Abaixa o limiar da alça e é o primeiro lugar para pequenas mudanças.</li><li><b>Alça de manutenção</b>: erro, exigência, pensamento de morte, isolamento, mais exigência. O ponto de entrada é a validação da exigência como sofrimento (e não como meta), enquanto a segurança segura o lado do afeto.</li></ul>
<p>O que fica para a clínica: quando o paciente não tem força para mudar, a intervenção é a postura. Aceitar o contexto não é esperar; é fazer, na relação, o que a rede dele não faz, e é disso que a mudança vai depender depois.</p>
"""),
    ],
    'checklist': [
        'Refiz o plano de segurança para qualquer grau de ideação, e não só para risco alto.',
        'Treinei as habilidades de regulação do plano em sessão calma, antes de precisar delas.',
        'Montei ou propus um objeto concreto de regulação, escolhendo os itens pelo cuidado e não pelo desempenho.',
        'Evitei argumentar sobre o potencial do paciente e sugerir o que ele já planejava.',
        'Contei quantas vezes usei "mas" depois de uma validação, e troquei por "e".',
        'Reconstruí um episódio hora a hora antes de propor qualquer coisa.',
        'Apresentei duas verdades ao mesmo tempo (diagnóstico e competência) em vez de pedir que o paciente aceite o diagnóstico.',
        'Verifiquei meu próprio cansaço e o que ele faz com a sessão.',
        'Busquei pequenas mudanças factíveis de contexto e de sono, e observei antes de ampliar.',
        'Chequei se a rede de apoio disponível é segura antes de contar com ela.',
    ],
    'questoes': [
        'O paciente diz que errou no trabalho e que "não adianta, eu sou assim mesmo". O que tu valida, o que tu não valida, e o que tu faz em seguida?',
        'Por que insistir no potencial de uma paciente com história de invalidação pode produzir raiva e rejeição? O que fazer no lugar?',
        'Qual é a diferença entre "aceitar o diagnóstico" como meta e a psicoeducação dialética que a supervisão propôs?',
        'Como tu aplicaria a impermanência a um paciente que generaliza um erro pequeno para a vida inteira?',
        'O que muda no manejo quando os pensamentos de morte são passageiros e sem plano, mas há tentativa prévia e recorrência?',
        'Que itens tu colocaria numa caixa de regulação emocional para um paciente teu, e pelo que tu os escolheria?',
        'Em que princípio da postura de aceitação tu escorrega mais, e o que o teu cansaço faz com a sessão?',
    ],
    'gabarito': {
     0: (K, u"Não há resposta certa. Uma boa resposta valida o sofrimento e a exigência como dor (\"errar te custa muito, e dá para ver de onde vem\"), não valida a conclusão (\"eu sou assim mesmo\") nem a regra de que errar prova alguma coisa, e em seguida <b>reconstrói o episódio hora a hora</b>, em vez de discordar ou tranquilizar. O erro comum é responder à conclusão com argumento (\"mas tu é ótima\"), que é a reatância descrita no material."),
     1: (K, u"Não há resposta certa. Uma boa resposta reconhece que o argumento sobre o potencial repete o <b>formato</b> da invalidação de origem (alguém dizendo o que ela deve ser), ativa o modo opositor e ameaça a autonomia, e propõe no lugar atenção ao momento presente, análise detalhada do contexto e validação prévia a qualquer proposta, pedindo permissão antes de sugerir."),
     2: (C, u"Como meta, \"aceitar o diagnóstico\" pede que a paciente escolha um lado (sou bipolar, logo não sou normal), e é isso que ela recusa. A psicoeducação dialética apresenta duas coisas verdadeiras ao mesmo tempo (tem um diagnóstico e é competente; errou e não é uma fraude), sem pedir escolha. A aceitação do diagnóstico, se vier, vem como consequência de uma relação em que ela pôde ter o transtorno sem ser diminuída."),
     3: (K, u"Não há resposta certa. Uma boa resposta usa o material do paciente: reconstrói as horas depois do erro e mostra que o estado passou, nomeia a generalização (\"o erro virou o dia, e o dia virou a vida\") e trata os altos e baixos como lombada, e não como prova. O erro comum é afirmar a impermanência em abstrato, o que o paciente aceita e continua generalizando."),
     4: (C, u"Muda a régua: o plano de segurança passa a valer para <b>qualquer grau de ideação</b>, e não só para risco alto; as habilidades de regulação são treinadas fora da crise; e a recorrência, mais a tentativa prévia e a ausência de rede, faz da avaliação de risco um item permanente da sessão, revisado nos momentos de conflito e falha, que são os gatilhos conhecidos."),
     5: (K, u"Não há resposta certa. Uma boa resposta lista itens concretos (táteis, de ancoragem sensorial, cartões com frases curtas, algo pequeno de autocuidado) e explicita o critério: <b>cuidado e não desempenho</b>, nada que possa virar tarefa em que o paciente falhe, e itens que modelem a postura de aceitação sem precisar de explicação."),
     6: (K, u"Não há resposta certa, e a pergunta é pessoal. Uma boa resposta nomeia um princípio (apressar o alívio por angústia própria, brigar com o fato passado, deixar o cansaço virar impaciência) e descreve o efeito concreto na sessão. O erro comum é responder \"nenhum\"."),
    },
    'referencias': [
        "Brehm, J. W. (1966). <em>A theory of psychological reactance.</em> Academic Press.",
        "Hayes, S. C., Hofmann, S. G., &amp; Ciarrochi, J. (2020). A process-based approach to psychological diagnosis and treatment. <em>Clinical Psychology Review, 82</em>, 101908.",
        "Linehan, M. M. (1993). <em>Cognitive-behavioral treatment of borderline personality disorder.</em> Guilford Press.",
        "Linehan, M. M. (2015). <em>DBT skills training manual</em> (2ª ed.). Guilford Press.",
        "Miller, W. R., &amp; Rollnick, S. (2013). <em>Motivational interviewing: Helping people change</em> (3ª ed.). Guilford Press.",
        "Stanley, B., &amp; Brown, G. K. (2012). Safety planning intervention: A brief intervention to mitigate suicide risk. <em>Cognitive and Behavioral Practice, 19</em>(2), 256–264.",
        "Swenson, C. R. (2016). <em>DBT principles in action: Acceptance, change, and dialectics.</em> Guilford Press. Edição brasileira: <em>Terapia comportamental dialética em ação.</em>",
        "Gonçalves, J. (2026). Aula 05: Aceitação, mudança e dialética. Curso Descomplicando a DBT. Texto de apoio enviado à supervisionanda.",
    ],
    'nota': u"""Material de estudo desidentificado. Foram generalizados ou removidos: idades, datas, serviço de origem, nomes e doses dos medicamentos, ocupações, composição familiar detalhada e circunstâncias específicas. A tentativa de suicídio anterior e os pensamentos de morte são referidos pela ocorrência, sem descrição. A supervisionanda e os demais participantes não são identificados.<br><br><strong>Fonte.</strong> O texto foi escrito a partir das anotações do encontro. Duas fontes se somam a elas: o texto de apoio enviado à terapeuta depois da supervisão (aula 5 do Descomplicando a DBT, resumido na seção própria e citado nas demais quando acrescenta ao caso) e a leitura em processos, desenvolvida pelo autor do material. A organização em prioridades foi pedida na própria supervisão.<br><br><strong>Plano de segurança e caixa de regulação.</strong> Descritos em nível geral, adequado à leitura profissional, sem detalhamento operacional e sem técnicas que envolvam desconforto físico. O material registra raciocínio clínico de supervisão e <strong>não substitui</strong> avaliação individualizada de risco.<br><br><strong>Sobre a analogia do acidente.</strong> Foi usada em sala para ilustrar o princípio da completude dos eventos e aparece aqui com a mesma função; não é um caso.<br><br>As referências sobre reatância, plano de segurança, validação e os princípios da postura foram acrescentadas para dar respaldo ao que a discussão afirmou sem citação. Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'REDE': REDE, 'ORDEM': ORDEM}
SUP_2109['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                      for sid, nav, tit, corpo in SUP_2109['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/supervisoes/subjugacao-violencia/index.html', encoding='utf-8').read()
    dest = SITE + '/supervisoes/' + SUP_2109['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(sup_common.pagina(SUP_2109, base))
    c = sup_common.pdf(SUP_2109)
    c['gabarito'] = SUP_2109['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
