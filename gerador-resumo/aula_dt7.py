# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 7: Avaliação diagnóstica. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

FORM = u"""<figure class='dg'><div class='dg-t'>A formulação como guia: de onde vem cada peça</div>
<svg viewBox='0 0 720 232' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Fatores predisponentes e precipitantes alimentam o modelo psicoterapêutico, que explica os problemas e gera o plano; a anamnese alimenta os predisponentes e a avaliação ecológica momentânea alimenta os precipitantes'>
<defs><marker id='fm' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='150' width='200' height='56' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='14' y='173' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Fatores predisponentes</text>
<text x='14' y='192' %(F)s font-size='10' fill='#6c6a55'>história, temperamento, contexto</text>
<rect x='0' y='76' width='200' height='56' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='14' y='99' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Precipitantes</text>
<text x='14' y='118' %(F)s font-size='10' fill='#6c6a55'>o que dispara cada episódio</text>
<path d='M100 146 L100 136' stroke='#8d876f' stroke-width='1.8' marker-end='url(#fm)'/>
<path d='M204 104 L262 104' stroke='#8d876f' stroke-width='1.8' marker-end='url(#fm)'/>
<path d='M204 178 L232 178 L232 104' fill='none' stroke='#8d876f' stroke-width='1.8'/>
<rect x='266' y='64' width='190' height='80' rx='10' fill='#43441f'/>
<text x='361' y='94' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#f0ede0'>Modelo psicoterapêutico</text>
<text x='361' y='112' text-anchor='middle' %(F)s font-size='10' fill='#9ca575'>o ciclo do vídeo 6, a rede</text>
<text x='361' y='128' text-anchor='middle' %(F)s font-size='10' fill='#9ca575'>de processos</text>
<path d='M460 104 L500 104' stroke='#8d876f' stroke-width='1.8' marker-end='url(#fm)'/>
<rect x='504' y='64' width='216' height='80' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='612' y='90' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Problemas 1 … n</text>
<text x='612' y='108' text-anchor='middle' %(F)s font-size='10' fill='#6c6a55'>explicados pelo mesmo modelo</text>
<text x='612' y='128' text-anchor='middle' %(F)s font-size='10.5' font-weight='800' fill='#a05a3c'>= plano de tratamento</text>
<text x='14' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a8894f'>ANAMNESE, ENTREVISTA ABERTA, OBSERVA&Ccedil;&Atilde;O</text>
<path d='M60 36 L60 70' stroke='#a8894f' stroke-width='1.4' stroke-dasharray='4 3' marker-end='url(#fm)'/>
<text x='14' y='224' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a8894f'>&#8593; e a AVALIA&Ccedil;&Atilde;O ECOL&Oacute;GICA MOMENT&Acirc;NEA alimenta os precipitantes</text>
</svg>
<figcaption>O esquema do slide, com o que o vídeo acrescenta: cada caixa da esquerda tem um método de coleta próprio. A entrevista conta a história; a EMA mostra o que dispara o episódio hoje.</figcaption></figure>""" % dict(F=F)

