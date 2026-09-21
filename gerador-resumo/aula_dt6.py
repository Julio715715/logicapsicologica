# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 6: Critérios diagnósticos do transtorno do jogo. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

NOVE = u"""<figure class='dg'><div class='dg-t'>Nove critérios, quatro famílias</div>
<svg viewBox='0 0 720 250' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Os nove critérios do DSM-5-TR para transtorno do jogo agrupados em quatro famílias: dependência, controle e função, caça e ocultação, dano'>
<rect x='0' y='6' width='172' height='170' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='12' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a8894f'>PARECE SUBST&Acirc;NCIA</text>
<text x='12' y='58' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>1</tspan> tolerância: precisa</text>
<text x='12' y='73' %(F)s font-size='11' fill='#2f2e24'>apostar mais para sentir</text>
<text x='12' y='88' %(F)s font-size='11' fill='#2f2e24'>a mesma excitação</text>
<text x='12' y='114' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>2</tspan> abstinência: inquieto</text>
<text x='12' y='129' %(F)s font-size='11' fill='#2f2e24'>ou irritado ao tentar</text>
<text x='12' y='144' %(F)s font-size='11' fill='#2f2e24'>reduzir ou parar</text>
<rect x='182' y='6' width='172' height='170' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='194' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a8894f'>CONTROLE E FUN&Ccedil;&Atilde;O</text>
<text x='194' y='58' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>3</tspan> esforços repetidos e</text>
<text x='194' y='73' %(F)s font-size='11' fill='#2f2e24'>malsucedidos de controlar</text>
<text x='194' y='99' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>4</tspan> preocupação frequente</text>
<text x='194' y='114' %(F)s font-size='11' fill='#2f2e24'>com o jogo</text>
<text x='194' y='140' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>5</tspan> joga quando se sente</text>
<text x='194' y='155' %(F)s font-size='11' fill='#2f2e24'>angustiado</text>
<rect x='364' y='6' width='172' height='170' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='376' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>CA&Ccedil;A E OCULTA&Ccedil;&Atilde;O</text>
<text x='376' y='58' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>6</tspan> depois de perder, volta</text>
<text x='376' y='73' %(F)s font-size='11' fill='#2f2e24'>outro dia para ficar quite</text>
<text x='376' y='88' %(F)s font-size='11' fill='#2f2e24'>(chasing)</text>
<text x='376' y='114' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>7</tspan> mente para esconder</text>
<text x='376' y='129' %(F)s font-size='11' fill='#2f2e24'>a extensão do</text>
<text x='376' y='144' %(F)s font-size='11' fill='#2f2e24'>envolvimento</text>
<rect x='546' y='6' width='174' height='170' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='558' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a8894f'>DANO</text>
<text x='558' y='58' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>8</tspan> prejudicou ou perdeu</text>
<text x='558' y='73' %(F)s font-size='11' fill='#2f2e24'>relação, emprego ou</text>
<text x='558' y='88' %(F)s font-size='11' fill='#2f2e24'>oportunidade</text>
<text x='558' y='114' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>9</tspan> depende de outros para</text>
<text x='558' y='129' %(F)s font-size='11' fill='#2f2e24'>saldar dívidas</text>
<text x='558' y='144' %(F)s font-size='11' fill='#2f2e24'>desesperadoras do jogo</text>
<rect x='120' y='194' width='480' height='48' rx='10' fill='#43441f'/>
<text x='360' y='214' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#f0ede0'>4 ou mais, em 12 meses, com sofrimento ou prejuízo</text>
<text x='360' y='232' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>e não explicado por episódio maníaco (critério B)</text>
</svg>
<figcaption>Os critérios 1 e 2 são os que aproximam o jogo das substâncias; 6 e 7 são os mais frequentes; 8 e 9 são os menos frequentes e marcam a forma grave.</figcaption></figure>""" % dict(F=F)

