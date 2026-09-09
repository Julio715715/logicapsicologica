# -*- coding: utf-8 -*-
"""Edição 1 (definitiva) da newsletter — página do site.
Substitui os itens de teste de newsletter/2026-09/index.html, o cabeçalho da
edição, o índice lateral, o card em newsletter/index.html, o bloco da home e o
nome da seção em todas as páginas."""
import io, re

SITE = '/home/claude/site'
FT = "font-family='Plus Jakarta Sans,sans-serif'"
NOME_ANTIGO = u"O que saiu no último mês"
NOME_NOVO = u"O que vale ler"

# ---------------------------------------------------------------- figuras
FIG_ARTMED = u"""<figure class='nwfig'><svg viewBox='0 0 720 190' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Sete convidados agrupados por processo: relação, formulação, transdiagnóstico e implementação'>
<rect x='0' y='6' width='226' height='176' rx='11' fill='#F1ECE0' stroke='#9ca575' stroke-width='1.4'/>
<text x='20' y='32' %(F)s font-size='11' font-weight='800' letter-spacing='1.4' fill='#a8894f'>RELAÇÃO</text>
<text x='20' y='60' %(F)s font-size='13' font-weight='800' fill='#2f2e24'>Mavis Tsai</text>
<text x='20' y='77' %(F)s font-size='11.5' fill='#6c6a55'>FAP, relação como alvo</text>
<text x='20' y='104' %(F)s font-size='13' font-weight='800' fill='#2f2e24'>William Miller</text>
<text x='20' y='121' %(F)s font-size='11.5' fill='#6c6a55'>habilidades do terapeuta eficaz</text>
<text x='20' y='148' %(F)s font-size='13' font-weight='800' fill='#2f2e24'>Peter Fonagy</text>
<text x='20' y='165' %(F)s font-size='11.5' fill='#6c6a55'>mentalização, aqui e agora</text>
<rect x='247' y='6' width='226' height='176' rx='11' fill='#FFFDF7' stroke='#43441f' stroke-width='1.6'/>
<text x='267' y='32' %(F)s font-size='11' font-weight='800' letter-spacing='1.4' fill='#43441f'>FORMULAÇÃO</text>
<text x='267' y='60' %(F)s font-size='13' font-weight='800' fill='#2f2e24'>Stefan Hofmann</text>
<text x='267' y='77' %(F)s font-size='11.5' fill='#6c6a55'>raciocínio clínico, personalização</text>
<text x='267' y='104' %(F)s font-size='13' font-weight='800' fill='#2f2e24'>Robert Leahy</text>
<text x='267' y='121' %(F)s font-size='11.5' fill='#6c6a55'>formulação de caso como competência</text>
<text x='267' y='156' %(F)s font-size='11.5' font-style='italic' fill='#43441f'>o terreno da TBP</text>
<rect x='494' y='6' width='226' height='176' rx='11' fill='#F1ECE0' stroke='#9ca575' stroke-width='1.4'/>
<text x='514' y='32' %(F)s font-size='11' font-weight='800' letter-spacing='1.4' fill='#a8894f'>TRANSDIAGNÓSTICO</text>
<text x='514' y='60' %(F)s font-size='13' font-weight='800' fill='#2f2e24'>David Barlow</text>
<text x='514' y='77' %(F)s font-size='11.5' fill='#6c6a55'>Protocolo Unificado</text>
<text x='514' y='104' %(F)s font-size='13' font-weight='800' fill='#2f2e24'>Luana Marques</text>
<text x='514' y='121' %(F)s font-size='11.5' fill='#6c6a55'>implementação, Harvard</text>
</svg>
<figcaption>Os sete convidados, agrupados pelo tema anunciado de cada um. As três colunas conversam entre si: relação, formulação e transdiagnóstico são camadas do mesmo raciocínio.</figcaption></figure>""" % dict(F=FT)

