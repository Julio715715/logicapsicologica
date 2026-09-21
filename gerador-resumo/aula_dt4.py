# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 4: Impactos na saúde. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

ANTES_DEPOIS = u"""<figure class='dg'><div class='dg-t'>O que vem antes e o que vem depois (Krossbakken et al., 2018)</div>
<svg viewBox='0 0 720 190' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Três colunas: fatores que antecedem a dependência de jogos, a dependência no centro, e consequências; depressão e solidão aparecem nos dois lados'>
<defs><marker id='ad' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='20' width='210' height='130' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='16' y='44' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>ANTECEDE</text>
<text x='16' y='72' %(F)s font-size='12' fill='#2f2e24'>agressividade física</text>
<text x='16' y='96' %(F)s font-size='12' fill='#2f2e24'>depressão</text>
<text x='16' y='120' %(F)s font-size='12' fill='#2f2e24'>solidão</text>
<path d='M214 85 L250 85' stroke='#8d876f' stroke-width='2' marker-end='url(#ad)'/>
<rect x='256' y='40' width='208' height='90' rx='10' fill='#43441f'/>
<text x='360' y='74' text-anchor='middle' %(F)s font-size='12.5' font-weight='800' fill='#f0ede0'>dependência de jogos</text>
<text x='360' y='96' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>estabilidade de 35%% em 3 anos</text>
<text x='360' y='113' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>em muitos casos, não passa sozinha</text>
<path d='M468 85 L504 85' stroke='#8d876f' stroke-width='2' marker-end='url(#ad)'/>
<rect x='510' y='20' width='210' height='130' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='526' y='44' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>CONSEQUÊNCIA</text>
<text x='526' y='72' %(F)s font-size='12' fill='#2f2e24'>ansiedade</text>
<text x='526' y='96' %(F)s font-size='12' fill='#2f2e24'>depressão</text>
<text x='526' y='120' %(F)s font-size='12' fill='#2f2e24'>solidão</text>
<text x='360' y='176' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#8d876f'>associados, sem direção definida: alto consumo de álcool</text>
</svg>
<figcaption>Depressão e solidão aparecem dos dois lados: são causa e consequência. É a alça que a formulação precisa desenhar, e não uma linha reta.</figcaption></figure>""" % dict(F=F)

