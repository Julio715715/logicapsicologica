# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 21: Psicoeducação para cuidadores e familiares. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

ESTILOS = u"""<figure class='dg'><div class='dg-t'>Estilos parentais e o que costuma aparecer nos filhos</div>
<svg viewBox='0 0 720 290' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Dois quadrantes lado a lado cruzando exigência e responsividade: à esquerda os quatro estilos parentais, à direita as características correspondentes das crianças e adolescentes'>
<g>
<line x1='170' y1='20' x2='170' y2='270' stroke='#2f2e24' stroke-width='1.4'/><line x1='20' y1='145' x2='320' y2='145' stroke='#2f2e24' stroke-width='1.4'/>
<text x='170' y='14' text-anchor='middle' %(F)s font-size='8.5' font-weight='800' letter-spacing='1' fill='#8d876f'>EXIG&Ecirc;NCIA +</text>
<text x='318' y='140' text-anchor='end' %(F)s font-size='8.5' font-weight='800' letter-spacing='1' fill='#8d876f'>RESPONSIVIDADE +</text>
<text x='95' y='40' text-anchor='middle' %(F)s font-size='10' font-weight='800' fill='#a05a3c'>AUTORIT&Aacute;RIOS</text>
<text x='95' y='56' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>rígidos, punitivos, frios,</text>
<text x='95' y='69' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>exigentes sem diálogo</text>
<text x='245' y='40' text-anchor='middle' %(F)s font-size='10' font-weight='800' fill='#43441f'>AUTORITATIVOS</text>
<text x='245' y='56' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>limites coerentes, dialogam,</text>
<text x='245' y='69' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>firmes mas justos, afetivos</text>
<text x='95' y='176' text-anchor='middle' %(F)s font-size='10' font-weight='800' fill='#a05a3c'>NEGLIGENTES</text>
<text x='95' y='192' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>indiferentes, omissos,</text>
<text x='95' y='205' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>inconstantes, frios</text>
<text x='245' y='176' text-anchor='middle' %(F)s font-size='10' font-weight='800' fill='#8d876f'>INDULGENTES</text>
<text x='245' y='192' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>afetivos em excesso, evitam</text>
<text x='245' y='205' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>conflito, "amigos" e não educadores</text>
</g>
<g>
<line x1='550' y1='20' x2='550' y2='270' stroke='#2f2e24' stroke-width='1.4'/><line x1='400' y1='145' x2='700' y2='145' stroke='#2f2e24' stroke-width='1.4'/>
<text x='550' y='14' text-anchor='middle' %(F)s font-size='8.5' font-weight='800' letter-spacing='1' fill='#8d876f'>FILHOS</text>
<text x='475' y='40' text-anchor='middle' %(F)s font-size='10' font-weight='800' fill='#a05a3c'>PASSIVOS</text>
<text x='475' y='56' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>ansiosos, baixa autoestima,</text>
<text x='475' y='69' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>dependentes de aprovação</text>
<text x='625' y='40' text-anchor='middle' %(F)s font-size='10' font-weight='800' fill='#43441f'>BEM ADAPTADOS</text>
<text x='625' y='56' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>seguros, socialmente competentes,</text>
<text x='625' y='69' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>boa autorregulação emocional</text>
<text x='475' y='176' text-anchor='middle' %(F)s font-size='10' font-weight='800' fill='#a05a3c'>N&Atilde;O ENVOLVIDOS</text>
<text x='475' y='192' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>inseguros, problemas de auto-</text>
<text x='475' y='205' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>rregulação, comportamentos de risco</text>
<text x='625' y='176' text-anchor='middle' %(F)s font-size='10' font-weight='800' fill='#8d876f'>EXIGENTES</text>
<text x='625' y='192' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>impulsivos, intolerantes à frustração,</text>
<text x='625' y='205' text-anchor='middle' %(F)s font-size='9' fill='#6c6a55'>dificuldade com regras externas</text>
</g>
<text x='360' y='282' text-anchor='middle' %(F)s font-size='9.5' font-style='italic' fill='#6c6a55'>exigência: regras e expectativas · responsividade: sensibilidade, apoio emocional e aceitação</text>
</svg>
<figcaption>Os dois quadrantes do slide, lado a lado. O estilo autoritativo (exigente e responsivo) é o que o módulo de limites e contratos tenta construir; os outros três são os que mais aparecem quando a família procura ajuda pela tela.</figcaption></figure>""" % dict(F=F)