CICLO = u"""<figure class='dg'><div class='dg-t'>O ciclo sucessivo de feedback</div>
<svg viewBox='0 0 720 236' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Seis etapas em ciclo: precipitantes, cognições, comportamento, reforço, consequência, emoções negativas reativas, que voltam aos precipitantes'>
<defs><marker id='cf' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='10' width='150' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='12' y='32' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Precipitantes</text>
<text x='12' y='52' %(F)s font-size='10.5' fill='#6c6a55'>tédio, estresse,</text>
<text x='12' y='67' %(F)s font-size='10.5' fill='#6c6a55'>briga familiar</text>
<path d='M154 56 L178 56' stroke='#8d876f' stroke-width='2' marker-end='url(#cf)'/>
<rect x='182' y='10' width='170' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='194' y='32' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Cognições</text>
<text x='194' y='52' %(F)s font-size='10.5' fill='#6c6a55'>"só vou jogar 10 min",</text>
<text x='194' y='67' %(F)s font-size='10.5' fill='#6c6a55'>"preciso checar o que</text>
<text x='194' y='82' %(F)s font-size='10.5' fill='#6c6a55'>estão dizendo"</text>
<path d='M356 56 L380 56' stroke='#8d876f' stroke-width='2' marker-end='url(#cf)'/>
<rect x='384' y='10' width='150' height='92' rx='10' fill='#43441f'/>
<text x='396' y='32' %(F)s font-size='11' font-weight='800' fill='#f0ede0'>Comportamento</text>
<text x='396' y='52' %(F)s font-size='10.5' fill='#9ca575'>horas de jogo,</text>
<text x='396' y='67' %(F)s font-size='10.5' fill='#9ca575'>apostas, verificação</text>
<path d='M538 56 L562 56' stroke='#8d876f' stroke-width='2' marker-end='url(#cf)'/>
<rect x='566' y='10' width='154' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='578' y='32' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Reforço</text>
<text x='578' y='52' %(F)s font-size='10.5' fill='#6c6a55'>prazer ou alívio:</text>
<text x='578' y='67' %(F)s font-size='10.5' fill='#6c6a55'>sensação de controle,</text>
<text x='578' y='82' %(F)s font-size='10.5' fill='#6c6a55'>distração dos problemas</text>
<path d='M643 106 L643 130' stroke='#8d876f' stroke-width='2' marker-end='url(#cf)'/>
<rect x='566' y='134' width='154' height='92' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.3'/>
<text x='578' y='156' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Consequência</text>
<text x='578' y='176' %(F)s font-size='10.5' fill='#6c6a55'>culpa, perda de tempo,</text>
<text x='578' y='191' %(F)s font-size='10.5' fill='#6c6a55'>insônia, isolamento</text>
<path d='M562 180 L538 180' stroke='#8d876f' stroke-width='2' marker-end='url(#cf)'/>
<rect x='364' y='134' width='170' height='92' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.3'/>
<text x='376' y='156' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Emoções negativas</text>
<text x='376' y='176' %(F)s font-size='10.5' fill='#6c6a55'>reativas: tristeza,</text>
<text x='376' y='191' %(F)s font-size='10.5' fill='#6c6a55'>frustração, vergonha</text>
<path d='M360 180 L200 180 L200 130 L75 130 L75 108' fill='none' stroke='#8d876f' stroke-width='2' stroke-dasharray='5 4' marker-end='url(#cf)'/>
<text x='215' y='170' %(F)s font-size='10.5' font-style='italic' fill='#8d876f'>viram o próximo precipitante</text>
</svg>
<figcaption>O ciclo dos slides, redesenhado. As emoções da última etapa são o material da primeira: a vergonha de ontem é o precipitante de hoje.</figcaption></figure>""" % dict(F=F)

GRAV = u"""<figure class='dg'><div class='dg-t'>Gravidade e curso: o que especificar</div>
<svg viewBox='0 0 720 214' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Três faixas de gravidade por número de critérios e quatro especificadores de curso'>
<rect x='0' y='8' width='226' height='78' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='12' y='30' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Leve · 4 ou 5 critérios</text>
<text x='12' y='50' %(F)s font-size='10.5' fill='#6c6a55'>em geral preocupação com o</text>
<text x='12' y='65' %(F)s font-size='10.5' fill='#6c6a55'>jogo e tentar recuperar perdas</text>
<rect x='247' y='8' width='226' height='78' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='259' y='30' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Moderada · 6 ou 7 critérios</text>
<rect x='494' y='8' width='226' height='78' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='506' y='30' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Grave · 8 ou 9 critérios</text>
<text x='506' y='50' %(F)s font-size='10.5' fill='#6c6a55'>perder relações ou oportunidades</text>
<text x='506' y='65' %(F)s font-size='10.5' fill='#6c6a55'>e depender de outros para pagar</text>
<line x1='0' y1='104' x2='720' y2='104' stroke='#d9d3c1' stroke-width='1'/>
<text x='0' y='126' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a8894f'>CURSO</text>
<text x='0' y='148' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>Episódico</tspan>: preencheu os critérios mais de uma vez, com os sintomas cedendo por vários meses entre os períodos.</text>
<text x='0' y='168' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>Persistente</tspan>: sintomas contínuos, preenchendo os critérios por vários anos.</text>
<text x='0' y='188' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>Remissão inicial</tspan>: nenhum critério preenchido por 3 meses ou mais, e menos de 12.</text>
<text x='0' y='208' %(F)s font-size='11' fill='#2f2e24'><tspan font-weight='800'>Remissão sustentada</tspan>: nenhum critério preenchido por 12 meses ou mais.</text>
</svg>
<figcaption>A contagem de critérios dá a gravidade; o calendário dá o curso. Os dois entram no diagnóstico.</figcaption></figure>""" % dict(F=F)

