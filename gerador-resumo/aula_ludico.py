# -*- coding: utf-8 -*-
"""Aula: Por que brincar é tão bom. Bases evolutivas do comportamento lúdico.
Primeira aula gravada da disciplina de dependências tecnológicas (Prof. Júlio).
Fonte: transcrição da aula. Gera página e PDF."""
import io, re, sys
sys.path.insert(0, '/home/claude')
from figs_ludico import BENEFICIOS, VALIOSO
import sup_common, gen_resumo
from aula_tept import pagina_aula
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'

LUD = {
    'slug': 'aula1',
    'titulo_txt': 'Por que brincar é tão bom: bases evolutivas do comportamento lúdico',
    'titulo_html': 'Por que brincar &eacute; t&atilde;o bom: bases evolutivas do comportamento l&uacute;dico',
    'data': 'Vídeo 1',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 1',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 1 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 1',
    'chave': 'mat-Aula-Ludico-',
    'arquivo': 'Aula-Ludico-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir da transcrição da primeira "
              u"aula gravada de uma disciplina de pós-graduação sobre avaliação e tratamento das dependências tecnológicas. "
              u"É uma aula de fundamentos: não trata de avaliação nem de intervenção, que vêm nas aulas seguintes.</p>"
              u"<p>Boa parte do conteúdo foi pensada para servir também como <strong>psicoeducação</strong> para pacientes. "
              u"Três moderações empíricas em relação ao que foi dito estão sinalizadas no corpo do texto, com a justificativa.</p></div>"),
    'tema': 'Por que a gente se engaja tanto em atividade lúdica, o que o brincar treina na nossa espécie, e o que muda '
            'quando o ambiente passa a entregar recompensa o tempo todo.',
    'essencial': [
        ('Brincar é universal, e não é bobagem.',
         'Aparece em chimpanzés, golfinhos, caçadores-coletores e em toda cultura humana. Comportamento que se mantém assim tem função.'),
        ('A infância é uma arena de simulação da vida adulta.',
         'Motor, emoção, regras, cultura, funções executivas e habilidades sociais são treinados no brincar antes de serem exigidos de verdade.'),
        ('A gente brinca para obter algo valioso.',
         'Prazer, status, vínculo, recurso. A palavra importante é valioso, e ela pode ser qualquer coisa.'),
        ('O que mudou foi a oferta, não o algoritmo.',
         'De gravetos a cassinos e rolagem infinita, o ambiente passou a entregar recompensa sem parar. O mecanismo de busca segue o mesmo.'),
        ('Entender isso é o começo do tratamento.',
         'O paciente chega com culpa e raiva de si. Mostrar a arquitetura em que ele vive desfaz estigma e abre espaço para autocompaixão.'),
    ],
    'secoes': [
        ('s0', 'Por que começar pela psicologia evolutiva', 'Por que começar pela psicologia evolutiva', u"""
<p>A aula abriu com uma escolha de ponto de partida. Antes de falar de transtorno, de avaliação ou de tratamento, vale entender por que a gente faz o que faz. A psicologia evolutiva e as neurociências são as áreas que melhor respondem a isso: uma no nível do comportamento complexo (por que sentimos ciúme, raiva, empatia), a outra no nível bioquímico e neurofisiológico.</p>
<p>A psicologia evolutiva tem um limite conhecido, e ele foi dito de saída: muitas de suas hipóteses não podem ser testadas diretamente, porque seria preciso voltar ao passado. O que ela oferece são hipóteses plausíveis sobre a origem de comportamentos que hoje parecem óbvios. E o comportamento lúdico, entendido aqui como <strong>brincar, interagir com o ambiente buscando satisfação no sentido jocoso da palavra</strong>, é um deles.</p>
<div class='callout note'><div class='co-t'>Para que serve isso na clínica</div>O paciente dentro do espectro da dependência tecnológica costuma chegar com muita culpa, ressentimento e raiva de si mesmo. Mostrar a ele que existe um mecanismo antigo por trás do prazer de rolar a tela, e que ele vive cercado por uma arquitetura desenhada para fazê-lo gastar, jogar e continuar rolando, gera insight, desfaz estigma e promove a autocompaixão de que ele precisa. Os conteúdos desta aula foram pensados para funcionar também como psicoeducação.</div>
<div class='obs'><h4>Uma moderação</h4><p>Dizer que as hipóteses evolutivas não são testáveis é forte demais. Elas não são testáveis por experimento direto sobre o passado, mas geram previsões que a pesquisa comparativa (entre espécies) e a pesquisa do desenvolvimento conseguem confrontar com dados. Os estudos com chimpanzés e golfinhos citados a seguir são exatamente isso: evidência indireta a favor de uma hipótese sobre função. A formulação defensável é que essas hipóteses são testadas por convergência de evidência, e não por prova direta.</p></div>
"""),
        ('s1', 'Brincar na natureza', 'Brincar na natureza', u"""
<p>A pergunta lançada à turma foi simples: por que é tão bom se engajar em atividade lúdica? Por que, no fim da tarde, depois do trabalho, rolar a tela e ver vídeo de bicho prende tanto? A resposta começa fora da nossa espécie.</p>
<h3>Chimpanzés</h3>
<p>Etólogos que vivem em reservas naturais observando animais sem intervenção humana registraram, ao longo de meses, filhotes fêmeas de chimpanzés selvagens tratando gravetos como bonecas: carregando de um lado para o outro, colocando para dormir, manejando com cuidado. É um comportamento complexo, que pode ser lido como brincadeira, como cuidado e como emulação da vida adulta. E ele surge sem nenhum modelo humano por perto.</p>
<h3>Golfinhos</h3>
<p>Estão entre os animais que mais emitem comportamento lúdico. Têm um som específico para a brincadeira, saltos fora da água com forma própria que sinalizam que aquilo é jogo, e perseguições. A natureza está repleta de brincadeira, e não seria diferente com os seres humanos.</p>
<h3>A hipótese do treino</h3>
<p>A hipótese mais aceita entre os autores da área, e a que o slide da aula atribui a Špinka, Newberry e Bekoff, é que o brincar da infância serve como <strong>treino para a vida adulta</strong>, inclusive para o inesperado. O ambiente infantil funciona como uma arena de simulação: é ali que se começa a treinar a interação com o ambiente e com as pessoas, e a se preparar para o que a vida adulta vai exigir.</p>
"""),
        ('s2', 'Universal, inclusive entre caçadores-coletores', 'Universal, inclusive entre caçadores-coletores', u"""
<p>Nos seres humanos, o comportamento lúdico é uma característica <strong>inteiramente universal</strong>. Em todas as culturas há algum nível dele: brincadeiras, piadas, jocosidade, interação com o ambiente por meio de telas, videogames, jogos de tabuleiro, quebra-cabeças.</p>
<p>A objeção natural apareceu na própria aula: e os caçadores-coletores? Também. As brincadeiras são mais naturais, como corrida, luta de mentira e quem pega a fruta primeiro, mas aparecem em alta frequência, sobretudo na infância e na adolescência. A conclusão da aula foi que a gente carrega uma espécie de algoritmo que nos impulsiona a brincar e a sentir prazer com isso.</p>
<p>Daí a pergunta seguinte, que organiza o resto da aula: se é uma função presente há milhares de anos, e se um comportamento se mantém porque é útil para a sobrevivência, qual é o benefício?</p>
"""),
        ('s3', 'O que o brincar treina', 'O que o brincar treina', u"""
{{BENEFICIOS}}
<h3>Motor, emoção, regras, cultura</h3>
<p>A criança desenvolve musculatura, mobilidade e alongamento na medida em que interage com o ambiente: engatinha até o brinquedo, se apoia na parede, alcança. Ao mesmo tempo, na interação com brinquedo, pai, mãe e amigos, aparecem os primeiros movimentos de expressar emoção. As regras vêm junto: a mão na boca do cachorro, o dedo na tomada, o que o pai diz que não pode, até chegar em regras morais e éticas. E a cultura passa pelo mesmo canal: o que importa naquela família, o limite que os pais colocam quando a brincadeira fica expansiva demais, o jeito de se vestir e de se comportar.</p>
<h3>Funções executivas</h3>
<p>Atenção, memória, planejamento, tomada de decisão, controle inibitório, flexibilidade cognitiva. O cérebro da criança é fortemente estimulado enquanto ela brinca, porque brincar impõe desafios, raciocínio lógico, simbolismo, língua, escrita. Um conjunto de estímulos que força o desenvolvimento dessas capacidades.</p>
<h3>Habilidades sociais</h3>
<p>Foi apontado em aula como o mais importante. Quanto mais gente no ambiente, mais a criança refina o jeito de interagir e aprende as sutilezas do comportamento social: além de como se comportar, processos como empatia, altruísmo, colocar-se no lugar do outro e o desenvolvimento de uma teoria da mente, a capacidade de entender mais ou menos o que a outra pessoa está pensando.</p>
<div class='callout note'><div class='co-t'>Leitura em processos</div>Essa lista é útil na formulação porque diz o que o paciente pode estar deixando de treinar quando a atividade lúdica migra inteira para a tela. Funções executivas e habilidades sociais são as que a tela substitui pior, e são as que mais aparecem prejudicadas na clínica.</div>
"""),
        ('s4', 'A função: obter algo valioso', 'A função: obter algo valioso', u"""
<p>A resposta à pergunta inicial é uma só: a gente se engaja em comportamento lúdico para <strong>obter algo valioso</strong>. E a palavra que importa é <em>valioso</em>, porque ela não precisa ser nada material. Pode ser emocional, como prazer. Pode ser comportamental e social, como interagir com outras pessoas e saber o que elas estão pensando. Pode ser físico, como dinheiro, uma moeda, o <em>cash</em> dentro de um jogo. Prazer, status, alegria, dinheiro: qualquer coisa que o organismo trate como recompensa.</p>
<p>É isso que liga o brincar ao processo neurológico e comportamental que as próximas aulas vão detalhar. O jogo, o vídeo engraçado, o aplicativo baixado para preencher os intervalos da vida estão todos apoiados na mesma busca.</p>
"""),
        ('s5', 'O ambiente mudou. O algoritmo, não', 'O ambiente mudou. O algoritmo, não', u"""
{{VALIOSO}}
<p>Da interação com pedras, gravetos e árvores até cartas, cassinos e games, o mundo mudou. O ponto da aula é que a busca por algo valioso se tornou <strong>insaciável</strong> porque o ambiente passou a fornecer coisas valiosas, em prazer, dinheiro e status, o tempo todo. A gente busca isso indefinidamente no dia a dia, e essa busca vira um problema grave quando se organiza como dependência, inclusive a tecnológica.</p>
<div class='obs'><h4>Duas moderações</h4><p>A aula disse que o mundo mudou <em>e o nosso cérebro também</em>. Em escala evolutiva, não: o cérebro que responde à rolagem infinita é o mesmo que respondia ao graveto. O que muda é a aprendizagem individual, que de fato remodela circuitos com o uso repetido. A leitura mais precisa é a do <strong>descompasso evolutivo</strong>: um mecanismo selecionado num ambiente de recompensa escassa, operando num ambiente de recompensa abundante e desenhada. Isso é até mais útil para a psicoeducação, porque tira do paciente a ideia de que o cérebro dele é defeituoso.</p><p>A segunda: a aula falou em busca insaciável <em>por dopamina</em>. A dopamina está mais ligada ao querer, à antecipação e à busca do que ao prazer em si; o prazer consumado depende de outros sistemas. É por isso que o paciente continua rolando sem gostar do que vê. Dizer que ele busca dopamina está certo; dizer que busca prazer, nem sempre.</p></div>
<h3>O que vem na próxima aula</h3>
<p>Como os produtos tecnológicos são desenvolvidos a partir de princípios evolutivos e neuronais. Ou seja, como a armadilha é montada em cima do mecanismo descrito aqui.</p>
"""),
    ],
    'checklist': [
        'Expliquei ao paciente por que rolar a tela é prazeroso antes de discutir quanto ele rola.',
        'Nomeei a arquitetura em que ele vive, desenhada para fazê-lo continuar, em vez de tratar o uso como falha de caráter.',
        'Perguntei o que de valioso o uso entrega a ele: prazer, status, vínculo, fuga, recurso.',
        'Mapeei o que o brincar dele treinava antes e o que a tela deixou de treinar.',
        'Evitei dizer que o cérebro dele mudou ou está defeituoso; falei em descompasso entre mecanismo e ambiente.',
        'Distingui querer de gostar ao ouvir o relato do uso.',
        'Usei o conteúdo evolutivo para reduzir culpa, e não para justificar o uso.',
        'Deixei claro que entender o mecanismo é o começo, e que avaliação e intervenção vêm depois.',
    ],
    'questoes': [
        'Defina comportamento lúdico como a aula definiu, e explique por que a universalidade dele sugere função.',
        'O que os estudos com chimpanzés e golfinhos acrescentam à hipótese de que o brincar treina para a vida adulta?',
        'Liste os benefícios do brincar apontados na aula e diga quais deles a tela substitui pior. Por quê?',
        'Explique a frase: a gente brinca para obter algo valioso. Por que a palavra valioso importa mais do que a lista de exemplos?',
        'Pense num paciente seu com uso problemático de tela. O que de valioso o uso entrega a ele, e o que ele deixou de treinar?',
        'Como você explicaria a um paciente a diferença entre um cérebro que mudou e um mecanismo antigo num ambiente novo, sem tirar a responsabilidade dele nem devolver a culpa?',
    ],
    'gabarito': {
     0: (C, u"Brincar é <b>interagir com o ambiente buscando satisfação no sentido jocoso</b>: jogos, vídeos engraçados, piadas, brincadeiras físicas, jogos de tabuleiro, telas. Aparece em todas as culturas humanas, inclusive entre caçadores-coletores, e em outras espécies. Pelo raciocínio evolutivo, um comportamento que se mantém tão amplamente e por tanto tempo tende a ter sido útil à sobrevivência; a universalidade é o indício de que há função, e a hipótese principal é a do treino para a vida adulta."),
     1: (C, u"Evidência indireta. Filhotes fêmeas de chimpanzés selvagens, sem modelo humano, tratam gravetos como bonecas, num comportamento que emula cuidado adulto; golfinhos têm sons, saltos e perseguições próprios da brincadeira. Se o brincar aparece em espécies próximas e distantes, com formas que antecipam comportamentos adultos, a hipótese do treino ganha apoio. É o tipo de teste que a psicologia evolutiva consegue fazer: por convergência, e não por experimento sobre o passado."),
     2: (C, u"Refinamento motor, expressão emocional, regras e moral, apropriação cultural, funções executivas e habilidades sociais. A tela substitui pior as <b>funções executivas</b> (a rolagem passiva exige pouco planejamento, controle inibitório ou flexibilidade) e, sobretudo, as <b>habilidades sociais</b>: empatia, altruísmo e teoria da mente se treinam na interação com gente de verdade, com suas sutilezas, e não com uma interface desenhada para ser previsível."),
     3: (C, u"A função do brincar é obter algo que o organismo trate como recompensa. A palavra <b>valioso</b> importa porque desloca a pergunta do objeto para a função: não interessa se é prazer, status, dinheiro, vínculo ou moeda de jogo, e sim que aquilo funciona como recompensa para aquela pessoa. Na clínica, é essa pergunta que abre a formulação: o que exatamente o uso entrega a este paciente."),
     4: (K, u"Não há resposta certa. Uma boa resposta nomeia com precisão o que o uso entrega (alívio de tédio, pertencimento, sensação de competência, fuga de conflito, status numa comunidade online) e o que deixou de ser treinado fora da tela (contato social ao vivo, tolerância a espera, planejamento). O erro comum é responder com a categoria (<em>ele busca prazer</em>) em vez de com a função concreta daquele uso naquela vida."),
     5: (K, u"Não há resposta certa. Uma boa resposta explica que o mecanismo de buscar recompensa é antigo e compartilhado por todos, que o ambiente atual entrega recompensa o tempo todo e foi desenhado para isso, e que por isso o problema não é defeito do cérebro dele. Ao mesmo tempo, mantém a responsabilidade: conhecer o mecanismo é o que permite escolher o ambiente e as regras de uso. O erro comum é escorregar para um dos lados: ou o paciente é vítima da tecnologia, ou é culpado por fraqueza."),
    },
    'referencias': [
        "Berridge, K. C., &amp; Robinson, T. E. (2016). Liking, wanting, and the incentive-sensitization theory of addiction. <em>American Psychologist, 71</em>(8), 670–679.",
        "Burghardt, G. M. (2005). <em>The genesis of animal play: Testing the limits.</em> MIT Press.",
        "Diamond, A. (2013). Executive functions. <em>Annual Review of Psychology, 64</em>, 135–168.",
        "Gray, P. (2009). Play as a foundation for hunter-gatherer social existence. <em>American Journal of Play, 1</em>(4), 476–522.",
        "Groos, K. (1898). <em>The play of animals.</em> D. Appleton.",
        "Kahlenberg, S. M., &amp; Wrangham, R. W. (2010). Sex differences in chimpanzees' use of sticks as play objects resemble those of children. <em>Current Biology, 20</em>(24), R1067–R1068.",
        "Kuczaj, S. A., &amp; Eskelinen, H. C. (2014). Why do dolphins play? <em>Animal Behavior and Cognition, 1</em>(2), 113–127.",
        "Li, N. P., van Vugt, M., &amp; Colarelli, S. M. (2018). The evolutionary mismatch hypothesis: Implications for psychological science. <em>Current Directions in Psychological Science, 27</em>(1), 38–44.",
        "Pellegrini, A. D., Dupuis, D., &amp; Smith, P. K. (2007). Play in evolution and development. <em>Developmental Review, 27</em>(2), 261–276.",
        "&Scaron;pinka, M., Newberry, R. C., &amp; Bekoff, M. (2001). Mammalian play: Training for the unexpected. <em>The Quarterly Review of Biology, 76</em>(2), 141–168.",
        "Yamamoto, M. E., &amp; Valentova, J. V. (Orgs.). (2018). <em>Manual de psicologia evolucionista.</em> EDUFRN.",
    ],
    'nota': u"""Material dirigido a psicólogos. É a primeira aula de uma disciplina de pós-graduação e trata só de fundamentos; avaliação e intervenção vêm nas aulas seguintes e não estão aqui.<br><br><strong>Três moderações empíricas, sinalizadas no texto.</strong> Primeira: as hipóteses da psicologia evolutiva foram descritas como não testáveis; o texto registra que elas são testadas por convergência de evidência comparativa e do desenvolvimento, que é o que os próprios estudos citados em aula fazem. Segunda: a aula disse que o cérebro mudou junto com o ambiente; o texto adota a formulação do descompasso evolutivo, em que o mecanismo é o mesmo e a oferta de recompensa é que mudou, porque é mais precisa e mais útil para a psicoeducação. Terceira: a busca insaciável foi descrita como busca por dopamina e por prazer; o texto separa querer de gostar, conforme a distinção de Berridge e Robinson, porque essa separação explica o uso que continua sem prazer.<br><br><strong>Acréscimos.</strong> Os slides da aula citam Kahlenberg e Wrangham (2010), Špinka, Newberry e Bekoff (2001) e Yamamoto et al. (2018), todos incluídos; o estudo dos golfinhos, citado só na fala, foi localizado (Kuczaj e Eskelinen, 2014). As demais referências dão respaldo à hipótese do treino, à universalidade do brincar entre caçadores-coletores, às funções executivas e ao descompasso evolutivo. Nenhuma citação foi construída para preencher lacuna. A observação pessoal do professor sobre vídeos de macacos foi mantida fora do texto, mas a turma sabe.""",
}

_FIGS = {'BENEFICIOS': BENEFICIOS, 'VALIOSO': VALIOSO}
LUD['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in LUD['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + LUD['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(LUD, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(LUD)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = LUD['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
