# -*- coding: utf-8 -*-
"""Edição 2 da newsletter — página do site.
Usa a página da Edição 1 (newsletter/2026-09/index.html) como molde: troca os
artigos, o índice lateral, o cabeçalho, o botão do PDF e o título. Acrescenta
o card no índice da newsletter. Idempotente: sempre parte da página da Ed. 1."""
import io, re, os

SITE = '/home/claude/site'
PASTA = '2026-09-17'
FT = "font-family='Plus Jakarta Sans,sans-serif'"
NEG = "font-weight='800'"

# ---------------------------------------------------------------- figuras
def fig_floresta():
    """Floresta de efeitos idiográficos, adaptada da Fig. 2 de Hayes et al. (2026):
    151 pessoas, 20 negativas, 38 positivas, 93 indeterminadas, média perto de zero."""
    import random
    random.seed(7)
    W, H = 720, 300
    x0, x1 = 40, 440          # eixo: -1,2 a 1,2
    def X(v): return x0 + (v + 1.2) / 2.4 * (x1 - x0)
    ests = [(-1.0 + i * 0.03, 0.22, '#a05a3c') for i in range(20)]
    ests += [(-0.42 + i * (0.75 / 93), 0.30 + random.random() * 0.12, '#c9c2a8') for i in range(93)]
    ests += [(0.28 + i * 0.016, 0.22, '#7c8054') for i in range(38)]
    top, bot = 30, 262
    linhas = []
    for k, (e, ci, cor) in enumerate(ests):
        y = top + k * (bot - top) / (len(ests) - 1)
        linhas.append("<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' stroke='%s' stroke-width='1.3'/>"
                      "<circle cx='%.1f' cy='%.1f' r='1.4' fill='#2f2e24'/>"
                      % (X(e - ci), y, X(e + ci), y, cor, X(e), y))
    return u"""<figure class='nwfig'><svg viewBox='0 0 %d %d' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Floresta de 151 efeitos individuais: 20 negativos, 38 positivos, 93 indeterminados; a média fica perto de zero'>
<rect x='%.1f' y='22' width='%.1f' height='248' fill='#5b5c2a' opacity='.16'/>
<line x1='%.1f' y1='22' x2='%.1f' y2='270' stroke='#2f2e24' stroke-width='1' stroke-dasharray='4 4'/>
%s
<text x='%.1f' y='290' text-anchor='middle' %s font-size='11' fill='#6c6a55'>&minus;1,0</text>
<text x='%.1f' y='290' text-anchor='middle' %s font-size='11' fill='#6c6a55'>0</text>
<text x='%.1f' y='290' text-anchor='middle' %s font-size='11' fill='#6c6a55'>+1,0</text>
<rect x='470' y='22' width='250' height='248' rx='11' fill='#FFFDF7' stroke='#EFE7D3' stroke-width='1.4'/>
<text x='490' y='50' %s font-size='11' %s letter-spacing='1.4' fill='#a8894f'>151 PESSOAS, UMA POR LINHA</text>
<text x='490' y='84' %s font-size='13' %s fill='#a05a3c'>20 com efeito negativo</text>
<text x='490' y='101' %s font-size='11.5' fill='#6c6a55'>preocupar-se piora o humor</text>
<text x='490' y='132' %s font-size='13' %s fill='#7c8054'>38 com efeito positivo</text>
<text x='490' y='149' %s font-size='11.5' fill='#6c6a55'>preocupar-se melhora o humor</text>
<text x='490' y='180' %s font-size='13' %s fill='#8d876f'>93 indeterminados</text>
<text x='490' y='197' %s font-size='11.5' fill='#6c6a55'>intervalo cruza o zero</text>
<text x='490' y='232' %s font-size='12' %s fill='#43441f'>média de todos: &minus;0,11</text>
<text x='490' y='250' %s font-size='11.5' font-style='italic' fill='#43441f'>a faixa verde; ninguém está dentro dela</text>
</svg>
<figcaption>Adaptado da Fig. 2 de Hayes et al. (2026), com os dados de Sahdra et al. (2025): a relação entre "me preocupo com minhas emoções positivas acabarem" e felicidade, estimada pessoa a pessoa. O efeito médio, perto de zero, era a soma de efeitos que se cancelavam.</figcaption></figure>""" % (
        W, H, X(-0.16), X(-0.06) - X(-0.16), X(0), X(0), ''.join(linhas),
        X(-1), FT, X(0), FT, X(1), FT,
        FT, NEG, FT, NEG, FT, FT, NEG, FT, FT, NEG, FT, FT, NEG, FT)