FIG_REDE = u"""<figure class='nwfig'><svg viewBox='0 0 720 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Rede de três processos; intervir no nó mais central e no menos central produziu resultados sem diferença clara'>
<line x1='80' y1='66' x2='180' y2='146' stroke='#c9c2a8' stroke-width='2.4'/>
<line x1='80' y1='66' x2='180' y2='52' stroke='#c9c2a8' stroke-width='4'/>
<line x1='180' y1='52' x2='180' y2='146' stroke='#c9c2a8' stroke-width='2'/>
<circle cx='180' cy='52' r='27' fill='#43441f'/>
<text x='180' y='56' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#f0ede0'>abertura</text>
<circle cx='80' cy='66' r='23' fill='#EFE7D3' stroke='#9ca575' stroke-width='1.6'/>
<text x='80' y='70' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>atenção</text>
<circle cx='180' cy='146' r='23' fill='#FFFDF7' stroke='#a05a3c' stroke-width='1.8'/>
<text x='180' y='150' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>engajar</text>
<text x='218' y='38' %(F)s font-size='11' font-weight='800' fill='#43441f'>mais central</text>
<text x='218' y='160' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>menos central</text>
<text x='40' y='192' %(F)s font-size='10.5' font-style='italic' fill='#8d876f'>exemplo de uma rede; a de cada participante era diferente</text>
<defs><marker id='a' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#43441f'/></marker>
<marker id='b' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#a05a3c'/></marker></defs>
<text x='330' y='44' %(F)s font-size='10.5' fill='#6c6a55'>2 semanas</text>
<path d='M330 58 L400 58' stroke='#43441f' stroke-width='2.2' marker-end='url(#a)'/>
<text x='330' y='138' %(F)s font-size='10.5' fill='#6c6a55'>2 semanas</text>
<path d='M330 152 L400 152' stroke='#a05a3c' stroke-width='2.2' marker-end='url(#b)'/>
<rect x='420' y='22' width='300' height='160' rx='11' fill='#FFFDF7' stroke='#EFE7D3' stroke-width='1.4'/>
<text x='440' y='48' %(F)s font-size='11' font-weight='800' letter-spacing='1.4' fill='#a8894f'>O QUE APARECEU</text>
<text x='440' y='76' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>4 de 6 melhoraram</text>
<text x='440' y='93' %(F)s font-size='11.5' fill='#6c6a55'>em interferência da dor</text>
<text x='440' y='120' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>sem fase claramente melhor</text>
<text x='440' y='137' %(F)s font-size='11.5' fill='#6c6a55'>num caso, o menos central rendeu mais</text>
<text x='440' y='166' %(F)s font-size='11.5' font-style='italic' fill='#a05a3c'>centralidade instável entre reestimações</text>
</svg>
<figcaption>A aposta era que tratar primeiro o nó mais central moveria mais a rede inteira. Com seis pessoas e duas semanas por alvo, a diferença não apareceu.</figcaption></figure>""" % dict(F=FT)

FOTO = u"""<figure class='nwfig nwfoto'><img src='/assets/julio-anos80.jpg' alt='Retrato do Prof. Júlio Gonçalves gerado por IA no estilo dos anos 80, num fliperama, com jaqueta jeans e revista MAD' loading='lazy'>
<figcaption>Eu também entrei na trend. Decididamente não me gostei, hehe.</figcaption></figure>"""