DT6 = {
    'slug': 'aula6',
    'titulo_txt': 'Critérios diagnósticos do transtorno do jogo: os nove sinais, o ciclo e o que especificar',
    'titulo_html': 'Crit&eacute;rios diagn&oacute;sticos do transtorno do jogo: os nove sinais, o ciclo e o que especificar',
    'data': 'Vídeo 6',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 6',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 6 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 6',
    'chave': 'mat-Aula-DT6-',
    'arquivo': 'Aula-DT6-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do sexto vídeo da "
              u"disciplina, sobre os critérios diagnósticos do transtorno do jogo no DSM-5-TR. Não havia transcrição.</p>"
              u"<p>Os slides mostram os critérios 3 a 9 por extenso; os critérios 1 e 2 foram completados a partir do manual. "
              u"Duas moderações e um aviso sobre fontes estão sinalizados no texto e na nota de método.</p></div>"),
    'tema': 'Os nove critérios do DSM-5-TR e a regra dos quatro em doze meses, o ciclo que mantém o jogo, gravidade e curso, '
            'dois perfis de jogador, quem adoece e quando, e o que ainda está em disputa no diagnóstico.',
    'essencial': [
        ('Quatro de nove, em doze meses, com sofrimento ou prejuízo.',
         'Essa é a regra do critério A. O critério B exclui o que o episódio maníaco explica melhor.'),
        ('Os nove se agrupam em quatro famílias.',
         'Tolerância e abstinência; controle, preocupação e função; chasing e mentira; dano e resgate financeiro. Ajuda a lembrar e a perguntar.'),
        ('Os mais frequentes são preocupação e chasing; os menos frequentes marcam a forma grave.',
         'Perder relação ou emprego e depender de outros para pagar dívidas aparecem mais nos casos de 8 ou 9 critérios.'),
        ('Contar critérios dá a gravidade; o calendário dá o curso.',
         'Leve, moderada, grave. Episódico ou persistente. Remissão inicial de 3 a 12 meses; sustentada a partir de 12.'),
        ('O ciclo é o que se trata.',
         'Precipitante, cognição permissiva, comportamento, reforço, consequência, emoção negativa, que vira o próximo precipitante.'),
        ('Dois jogadores, duas funções.',
         'O deprimido joga para não sentir; o ansioso e impulsivo joga para sentir. A pergunta pelo risco de suicídio é obrigatória nos dois.'),
    ],
    'secoes': [
        ('s0', 'Critério A: os nove sinais', 'Critério A: os nove sinais', u"""
{{NOVE}}
<p>O DSM-5-TR define o transtorno do jogo como <strong>comportamento de jogo problemático persistente e recorrente</strong>, que leva a sofrimento ou comprometimento clinicamente significativo, indicado pela presença de <strong>quatro ou mais</strong> dos nove critérios num período de <strong>doze meses</strong>. Os slides mostram os critérios 3 a 9 por extenso; os dois primeiros estão completados aqui a partir do manual, porque sem eles a lista não fecha.</p>
<ul class='key'><li><b>1. Tolerância</b>: necessidade de apostar quantias crescentes de dinheiro para alcançar a excitação desejada.</li><li><b>2. Abstinência</b>: inquietação ou irritabilidade quando tenta reduzir ou parar de jogar.</li><li><b>3.</b> Fez esforços repetidos e <b>malsucedidos</b> no sentido de controlar, reduzir ou interromper.</li><li><b>4.</b> <b>Preocupação</b> frequente com o jogo: reviver experiências passadas, planejar a próxima, pensar em como conseguir dinheiro.</li><li><b>5.</b> Frequentemente joga quando se sente <b>angustiado</b> (impotência, culpa, ansiedade, depressão).</li><li><b>6.</b> Após perder dinheiro, frequentemente volta outro dia <b>para ficar quite</b>. É o chasing do vídeo 5.</li><li><b>7.</b> <b>Mente</b> para esconder a extensão do seu envolvimento com o jogo.</li><li><b>8.</b> Prejudicou ou <b>perdeu um relacionamento significativo</b>, o emprego ou uma oportunidade educacional ou profissional em razão do jogo.</li><li><b>9.</b> <b>Depende de outras pessoas</b> para obter dinheiro a fim de saldar situações financeiras desesperadoras causadas pelo jogo.</li></ul>
<h3>As quatro famílias</h3>
<p>Vale ler os nove em quatro grupos, porque é assim que eles se perguntam. Os critérios 1 e 2 são os que <strong>aproximam o jogo das substâncias</strong>: tolerância e abstinência, sem droga nenhuma. Foi por causa deles que o DSM-5 tirou o jogo patológico do capítulo de controle dos impulsos e o colocou junto das dependências. Os critérios 3, 4 e 5 descrevem <strong>controle e função</strong>: a pessoa não consegue parar, pensa no jogo o tempo todo e joga para regular o que sente. Os critérios 6 e 7 são a <strong>caça e a ocultação</strong>, o par que mais aparece na prática. E os critérios 8 e 9 são o <strong>dano</strong>, os menos frequentes e os que marcam a forma grave.</p>
<div class='obs'><h4>O que o slide comenta sobre o critério 5</h4><p>O slide observa que os estudos apontam relação estreita entre disfunção executiva e certos perfis de personalidade e o transtorno do jogo, o que abre espaço para investigar níveis de suscetibilidade. Na prática, é o aviso de que jogar quando angustiado não é só um sintoma a contar: é uma pista sobre quanto a pessoa dispõe de outras formas de regulação. As duas citações do slide (Moreira, 2004; Dash, 2019) não puderam ser conferidas e por isso não estão nas referências.</p></div>
"""),
        ('s1', 'Tolerância: o gráfico da dopamina', 'Tolerância: o gráfico da dopamina', u"""
<p>Para explicar o critério 1, o vídeo usa um esquema de <strong>taxa dopaminérgica basal</strong> diante de estímulos naturais. A cada ciclo de estímulo (1, 2, 3, 4), o pico sobe mais alto e a linha de base desce mais fundo. A leitura é a da tolerância: precisa de mais para sentir o mesmo, e entre um pico e outro a pessoa fica abaixo de onde estava antes de começar. O slide liga isso diretamente ao humor: em adolescentes, problemas externalizantes (comportamento antissocial, controle da raiva) e internalizantes (sofrimento emocional, baixa autoestima); em adultos, mais sintomas depressivos e ansiosos.</p>
<div class='obs'><h4>Uma moderação</h4><p>O gráfico é um esquema didático, e vale apresentá-lo como tal. Para substâncias, a regulação para baixo dos receptores dopaminérgicos com uso repetido está bem documentada. Para o jogo, o que existe é evidência de alteração na resposta do sistema de recompensa, com achados que vão em mais de uma direção, e não uma curva tão limpa quanto a do slide. O que a clínica sustenta sem dúvida é o fenômeno comportamental: aumento progressivo das quantias apostadas e mal-estar quando reduz. É por ele que o critério se preenche, e não pelo mecanismo.</p></div>
"""),
        ('s2', 'O ciclo que mantém o jogo', 'O ciclo que mantém o jogo', u"""
{{CICLO}}
<p>O slide seguinte desenha o <strong>ciclo sucessivo de feedback</strong>, e é a peça mais útil do vídeo para quem vai tratar. Seis etapas: <strong>precipitantes</strong> (tédio, estresse, briga familiar); <strong>cognições</strong> permissivas ("só vou jogar dez minutos", "preciso checar o que estão dizendo"); o <strong>comportamento</strong> (horas de jogo, apostas, verificação); o <strong>reforço</strong>, prazer ou alívio, com sensação de controle e distração dos problemas; as <strong>consequências</strong> (culpa, perda de tempo, insônia, isolamento); e as <strong>emoções negativas reativas</strong> (tristeza, frustração, vergonha), que fecham o ciclo virando o próximo precipitante.</p>
<p>O texto do slide acrescenta o que sustenta o ciclo: as <strong>estratégias compensatórias</strong> baseadas na crença "não posso perder, senão terei falhado" ou "não posso demonstrar que dependo disso". A manutenção do ciclo gera consequências punitivas, e em adolescentes o risco de insucesso acadêmico, reprovação ou abandono escolar, problemas psicossociais e de sono é maior.</p>
<div class='callout note'><div class='co-t'>Onde entrar</div>Cada etapa é um ponto de entrada possível, e a escolha depende do paciente. A cognição permissiva é a entrada mais rápida (pegar o "só dez minutos" no ato). O reforço é a entrada mais durável (encontrar outra fonte de controle e de distração, ou tratar o problema do qual ele se distrai). A emoção reativa é a entrada que evita a recaída (o que fazer com a vergonha de ontem para que ela não vire a aposta de hoje). O erro comum é tratar só o comportamento, que é a única etapa que o ciclo repõe sozinho.</div>
"""),
        ('s3', 'Critério B, gravidade e curso', 'Critério B, gravidade e curso', u"""
{{GRAV}}
<p>O <strong>critério B</strong> é uma exclusão: o comportamento de jogo não é mais bem explicado por um episódio maníaco. Em mania, apostar entra num quadro de expansividade, impulsividade e gasto excessivo que se resolve com o episódio; não é transtorno do jogo. Vale perguntar por outros sinais de mania sempre que o jogo aparece em surtos.</p>
<h3>Gravidade, pela contagem</h3>
<p><strong>Leve</strong>, com 4 ou 5 critérios: os preenchidos com maior frequência costumam ser a preocupação com o jogo e a tentativa de recuperar as perdas. <strong>Moderada</strong>, com 6 ou 7. <strong>Grave</strong>, com 8 ou 9: colocar em risco relacionamentos ou oportunidades profissionais e depender de outros para cobrir as perdas são os critérios menos frequentes e aparecem mais entre pessoas com a forma mais grave.</p>
<h3>Curso, pelo calendário</h3>
<p>O slide usa um calendário de doze meses para mostrar os quatro especificadores. <strong>Episódico</strong>: satisfaz os critérios mais de uma vez, com os sintomas cedendo entre os períodos por no mínimo vários meses. <strong>Persistente</strong>: sintomas contínuos, satisfazendo os critérios por vários anos. <strong>Em remissão inicial</strong>: depois do diagnóstico, nenhum critério preenchido por pelo menos 3 meses e menos de 12. <strong>Em remissão sustentada</strong>: nenhum critério preenchido por 12 meses ou mais.</p>
<div class='obs'><h4>Por que registrar o curso</h4><p>O especificador de remissão obriga a acompanhar o paciente com a lista na mão, mês a mês, e não só pela sensação de melhora. E o episódico avisa: um período bom de vários meses não é alta. É intervalo.</p></div>
"""),
        ('s4', 'Dois perfis e o risco', 'Dois perfis de jogador, e o risco que não se pergunta sozinho', u"""
<p>O vídeo descreve dois perfis, que o DSM-5-TR traz na seção de características associadas e que a literatura de caminhos para o jogo problemático também reconhece.</p>
<ul class='key'><li><b>Deprimidos</b>: indivíduos deprimidos e solitários, que podem jogar quando se sentem impotentes, culpados ou deprimidos. Jogam <strong>para não sentir</strong>.</li><li><b>Ansiosos</b>: indivíduos impulsivos, competitivos, cheios de energia, inquietos, que se entediam com facilidade; podem se mostrar preocupados com a aprovação dos outros e generosos a ponto da extravagância quando ganham. Jogam <strong>para sentir</strong>.</li></ul>
<p>A distinção importa porque a função é oposta, e o tratamento que serve a um não serve ao outro: o primeiro precisa de outra forma de regular o afeto negativo; o segundo, de outra fonte de estimulação e de um freio.</p>
<h3>O dado que obriga a perguntar</h3>
<p>O slide traz o número do manual: <strong>até metade</strong> das pessoas em tratamento para transtorno do jogo tem ideação suicida, e cerca de <strong>17%</strong> tentaram suicídio. É uma taxa alta o suficiente para tornar a avaliação de risco parte obrigatória da primeira entrevista de qualquer paciente com jogo problemático, e para repeti-la nos momentos de perda grande, de descoberta pela família e de dívida que estoura. Não é um item para quando o paciente trouxer.</p>
"""),
        ('s5', 'Quem adoece e quando', 'Quem adoece, quando, e em que contexto', u"""
<h3>O curso ao longo da vida</h3>
<p>O gráfico do slide mostra o investimento em jogo (tempo, dinheiro) por faixa etária, para homens e mulheres, com pico entre os 26 e os 35 anos e queda depois. As anotações resumem o que muda em cada fase:</p>
<ul class='key'><li><b>Início precoce</b> (até os 15): baixa competência social, desregulação emocional, não participa de esportes, joga para regular emoções. Taxas mais elevadas entre crianças e adolescentes, forte base genética. Podem melhorar, mas com maior tendência à recaída.</li><li><b>Fase de pico</b>: um ou dois jogos concentram o problema; fica intenso em fases estressantes. Progressão lenta, com aumento gradual dos investimentos; mulheres têm um leve pico de progressão a mais que homens.</li><li><b>Início tardio</b>: comum em mulheres, com curso mais curto. Mulheres buscam tratamento com mais frequência que homens jovens. Transtorno depressivo maior, bipolar e ansiedade são mais comuns entre mulheres; personalidade antissocial e uso de substâncias, entre homens.</li></ul>
<div class='callout note'><div class='co-t'>Um aviso sobre as fontes desse gráfico</div>As anotações do slide misturam duas literaturas: a do transtorno do jogo, que é o tema do vídeo, e a do transtorno de jogos pela internet (as horas médias por dia e a menção a gêneros de jogo vêm da segunda). As fontes citadas no slide (APA, 2013; Wichstrøm et al., 2016; Rehbein et al., 2019) não puderam ser conferidas neste material e por isso não estão nas referências. O desenho geral do curso, com pico no adulto jovem, início precoce mais grave e início tardio feminino, coincide com o que o DSM-5-TR descreve.</div>
<h3>Cultura e gênero</h3>
<p>A tabela do slide reproduz a seção de questões diagnósticas do manual. Há atividades de jogo <strong>específicas de certas culturas</strong> (dominós, rinhas de galo, corridas de cavalo); nos Estados Unidos, as taxas de prevalência são mais altas entre afro-americanos do que entre americanos de origem europeia, semelhantes entre hispano-americanos, e altas em populações indígenas. Homens desenvolvem o transtorno em taxas mais elevadas e tendem a apostar em cartas, esportes e corridas; mulheres tendem a preferir caça-níqueis e bingo. Jogos via internet ou videogame são mais comuns em RPG, tiros, simulação e habilidades cognitivas (aqui, de novo, o slide cruza para o transtorno de jogos).</p>
<p>Para a clínica brasileira, a lição da tabela não são os números norte-americanos, e sim a pergunta: <strong>qual é o jogo</strong> deste paciente, em qual contexto cultural ele acontece, e o que é normativo ali. A resposta muda a avaliação e muda o que se pode pedir que ele deixe.</p>
<h3>Consequências funcionais</h3>
<p>Colocar em risco ou perder relacionamentos importantes; problemas gerados por mentiras e empréstimos; impacto no emprego ou nos estudos, por absenteísmo ou baixo desempenho; saúde geral debilitada, com uso elevado de serviços médicos. Em termos de comorbidades, o manual lista taquicardia e angina, transtornos por uso de substâncias, depressivos, de ansiedade e da personalidade.</p>
"""),
        ('s6', 'Aspectos controversos', 'Aspectos controversos no diagnóstico', u"""
<p>O vídeo fecha com quatro pontos em disputa, e eles servem de ponte para o resto da disciplina, porque valem mais para as dependências tecnológicas em geral do que para o jogo de azar em particular.</p>
<ul class='key'><li><b>Generalização diagnóstica</b>: há risco de patologizar comportamentos normativos, especialmente em populações jovens com alta exposição digital.</li><li><b>Tempo versus prejuízo funcional</b>: há quem defenda que a quantidade de tempo não deve ser critério primário; o foco deve ser prejuízo e compulsividade. É a posição que o vídeo 3 já tinha adotado.</li><li><b>Diferenças culturais e contextuais</b>: o que é problemático num país pode não ser em outro. O exemplo do slide são os profissionais de e-sports, para quem horas de jogo são trabalho.</li><li><b>Outros comportamentos digitais problemáticos</b> (redes sociais, smartphones, pornografia) ainda não têm critérios formais nas classificações diagnósticas.</li></ul>
<p>Repare que o transtorno do jogo é, dos quadros da disciplina, o mais bem estabelecido: tem critérios, especificadores, dados de curso e tratamento com evidência. Os quatro pontos acima mostram por que ele serve de modelo e, ao mesmo tempo, por que o modelo não se transfere sem cuidado para o resto.</p>
"""),
        ('s7', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>Os critérios descrevem o produto; o ciclo descreve o processo. Para a formulação, o que o vídeo entrega é isto:</p>
<ul class='key'><li><b>O critério 5 é a função.</b> Jogar quando angustiado diz o que o jogo faz pela pessoa, e o perfil (deprimido ou ansioso) diz em que direção: baixar afeto negativo ou levantar afeto positivo.</li><li><b>Os critérios 1 e 2 são a alça biológica</b>, e o gráfico da dopamina é o esquema dela, com a moderação feita acima.</li><li><b>O critério 6 é a alça cognitiva</b> que o vídeo 5 já tinha marcado: chasing sustentado pela ideia de sorte e azar.</li><li><b>Os critérios 7, 8 e 9 são o custo social</b>, e são também o que alimenta a vergonha que fecha o ciclo e reabre o precipitante.</li><li><b>O curso é o que se monitora</b>: episódico ou persistente muda a expectativa; remissão inicial e sustentada dão o marco para o acompanhamento.</li></ul>
<p>Na prática: contar os critérios para diagnosticar e classificar, desenhar o ciclo para tratar, e voltar aos critérios, mês a mês, para saber se o ciclo foi mesmo interrompido.</p>
"""),
    ],
    'checklist': [
        'Percorri os nove critérios com o paciente, e não só os que ele trouxe; anotei quais e quantos.',
        'Confirmei o período de doze meses e o sofrimento ou prejuízo antes de fechar o diagnóstico.',
        'Descartei episódio maníaco quando o jogo aparece em surtos de gasto e expansividade.',
        'Classifiquei a gravidade pela contagem (leve, moderada, grave) e registrei o especificador de curso.',
        'Desenhei o ciclo com o paciente: precipitante, cognição permissiva, comportamento, reforço, consequência, emoção reativa.',
        'Identifiquei o perfil (joga para não sentir ou joga para sentir) e ajustei a função-alvo.',
        'Avaliei risco de suicídio na primeira entrevista e nos momentos de perda grande, descoberta pela família ou dívida.',
        'Perguntei qual é o jogo, em que contexto cultural, e o que é normativo ali antes de decidir o que pedir que ele deixe.',
        'Acompanhei a remissão com a lista de critérios, mês a mês, em vez de pela sensação de melhora.',
    ],
    'questoes': [
        'Enuncie a regra do critério A e liste os nove critérios agrupados nas quatro famílias.',
        'Quais critérios são os mais frequentes e quais são os menos frequentes, e o que isso diz sobre a gravidade?',
        'Descreva as seis etapas do ciclo sucessivo de feedback e explique por que a última etapa reabre a primeira.',
        'Diferencie os quatro especificadores de curso (episódico, persistente, remissão inicial, remissão sustentada) pelos prazos.',
        'Quais são os dois perfis de jogador descritos, e como a função do jogo muda de um para o outro?',
        'Pense num paciente teu com jogo problemático. Em que etapa do ciclo tu entraria primeiro, e por quê?',
    ],
    'gabarito': {
     0: (C, u"Comportamento de jogo problemático persistente e recorrente, com sofrimento ou prejuízo clinicamente significativo, indicado por quatro ou mais critérios em doze meses. Parece substância: 1 tolerância, 2 abstinência. Controle e função: 3 esforços malsucedidos de controlar, 4 preocupação frequente, 5 joga quando angustiado. Caça e ocultação: 6 volta para ficar quite, 7 mente sobre a extensão. Dano: 8 prejudicou ou perdeu relação, emprego ou oportunidade, 9 depende de outros para saldar dívidas do jogo. Critério B: não é mais bem explicado por episódio maníaco."),
     1: (C, u"Os mais frequentes são a preocupação com o jogo e a tentativa de recuperar as perdas, típicos da forma leve (4 ou 5 critérios). Os menos frequentes são colocar em risco relacionamentos ou oportunidades e depender de outros para cobrir as perdas, que aparecem mais na forma grave (8 ou 9). Ou seja, a gravidade não é só a contagem: os critérios de dano tendem a chegar por último."),
     2: (C, u"Precipitantes (tédio, estresse, briga familiar); cognições permissivas (\"só dez minutos\", \"preciso checar\"); comportamento (horas de jogo, apostas, verificação); reforço (prazer ou alívio, sensação de controle, distração); consequências (culpa, perda de tempo, insônia, isolamento); emoções negativas reativas (tristeza, frustração, vergonha). A última reabre a primeira porque a vergonha e a frustração de ontem são exatamente o tipo de estado que serve de precipitante hoje; o ciclo produz o seu próprio combustível."),
     3: (C, u"Episódico: preencheu os critérios mais de uma vez, com os sintomas cedendo por no mínimo vários meses entre os períodos. Persistente: sintomas contínuos, preenchendo os critérios por vários anos. Remissão inicial: depois do diagnóstico, nenhum critério preenchido por pelo menos 3 meses e menos de 12. Remissão sustentada: nenhum critério preenchido por 12 meses ou mais."),
     4: (C, u"Deprimidos: solitários, jogam quando se sentem impotentes, culpados ou deprimidos; a função é baixar o afeto negativo, jogar para não sentir. Ansiosos: impulsivos, competitivos, cheios de energia, inquietos, entediam-se fácil, preocupados com aprovação e extravagantes quando ganham; a função é levantar o afeto positivo, jogar para sentir. Como a função é oposta, o substituto que o tratamento precisa oferecer também é."),
     5: (K, u"Não há resposta certa. Uma boa resposta escolhe a etapa a partir do paciente e justifica: a cognição permissiva quando o paciente já monitora bem os gatilhos e precisa de um freio no ato; o reforço quando o jogo é a única fonte de controle ou de alívio que ele tem, o que exige construir outra; a emoção reativa quando a recaída vem sempre pela vergonha do dia anterior. O erro comum é entrar pelo comportamento (reduzir horas ou valor) sem mexer no que o repõe."),
    },
    'referencias': [
        "American Psychiatric Association. (2022). <em>Manual diagnóstico e estatístico de transtornos mentais: DSM-5-TR</em> (5. ed., texto revisado). Artmed.",
        "Blaszczynski, A., &amp; Nower, L. (2002). A pathways model of problem and pathological gambling. <em>Addiction, 97</em>(5), 487–499.",
        "Ladouceur, R., Sylvain, C., Boutin, C., &amp; Doucet, C. (2002). <em>Understanding and treating the pathological gambler.</em> Wiley.",
        "Potenza, M. N., Balodis, I. M., Derevensky, J., Grant, J. E., Petry, N. M., Verdejo-Garcia, A., &amp; Yip, S. W. (2019). Gambling disorder. <em>Nature Reviews Disease Primers, 5</em>, 51.",
        "Sharpe, L. (2002). A reformulated cognitive-behavioral model of problem gambling: A biopsychosocial perspective. <em>Clinical Psychology Review, 22</em>(1), 1–25.",
        "World Health Organization. (2019). <em>International classification of diseases, 11th revision (ICD-11)</em>: 6C50 Gambling disorder.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o sexto vídeo de uma disciplina de pós-graduação; a avaliação diagnóstica das demandas de dependência tecnológica vem no vídeo 7.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. Os slides apresentam os critérios 3 a 9 por extenso; os critérios 1 e 2 foram completados a partir do DSM-5-TR e estão indicados como tal. O agrupamento em quatro famílias, o quadro "onde entrar" no ciclo, a leitura dos dois perfis pela função e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina.<br><br><strong>Duas moderações, sinalizadas no texto.</strong> Primeira: o gráfico da taxa dopaminérgica basal foi apresentado como esquema didático; a regulação para baixo dos receptores está bem documentada para substâncias, e para o jogo a evidência de alteração no sistema de recompensa existe, mas com achados em mais de uma direção. Segunda: as anotações do gráfico de curso por idade misturam a literatura do transtorno do jogo com a do transtorno de jogos pela internet (horas médias diárias, gêneros de jogo); o texto avisa onde isso ocorre.<br><br><strong>Fontes não conferidas.</strong> As citações que aparecem nos slides sem dados completos (Moreira, 2004; Dash, 2019; Wichstrøm et al., 2016; Rehbein et al., 2019) não puderam ser localizadas com segurança e ficaram fora das referências, que trazem apenas o manual e obras que sustentam o que o texto afirma. Nenhuma citação foi construída para preencher lacuna.<br><br><strong>Sobre o dado de suicídio.</strong> A taxa citada é do manual e foi mantida porque o material se dirige a profissionais; o texto a converte em conduta (avaliação de risco obrigatória e repetida), sem qualquer detalhe além da prevalência.""",
}

_FIGS = {'NOVE': NOVE, 'CICLO': CICLO, 'GRAV': GRAV}
DT6['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DT6['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT6['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT6, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT6)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT6['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