FIG_HAYES = fig_floresta()

FIG_TRETA = u"""<figure class='nwfig'><svg viewBox='0 0 720 210' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='De um lado, o que a declaração de IA do artigo diz; do outro, o que o artigo defende; embaixo, a pergunta que a discussão levantou'>
<rect x='0' y='8' width='346' height='128' rx='11' fill='#F1ECE0' stroke='#9ca575' stroke-width='1.4'/>
<text x='20' y='34' %(F)s font-size='11' font-weight='800' letter-spacing='1.4' fill='#a8894f'>O QUE A DECLARAÇÃO DIZ</text>
<text x='20' y='62' %(F)s font-size='12.5' fill='#2f2e24'>Claude e ChatGPT foram usados para</text>
<text x='20' y='80' %(F)s font-size='12.5' fill='#2f2e24'>edição de rotina, modificação de figuras</text>
<text x='20' y='98' %(F)s font-size='12.5' fill='#2f2e24'>e geração de destaques gráficos.</text>
<text x='20' y='122' %(F)s font-size='11.5' font-style='italic' fill='#6c6a55'>Os autores revisaram e assumem o conteúdo.</text>
<rect x='374' y='8' width='346' height='128' rx='11' fill='#FFFDF7' stroke='#43441f' stroke-width='1.6'/>
<text x='394' y='34' %(F)s font-size='11' font-weight='800' letter-spacing='1.4' fill='#43441f'>O QUE O ARTIGO DEFENDE</text>
<text x='394' y='62' %(F)s font-size='12.5' fill='#2f2e24'>Que a média de grupo não descreve</text>
<text x='394' y='80' %(F)s font-size='12.5' fill='#2f2e24'>a pessoa, e que a ciência clínica precisa</text>
<text x='394' y='98' %(F)s font-size='12.5' fill='#2f2e24'>começar pelo caso particular.</text>
<text x='394' y='122' %(F)s font-size='11.5' font-style='italic' fill='#6c6a55'>Um modelo de linguagem é a média em forma de texto.</text>
<rect x='120' y='156' width='480' height='46' rx='9' fill='#43441f'/>
<text x='360' y='176' text-anchor='middle' %(F)s font-size='12.5' font-weight='800' fill='#f0ede0'>A pergunta da semana</text>
<text x='360' y='194' text-anchor='middle' %(F)s font-size='11.5' fill='#9ca575'>editar com IA e pensar com IA são a mesma coisa?</text>
</svg>
<figcaption>Os dois lados da discussão vêm do próprio PDF: a declaração obrigatória de uso de IA generativa, no fim do texto, e a tese do artigo. A discussão da semana foi sobre a distância entre um e outro.</figcaption></figure>""" % dict(F=FT)