CICLO_P = u"""<figure class='dg'><div class='dg-t'>O ciclo da raiva dos pais</div>
<svg viewBox='0 0 720 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Seis etapas em ciclo: precipitantes, cognições, comportamento, reforço, consequência, emoções negativas reativas, aplicadas à raiva dos pais com o filho'>
<defs><marker id='cp' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<g %(F)s font-size='9.5' fill='#2f2e24' text-anchor='middle'>
<rect x='0' y='10' width='112' height='72' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='56' y='32' font-weight='800'>Precipitantes</text><text x='56' y='50' fill='#6c6a55'>problemas com</text><text x='56' y='64' fill='#6c6a55'>a família</text>
<path d='M116 46 L136 46' stroke='#8d876f' stroke-width='1.8' marker-end='url(#cp)'/>
<rect x='140' y='10' width='128' height='72' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='204' y='32' font-weight='800'>Cognições</text><text x='204' y='50' fill='#6c6a55'>"ninguém sabe resolver</text><text x='204' y='64' fill='#6c6a55'>nada nessa casa"</text>
<path d='M272 46 L292 46' stroke='#8d876f' stroke-width='1.8' marker-end='url(#cp)'/>
<rect x='296' y='10' width='112' height='72' rx='9' fill='#43441f'/><text x='352' y='32' font-weight='800' fill='#f0ede0'>Comportamento</text><text x='352' y='50' fill='#9ca575'>briga,</text><text x='352' y='64' fill='#9ca575'>explosões</text>
<path d='M412 46 L432 46' stroke='#8d876f' stroke-width='1.8' marker-end='url(#cp)'/>
<rect x='436' y='10' width='128' height='72' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='500' y='32' font-weight='800'>Reforço</text><text x='500' y='50' fill='#6c6a55'>alívio, sensação de</text><text x='500' y='64' fill='#6c6a55'>controle, justiça feita</text>
<path d='M568 46 L588 46' stroke='#8d876f' stroke-width='1.8' marker-end='url(#cp)'/>
<rect x='592' y='10' width='128' height='72' rx='9' fill='#fffdf7' stroke='#a05a3c'/><text x='656' y='32' font-weight='800'>Consequência</text><text x='656' y='50' fill='#6c6a55'>mal-estar, modelo</text><text x='656' y='64' fill='#6c6a55'>parental instalado</text>
<path d='M656 86 L656 110' stroke='#8d876f' stroke-width='1.8' marker-end='url(#cp)'/>
<rect x='560' y='114' width='160' height='60' rx='9' fill='#fffdf7' stroke='#a05a3c'/><text x='640' y='136' font-weight='800'>Emoções reativas</text><text x='640' y='154' fill='#6c6a55'>raiva, culpa, ansiedade</text>
<path d='M556 144 L56 144 L56 90' fill='none' stroke='#8d876f' stroke-width='1.8' stroke-dasharray='5 4' marker-end='url(#cp)'/>
<text x='300' y='138' %(F)s font-size='9.5' font-style='italic' fill='#8d876f'>a explosão de hoje é o precipitante de amanhã, e o modelo que o filho aprende</text>
</g>
</svg>
<figcaption>O mesmo ciclo do vídeo 6, agora com os pais no centro. A consequência que mais importa está na quinta caixa: o modelo parental instalado é o que o filho vai repetir com a tela.</figcaption></figure>""" % dict(F=F)