FIG_NOST = u"""<figure class='nwfig'><svg viewBox='0 0 720 210' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Ciclo da nostalgia: desconforto dispara a nostalgia, que devolve conexão, continuidade e sentido; a saída pode alimentar ação ou virar refúgio'>
<rect x='0' y='20' width='200' height='96' rx='11' fill='#FAF3EE' stroke='#a05a3c' stroke-width='1.4'/>
<text x='18' y='44' %(F)s font-size='11' font-weight='800' letter-spacing='1.4' fill='#a05a3c'>DISPARA</text>
<text x='18' y='66' %(F)s font-size='12' fill='#2f2e24'>solidão, tédio</text>
<text x='18' y='84' %(F)s font-size='12' fill='#2f2e24'>incerteza sobre si</text>
<text x='18' y='102' %(F)s font-size='12' fill='#2f2e24'>descontinuidade do self</text>
<path d='M204 68 L252 68' stroke='#8d876f' stroke-width='2' marker-end='url(#n1)'/>
<rect x='258' y='20' width='200' height='96' rx='11' fill='#43441f'/>
<text x='358' y='60' text-anchor='middle' %(F)s font-size='15' font-weight='800' fill='#f0ede0'>nostalgia</text>
<text x='358' y='82' text-anchor='middle' %(F)s font-size='11' fill='#9ca575'>lembrança de si com vínculos,</text>
<text x='358' y='98' text-anchor='middle' %(F)s font-size='11' fill='#9ca575'>numa época em que estava bem</text>
<path d='M462 68 L510 68' stroke='#8d876f' stroke-width='2' marker-end='url(#n1)'/>
<rect x='516' y='20' width='204' height='96' rx='11' fill='#F1ECE0' stroke='#9ca575' stroke-width='1.4'/>
<text x='534' y='44' %(F)s font-size='11' font-weight='800' letter-spacing='1.4' fill='#a8894f'>DEVOLVE</text>
<text x='534' y='66' %(F)s font-size='12' fill='#2f2e24'>conexão social</text>
<text x='534' y='84' %(F)s font-size='12' fill='#2f2e24'>continuidade do self</text>
<text x='534' y='102' %(F)s font-size='12' fill='#2f2e24'>sentido, otimismo</text>
<defs><marker id='n1' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<line x1='618' y1='118' x2='618' y2='134' stroke='#8d876f' stroke-width='2'/>
<line x1='428' y1='134' x2='630' y2='134' stroke='#8d876f' stroke-width='2'/>
<line x1='428' y1='134' x2='428' y2='152' stroke='#8d876f' stroke-width='2'/>
<line x1='630' y1='134' x2='630' y2='152' stroke='#8d876f' stroke-width='2'/>
<polygon points='422,152 434,152 428,160' fill='#8d876f'/>
<polygon points='624,152 636,152 630,160' fill='#8d876f'/>
<rect x='330' y='160' width='196' height='42' rx='9' fill='#eef1e4' stroke='#9ca575' stroke-width='1.3'/>
<text x='428' y='178' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#2f2e24'>alimenta ação no presente</text>
<text x='428' y='194' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>liga, retoma, procura gente</text>
<rect x='540' y='160' width='180' height='42' rx='9' fill='#FAF3EE' stroke='#a05a3c' stroke-width='1.3'/>
<text x='630' y='178' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#2f2e24'>vira refúgio do presente</text>
<text x='630' y='194' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>compara, se recolhe</text>
</svg>
<figcaption>O modelo regulatório de Sedikides e Wildschut: a nostalgia costuma responder a um desconforto e devolver o que faltava. O que interessa na clínica é a bifurcação de baixo.</figcaption></figure>""" % dict(F=FT)


def item(n, tipo, titulo, resumo, ficha, figura, clinica, limites, acao, pergunta, ref, url, rotulo):
    chips = ''.join(u"<span class='chip'><b>%s</b>%s</span>" % (a, b) for a, b in ficha)
    li = lambda xs: ''.join(u"<li>%s</li>" % x for x in xs)
    return u"""<article class='nw' id='i%(N)d'>
<div class='nw-k'>%(TIPO)s</div>
<h3>%(TITULO)s</h3>
<p class='nw-r'>%(RESUMO)s</p>
<details class='nw-d'><summary>Ler completo</summary><div class='nw-in'>
<div class='ficha'>%(CHIPS)s</div>
%(FIG)s
<div class='duo'>
<div class='nw-c'><b>Muda na clínica</b><ul>
%(CLI)s</ul></div>
<div class='nw-c lim'><b>Não autoriza dizer</b><ul>
%(LIM)s</ul></div>
</div>
<div class='nw-q'><span class='lb'>Ação para a clínica</span>
<p class='ac'>%(ACAO)s</p>
<p class='pg'><b>E uma pergunta</b>%(PERG)s</p></div>
<div class='nw-f'>%(REF)s <a href='%(URL)s' target='_blank' rel='noopener'>%(ROT)s &#8599;</a></div>
</div></details></article>""" % dict(N=n, TIPO=tipo, TITULO=titulo, RESUMO=resumo, CHIPS=chips,
                                     FIG=figura, CLI=li(clinica), LIM=li(limites), ACAO=acao,
                                     PERG=pergunta, REF=ref, URL=url, ROT=rotulo)