FIG_JOVENS = u"""<figure class='nwfig'><svg viewBox='0 0 720 170' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Quatro números do levantamento: 19 por cento usaram, 43 por cento pelo menos mensalmente, 92 por cento acharam útil, 63 por cento não contaram a ninguém'>
<rect x='0' y='8' width='168' height='150' rx='11' fill='#F1ECE0' stroke='#9ca575' stroke-width='1.4'/>
<text x='84' y='68' text-anchor='middle' %(F)s font-size='38' font-weight='800' fill='#43441f'>19%%</text>
<text x='84' y='96' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>já pediram conselho</text>
<text x='84' y='112' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>de saúde mental a</text>
<text x='84' y='128' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>um chatbot</text>
<rect x='184' y='8' width='168' height='150' rx='11' fill='#F1ECE0' stroke='#9ca575' stroke-width='1.4'/>
<text x='268' y='68' text-anchor='middle' %(F)s font-size='38' font-weight='800' fill='#43441f'>43%%</text>
<text x='268' y='96' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>desses, pelo menos</text>
<text x='268' y='112' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>uma vez por mês</text>
<rect x='368' y='8' width='168' height='150' rx='11' fill='#F1ECE0' stroke='#9ca575' stroke-width='1.4'/>
<text x='452' y='68' text-anchor='middle' %(F)s font-size='38' font-weight='800' fill='#43441f'>92%%</text>
<text x='452' y='96' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>acharam o conselho</text>
<text x='452' y='112' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>útil ou muito útil</text>
<rect x='552' y='8' width='168' height='150' rx='11' fill='#FAF3EE' stroke='#a05a3c' stroke-width='1.6'/>
<text x='636' y='68' text-anchor='middle' %(F)s font-size='38' font-weight='800' fill='#a05a3c'>63%%</text>
<text x='636' y='96' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>não contaram</text>
<text x='636' y='112' text-anchor='middle' %(F)s font-size='11.5' fill='#2f2e24'>a ninguém</text>
</svg>
<figcaption>Amostra nacional ponderada dos Estados Unidos, 1.009 jovens de 12 a 21 anos, novembro de 2025. Mulheres usaram o dobro; jovens de 18 a 21, quase quatro vezes mais que os de 12 a 14.</figcaption></figure>""" % dict(F=FT)

def barra(x, d, cor, rot):
    h = d * 200
    y = 226 - h
    return ("<rect x='%d' y='%.1f' width='38' height='%.1f' rx='4' fill='%s'/>"
            "<text x='%d' y='%.1f' text-anchor='middle' %s font-size='12' font-weight='800' fill='#2f2e24'>%s</text>"
            "<text x='%d' y='244' text-anchor='middle' %s font-size='10.5' fill='#6c6a55'>%s</text>"
            % (x, y, h, cor, x + 19, y - 6, FT, ('%.2f' % d).replace('.', ','), x + 19, FT, rot))