DT21 = {
    'slug': 'aula21',
    'titulo_txt': 'Psicoeducação para cuidadores e familiares: quatro módulos para a casa em que a tela mora',
    'titulo_html': 'Psicoeduca&ccedil;&atilde;o para cuidadores e familiares: quatro m&oacute;dulos para a casa em que a tela mora',
    'data': 'Vídeo 21',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 21',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 21 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 21',
    'chave': 'mat-Aula-DT21-',
    'arquivo': 'Aula-DT21-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do vigésimo primeiro e último vídeo da "
              u"disciplina, sobre psicoeducação para cuidadores e familiares. Não havia transcrição.</p>"
              u"<p>É o vídeo mais longo da série: um estudo, dois programas de parentalidade e quatro módulos. Uma moderação sobre os limites de tempo por idade está sinalizada.</p></div>"),
    'tema': 'O que dizer aos pais: controle comportamental protege e controle psicológico não, a relação modera tudo, e quatro '
            'módulos para trabalhar com a família: psicoeducação por idade, estilos parentais, limites e contratos, manejo da raiva.',
    'essencial': [
        ('Regras claras protegem; manipulação emocional não.',
         'Estudo com quase dois mil adolescentes chineses: controle comportamental associado a menos dependência; controle psicológico, a mais. A relação pai-filho modera os dois.'),
        ('Dois programas com evidência para indicar.',
         'ACT Raising Safe Kids, da APA, do nascimento aos 10 anos; Triple P, parentalidade positiva, mais de 35 anos de pesquisa.'),
        ('Módulo 1: cada idade tem seu padrão e sua pergunta.',
         'Da exposição passiva na primeira infância ao uso noturno na adolescência, e a pergunta que o vídeo faz aos pais sobre o próprio uso.'),
        ('Módulo 2: o estilo autoritativo é o alvo.',
         'Exigência com responsividade. Autoritário, indulgente e negligente são os que mais chegam ao consultório pela tela.'),
        ('Módulo 3: limites de tempo, de lugar e por dispositivo, com contrato.',
         'Quarto sem telas à noite, zona comum, ilhas offline, e o sistema de fichas como contrato visível.'),
        ('Módulo 4: os pais também têm um ciclo.',
         'Raiva com função e com custo. O pinheiro de 20 centímetros: emoções se manejam pequenas.'),
    ],
    'secoes': [
        ('s0', 'O que a evidência diz', 'O que a evidência diz aos pais', u"""
<p>O vídeo abre com um estudo publicado no <em>Frontiers in Public Health</em> em 2023 (Zhu, Deng e Bai), com quase dois mil adolescentes chineses de 14 a 22 anos. O <strong>controle comportamental dos pais</strong> (regras claras, supervisão) está negativamente associado à dependência de internet; o <strong>controle psicológico</strong> (manipulação emocional, crítica) tende a aumentar o risco, ainda que marginalmente; e a <strong>qualidade da relação pai-filho</strong> moderou os dois efeitos.</p>
<p>É a frase que organiza o vídeo inteiro: <strong>regra protege, chantagem não, e a relação decide quanto cada uma pesa</strong>. Os quatro módulos são o desdobramento disso: entender o filho por idade, entender o próprio estilo, construir regras que funcionam e manejar a raiva que estraga a relação.</p>
<h3>Dois programas para indicar</h3>
<p>O slide mostra dois programas de parentalidade com evidência. O <strong>ACT Raising Safe Kids</strong> (Criando Crianças Seguras), da American Psychological Association, ensina habilidades parentais positivas para pais e cuidadores de crianças do nascimento aos 10 anos, com formações no Brasil (Pelotas aparece na página). O <strong>Triple P</strong> (Programa de Parentalidade Positiva), respaldado por mais de 35 anos de pesquisa, oferece estratégias práticas para construir relacionamentos fortes, gerenciar o comportamento dos filhos e prevenir problemas; é usado em mais de 30 países. Para o psicólogo, são o encaminhamento para a família que precisa de mais do que quatro sessões de psicoeducação.</p>
"""),
        ('s1', 'Módulo 1', 'Módulo 1: psicoeducação, por idade', u"""
<p>O primeiro módulo cobre a compreensão da dependência tecnológica (sinais, sintomas e impactos), os <strong>mitos comuns</strong> ("é só fase", "quanto mais tecnologia, melhor para aprender") e a diferença entre uso saudável, uso problemático e dependência (vídeo 3). O slide observa que os mitos pedem reestruturação cognitiva, análise de vantagens e desvantagens e apresentação de estudos sobre as consequências negativas, ou seja, as mesmas técnicas do paciente, agora com os pais.</p>
<p>O quadro por idade é a peça central, com padrões, pontos críticos e uma pergunta para reflexão em cada faixa.</p>
<ul class='key'><li><b>Primeira infância (0 a 5)</b>: exposição passiva a telas. Crítico: uso para acalmar a criança na birra, falta de estimulação sensório-motora. Pergunta: em quais momentos recorremos à tecnologia para regular o comportamento da criança?</li><li><b>Idade escolar (6 a 10)</b>: jogos online, vídeos, primeiros contatos com redes. Crítico: dificuldade em estabelecer limites, tela antes de dormir, conflito entre brincar offline e online. Pergunta: como equilibramos tarefas, lazer offline e telas?</li><li><b>Pré-adolescência (11 a 13)</b>: intensificação de redes, jogos multiplayer, comunicação por aplicativos. Crítico: conteúdo inapropriado, cyberbullying, queda no rendimento, isolamento. Pergunta: quais sinais indicam que a tecnologia está começando a substituir atividades sociais e escolares?</li><li><b>Adolescência (14 a 17)</b>: uso intenso de redes, streaming, jogos competitivos, múltiplas horas por dia. Crítico: uso noturno comprometendo sono, dependência de validação social, conflitos sobre regras. Pergunta: o adolescente consegue ficar períodos sem tecnologia sem irritabilidade ou ansiedade?</li><li><b>Vida adulta dos pais</b>: tecnologia para trabalho, redes e entretenimento. Crítico: pais modelam padrões de uso excessivo, ausência de momentos familiares offline, multitarefa constante (celular na refeição). Pergunta: o quanto o nosso uso está servindo de modelo saudável ou problemático para nossos filhos?</li></ul>
<div class='obs'><h4>A última linha é a que mais importa</h4><p>O quadro termina com os pais, e é de propósito. A pergunta da primeira infância ("quando usamos a tela para regular a criança?") e a da vida adulta ("que modelo estamos dando?") são a mesma pergunta em dois momentos: a tela como regulador emocional é aprendida em casa, e a família que chega pedindo ajuda com o filho costuma ter o mesmo padrão no sofá. O módulo 4 volta a isso.</p></div>
"""),
        ('s2', 'Módulo 2', 'Módulo 2: estilos parentais', u"""
{{ESTILOS}}
<p>Dois eixos. <strong>Exigência</strong>: o grau em que os pais estabelecem expectativas, regras e padrões de comportamento. <strong>Responsividade</strong>: o nível de sensibilidade, apoio emocional e aceitação das necessidades e sentimentos dos filhos. Cruzados, dão quatro estilos.</p>
<ul class='key'><li><b>Autoritários</b> (exigência alta, responsividade baixa): rígidos, controladores, punitivos, impositivos e frios, hierárquicos, exigentes sem diálogo, pouco afetivos. Filhos <b>passivos</b>: ansiosos ou com baixa autoestima, retraídos ou hostis, dependentes de aprovação, agressividade encoberta, não tomam decisões.</li><li><b>Autoritativos</b> (as duas altas): limites coerentes, acolhedores, dialogam, democráticos, firmes mas justos, encorajam autonomia, afetivos mas racionais. Filhos <b>bem adaptados</b>: seguros, socialmente competentes, autônomos mas respeitosos, boa autorregulação, maior autoestima.</li><li><b>Negligentes</b> (as duas baixas): indiferentes, distantes, desengajados, omissos, inconstantes, frios. Filhos <b>não envolvidos</b>: inseguros, baixa autoestima, problemas de autorregulação, comportamentos de risco, dificuldade em formar vínculos.</li><li><b>Indulgentes</b> (exigência baixa, responsividade alta): afetivos em excesso, evitam conflitos, flexíveis demais, protetores, pouco limitadores, "amigos" mais que educadores. Filhos <b>exigentes</b>: afetivos e comunicativos, mas intolerantes à frustração, impulsivos, dificuldade com regras externas, opositores, autoestima elevada.</li></ul>
<p>O slide traz também o <strong>Questionário de Estilos Parentais</strong>, com 24 itens em escala de 1 a 5, que avalia os quatro estilos pelas duas dimensões. Os itens de estilo autoritativo mostrados: explico o motivo da regra antes de aplicar consequências; busco ouvir meu filho antes de decidir; em conflitos mantenho a firmeza com afeto; incentivo meu filho a tomar decisões por si mesmo.</p>
<div class='callout note'><div class='co-t'>Como ler com os pais</div>O estudo da abertura já disse qual quadrante protege: regra clara (exigência) com relação boa (responsividade) é o autoritativo. Vale mostrar aos pais os outros três sem julgamento, como respostas compreensíveis ao cansaço (indulgente), ao medo (autoritário) ou à sobrecarga (negligente), e perguntar em qual eles se veem quando o assunto é a tela. A resposta costuma ser diferente para cada um dos pais, e a diferença entre os dois é, muitas vezes, o problema.</div>
"""),
        ('s3', 'Módulo 3', 'Módulo 3: limites e contratos', u"""
<h3>Limites de tempo</h3>
<p>O slide apresenta regras por faixa etária, "seguindo orientações de entidades como a American Academy of Pediatrics": <b>0 a 2 anos</b>, evitar exposição (exceto chamadas de vídeo com familiares); <b>2 a 5</b>, até 1 hora por dia, com conteúdo educativo e supervisão; <b>6 a 12</b>, até 2 horas por dia de lazer digital, equilibrando com outras atividades; <b>adolescentes</b>, uso negociado, com pausas e monitoramento dos impactos no sono, na escola e na vida social. Mais duas orientações: <strong>rotina fixa</strong>, com horários livres de tela (refeições, antes de dormir, ao acordar), e <strong>uso progressivo de contratos familiares</strong>, construídos junto com a criança ou o adolescente ("duas horas por dia, em blocos de trinta minutos").</p>
<div class='obs'><h4>Uma moderação sobre os limites por idade</h4><p>As faixas de 0 a 2 e de 2 a 5 correspondem às recomendações atuais da AAP. A partir dos 6 anos, a AAP deixou de indicar um número fixo de horas em 2016 e passou a recomendar um plano familiar de mídia, com limites consistentes definidos pela família; o "até 2 horas" do slide é a orientação anterior, e continua sendo um teto razoável como ponto de partida. Para os pais, a mensagem prática é a que o próprio slide dá logo abaixo: o número importa menos que a rotina fixa e o contrato.</p></div>
<h3>Limites de lugar</h3>
<p><strong>Quarto sem telas à noite</strong>: melhora o sono e reduz o uso secreto. <strong>Zona comum para tecnologia</strong>: sala e cozinha, para facilitar a supervisão. <strong>Ilhas offline</strong>: mesa de jantar, área de leitura, quintal. <strong>Uso diferenciado por dispositivo</strong>: celular fora do quarto à noite, carregando na sala; videogame só em horário acordado e em área comum; notebook no quarto se for estudo, na sala se for lazer.</p>
<h3>O contrato visível</h3>
<p>Dois exemplos. Para crianças menores, um <strong>quadro de tarefas</strong> semanal (trocar de roupa ao acordar, escovar os dentes, arrumar os brinquedos, tarefas escolares, comida à mesa, ajudar numa tarefa, recolher as roupas, banho sem pirraça, não brigar). Para o uso de telas, um <strong>sistema de fichas</strong>: três fichas por dia; cada ficha vale 30 minutos; a tabela registra o dia, as fichas recebidas, a atividade (videogame, YouTube, streaming, redes), as fichas gastas, o tempo e o saldo. Na quarta-feira do exemplo, a criança não usou e ficou com três de saldo.</p>
<p>O sistema de fichas faz o que a regra verbal não faz: torna o limite <strong>visível, contável e negociável</strong>. A criança decide em que gasta as fichas, o saldo mostra a escolha, e a discussão do fim do dia deixa de ser "tu já ficou demais" e vira "quantas fichas sobraram".</p>
"""),
        ('s4', 'Módulo 4', 'Módulo 4: manejo da raiva', u"""
{{CICLO_P}}
<p>O último módulo trabalha os pais como pacientes. A <strong>raiva</strong> é parte da resposta de luta ou fuga, que prepara para lidar com ameaças percebidas. Tem <strong>função adaptativa</strong>: defender interesses, estabelecer limites, proteger, resolver problemas; é reação natural a situações injustas. Quando não é manejada, traz <strong>consequências negativas</strong>: conflitos, prejuízos à saúde, problemas no trabalho e nas relações familiares. E a raiva crônica tem <strong>efeitos a longo prazo</strong> na saúde mental e física: ansiedade, depressão, problemas cardíacos e hipertensão.</p>
<p>O ciclo sucessivo de feedback (vídeo 6) aparece com os pais no centro: precipitantes (problemas com a família), cognições ("ninguém sabe resolver nada nessa casa"), comportamento (briga, explosões), reforço (alívio, sensação de controle, justiça feita), consequência (mal-estar generalizado, <strong>modelo parental instalado</strong>), emoções negativas reativas (raiva, culpa, ansiedade), que reabrem o ciclo.</p>
<h3>O pinheiro</h3>
<p>O slide diz: é importante trabalhar com os pais regulação emocional e manejo da raiva, porque eles são modelos para os filhos. A analogia é a do pinheiro. <em>Imagine um pinheiro de 20 metros: tu consegue pisar nele e quebrá-lo? Agora um pinheiro de 20 centímetros: tu consegue? Emoções são a mesma coisa. Se tu as "quebra" enquanto estão em pequena proporção, elas não vão crescer. Vamos tentar?</em></p>
<p>É a versão para pais do atraso voluntário da resposta (vídeo 12) e da curva de exposição (vídeo 18): a raiva se maneja no começo da subida, e não no pico. O instrumento do módulo é o <strong>Manifesto da Irritabilidade</strong>, uma tabela em duas colunas: problema, situação e intensidade de um lado; envolvidos e potencial solução do outro. Preenchida ao longo da semana, ela mostra aos pais os pinheiros de 20 centímetros antes que virem os de 20 metros, e transforma cada irritação num problema com solução, que é a lógica do vídeo 15.</p>
<div class='callout note'><div class='co-t'>Por que fechar a disciplina aqui</div>O vídeo 21 é o último, e termina com os pais e não com o paciente, o que faz sentido pela disciplina inteira: a tela é regulador emocional aprendido em casa (módulo 1), sustentado por um estilo parental (módulo 2), sem limites visíveis (módulo 3) e num ambiente em que a raiva dos adultos é o modelo de como se lida com o que incomoda (módulo 4). Tratar o adolescente sem tocar em nada disso é tratar a alça num nó só.</div>
"""),
        ('s5', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<ul class='key'><li><b>O estudo de abertura é a rede da família</b>: controle comportamental como contexto protetor, controle psicológico como contexto de risco, e a relação como moderador de tudo.</li><li><b>O quadro por idade é a formulação do desenvolvimento</b>: em que momento a tela vira regulador, e a última linha mostra de quem a criança aprende isso.</li><li><b>Os estilos parentais são o contexto estável</b>, e o alvo (autoritativo) é exigência com responsividade, ou seja, regra com relação.</li><li><b>Limites e contratos são o arranjo do ambiente</b> (vídeo 12) na escala da casa: lugar, hora, dispositivo, e um sistema visível que substitui a discussão pela contagem.</li><li><b>O manejo da raiva é o ciclo dos pais</b>, e a consequência que importa é o modelo. Trabalhar a raiva dos pais é intervir no nó que ensina o filho a usar a tela quando incomodado.</li></ul>
<p>Na prática: o estudo para dar a mensagem, o quadro por idade para localizar a família, o questionário para o estilo, o contrato de fichas para a casa, e o manifesto da irritabilidade para os pais. Quatro sessões, e o encaminhamento para ACT ou Triple P quando quatro não bastam.</p>
"""),
    ],
    'checklist': [
        'Dei aos pais a mensagem do estudo: regra clara protege, manipulação emocional não, e a relação decide o peso das duas.',
        'Localizei a criança ou o adolescente no quadro por idade e fiz a pergunta da faixa aos pais.',
        'Fiz a pergunta da última linha: que modelo de uso os pais estão dando.',
        'Trabalhei os mitos ("é só fase") com balança e evidência, como faria com o paciente.',
        'Identifiquei o estilo parental de cada um dos pais quando o assunto é a tela, e a diferença entre os dois.',
        'Construí com a família limites de tempo, de lugar e por dispositivo, e um contrato visível (fichas ou quadro).',
        'Apresentei o ciclo da raiva com os pais no centro e a analogia do pinheiro.',
        'Deixei o Manifesto da Irritabilidade como tarefa dos pais.',
        'Quando quatro sessões não bastaram, encaminhei para ACT ou Triple P.',
    ],
    'questoes': [
        'O que o estudo de Zhu, Deng e Bai (2023) mostrou sobre controle comportamental, controle psicológico e a relação pai-filho?',
        'Descreva o quadro por idade do módulo 1: padrão, ponto crítico e pergunta de cada faixa.',
        'Quais são os dois eixos e os quatro estilos parentais, e o que costuma aparecer nos filhos de cada um?',
        'Descreva os limites de tempo, de lugar e por dispositivo do módulo 3, e explique o sistema de fichas.',
        'Descreva o ciclo da raiva dos pais e a analogia do pinheiro.',
        'Pense numa família que tu atende. Em que faixa do quadro está o filho, que estilo tem cada um dos pais, e que contrato tu proporia primeiro?',
    ],
    'gabarito': {
     0: (C, u"Em quase dois mil adolescentes chineses de 14 a 22 anos, o controle comportamental dos pais (regras claras, supervisão) esteve negativamente associado à dependência de internet; o controle psicológico (manipulação emocional, crítica) tendeu a aumentar o risco, marginalmente; e a qualidade da relação pai-filho moderou os dois efeitos. Regra protege, chantagem não, e a relação decide o peso."),
     1: (C, u"0 a 5: exposição passiva; uso para acalmar na birra e falta de estimulação; quando usamos a tela para regular a criança? 6 a 10: jogos, vídeos, primeiras redes; limites, tela antes de dormir, offline versus online; como equilibramos tarefas, lazer e telas? 11 a 13: redes, multiplayer, aplicativos; conteúdo inapropriado, cyberbullying, rendimento, isolamento; que sinais mostram a tecnologia substituindo o social e o escolar? 14 a 17: uso intenso, muitas horas; uso noturno, validação social, conflito sobre regras; consegue ficar sem tecnologia sem irritabilidade? Pais: trabalho, redes, entretenimento; modelagem de uso excessivo, ausência de momentos offline, multitarefa; que modelo estamos dando?"),
     2: (C, u"Exigência (regras, expectativas) e responsividade (sensibilidade, apoio, aceitação). Autoritários (exigência alta, responsividade baixa): filhos passivos, ansiosos, dependentes de aprovação. Autoritativos (as duas altas): filhos bem adaptados, seguros, com boa autorregulação. Negligentes (as duas baixas): filhos não envolvidos, inseguros, com comportamentos de risco. Indulgentes (exigência baixa, responsividade alta): filhos exigentes, impulsivos, intolerantes à frustração."),
     3: (C, u"Tempo: 0 a 2 evitar (exceto chamadas de vídeo), 2 a 5 até 1 hora com supervisão, 6 a 12 até 2 horas de lazer digital, adolescentes uso negociado com pausas e monitoramento; rotina fixa com horários sem tela e contratos construídos com a criança. Lugar: quarto sem telas à noite, zona comum, ilhas offline. Dispositivo: celular fora do quarto à noite, videogame só em horário combinado e área comum, notebook no quarto para estudo e na sala para lazer. Fichas: três por dia, cada uma vale 30 minutos, com registro de atividade, fichas gastas e saldo; torna o limite visível, contável e negociável."),
     4: (C, u"Precipitantes (problemas com a família), cognições (\"ninguém sabe resolver nada nessa casa\"), comportamento (briga, explosões), reforço (alívio, controle, justiça feita), consequência (mal-estar e modelo parental instalado), emoções reativas (raiva, culpa, ansiedade), que reabrem o ciclo. O pinheiro: de 20 metros não se quebra pisando; de 20 centímetros, sim. Emoções se manejam pequenas, no começo da subida, e não no pico."),
     5: (K, u"Não há resposta certa. Uma boa resposta localiza o filho numa faixa com o ponto crítico correspondente, nomeia o estilo de cada um dos pais (que costumam ser diferentes, e a diferença é parte do problema) e propõe um contrato proporcional à idade e ao conflito atual: fichas para os menores, contrato negociado de horários e lugares para adolescentes, começando pelo limite de lugar (quarto sem telas à noite) quando o sono é o ponto crítico. O erro comum é começar pelo número de horas."),
    },
    'referencias': [
        "American Academy of Pediatrics, Council on Communications and Media. (2016). Media and young minds. <em>Pediatrics, 138</em>(5), e20162591.",
        "American Academy of Pediatrics, Council on Communications and Media. (2016). Media use in school-aged children and adolescents. <em>Pediatrics, 138</em>(5), e20162592.",
        "Baumrind, D. (1991). The influence of parenting style on adolescent competence and substance use. <em>Journal of Early Adolescence, 11</em>(1), 56–95.",
        "Maccoby, E. E., &amp; Martin, J. A. (1983). Socialization in the context of the family: Parent-child interaction. In P. H. Mussen (Ed.), <em>Handbook of child psychology</em> (Vol. 4, pp. 1–101). Wiley.",
        "Sanders, M. R. (2012). Development, evaluation, and multinational dissemination of the Triple P-Positive Parenting Program. <em>Annual Review of Clinical Psychology, 8</em>, 345–379.",
        "Zhu, X., Deng, C., &amp; Bai, W. (2023). Parental control and adolescent internet addiction: The moderating effect of parent-child relationships. <em>Frontiers in Public Health, 11</em>, 1190534.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o vigésimo primeiro e último vídeo de uma disciplina de pós-graduação.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. Os dois quadrantes de estilos parentais e o ciclo da raiva foram redesenhados com o conteúdo dos slides. Os quadros "a última linha é a que mais importa", "como ler com os pais", a observação sobre o sistema de fichas, "por que fechar a disciplina aqui" e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina.<br><br><strong>Uma moderação, sinalizada no texto.</strong> Os limites de tempo por idade do slide citam a American Academy of Pediatrics. As faixas de 0 a 2 e 2 a 5 correspondem às recomendações atuais; a partir dos 6 anos, a AAP deixou de indicar horas fixas em 2016 e recomenda um plano familiar de mídia com limites consistentes; o "até 2 horas" é a orientação anterior e foi mantido como teto de partida, com a ressalva. O estudo de abertura (Zhu, Deng e Bai, 2023) foi localizado e está nas referências. O Questionário de Estilos Parentais é apresentado no slide como material do professor; o material o descreve como o slide o apresenta.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'ESTILOS': ESTILOS, 'CICLO_P': CICLO_P}
DT21['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT21['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT21['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT21, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT21)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT21['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