ITENS = [
 item(1, u"Agenda &middot; Artmed Experience, outubro",
   u"Sete nomes da psicoterapia mundial em São Paulo, com uma pergunta em comum",
   u"De 15 a 17 de outubro, o Artmed Experience reúne no Expo Center Norte Barlow, Leahy, Hofmann, Tsai, Fonagy, Miller e Luana Marques, com simulações clínicas ao vivo comentadas. O tema anunciado é <strong>o que diferencia terapeutas extraordinários</strong>. Para quem trabalha com processos, essa conversa já é de casa.",
   [(u"Quando", u"15 a 17 de outubro de 2026"), (u"Onde", u"Expo Center Norte, São Paulo"),
    (u"Formato", u"presencial, com tradução simultânea"), (u"Edição", u"segunda; a de 2025 teve Beck, Hayes e Hofmann")],
   FIG_ARTMED,
   [u"Os temas dos convidados convergem: relação terapêutica, formulação de caso e personalização do tratamento. É o terreno da Terapia Baseada em Processos tratado como centro da conversa, e por uma editora que fala com o mainstream.",
    u"Simulação comentada é treino de raciocínio clínico. Dá para observar, em tempo real, o momento em que o terapeuta escolhe um alvo e o que ele deixa de lado para escolher.",
    u"Miller, Tsai e Fonagy olham para a mesma variável por ângulos diferentes: o que o terapeuta faz dentro da sessão que muda o rumo do caso. Vale assistir aos três com essa pergunta na mão."],
   [u"Que o evento ensina TBP. Hofmann é um entre sete, e a programação fala de personalização e raciocínio clínico, e não de rede de processos.",
    u"Que assistir a quem faz muito bem transfere a habilidade. O que se leva embora depende do que se pratica com feedback depois.",
    u"Que faz sentido para qualquer momento de carreira: os ingressos partem de R$ 2.199, e os livros dos mesmos autores custam uma fração disso."],
   u"Antes do evento, escolha um caso seu e escreva em meia página o que você acha que um terapeuta muito bom faria de diferente nele: qual processo leria primeiro, que tipo de relação construiria, o que deixaria de fora. Se for, compare com cada simulação e anote o que você não tinha visto. Se não for, faça o mesmo exercício com uma sessão gravada sua.",
   u"Quando você diz que um terapeuta é bom, está descrevendo o que ele faz na sessão ou o quanto gosta dele?",
   u"Artmed Academy (2026). <em>Artmed Experience, edição 2026</em>. 15 a 17 de outubro, Expo Center Norte, São Paulo.",
   u"https://www.artmedacademy.com.br/experience", u"Ver o evento"),

 item(2, u"Experimento de caso único &middot; Frontiers in Psychology",
   u"Intervir no nó mais central da rede não rendeu mais do que intervir no menos central",
   u"Seis pessoas com dor crônica responderam a cinco medidas por dia durante semanas. Com essas séries, a equipe estimou a rede de inflexibilidade psicológica de cada uma e testou a hipótese da centralidade: tratar primeiro o processo mais central deveria mover mais a rede inteira. <strong>Não foi o que apareceu.</strong>",
   [(u"Desenho", u"caso único, linha de base múltipla"), (u"Participantes", u"6 analisados, de 16 que consentiram"),
    (u"Medida", u"EMA, 5 vezes ao dia"), (u"Intervenção", u"ACT online, duas fases de 2 semanas"), (u"Publicado", u"abril de 2026")],
   FIG_REDE,
   [u"A rede do caso segue valendo para formular. O que o estudo derruba é a promessa de que a estatística escolhe o alvo por você.",
    u"A centralidade estimada dos mesmos dados variou entre reestimações. Se o número muda de uma rodada para outra, ele não pode ser o único critério para escolher onde intervir.",
    u"Duas semanas por alvo foi pouco para separar efeitos. Na clínica, concluir que um alvo não funcionou também pede tempo, e um marcador combinado antes."],
   [u"Que redes idiográficas não servem: em análise exploratória, o próprio grupo achou sinal em outro modelo de rede, contemporâneo em tempo discreto.",
    u"Que vale para além de dor crônica e de ACT. São seis pessoas, um problema, uma abordagem, quatro semanas.",
    u"Que a ordem dos alvos tanto faz. O estudo não conseguiu discernir diferença, o que é diferente de mostrar equivalência."],
   u"Na próxima formulação em rede, registre por escrito por que você escolheu o alvo: centralidade (o que mais conecta), acesso (o que o paciente consegue mexer agora) ou função (o que sustenta o resto). Volte a essa nota em quatro semanas e veja qual dos três critérios previu melhor a mudança que aconteceu.",
   u"Quando o diagrama aponta um nó como central, você trata isso como hipótese a testar ou como decisão já tomada?",
   u"Lavefjord, A., Sundström, F. T. A., Preihs, L., Hammar, A., Forslund, S., Clason van de Leur, J., Scholten, S., Buhrman, M., &amp; McCracken, L. M. (2026). Examining the utility of process-focused data driven psychological networks for individualizing psychological treatment in chronic pain: a single case experiment testing the centrality hypothesis. <em>Frontiers in Psychology, 17</em>, 1809958.",
   u"https://doi.org/10.3389/fpsyg.2026.1809958", u"Ver o estudo"),

 item(3, u"Cultura &middot; a trend dos anos 80 e a pesquisa sobre nostalgia",
   u"Todo mundo virou anos 80 no feed. O que a nostalgia está fazendo por essas pessoas?",
   u"Na primeira semana de setembro o Instagram encheu de retratos gerados por IA com cabelo armado, grão de filme e cor desbotada, inclusive de quem nasceu depois de 1990. Uma revisão de Sedikides e Wildschut na <em>Emotion Review</em>, que reúne duas décadas de estudos experimentais sobre nostalgia, dá uma leitura que vai além da moda: <strong>a nostalgia costuma ser disparada por desconforto e devolve conexão, continuidade e sentido.</strong>",
   [(u"Fenômeno", u"trend “eu nos anos 80”"), (u"Ferramenta", u"ChatGPT ou Gemini, com foto e prompt"),
    (u"Quando", u"primeira semana de setembro de 2026"), (u"Base", u"Sedikides &amp; Wildschut, Emotion Review")],
   FOTO + FIG_NOST,
   [u"Quando um paciente fala muito do passado, a pergunta útil é o que o presente está deixando de fornecer: pertencimento, continuidade de quem ele é, sentido.",
    u"Nostalgia por uma época que a pessoa não viveu ainda é nostalgia. O objeto é uma versão de si, com os vínculos e a estética que ela associa a estar bem.",
    u"Postar o retrato é comportamento social. Parte do efeito vem dos comentários e das respostas de quem viu, e isso diz algo sobre o que a pessoa está buscando."],
   [u"Que a trend é sinal de sofrimento coletivo. Trend se espalha por imitação e pela novidade da ferramenta; a função regulatória é uma leitura possível, e não uma medida.",
    u"Que nostalgia é sempre boa. Boa parte dos estudos é de laboratório, com efeito medido logo depois da indução e sem seguimento.",
    u"Que ruminar o passado é a mesma coisa. A nostalgia é predominantemente positiva; o que pede atenção é quando o passado vira comparação que paralisa."],
   u"Com o paciente que idealiza uma época, mapeie a função em vez de discutir o conteúdo: o que ele sente logo depois de lembrar (conexão, calma, tristeza) e o que faz na hora seguinte. Se lembrar leva a ligar para alguém ou retomar algo, a nostalgia está a serviço de valores. Se leva a se recolher e comparar, trabalhe a evitação que a lembrança está cobrindo.",
   u"Quando você mesmo posta ou consome esse tipo de conteúdo, o que está buscando: a estética, ou uma versão de si com mais vínculo e menos incerteza?",
   u"Sedikides, C., &amp; Wildschut, T. (2025). On the nature of nostalgia: a psychological perspective. <em>Emotion Review</em>. Sobre a trend: Metrópoles, 7 de setembro de 2026.",
   u"https://doi.org/10.1177/17540739241303497", u"Ver o artigo"),
]