FIG_THERABOT = u"""<figure class='nwfig'><svg viewBox='0 0 720 262' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Tamanhos de efeito do Therabot contra lista de espera em depressão, ansiedade generalizada e risco de transtorno alimentar, em 4 e 8 semanas'>
<line x1='40' y1='226' x2='470' y2='226' stroke='#c9c2a8' stroke-width='1.4'/>
<line x1='40' y1='%(y08)s' x2='468' y2='%(y08)s' stroke='#a8894f' stroke-width='1' stroke-dasharray='4 4'/>
<text x='474' y='%(y08)s' dominant-baseline='middle' %(F)s font-size='10' fill='#a8894f'>d = 0,8</text>
%(B)s
<text x='90' y='22' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>Depressão</text>
<text x='230' y='22' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>Ansiedade generalizada</text>
<text x='380' y='22' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>Risco de TA</text>
<rect x='524' y='34' width='196' height='192' rx='11' fill='#FFFDF7' stroke='#EFE7D3' stroke-width='1.4'/>
<text x='538' y='60' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>O QUE FICOU DE FORA</text>
<text x='538' y='88' %(F)s font-size='12' fill='#2f2e24'>comparação com terapeuta</text>
<text x='538' y='110' %(F)s font-size='12' fill='#2f2e24'>controle ativo (o grupo</text>
<text x='538' y='126' %(F)s font-size='12' fill='#2f2e24'>controle ficou na fila)</text>
<text x='538' y='150' %(F)s font-size='12' fill='#2f2e24'>seguimento além de 4 semanas</text>
<text x='538' y='174' %(F)s font-size='12' fill='#2f2e24'>casos graves e risco agudo</text>
<text x='538' y='204' %(F)s font-size='10' font-style='italic' fill='#a05a3c'>28 intervenções humanas, 8 semanas</text>
</svg>
<figcaption>Cohen's d contra lista de espera, em 4 e 8 semanas (Heinz et al., 2025). Efeito grande contra quem ficou esperando é o que quase toda intervenção ativa mostra; a pergunta clínica começa nas colunas que faltam.</figcaption></figure>""" % dict(
    F=FT, y08=226 - 0.8 * 200, y08t=226 - 0.8 * 200 - 6,
    B=barra(60, 0.845, '#9ca575', '4 sem') + barra(104, 0.903, '#5b5c2a', '8 sem')
      + barra(200, 0.840, '#9ca575', '4 sem') + barra(244, 0.794, '#5b5c2a', '8 sem')
      + barra(350, 0.819, '#9ca575', '4 sem') + barra(394, 0.627, '#5b5c2a', '8 sem'))


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
 item(1, u"A treta da semana &middot; Clinical Psychology Review",
   u"Tchê, essa semana a treta foi grande com o Hayes e colaboradores",
   u"Hayes, Ciarrochi, Sahdra, Hofmann, Ong e Hernández publicaram um texto de posição pedindo que a psicologia clínica pare de aplicar a média de grupo a pessoas particulares. No fim do artigo, a declaração obrigatória de uso de IA generativa diz que <strong>Claude e ChatGPT foram usados na preparação do manuscrito</strong>. Foi o suficiente para a discussão da semana virar outra: um texto que defende a ciência da pessoa particular pode ser lapidado por uma máquina que é, por construção, a média de tudo o que já foi escrito?",
   [(u"Artigo", u"One size fits none: a call for an idionomic revolution"), (u"Publicado", u"online em 6 de setembro de 2026"),
    (u"Tese", u"erro ergódico: a média não descreve ninguém"), (u"Declaração de IA", u"Claude e ChatGPT para edição de rotina, figuras e destaques gráficos"),
    (u"A treta", u"discussão pública sobre o uso de IA por um grupo de referência")],
   FIG_TRETA,
   [u"A declaração é o que a revista exige, e diz exatamente o que a IA fez: edição, figuras e destaques. Isso separa duas coisas que a discussão misturou. Usar IA para lapidar texto é uma escolha de ofício; usar IA para chegar ao argumento seria outra, e o artigo não diz que fez isso.",
    u"O argumento do artigo sobrevive à treta. Com 151 pessoas, um efeito médio perto de zero escondia 20 pessoas com efeito negativo e 38 com efeito positivo. Quem quer derrubar o texto precisa responder a isso, e não a quem revisou a gramática.",
    u"A mesma pergunta vale para a clínica. O paciente que pergunta ao chatbot antes de perguntar a você (item 2) e o chatbot que reduz sintomas com supervisão humana (item 3) mostram a IA fazendo a parte que é média: informação, psicoeducação, ensaio. O que é particular no caso continua precisando de alguém."],
   [u"Que o artigo foi escrito por IA. A declaração diz edição, figuras e destaques gráficos, e os autores assumem o conteúdo. Não há evidência pública de que o raciocínio tenha vindo de um modelo.",
    u"Que usar IA invalida a tese. Um texto pode ser editado por uma máquina e continuar certo, ou ser escrito à mão e estar errado. O erro ergódico se sustenta ou cai pela matemática (Molenaar, 2004), não pelo processo de edição.",
    u"Que a treta foi sobre nada. Ela expõe uma pergunta real: se a comunidade que mais fala em contexto e função aceita ferramentas que nivelam o estilo, o que sobra de idiográfico no próprio jeito de escrever ciência?"],
   u"Faça com o artigo o que ele pede que você faça com o paciente: separe o que é média do que é particular. Leia a seção 9 e a seção 12 sem olhar a declaração de IA, e anote se o argumento se sustenta. Depois, na sua própria prática, escreva numa linha para que você usa IA (transcrição, resumo, revisão de texto, rascunho de psicoeducação) e para que não usa (formulação, decisão de alvo, o que diz ao paciente). Se a segunda lista estiver vazia, é aí que a treta se aplica a você.",
   u"Quando você usa IA para escrever sobre um caso, ela está editando o que você pensou ou pensando no seu lugar? Como você sabe a diferença?",
   u"Hayes, S. C., Ciarrochi, J., Sahdra, B. K., Hofmann, S. G., Ong, C. W., &amp; Hernández, C. (2026). One size fits none: A call for an idionomic revolution. <em>Clinical Psychology Review, 129</em>, 102800. A declaração de uso de IA generativa está na seção final do artigo.",
   u"https://doi.org/10.1016/j.cpr.2026.102800", u"Ver o artigo"),

 item(2, u"Levantamento nacional &middot; JAMA Pediatrics",
   u"Um em cada cinco jovens já pediu conselho de saúde mental a um chatbot. Dois em cada três não contaram a ninguém",
   u"Pesquisadores da RAND e de Harvard entrevistaram uma amostra representativa de jovens de 12 a 21 anos dos Estados Unidos. Quase 20% já usaram um chatbot de IA para pedir conselho sobre saúde mental, a maioria achou útil, e <strong>63% fizeram isso sem contar a pais, amigos ou profissionais</strong>. A conversa que a IA teve com o seu paciente pode ser a que ele não teve com você.",
   [(u"Desenho", u"transversal, amostra nacional ponderada (EUA)"), (u"Amostra", u"1.009 jovens de 12 a 21 anos"),
    (u"Coleta", u"novembro de 2025"), (u"Publicado", u"JAMA Pediatrics, junho de 2026"),
    (u"Autores", u"McBain, Cantor e colegas, RAND e Harvard")],
   FIG_JOVENS,
   [u"A anamnese ganha uma pergunta que não pode mais faltar, e não só com adolescentes: o que você usa quando está mal, o que pergunta, e o que faz com a resposta. Se dois terços não contam, quem não pergunta não fica sabendo.",
    u"Quem já conversava com um médico sobre saúde mental usou quase o dobro. A IA não parece estar substituindo o pedido de ajuda; está se somando a ele, e por isso vale mapear como parte da rede de apoio do caso, com função própria.",
    u"O silêncio é dado clínico. Perguntar a uma máquina e não a uma pessoa pode ser acesso, pode ser vergonha, pode ser evitação de se expor. São processos diferentes e pedem intervenções diferentes."],
   [u"Que o conselho foi bom. O estudo não avaliou nem o tipo de chatbot nem a qualidade da resposta; 92% de “útil” é satisfação relatada no momento, e não desfecho.",
    u"Que os números valem para o Brasil. É uma amostra dos Estados Unidos, respondida on-line em inglês, com taxa de conclusão de 58%.",
    u"Que a tecnologia de hoje é a de novembro de 2025. Entre a coleta e a leitura, os modelos mudaram, e o uso provavelmente cresceu."],
   u"Inclua na avaliação inicial e revise a cada poucos meses: “Quando você está mal, usa algum app ou IA? O que costuma perguntar? O que faz logo depois da resposta?” Registre a função na formulação (regular, informar-se, ensaiar o que dizer, evitar pedir a uma pessoa) e trate a IA como mais um elo da rede do caso.",
   u"Se um paciente contar que perguntou ao ChatGPT antes de perguntar a você, o que isso diz sobre a relação, e o que você faz com essa informação na sessão?",
   u"McBain, R. K., Cantor, J. H., Breslau, J., Diliberti, M., Zhang, F., Rader, B., Burnett, A., Zhang, L. A., Kofner, A., Pataranutaporn, P., Stein, B. D., Yu, H., &amp; Mehrotra, A. (2026). AI chatbot use and disclosure for mental health among US adolescents and young adults. <em>JAMA Pediatrics, 180</em>(8).",
   u"https://jamanetwork.com/journals/jamapediatrics/fullarticle/2849307", u"Ver o estudo"),

 item(3, u"Ensaio randomizado e debate &middot; NEJM AI e British Journal of Psychiatry",
   u"O chatbot que reduziu sintomas em quatro semanas, e a discussão sobre entregar a psicoterapia à IA",
   u"O Therabot, um chatbot generativo treinado pela equipe de Dartmouth, foi testado em 210 adultos com depressão, ansiedade generalizada ou risco de transtorno alimentar. Contra lista de espera, produziu <strong>efeitos grandes nos três grupos</strong> e uma aliança relatada comparável à de pacientes em psicoterapia presencial. No British Journal of Psychiatry, Allen Frances escreveu que os chatbots vão dominar a psicoterapia; um grupo de psiquiatras respondeu que não é hora de levantar a bandeira branca. Os dois lados citam o mesmo ensaio.",
   [(u"Desenho", u"ECR, controle em lista de espera"), (u"Amostra", u"210 adultos, 106 no Therabot e 104 na fila"),
    (u"Dose", u"4 semanas com uso estimulado, 4 opcionais"), (u"Efeitos", u"d entre 0,63 e 0,90 nos três grupos"),
    (u"Aliança", u"WAI-SR 3,59 de 5"), (u"Debate", u"BJPsych 228(5), maio de 2026")],
   FIG_THERABOT,
   [u"Em 8 semanas, a equipe precisou intervir 15 vezes por risco (ideação suicida entre elas) e 13 vezes para corrigir respostas inadequadas do chatbot. Supervisão humana foi parte do tratamento testado. Quando o seu paciente usa uma IA sem ninguém olhando, ele está fora das condições do ensaio.",
    u"A aliança relatada com o chatbot ficou na faixa de amostras ambulatoriais. Isso desloca a pergunta: se vínculo relatado não distingue humano de máquina, o que distingue é o que a relação faz com o comportamento do paciente, e isso se formula em processos.",
    u"Frances propõe que a profissão treine para o que a IA faz mal: casos graves, risco, situações imprevisíveis, e o que acontece entre duas pessoas na sala. É uma agenda de formação, e coincide com o que a formulação por processos já pede."],
   [u"Que o Therabot equivale a psicoterapia. Ele nunca foi comparado com terapeuta, nem com controle ativo. Efeito grande contra lista de espera é o que quase toda intervenção ativa mostra.",
    u"Que o efeito dura. O seguimento foi de quatro semanas depois da fase de uso, e os efeitos em ansiedade e risco alimentar já vinham caindo na segunda medida.",
    u"Que vale para quem você atende. Recrutamento por anúncio no Meta, 25 dólares por avaliação, casos graves e risco agudo excluídos, e 75% do grupo sem nenhum outro tratamento."],
   u"Em vez de decidir se é contra ou a favor, decida por processo. Para o seu caso mais difícil, liste o que um chatbot conseguiria mover (psicoeducação, registro entre sessões, ensaio de habilidades, acesso às 3 da manhã) e o que depende de alguém que sente o impacto do que o paciente faz (ruptura e reparo, exposição interpessoal, contingência social ao vivo). Use a IA de propósito na primeira lista e proteja a sessão para a segunda.",
   u"Quais processos do seu caso mais difícil um chatbot moveria, e quais dependem de uma pessoa que reage ao que o paciente faz?",
   u"Heinz, M. V., Mackin, D. M., Trudeau, B. M., et al. (2025). Randomized trial of a generative AI chatbot for mental health treatment. <em>NEJM AI, 2</em>(4). Frances, A. (2026). Warning: AI chatbots will soon dominate psychotherapy. <em>British Journal of Psychiatry, 228</em>(5), 474&ndash;478. Sasso, D. A., et al. (2026). Psychotherapists versus artificial intelligence: let’s not raise the white flag. <em>British Journal of Psychiatry, 228</em>(5), 487&ndash;488.",
   u"https://doi.org/10.1056/AIoa2400802", u"Ver o ensaio"),
]