COMORB = u"""<figure class='dg'><div class='dg-t'>Dez quadros que cercam o uso problemático</div>
<svg viewBox='0 0 720 300' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Dez comorbidades e a função que o uso de tecnologia cumpre em cada uma'>
<rect x='0' y='6' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='10' y='26' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>Ansiedade social</text>
<text x='10' y='46' %(F)s font-size='9.5' fill='#6c6a55'>substitui interação real</text>
<text x='10' y='60' %(F)s font-size='9.5' fill='#6c6a55'>por ambiente mais</text>
<text x='10' y='74' %(F)s font-size='9.5' fill='#6c6a55'>controlável</text>
<rect x='145' y='6' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='155' y='26' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>TAG</text>
<text x='155' y='46' %(F)s font-size='9.5' fill='#6c6a55'>uso como evitação</text>
<text x='155' y='60' %(F)s font-size='9.5' fill='#6c6a55'>das preocupações</text>
<rect x='290' y='6' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='300' y='26' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>Pânico</text>
<text x='300' y='46' %(F)s font-size='9.5' fill='#6c6a55'>isolamento e</text>
<text x='300' y='60' %(F)s font-size='9.5' fill='#6c6a55'>desregulação piorados</text>
<text x='300' y='74' %(F)s font-size='9.5' fill='#6c6a55'>por ciclos de uso</text>
<rect x='435' y='6' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='445' y='26' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>Depressão</text>
<text x='445' y='46' %(F)s font-size='9.5' fill='#6c6a55'>vazio, anedonia</text>
<text x='445' y='60' %(F)s font-size='9.5' fill='#6c6a55'>offline, isolamento</text>
<text x='445' y='74' %(F)s font-size='9.5' fill='#6c6a55'>prolongado</text>
<rect x='580' y='6' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='590' y='26' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>T. alimentares</text>
<text x='590' y='46' %(F)s font-size='9.5' fill='#6c6a55'>redes, autoimagem,</text>
<text x='590' y='60' %(F)s font-size='9.5' fill='#6c6a55'>comparação e</text>
<text x='590' y='74' %(F)s font-size='9.5' fill='#6c6a55'>compensação</text>
<rect x='0' y='100' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='10' y='120' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>TDAH</text>
<text x='10' y='140' %(F)s font-size='9.5' fill='#6c6a55'>busca de reforço</text>
<text x='10' y='154' %(F)s font-size='9.5' fill='#6c6a55'>imediato: jogos,</text>
<text x='10' y='168' %(F)s font-size='9.5' fill='#6c6a55'>vídeos curtos</text>
<rect x='145' y='100' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='155' y='120' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>TOC</text>
<text x='155' y='140' %(F)s font-size='9.5' fill='#6c6a55'>checagem repetida,</text>
<text x='155' y='154' %(F)s font-size='9.5' fill='#6c6a55'>obsessão por estar</text>
<text x='155' y='168' %(F)s font-size='9.5' fill='#6c6a55'>conectado</text>
<rect x='290' y='100' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='300' y='120' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>TEA</text>
<text x='300' y='140' %(F)s font-size='9.5' fill='#6c6a55'>preferência por</text>
<text x='300' y='154' %(F)s font-size='9.5' fill='#6c6a55'>interação mediada</text>
<text x='300' y='168' %(F)s font-size='9.5' fill='#6c6a55'>por tela</text>
<rect x='435' y='100' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='445' y='120' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>Controle de impulsos</text>
<text x='445' y='140' %(F)s font-size='9.5' fill='#6c6a55'>coexiste com gastos,</text>
<text x='445' y='154' %(F)s font-size='9.5' fill='#6c6a55'>apostas, compras</text>
<rect x='580' y='100' width='140' height='84' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='590' y='120' %(F)s font-size='10.5' font-weight='800' fill='#2f2e24'>Sono</text>
<text x='590' y='140' %(F)s font-size='9.5' fill='#6c6a55'>insônia, atraso de</text>
<text x='590' y='154' %(F)s font-size='9.5' fill='#6c6a55'>fase, sonolência</text>
<text x='590' y='168' %(F)s font-size='9.5' fill='#6c6a55'>diurna</text>
<rect x='120' y='210' width='480' height='74' rx='11' fill='#43441f'/>
<text x='360' y='240' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#f0ede0'>em quase todas, a tela cumpre função para o quadro</text>
<text x='360' y='262' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>evitar, regular, substituir, estimular. Tratar a tela sem tratar a função não segura.</text>
</svg>
<figcaption>A tabela dos slides, lida pela função. Não é uma lista de diagnósticos que "acompanham" o uso; é uma lista do que o uso está fazendo por cada um deles.</figcaption></figure>""" % dict(F=F)