ESCALAS = u"""<figure class='dg'><div class='dg-t'>Cinco instrumentos, cinco perguntas diferentes</div>
<svg viewBox='0 0 720 246' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Cinco instrumentos organizados por o que medem: EMA-DT (uso e estado no dia), EDTec (grau de dependência), IGD-20 (jogos pela internet), G-SAS (sintomas de jogo de azar), GRCS (crenças sobre o jogo de azar)'>
<rect x='0' y='6' width='226' height='108' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='12' y='28' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>EMA-DT</text>
<text x='12' y='46' %(F)s font-size='9.5' fill='#a8894f' font-weight='800' letter-spacing='1'>DI&Aacute;RIO &middot; TODO O DIA</text>
<text x='12' y='68' %(F)s font-size='10.5' fill='#6c6a55'>tempo, finalidade, estado</text>
<text x='12' y='84' %(F)s font-size='10.5' fill='#6c6a55'>emocional, impulsividade,</text>
<text x='12' y='100' %(F)s font-size='10.5' fill='#6c6a55'>impacto funcional do dia</text>
<rect x='247' y='6' width='226' height='108' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='259' y='28' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>EDTec</text>
<text x='259' y='46' %(F)s font-size='9.5' fill='#a8894f' font-weight='800' letter-spacing='1'>15 ITENS &middot; 5 DIMENS&Otilde;ES</text>
<text x='259' y='68' %(F)s font-size='10.5' fill='#6c6a55'>frequência de comportamentos</text>
<text x='259' y='84' %(F)s font-size='10.5' fill='#6c6a55'>de dependência em celular,</text>
<text x='259' y='100' %(F)s font-size='10.5' fill='#6c6a55'>internet, redes, jogos</text>
<rect x='494' y='6' width='226' height='108' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='506' y='28' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>IGD-20</text>
<text x='506' y='46' %(F)s font-size='9.5' fill='#a8894f' font-weight='800' letter-spacing='1'>20 ITENS &middot; 12 MESES</text>
<text x='506' y='68' %(F)s font-size='10.5' fill='#6c6a55'>jogos pela internet: saliência,</text>
<text x='506' y='84' %(F)s font-size='10.5' fill='#6c6a55'>modificação de humor, tolerância,</text>
<text x='506' y='100' %(F)s font-size='10.5' fill='#6c6a55'>abstinência, conflito, recaída</text>
<rect x='120' y='132' width='226' height='108' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.3'/>
<text x='132' y='154' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>G-SAS</text>
<text x='132' y='172' %(F)s font-size='9.5' fill='#a05a3c' font-weight='800' letter-spacing='1'>JOGO DE AZAR &middot; &Uacute;LTIMA SEMANA</text>
<text x='132' y='194' %(F)s font-size='10.5' fill='#6c6a55'>gravidade dos sintomas: vontade,</text>
<text x='132' y='210' %(F)s font-size='10.5' fill='#6c6a55'>pensamentos, comportamento e</text>
<text x='132' y='226' %(F)s font-size='10.5' fill='#6c6a55'>consequências emocionais</text>
<rect x='374' y='132' width='226' height='108' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.3'/>
<text x='386' y='154' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>GRCS</text>
<text x='386' y='172' %(F)s font-size='9.5' fill='#a05a3c' font-weight='800' letter-spacing='1'>JOGO DE AZAR &middot; 23 ITENS</text>
<text x='386' y='194' %(F)s font-size='10.5' fill='#6c6a55'>crenças: expectativas, ilusão de</text>
<text x='386' y='210' %(F)s font-size='10.5' fill='#6c6a55'>controle, controle preditivo,</text>
<text x='386' y='226' %(F)s font-size='10.5' fill='#6c6a55'>incapacidade de parar, viés</text>
</svg>
<figcaption>Em cima, os instrumentos para dependência tecnológica em geral e jogos; embaixo, os dois específicos de jogo de azar. A GRCS é a única que mede crenças, e por isso é a que conversa com a primeira tarefa clínica do vídeo 5.</figcaption></figure>""" % dict(F=F)