IDX = [(1, u"A treta do Hayes com a IA"), (2, u"Jovens e chatbots: um em cinco"),
       (3, u"Therabot e a bandeira branca")]

TEMA = (u"Hayes e colegas publicaram um artigo dizendo que a média não descreve ninguém, e a declaração de que usaram Claude e ChatGPT no manuscrito virou a discussão da semana. "
        u"Ao lado, dois retratos da IA na clínica: um em cada cinco jovens já pediu conselho a um chatbot, e "
        u"o ensaio do Therabot mostra efeito grande contra lista de espera, com 28 intervenções humanas no meio. "
        u"Cada item com o que sustenta e o que não autoriza dizer.")

RESUMO_CARD = u"A treta do Hayes com a IA · jovens e chatbots: um em cinco · o Therabot e a bandeira branca"
RESUMO_HOME = u"A treta do Hayes com a IA &middot; jovens e chatbots &middot; o Therabot e a bandeira branca &middot; <b>edição em PDF</b>"


def conferir(ok, msg):
    if not ok:
        raise SystemExit('FALHOU: ' + msg)


if __name__ == '__main__':
    base = SITE + '/newsletter/2026-09/index.html'
    h = io.open(base, encoding='utf-8').read()
    i = h.index("<article class='nw'")
    j = h.rindex("</article>") + len("</article>")
    h = h[:i] + '\n'.join(ITENS) + h[j:]
    a = h.index("<div class='idx'>"); b = h.index("</div>", a) + 6
    h = h[:a] + "<div class='idx'>" + ''.join(u"<a href='#i%d'>%s</a>" % x for x in IDX) + "</div>" + h[b:]
    conferir(u"<div class='sub'>Edição 1</div>" in h, 'número da edição')
    h = h.replace(u"<div class='sub'>Edição 1</div>", u"<div class='sub'>Edição 2</div>")
    conferir(u"Três leituras</div>" in h, 'meta do hero')
    a = h.index("<p class='tema'>"); b = h.index("</p>", a) + 4
    h = h[:a] + u"<p class='tema'>" + TEMA + u"</p>" + h[b:]
    h = re.sub(r"<title>.*?</title>", u"<title>Edição 2 · O que vale ler · Lógica Psicológica</title>", h, count=1)
    conferir("href='edicao-01.pdf'" in h, 'botão do pdf')
    h = h.replace("href='edicao-01.pdf'", "href='edicao-02.pdf'")
    # a Ed. 1 tinha CSS da foto anos 80; fica sem uso, não atrapalha
    os.makedirs(SITE + '/newsletter/' + PASTA, exist_ok=True)
    io.open(SITE + '/newsletter/%s/index.html' % PASTA, 'w', encoding='utf-8').write(h)
    print('edição 2: %d itens' % h.count("<article class='nw'"))

    # ---- índice da newsletter: card da Ed. 2 antes do card da Ed. 1
    f = SITE + '/newsletter/index.html'
    h = io.open(f, encoding='utf-8').read()
    if u"Edição 2</div>" not in h:
        card = (u"<div class='card bydate live'><div class='ct'><span class='dt'>02</span></div>"
                u"<div class='tt'>Edição 2</div><div class='pr'>%s</div>"
                u"<div class='acts'><a class='go' href='%s/'>Abrir</a><a class='pdf' href='%s/edicao-02.pdf'>PDF</a></div></div>"
                % (RESUMO_CARD, PASTA, PASTA))
        conferir("<div class='cards'>" in h, 'grade de cards')
        h = h.replace("<div class='cards'>", "<div class='cards'>" + card, 1)
        io.open(f, 'w', encoding='utf-8').write(h)
        print('card da edição 2 inserido no índice')
    print('trecho para a home (span.nres): ' + RESUMO_HOME)