IDX = [(1, u"Artmed Experience em outubro"), (2, u"A hipótese da centralidade posta à prova"),
       (3, u"A trend dos anos 80 e a nostalgia")]

TEMA = (u"Um evento que coloca a personalização no centro da psicoterapia brasileira, um estudo que "
        u"testou a rede idiográfica na escolha do alvo e não confirmou a aposta, e uma trend do Instagram "
        u"lida pela pesquisa sobre nostalgia. Cada item com o que sustenta e o que não autoriza dizer.")

RESUMO_CARD = u"Artmed Experience em outubro · a hipótese da centralidade posta à prova · a trend dos anos 80 e a nostalgia"
RESUMO_HOME = u"Artmed Experience &middot; centralidade na rede &middot; nostalgia e a trend dos anos 80 &middot; <b>edição em PDF</b>"


def conferir(ok, msg):
    if not ok:
        raise SystemExit('FALHOU: ' + msg)


if __name__ == '__main__':
    # ---- página da edição
    f = SITE + '/newsletter/2026-09/index.html'
    h = io.open(f, encoding='utf-8').read()
    i = h.index("<article class='nw'")
    j = h.rindex("</article>") + len("</article>")
    h = h[:i] + '\n'.join(ITENS) + h[j:]
    # índice lateral
    a = h.index("<div class='idx'>"); b = h.index("</div>", a) + 6
    h = h[:a] + "<div class='idx'>" + ''.join(u"<a href='#i%d'>%s</a>" % x for x in IDX) + "</div>" + h[b:]
    # cabeçalho
    conferir(u"Quatro leituras</div>" in h, 'meta do hero')
    h = h.replace(u"Quatro leituras</div>", u"Três leituras</div>")
    a = h.index("<p class='tema'>"); b = h.index("</p>", a) + 4
    h = h[:a] + u"<p class='tema'>" + TEMA + u"</p>" + h[b:]
    conferir(NOME_ANTIGO in h, 'nome da seção na edição')
    h = h.replace(NOME_ANTIGO, NOME_NOVO)
    # título da aba
    h = re.sub(r"<title>.*?</title>", u"<title>Edição 1 · O que vale ler · Lógica Psicológica</title>", h, count=1)
    h = h.replace('</style></head>', '.nwfoto{display:flex;gap:16px;align-items:center;}.nwfoto img{width:132px;flex:none;border-radius:8px;}.nwfoto figcaption{margin:0;font-size:.92rem;line-height:1.5;color:#403F32;}@media(max-width:560px){.nwfoto{flex-direction:column;align-items:flex-start;}}\n</style></head>', 1)
    io.open(f, 'w', encoding='utf-8').write(h)
    print('edição: %d itens' % h.count("<article class='nw'"))

    # ---- índice da newsletter
    f = SITE + '/newsletter/index.html'
    h = io.open(f, encoding='utf-8').read()
    a = h.index("<div class='pr'>", h.index("Edição 1</div>")); b = h.index("</div>", a) + 6
    h = h[:a] + u"<div class='pr'>" + RESUMO_CARD + u"</div>" + h[b:]
    conferir(NOME_ANTIGO in h, 'nome da seção no índice')
    h = h.replace(NOME_ANTIGO, NOME_NOVO)
    io.open(f, 'w', encoding='utf-8').write(h)

    # ---- home
    f = SITE + '/index.html'
    h = io.open(f, encoding='utf-8').read()
    a = h.index("<span class='nres'>"); b = h.index("</span>", a) + 7
    h = h[:a] + u"<span class='nres'>" + RESUMO_HOME + u"</span>" + h[b:]
    # bio sem foto: a foto grande já está no bloco da comunidade logo abaixo
    conferir("<div class='quem'><img alt='Prof. Júlio Gonçalves' src='/assets/julio.jpg'>" in h, 'foto da bio na home')
    h = h.replace("<div class='quem'><img alt='Prof. Júlio Gonçalves' src='/assets/julio.jpg'>", "<div class='quem'>", 1)
    h = h.replace('</style></head>', '.quem{grid-template-columns:1fr;}\n</style></head>', 1)
    conferir(h.count(NOME_ANTIGO) == 2, 'nome da seção na home (%d)' % h.count(NOME_ANTIGO))
    h = h.replace(NOME_ANTIGO, NOME_NOVO)
    io.open(f, 'w', encoding='utf-8').write(h)

    # ---- demais páginas (menu lateral)
    for p in ['aulas', 'jornada', 'processos', 'psicoterapeutas-eficazes', 'supervisoes']:
        f = SITE + '/' + p + '/index.html'
        h = io.open(f, encoding='utf-8').read()
        conferir(NOME_ANTIGO in h, 'nome da seção em ' + p)
        io.open(f, 'w', encoding='utf-8').write(h.replace(NOME_ANTIGO, NOME_NOVO))
    print('nome da seção trocado em todas as páginas')