DT4 = {
    'slug': 'aula4',
    'titulo_txt': 'Impactos na saúde: o que o uso problemático custa e o que ele acompanha',
    'titulo_html': 'Impactos na sa&uacute;de: o que o uso problem&aacute;tico custa e o que ele acompanha',
    'data': 'Vídeo 4',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 4',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 4 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 4',
    'chave': 'mat-Aula-DT4-',
    'arquivo': 'Aula-DT4-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do quarto vídeo da "
              u"disciplina, sobre os impactos do uso problemático de tecnologia na saúde. Não havia transcrição.</p>"
              u"<p>Os três estudos mostrados nos slides foram localizados e estão nas referências. Duas moderações empíricas "
              u"estão sinalizadas no corpo do texto, e uma delas mexe numa afirmação forte do slide (a relação causal entre redes sociais e depressão).</p></div>"),
    'tema': 'Cinco mudanças de comportamento, um retrato do tempo de uso, dez comorbidades lidas pela função, e três estudos sobre '
            'jogos que mostram o que vem antes, o que vem depois e o que não passa sozinho.',
    'essencial': [
        ('O impacto se mede em função, não em horas.',
         'Seis a sete horas por dia é a média global de adultos. O que prejudica é o que a tela substitui e o que ela regula.'),
        ('Depressão e solidão são causa e consequência.',
         'No estudo longitudinal, aparecem dos dois lados da dependência de jogos. A formulação precisa de alça, e não de seta.'),
        ('Um terço não passa sozinho.',
         'Estabilidade de 35% em três anos: em muitos adolescentes o quadro persiste sem melhora espontânea. Esperar crescer não é plano.'),
        ('A comorbidade quase sempre explica a função do uso.',
         'Ansiedade social, TAG, depressão, TDAH, TEA, sono: em cada uma a tela evita, regula, substitui ou estimula algo.'),
        ('Causalidade entre redes e depressão é hipótese forte, não fato.',
         'A associação existe e é pequena em amostras grandes; a direção é disputada. Dá para dizer que redes pioram autoimagem em quem já se compara.'),
    ],
    'secoes': [
        ('s0', 'Cinco mudanças de comportamento', 'Cinco mudanças de comportamento', u"""
<p>O vídeo abre com o que a tecnologia moderna mudou no comportamento individual, em cinco blocos.</p>
<ul class='key'><li><b>Novos velhos vícios</b>: internet, pornografia, videogames, smartphones, redes sociais, apostas digitais. O objeto é novo; o mecanismo, como os vídeos 1 e 2 mostraram, é antigo.</li><li><b>Interações sociais e humor</b>: isolamento e solidão, vulnerabilidade, cyberbullying, hábitos de sono e irritação.</li><li><b>Menos inibidos</b>: o efeito de desinibição online. As pessoas ficam demasiadamente confiantes e ingênuas, ou agressivas e críticas, de um jeito que não seriam presencialmente.</li><li><b>Dessensibilização ao absurdo</b>: notícias de tragédia e de homicídio se espalham tão rápido que viram comuns.</li><li><b>Saúde mental e redes sociais</b>: o slide afirma relação causal entre depressão, redes sociais e problemas de autoimagem em jovens.</li></ul>
<div class='obs'><h4>Uma moderação, e ela importa</h4><p>A palavra <em>causal</em> no último bloco é mais forte do que a evidência autoriza. Em amostras grandes, a associação entre uso de redes e bem-estar é pequena, e a direção é disputada: jovens deprimidos usam mais, e o uso pode piorar o humor, nas duas ordens. O que se sustenta melhor é o efeito da <strong>comparação social</strong> e do uso passivo sobre a autoimagem, em quem já se compara. A afirmação defensável: redes sociais são fator de risco e de manutenção para problemas de autoimagem e humor em jovens, com efeito modesto na média e grande em subgrupos. O texto segue com essa formulação.</p></div>
"""),
        ('s1', 'Quanto tempo a gente passa online', 'Quanto tempo a gente passa online', u"""
<p>O slide traz o levantamento global de janeiro de 2023 (GWI, via DataReportal): tempo médio diário de uso da internet, em qualquer dispositivo, por faixa etária. Entre 16 e 24 anos, cerca de <strong>sete horas e meia</strong> por dia para mulheres e pouco mais de sete para homens. A média cai com a idade, mas mesmo entre 55 e 64 anos passa de cinco horas.</p>
<p>O ponto pedagógico não é assustar com o número. É lembrar que sete horas é a <strong>média</strong>, ou seja, é o normal estatístico. Uso problemático não se define por estar acima dela (vídeo 3), e sim pelo que essas horas substituem e pelo que elas regulam.</p>
<h3>O que elas substituem</h3>
<p>O gráfico seguinte, do levantamento norte-americano <em>Monitoring the Future</em>, mostra a proporção de estudantes que encontram amigos "quase todo dia" fora da escola, de 1991 a 2017. A queda é gradual até 2010 e acelera depois, na faixa que o slide marca como o avanço dos smartphones, chegando perto de 25% entre as meninas.</p>
<div class='callout note'><div class='co-t'>Como ler o gráfico</div>É uma correlação temporal, e o próprio gráfico mostra que a queda começou antes dos smartphones. O que ele sustenta com segurança é o deslocamento: a interação presencial caiu enquanto a mediada por tela subiu. Para a clínica, é o dado que mais importa, porque o que se perde na presença (leitura de rosto, tolerância a conflito, habilidades sociais do vídeo 1) não se recupera na tela.</div>
"""),
        ('s2', 'Dez comorbidades, lidas pela função', 'Dez comorbidades, lidas pela função', u"""
{{COMORB}}
<p>A tabela dos slides lista dez quadros que aparecem junto com o uso problemático. Vale ler cada célula não como "diagnóstico que acompanha", mas como <strong>função que a tela cumpre para aquele quadro</strong>.</p>
<ul class='key'><li><b>Ansiedade social</b>: muito prevalente em jovens que substituem interações reais por ambientes virtuais mais controláveis.</li><li><b>Ansiedade generalizada</b>: o uso excessivo funciona como evitação das preocupações.</li><li><b>Pânico</b>: isolamento e desregulação emocional exacerbados por ciclos de uso compulsivo.</li><li><b>Depressão maior</b>: sensação de vazio, falta de prazer nas atividades offline, isolamento prolongado.</li><li><b>Transtornos alimentares</b>: uso compulsivo de redes associado a distorção da autoimagem, comparação social e comportamentos compensatórios.</li><li><b>TDAH</b>: busca de estimulação rápida, o que torna a pessoa mais suscetível a conteúdos de reforço imediato, como jogos e vídeos curtos.</li><li><b>TOC</b>: uso repetitivo, mesmo com consciência do prejuízo, pode mimetizar padrões compulsivos; obsessões sobre estar conectado e checar notificações.</li><li><b>TEA</b>: preferência por interações mediadas por tela, que pode evoluir para uso problemático de jogos e vídeos.</li><li><b>Controle de impulsos</b>: a própria dependência tecnológica é vista como quadro impulsivo-compulsivo e pode coexistir com gastos excessivos, apostas e compras.</li><li><b>Sono</b>: insônia, atraso de fase, sonolência diurna, sobretudo em quem usa o aparelho na cama.</li></ul>
<p>A consequência para a avaliação é direta: quando a comorbidade é identificada, a pergunta seguinte é <strong>o que a tela faz por ela</strong>. É essa resposta que vira alvo, e não a tela.</p>
"""),
        ('s3', 'Jogos: o que vem antes e o que vem depois', 'Jogos: o que vem antes e o que vem depois', u"""
<p>Os slides trazem três estudos sobre o transtorno de jogo, e o primeiro é o mais útil porque é longitudinal. Krossbakken e colegas acompanharam adolescentes noruegueses por <strong>três anos</strong>, com um desenho de painéis cruzados, que permite perguntar o que precede o quê.</p>
{{ANTES_DEPOIS}}
<ul class='key'><li><b>Depressão e solidão</b> são tanto causas quanto consequências do uso patológico de jogos.</li><li><b>Agressividade física</b> é fator que antecede a dependência.</li><li><b>Ansiedade</b> aparece como consequência direta.</li><li><b>Alto consumo de álcool</b> está associado a jogadores dependentes.</li><li>A <b>solidão</b> tende a aumentar entre jogadores problemáticos, mesmo os que não fecham critérios.</li><li>A dependência tem <b>estabilidade de 35%</b>: em muitos casos, persiste por anos sem melhora espontânea.</li></ul>
<div class='callout note'><div class='co-t'>Para a formulação</div>Depressão e solidão nos dois lados é o retrato de uma alça de manutenção: a pessoa joga para não sentir, e jogar isola, e isolar deprime. A agressividade como antecedente pede outra pergunta: o jogo está regulando raiva? E os 35% dizem que esperar o adolescente "crescer e largar" é aposta que perde uma vez em três.</div>
"""),
        ('s4', 'Jogos: o retrato transversal e o que se sabe de intervenção', 'Jogos: o retrato transversal e o que se sabe de intervenção', u"""
<h3>Correlatos psicossociais</h3>
<p>Bargeron e Hormes aplicaram os critérios propostos pelo DSM-5 a 257 jogadores frequentes. <strong>8,7%</strong> preencheram critérios para o transtorno. Esses jogavam com mais frequência e por mais horas consecutivas, sentiam impulsos subjetivos fortes para continuar, tinham mais depressão, ansiedade e estresse, menor satisfação com a vida e autoestima mais baixa, e mais <strong>impulsividade</strong> motora e atencional.</p>
<p>É um estudo transversal, então descreve o perfil de quem fecha critérios, sem dizer o que veio primeiro. Combinado com o anterior, ajuda a montar o quadro: impulsividade e agressividade como terreno, depressão e solidão como alça, ansiedade como custo.</p>
<h3>Intervenção em adolescentes</h3>
<p>A revisão sistemática mostrada no slide reúne o que se sabe de intervenção para dependência de jogos em adolescentes. Os pontos que a aula destacou: a inclusão do transtorno no DSM-5 incentivou pesquisa e reconheceu que o quadro compartilha sintomas com dependência de substâncias, como compulsão e perda de controle; crianças e adolescentes são os mais vulneráveis, pela atratividade dos jogos e pelo sistema de recompensa embutido neles; a pandemia agravou a situação; a causa do transtorno não está clara, mas fatores psicológicos como <strong>baixa autorregulação</strong> e a <strong>motivação para jogar</strong> estão relacionados; e há poucos estudos de prevenção.</p>
<div class='obs'><h4>Uma moderação sobre a fonte</h4><p>A revisão citada foi publicada num periódico de menor circulação e reúne poucos estudos. O que ela diz coincide com revisões maiores (a evidência de tratamento é majoritariamente cognitivo-comportamental, com ensaios pequenos e seguimento curto, e a prevenção é o buraco), e é por isso que o texto mantém as conclusões, mas com esse peso.</p></div>
"""),
        ('s5', 'Os quatro sinais e o que fazer com eles', 'Os quatro sinais e o que fazer com eles', u"""
<p>O vídeo fecha com uma frase e quatro sinais. A frase: apesar dos inúmeros benefícios da internet, essas atividades também podem prejudicar a saúde e o desenvolvimento. Os sinais:</p>
<ul class='key'><li>Precisar de <b>cada vez mais tempo</b> para jogar ou estar online.</li><li>Ser <b>incapaz de se controlar</b> ao tentar reduzir ou interromper o uso.</li><li>Apresentar <b>inquietação, nervosismo, ansiedade, mau humor ou depressão</b> ao tentar diminuir o tempo de uso.</li><li>Usar a internet como forma constante de <b>escapar</b> de problemas ou de lidar com dificuldades emocionais.</li></ul>
<p>Repare que os quatro são critérios do DSM-5-TR do vídeo 3, na ordem: tolerância, perda de controle, abstinência e uso para escapar. O último é o que mais conversa com este vídeo: se a tela é a forma constante de lidar com dificuldade emocional, a dificuldade emocional é o alvo, e as comorbidades da seção 3 dizem qual.</p>
<div class='callout note'><div class='co-t'>Leitura em processos</div>Os impactos deste vídeo (isolamento, sono, humor, autoimagem) são ao mesmo tempo consequência do uso e combustível dele. Na rede do caso, isso aparece como alças: uso, isolamento, solidão, uso. A intervenção que quebra a alça raramente é sobre a tela; é sobre o que entra no lugar dela quando ela sai.</div>
<h3>O que vem no próximo vídeo</h3>
<p>Os critérios diagnósticos do transtorno do jogo.</p>
"""),
    ],
    'checklist': [
        'Avaliei o que as horas de tela substituem e o que regulam, e não só quantas são.',
        'Para cada comorbidade identificada, perguntei o que a tela faz por ela.',
        'Desenhei a alça uso, isolamento, solidão, uso, em vez de uma seta de causa única.',
        'Investiguei agressividade e impulsividade como terreno anterior ao uso.',
        'Avaliei sono como alvo próprio, e não como efeito colateral.',
        'Evitei dizer ao paciente ou à família que redes sociais "causam" depressão; falei em risco e manutenção.',
        'Não contei com melhora espontânea em adolescente com quadro instalado.',
        'Verifiquei os quatro sinais: tempo crescente, perda de controle, mal-estar ao reduzir, uso para escapar.',
    ],
    'questoes': [
        'Quais são as cinco mudanças de comportamento listadas no vídeo, e qual delas pede moderação empírica? Por quê?',
        'O que o estudo longitudinal de três anos mostra sobre depressão e solidão, e o que isso muda na formulação?',
        'O que significa a estabilidade de 35% da dependência de jogos em adolescentes, na prática?',
        'Escolha três comorbidades da tabela e descreva a função que o uso de tecnologia cumpre em cada uma.',
        'Pense num paciente teu. Que alça de manutenção liga o uso dele aos impactos deste vídeo, e por onde tu entraria?',
        'Como tu responderia a um pai que pergunta se o celular causou a depressão do filho?',
    ],
    'gabarito': {
     0: (C, u"Novos velhos vícios; interações sociais e humor; menos inibidos (efeito de desinibição); dessensibilização ao absurdo; saúde mental e redes sociais. A última pede moderação: o slide fala em relação causal, e a evidência sustenta associação pequena na média, com direção disputada, e efeito mais claro da comparação social sobre a autoimagem em subgrupos. A formulação defensável é fator de risco e de manutenção, não causa."),
     1: (C, u"Que depressão e solidão aparecem <b>dos dois lados</b>: antecedem a dependência de jogos e são consequência dela. Na formulação, isso vira alça de manutenção (jogar para não sentir, isolar, deprimir, jogar) e não seta única. O estudo também mostra agressividade como antecedente e ansiedade como consequência, o que orienta o que investigar antes e o que esperar depois."),
     2: (C, u"Que, em três anos, cerca de um terço dos adolescentes com dependência de jogos continuava com o quadro, sem melhora espontânea. Na prática, esperar que o jovem cresça e largue é uma aposta que perde uma em três vezes, e o quadro instalado merece intervenção, e não observação."),
     3: (K, u"Não há resposta certa. Uma boa resposta escolhe três quadros e nomeia a função em cada um com precisão: por exemplo, na ansiedade social a tela substitui a interação real por uma controlável; na TAG, evita as preocupações; no TDAH, entrega o reforço rápido que a pessoa busca; no sono, o uso na cama atrasa a fase. O erro comum é descrever a comorbidade e a tela lado a lado sem dizer o que uma faz pela outra."),
     4: (K, u"Não há resposta certa. Uma boa resposta desenha a alça com os elementos deste vídeo (uso, isolamento, sono, humor, autoimagem) e escolhe o ponto de entrada pela função e pelo acesso: o que sai da tela e o que entra no lugar. O erro comum é entrar pela redução de horas, que costuma quebrar a alça só enquanto o terapeuta está olhando."),
     5: (K, u"Não há resposta certa. Uma boa resposta valida a preocupação, evita o \"sim\" e o \"não\", e explica que o uso costuma ser ao mesmo tempo consequência e combustível do humor: o filho usa mais porque está mal, e usar mais isola e piora. Depois reorienta para o que se pode fazer com a alça, em vez de para a culpa do aparelho. O erro comum é confirmar a causalidade para tranquilizar o pai."),
    },
    'referencias': [
        "Bargeron, A. H., &amp; Hormes, J. M. (2017). Psychosocial correlates of internet gaming disorder: Psychopathology, life satisfaction, and impulsivity. <em>Computers in Human Behavior, 68</em>, 388–394.",
        "Kemp, S. (2023). <em>Digital 2023: Global overview report.</em> DataReportal / We Are Social / Meltwater, com dados da GWI.",
        "Krossbakken, E., Pallesen, S., Mentzoni, R. A., King, D. L., Molde, H., Finser&aring;s, T. R., &amp; Torsheim, T. (2018). A cross-lagged study of developmental trajectories of video game engagement, addiction, and mental health. <em>Frontiers in Psychology, 9</em>, 2239.",
        "Orben, A., &amp; Przybylski, A. K. (2019). The association between adolescent well-being and digital technology use. <em>Nature Human Behaviour, 3</em>(2), 173–182.",
        "Stevens, M. W. R., King, D. L., Dorstyn, D., &amp; Delfabbro, P. H. (2019). Cognitive-behavioral therapy for internet gaming disorder: A systematic review and meta-analysis. <em>Clinical Psychology &amp; Psychotherapy, 26</em>(2), 191–203.",
        "Suler, J. (2004). The online disinhibition effect. <em>CyberPsychology &amp; Behavior, 7</em>(3), 321–326.",
        "Twenge, J. M. (2017). <em>iGen.</em> Atria Books. (Fonte do gráfico de encontros com amigos, a partir do levantamento Monitoring the Future.)",
        "Effect of intervention for gaming addiction among adolescents: A systematic review. (2022). <em>International Journal of Health Sciences, 6</em>(S3). https://doi.org/10.53730/ijhs.v6nS3.8718",
    ],
    'nota': u"""Material dirigido a psicólogos. É o quarto vídeo de uma disciplina de pós-graduação; avaliação e intervenção vêm nos vídeos seguintes.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. Os três estudos mostrados foram localizados: Krossbakken et al. (2018), Bargeron e Hormes (2017) e a revisão de 2022, esta citada por título e DOI porque a autoria não pôde ser conferida. A leitura das comorbidades pela função e a seção final em processos foram desenvolvidas pelo autor do material a partir da lógica da disciplina.<br><br><strong>Duas moderações, sinalizadas no texto.</strong> Primeira, e a mais importante: o slide afirma relação causal entre redes sociais e depressão em jovens; a evidência sustenta associação pequena na média, com direção disputada, e efeito mais claro da comparação social sobre a autoimagem; o texto usa a formulação de fator de risco e de manutenção. Segunda: a revisão sistemática sobre intervenção em adolescentes vem de um periódico de menor circulação e reúne poucos estudos; suas conclusões coincidem com revisões maiores e foram mantidas com esse peso. O gráfico de encontros com amigos foi descrito como o que é, uma série temporal cuja queda começa antes dos smartphones.<br><br><strong>Acréscimos.</strong> As referências do efeito de desinibição, da fonte do gráfico, da associação uso e bem-estar e da metanálise de TCC para transtorno de jogo foram acrescentadas para dar respaldo ao que os slides afirmam sem citação. Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'ANTES_DEPOIS': ANTES_DEPOIS, 'COMORB': COMORB}
DT4['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DT4['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT4['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT4, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT4)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT4['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