DT7 = {
    'slug': 'aula7',
    'titulo_txt': 'Avaliação diagnóstica: formulação de caso, avaliação ecológica momentânea e as escalas',
    'titulo_html': 'Avalia&ccedil;&atilde;o diagn&oacute;stica: formula&ccedil;&atilde;o de caso, avalia&ccedil;&atilde;o ecol&oacute;gica moment&acirc;nea e as escalas',
    'data': 'Vídeo 7',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 7',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 7 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 7',
    'chave': 'mat-Aula-DT7-',
    'arquivo': 'Aula-DT7-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do sétimo vídeo da "
              u"disciplina, sobre avaliação diagnóstica das demandas de dependência tecnológica. Não havia transcrição.</p>"
              u"<p>O caso apresentado nos slides (Gustavo) é uma vinheta didática. Os instrumentos citados estão descritos "
              u"como os slides os apresentam; a nota de método distingue os que têm validação publicada dos que são ferramentas da disciplina.</p></div>"),
    'tema': 'A formulação de caso como guia da avaliação e da intervenção, a avaliação ecológica momentânea como método para pegar '
            'o que a entrevista não pega, e cinco instrumentos com o que cada um mede.',
    'essencial': [
        ('A formulação guia a avaliação, e não o contrário.',
         'Predisponentes, precipitantes e um modelo que explica os problemas geram o plano. A avaliação serve para preencher essas caixas.'),
        ('Cada caixa tem um método de coleta.',
         'Entrevista aberta, anamnese e observação enchem os predisponentes; a avaliação ecológica momentânea enche os precipitantes.'),
        ('A EMA pega o que o relato retrospectivo perde.',
         'Registro no contexto real, uma vez ao dia, com viés de memória reduzido. No caso do vídeo, revelou um padrão que o paciente nunca tinha relatado.'),
        ('Dados da EMA viram plano.',
         'Horário, lugar, estado emocional e gatilho de cada episódio dizem quando e onde intervir. É personalização com base no comportamento real.'),
        ('Cinco instrumentos, cinco perguntas.',
         'EMA-DT e EDTec para o uso de tecnologia em geral; IGD-20 para jogos; G-SAS e GRCS para jogo de azar. A GRCS mede crenças, as outras medem sintomas.'),
    ],
    'secoes': [
        ('s0', 'A formulação como guia', 'A formulação de caso como guia da avaliação e da intervenção', u"""
{{FORM}}
<p>O vídeo abre com um esquema conhecido de formulação cognitivo-comportamental: <strong>fatores predisponentes</strong> e <strong>precipitantes</strong> alimentam um <strong>modelo psicoterapêutico</strong> (o modelo cognitivo da TCC, no exemplo do slide), e esse modelo explica os problemas 1 a 5 do paciente. O conjunto é o plano de tratamento. A ideia central é que a avaliação não é uma lista de exames a aplicar; é o trabalho de preencher essas caixas com dados bons o suficiente para o modelo funcionar.</p>
<p>O acréscimo do vídeo está nas duas setas de coleta. Os predisponentes se preenchem com <strong>entrevistas abertas, anamnese e observação comportamental</strong>: história de vida, temperamento, contexto familiar, o que já existia antes do uso. Os precipitantes, que são o que dispara cada episódio hoje, se preenchem com a <strong>avaliação ecológica momentânea</strong>, porque a entrevista, por melhor que seja, pede que o paciente lembre, e a memória do que aconteceu na terça à noite é ruim.</p>
<div class='callout note'><div class='co-t'>Para quem formula em processos</div>O esquema é o mesmo da rede: predisponentes são os nós de fundo (história, temperamento, contexto), precipitantes são os antecedentes de cada episódio, o modelo psicoterapêutico é o ciclo do vídeo 6, e os problemas são os pontos onde a rede toca a vida da pessoa. A vantagem de pensar assim é que os cinco problemas param de ser cinco planos e viram um só.</div>
"""),
        ('s1', 'O caso e o assistente', 'O caso do vídeo e o assistente de formulação', u"""
<p>O slide apresenta o <strong>FormulaPsi</strong>, assistente virtual do professor para formulação de casos em psicoterapia, e uma vinheta para treinar com ele. Gustavo, 23 anos, estudante de engenharia de software e estagiário remoto, apresenta há 18 meses uso excessivo de internet com foco em jogos online do tipo MMORPG, até 16 horas por dia, com prejuízo funcional: reprovações, faltas no estágio, negligência com autocuidados, isolamento progressivo. Relata irritabilidade intensa quando interrompido, mentiras sobre o tempo online, falhas repetidas em reduzir e sintomas de abstinência (ansiedade, taquicardia) ao tentar interromper. A avaliação aponta ansiedade e humor deprimido leve, sem critérios suficientes para transtorno depressivo maior ou ansiedade social isoladamente. Os sintomas se intensificaram no pós-pandemia e persistiram com a volta da rotina presencial.</p>
<h3>O que a vinheta já entrega</h3>
<ul class='key'><li><b>Critérios</b> (vídeo 6, adaptados ao jogo pela internet): tolerância implícita nas 16 horas, abstinência, esforços malsucedidos, mentira, prejuízo em estudo e trabalho. A contagem fecha com folga.</li><li><b>Predisponentes</b> a investigar: a pandemia como contexto de instalação, o estágio remoto que mantém a tela como ambiente de trabalho e de lazer, o quadro ansioso-depressivo leve que pode ser anterior.</li><li><b>Precipitantes</b> desconhecidos: a vinheta não diz quando Gustavo joga mais, nem o que acontece pouco antes. É exatamente a lacuna que a EMA vai preencher.</li></ul>
"""),
        ('s2', 'A EMA-DT', 'Avaliação ecológica momentânea: o instrumento do vídeo', u"""
<p>A <strong>EMA-DT</strong> (Avaliação Ecológica Momentânea Diária para Dependência Tecnológica) é um instrumento desenvolvido para ser aplicado uma vez ao dia, com o objetivo de monitorar o uso de tecnologias digitais e suas relações com estado emocional, impulsividade e impactos funcionais. É inspirada no modelo de avaliação ecológica momentânea, que captura os dados no ambiente natural da pessoa, com foco em comportamentos e emoções recentes, reduzindo o viés de memória dos autorrelatos retrospectivos.</p>
<p>Os dois primeiros itens mostrados no slide dão a medida do formato: uma estimativa do tempo de uso no dia, em cinco faixas (menos de 1 hora até mais de 8), e a finalidade predominante do uso, com múltipla escolha (trabalho ou estudos, comunicação, redes sociais, jogos, streaming, outro). Os itens seguintes, pelo objetivo declarado, cobrem estado emocional, impulsividade e impacto funcional.</p>
<h3>Por que a EMA importa</h3>
<ul class='key'><li><b>Alta validade ecológica</b>: o comportamento é registrado no contexto real (quarto, transporte, trabalho), o que permite capturar padrões e gatilhos contextuais, como ansiedade antes de dormir seguida de uso de redes sociais.</li><li><b>Monitoramento de variações dinâmicas</b>: flutuações diárias de humor, desejo de uso, impulsividade e sensação de controle. Identifica os momentos críticos de uso compulsivo.</li><li><b>Personalização de intervenções</b>: com os dados, o terapeuta identifica situações de risco e padrões de evitação, planeja exposições e ajusta o plano com base no comportamento real, e não só no relato.</li></ul>
<div class='obs'><h4>Como ela funciona no caso</h4><p>O slide mostra o que a EMA revelou num paciente de uso excessivo de redes. Os registros indicam que o uso ocorre predominantemente no <strong>quarto, entre 23h e 1h</strong>, geralmente após <strong>episódios de ansiedade noturna</strong> ligados ao trabalho do dia seguinte. Esse dado não havia sido relatado nas sessões. Ao longo de 14 dias, desejo de uso e ansiedade aumentam nos <strong>domingos à noite</strong> e em vésperas de reuniões importantes, com queda do senso de controle e aumento da impulsividade nesses períodos: um padrão cíclico de vulnerabilidade ligado a antecipações negativas.</p><p>E o plano muda em função disso: treinamento de regulação emocional nas noites de domingo; manejo das antecipações negativas; mindfulness antes de dormir para reduzir o uso automático do celular; estratégias alternativas para a hora crítica (leitura leve, áudio relaxante); planejamento e resolução de problemas; e monitoramento em tempo real da adesão, com ajuste semanal. Repare que nenhuma dessas seis intervenções poderia ter sido escolhida com precisão a partir do relato "uso muito o celular".</p></div>
"""),
        ('s3', 'As escalas', 'As escalas: o que cada uma mede', u"""
{{ESCALAS}}
<p>Além da EMA, o vídeo apresenta quatro instrumentos de aplicação única, com links para baixar.</p>
<ul class='key'><li><b>EDTec (Escala de Dependência Tecnológica)</b>: desenvolvida para avaliar o grau de dependência de tecnologias digitais (celular, computador, redes sociais, internet). Quinze itens em cinco dimensões; responde-se com a frequência com que cada afirmação se aplica.</li><li><b>IGD-20 (Internet Gaming Disorder Test)</b>: vinte itens que avaliam presença e gravidade do transtorno de jogos pela internet nos últimos doze meses, em qualquer dispositivo, online ou offline. Explora as dimensões clássicas do modelo de componentes da dependência: saliência, modificação de humor, tolerância, abstinência, conflito e recaída. Escala Likert de cinco pontos.</li><li><b>G-SAS (Gambling Symptom Assessment Scale)</b>: escala padronizada para sintomas relacionados ao jogo patológico, projetada para mensurar a gravidade dos comportamentos, pensamentos e consequências emocionais associados ao jogo. O primeiro item pergunta pela intensidade média da vontade de jogar na última semana, de nenhuma a extrema. É uma escala de gravidade e de acompanhamento, boa para medir mudança semana a semana.</li><li><b>GRCS (Gambling Related Cognitions Scale)</b>: 23 itens que avaliam crenças relacionadas ao jogo de azar, em cinco domínios: expectativas positivas sobre o jogo, ilusão de controle, crenças de controle preditivo, incapacidade percebida de parar e viés interpretativo. Escala de sete pontos.</li></ul>
<div class='callout note'><div class='co-t'>Qual usar</div>Para a demanda de tecnologia em geral, EMA-DT para o dia a dia e EDTec para uma medida de grau. Para jogos, IGD-20. Para jogo de azar, G-SAS para gravidade e evolução e GRCS para o alvo cognitivo do vídeo 5: se a GRCS vem alta em ilusão de controle e controle preditivo, a primeira tarefa clínica está confirmada e mensurável.</div>
"""),
        ('s4', 'Monitoramento contínuo', 'Monitoramento contínuo: a HumanTrack', u"""
<p>O vídeo fecha com a <strong>HumanTrack</strong>, plataforma de monitoramento de saúde comportamental em tempo real, com a qual o terapeuta acompanha e avalia o progresso do paciente com dados mais precisos, aumenta a probabilidade de engajamento e mantém a segurança das informações. Na lógica do vídeo, é a EMA levada ao aplicativo: em vez de formulário em papel uma vez ao dia, registros no celular, com gráfico para o terapeuta.</p>
<p>O ponto pedagógico não é a ferramenta em si, e sim o que ela permite: fechar o ciclo entre avaliação e intervenção. Avaliação contínua deixa de ser "linha de base e alta" e vira o próprio instrumento de ajuste do plano, semana a semana, como o caso da seção anterior mostrou.</p>
"""),
        ('s5', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>Para quem trabalha com formulação processual, este vídeo resolve um problema prático: de onde vêm os dados da rede.</p>
<ul class='key'><li><b>Os nós de fundo</b> (história, temperamento, contexto) vêm da anamnese e da entrevista aberta. São estáveis, e uma boa entrevista basta.</li><li><b>Os antecedentes e as consequências de cada episódio</b> vêm da EMA. São variáveis, dependem de hora, lugar e estado, e a memória não os guarda bem. É aqui que o relato retrospectivo mais engana e a medida no momento mais rende.</li><li><b>A força dos nós cognitivos</b> vem das escalas de crença (GRCS) e a gravidade geral, das escalas de sintoma (G-SAS, IGD-20, EDTec). Servem para saber por onde entrar e para medir se a entrada funcionou.</li><li><b>A rede muda</b>, e por isso a avaliação precisa continuar. Monitoramento contínuo é o que permite ver a alça se abrindo ou se fechando, e não só o paciente dizendo que está melhor.</li></ul>
<p>Na prática, o caso do vídeo mostra a sequência inteira: entrevista, EMA por duas semanas, padrão encontrado, plano ajustado ao padrão, monitoramento da adesão. É um bom protocolo de avaliação para qualquer demanda de uso de tecnologia.</p>
"""),
    ],
    'checklist': [
        'Comecei a avaliação com o esquema de formulação na mão: o que preenche predisponentes, o que preenche precipitantes.',
        'Fiz a anamnese e a entrevista aberta antes de aplicar qualquer escala.',
        'Pedi ao paciente um registro diário (EMA) por pelo menos duas semanas antes de fechar o plano.',
        'Procurei nos registros o padrão de hora, lugar e estado emocional que precede o uso.',
        'Comparei o que a EMA mostrou com o que o paciente relatou nas sessões, e anotei as diferenças.',
        'Escolhi a escala pela pergunta: grau geral (EDTec), jogos (IGD-20), gravidade de jogo de azar (G-SAS), crenças (GRCS).',
        'Ajustei o plano ao padrão encontrado, e não ao relato genérico de uso excessivo.',
        'Mantive alguma forma de monitoramento contínuo durante o tratamento, para ajustar semana a semana.',
    ],
    'questoes': [
        'Descreva o esquema de formulação de caso do vídeo e diga qual método de coleta alimenta cada uma das caixas da esquerda.',
        'O que é a avaliação ecológica momentânea e por que ela reduz o viés de memória dos autorrelatos?',
        'No caso do vídeo, o que a EMA revelou que o paciente não havia relatado, e como isso mudou o plano?',
        'Quais são os cinco instrumentos apresentados, e o que cada um mede?',
        'Por que a GRCS é o instrumento que melhor conversa com a primeira tarefa clínica do vídeo 5?',
        'Pense num paciente teu com uso problemático de tecnologia. O que tu sabe por relato e o que só uma EMA mostraria? Como tu montaria esse registro?',
    ],
    'gabarito': {
     0: (C, u"Fatores predisponentes e precipitantes alimentam um modelo psicoterapêutico, que explica os problemas do paciente; o conjunto é o plano de tratamento. Os predisponentes (história, temperamento, contexto) se preenchem com entrevistas abertas, anamnese e observação comportamental; os precipitantes (o que dispara cada episódio) se preenchem com a avaliação ecológica momentânea, porque dependem de hora, lugar e estado, e a memória retrospectiva não os guarda bem."),
     1: (C, u"É a coleta de dados no ambiente natural da pessoa, próxima do momento em que o comportamento e a emoção acontecem (na EMA-DT, uma vez ao dia, sobre o dia). Reduz o viés de memória porque pergunta pelo recente em vez de pedir que a pessoa reconstrua semanas de uso na sessão, o que costuma sair suavizado, arredondado ou simplesmente errado."),
     2: (C, u"Que o uso excessivo de redes ocorria no quarto, entre 23h e 1h, depois de episódios de ansiedade noturna ligados ao trabalho do dia seguinte, com pico de desejo e ansiedade nos domingos à noite e em vésperas de reuniões. O plano passou a incluir regulação emocional nas noites de domingo, manejo das antecipações negativas, mindfulness antes de dormir, estratégias alternativas para a hora crítica, resolução de problemas e monitoramento semanal da adesão."),
     3: (C, u"EMA-DT: registro diário de tempo, finalidade, estado emocional, impulsividade e impacto funcional. EDTec: grau de dependência tecnológica, 15 itens em cinco dimensões. IGD-20: presença e gravidade do transtorno de jogos pela internet nos últimos 12 meses, nas dimensões de saliência, modificação de humor, tolerância, abstinência, conflito e recaída. G-SAS: gravidade dos sintomas de jogo de azar na última semana (vontade, pensamentos, comportamento, consequências emocionais). GRCS: crenças sobre o jogo de azar em cinco domínios (expectativas, ilusão de controle, controle preditivo, incapacidade de parar, viés interpretativo)."),
     4: (C, u"Porque a primeira tarefa do vídeo 5 é desfazer a ideia de que o jogo depende de sorte, azar ou método, e a GRCS mede exatamente essas crenças (ilusão de controle, controle preditivo, expectativas). Ela confirma o alvo, mostra em que domínio a crença está mais forte e permite medir se a intervenção mexeu nela."),
     5: (K, u"Não há resposta certa. Uma boa resposta separa com clareza o que o relato já deu (história, contexto, quanto a pessoa diz que usa, o que perdeu) do que só o registro no momento daria (hora, lugar, estado antes e depois, o que a pessoa estava evitando), e descreve um registro viável: poucas perguntas, uma vez ao dia, no celular ou no papel, por duas semanas, com data para olhar junto. O erro comum é montar um diário longo demais, que o paciente abandona no terceiro dia."),
    },
    'referencias': [
        "Kim, S. W., Grant, J. E., Potenza, M. N., Blanco, C., &amp; Hollander, E. (2009). The Gambling Symptom Assessment Scale (G-SAS): A reliability and validity study. <em>Psychiatry Research, 166</em>(1), 76–84.",
        "Pontes, H. M., Király, O., Demetrovics, Z., &amp; Griffiths, M. D. (2014). The conceptualisation and measurement of DSM-5 Internet Gaming Disorder: The development of the IGD-20 Test. <em>PLoS ONE, 9</em>(10), e110137.",
        "Raylu, N., &amp; Oei, T. P. S. (2004). The Gambling Related Cognitions Scale (GRCS): Development, confirmatory factor validation and psychometric properties. <em>Addiction, 99</em>(6), 757–769.",
        "Shiffman, S., Stone, A. A., &amp; Hufford, M. R. (2008). Ecological momentary assessment. <em>Annual Review of Clinical Psychology, 4</em>, 1–32.",
        "Persons, J. B. (2008). <em>The case formulation approach to cognitive-behavior therapy.</em> Guilford Press.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o sétimo vídeo de uma disciplina de pós-graduação; as etapas do processo interventivo vêm no vídeo 8.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. A leitura da vinheta pelos critérios, o quadro "qual usar" e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina. A figura do esquema de formulação foi redesenhada com as duas setas de coleta que o slide acrescenta.<br><br><strong>Sobre os instrumentos.</strong> IGD-20, G-SAS e GRCS têm desenvolvimento e validação publicados e estão nas referências. A EMA-DT e a EDTec são apresentadas nos slides como instrumentos desenvolvidos para a disciplina; o material as descreve como os slides as apresentam e não encontrou dados psicométricos publicados, o que não as invalida como ferramenta clínica de registro, mas pede cautela para usá-las como medida de gravidade comparável entre pacientes. O FormulaPsi e a HumanTrack são ferramentas citadas no vídeo, com link; o material as descreve sem avaliá-las.<br><br><strong>Sobre o caso.</strong> Gustavo é vinheta didática dos slides, e o exemplo de EMA (uso no quarto entre 23h e 1h) é apresentado no slide como caso ilustrativo. Nenhum dado de paciente real entrou no material.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'FORM': FORM, 'ESCALAS': ESCALAS}
DT7['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DT7['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT7['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT7, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT7)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT7['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
