# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 18: Exposição imaginada. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

CURVAS = u"""<figure class='dg'><div class='dg-t'>Fuga e habituação: as duas curvas do slide</div>
<svg viewBox='0 0 720 240' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Dois gráficos de intensidade do sofrimento por tempo: à esquerda, a curva sobe e cai abruptamente quando a pessoa foge; à direita, uma família de curvas cada vez mais baixas quando a pessoa suporta a curva, com habituação'>
<defs><marker id='ex' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<line x1='30' y1='20' x2='30' y2='200' stroke='#2f2e24' stroke-width='1.4'/><line x1='30' y1='200' x2='340' y2='200' stroke='#2f2e24' stroke-width='1.4'/>
<text x='14' y='110' %(F)s font-size='9' fill='#6c6a55' transform='rotate(-90 14 110)' text-anchor='middle'>intensidade do sofrimento</text>
<text x='185' y='222' text-anchor='middle' %(F)s font-size='9.5' fill='#6c6a55'>tempo</text>
<path d='M50 190 C 90 190, 110 60, 170 40' fill='none' stroke='#a05a3c' stroke-width='2.6'/>
<line x1='172' y1='40' x2='172' y2='190' stroke='#d59a4b' stroke-width='2.4'/>
<path d='M172 190 L 250 190' fill='none' stroke='#d59a4b' stroke-width='2.4'/>
<text x='200' y='60' %(F)s font-size='9.5' fill='#d59a4b'>fuga, esquiva,</text>
<text x='200' y='73' %(F)s font-size='9.5' fill='#d59a4b'>compensação</text>
<text x='200' y='120' %(F)s font-size='9.5' font-style='italic' fill='#6c6a55'>alívio agora,</text>
<text x='200' y='133' %(F)s font-size='9.5' font-style='italic' fill='#6c6a55'>curva igual amanhã</text>
<line x1='400' y1='20' x2='400' y2='200' stroke='#2f2e24' stroke-width='1.4'/><line x1='400' y1='200' x2='710' y2='200' stroke='#2f2e24' stroke-width='1.4'/>
<text x='555' y='222' text-anchor='middle' %(F)s font-size='9.5' fill='#6c6a55'>tempo</text>
<path d='M420 190 C 470 190, 490 40, 540 40 C 590 40, 620 150, 700 190' fill='none' stroke='#a05a3c' stroke-width='2.4'/>
<path d='M420 190 C 470 190, 490 80, 540 80 C 590 80, 620 165, 700 190' fill='none' stroke='#8d876f' stroke-width='2.2'/>
<path d='M420 190 C 470 190, 490 115, 540 115 C 590 115, 620 175, 700 190' fill='none' stroke='#9ca575' stroke-width='2.2'/>
<path d='M420 190 C 470 190, 490 150, 540 150 C 590 150, 620 185, 700 190' fill='none' stroke='#43441f' stroke-width='2.2'/>
<text x='560' y='36' %(F)s font-size='9.5' fill='#43441f' font-weight='800'>suportar a curva</text>
<text x='610' y='150' %(F)s font-size='9.5' font-style='italic' fill='#43441f'>habituação:</text>
<text x='610' y='163' %(F)s font-size='9.5' font-style='italic' fill='#43441f'>cada vez mais baixa</text>
</svg>
<figcaption>Os dois desenhos à mão do slide, redesenhados. À esquerda, a fuga corta a curva e ela volta inteira; à direita, ficar até a queda natural faz cada exposição seguinte começar mais baixa.</figcaption></figure>""" % dict(F=F)

DT18 = {
    'slug': 'aula18',
    'titulo_txt': 'Exposição imaginada: a cena como um filme, para o que a tela evita',
    'titulo_html': 'Exposi&ccedil;&atilde;o imaginada: a cena como um filme, para o que a tela evita',
    'data': 'Vídeo 18',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 18',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 18 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 18',
    'chave': 'mat-Aula-DT18-',
    'arquivo': 'Aula-DT18-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo oitavo vídeo da "
              u"disciplina, sobre exposição imaginada para a ansiedade social que a tela costuma evitar. Não havia transcrição.</p>"
              u"<p>O roteiro da cafeteria é o exemplo do slide, resumido aqui.</p></div>"),
    'tema': 'Quatro passos para expor à situação social evitada: avaliar (BSPS e Liebowitz), entender as duas curvas, escrever a cena '
            'como um filme na primeira pessoa e no presente, e conduzir a exposição com SUDS e gravação.',
    'essencial': [
        ('A tela costuma evitar uma situação social.',
         'Ansiedade social é a comorbidade mais ligada à função de substituição (vídeo 4). Expor ao que se evita é tirar da tela essa função.'),
        ('Duas curvas: fuga e habituação.',
         'Fugir corta o pico e devolve a curva inteira amanhã; suportar até a queda faz cada exposição começar mais baixa.'),
        ('Avaliar antes: BSPS e Liebowitz.',
         'Medo e esquiva por situação, sintomas fisiológicos, e a lista de 24 situações de desempenho e sociais. Dão a hierarquia.'),
        ('A cena é um filme, e não uma lista de preocupações.',
         'Primeira pessoa, presente, detalhes sensoriais, e o significado do evento ("isso significa que fracassei").'),
        ('Começar pelo roteiro menos aversivo, medir com SUDS, gravar.',
         'Olhos fechados, detalhes vívidos, 0 a 100 ao longo da cena, e o áudio como tarefa entre sessões.'),
    ],
    'secoes': [
        ('s0', 'Passo 1: as curvas', 'Passo 1: entender as duas curvas', u"""
{{CURVAS}}
<p>O vídeo abre a exposição com o par de desenhos que sustenta toda a técnica. No primeiro, o estímulo aversivo aparece, a intensidade do sofrimento sobe, e no pico a pessoa faz um <strong>comportamento compensatório ou de fuga</strong>: a curva cai em linha reta. A anotação do slide: <em>efetiva no curto prazo, mas no longo...</em> A curva volta inteira na próxima vez, porque a pessoa nunca ficou para ver o que aconteceria.</p>
<p>No segundo, a pessoa <strong>suporta a curva</strong>: o sofrimento sobe, chega ao pico, e cai sozinho, com a queda angular que o slide marca. E a cada repetição a curva começa e termina mais baixa: <strong>habituação</strong>. É o que a tela impede: pegar o celular no meio de uma situação social é o comportamento de fuga do primeiro desenho, e por isso a ansiedade social de quem usa muita tela não melhora nunca.</p>
"""),
        ('s1', 'Passo 2: avaliar', 'Passo 2: avaliação completa', u"""
<p>Antes de expor, o slide pede uma <strong>avaliação completa</strong> do paciente: a gravidade da ansiedade social, as crenças, os tipos de situação social que disparam a ansiedade, e os <strong>comportamentos de evitação</strong>. Dois instrumentos, ambos com link para download.</p>
<ul class='key'><li><b>BSPS (Brief Social Phobia Scale)</b>, na tradução e adaptação de Crippa e colaboradores (2003): sete situações (falar em público, conversar com autoridades, com estranhos, ficar envergonhado, ser criticado, reuniões sociais, fazer coisas sendo observado), cada uma avaliada em <strong>medo</strong> e em <strong>esquiva</strong>, mais quatro sintomas fisiológicos (rubor, palpitações, tremores, transpiração). É entrevista, e não autorrelato.</li><li><b>Escala de Ansiedade Social de Liebowitz</b>: 24 situações, marcadas como de desempenho (P) ou sociais (S), cada uma com nota de ansiedade e de evitação. Os cortes do slide: até 54, pouco significativa; 55 a 65, leve; 66 a 80, moderada; 81 a 95, grave; 96 ou mais, muito grave.</li></ul>
<p>O que se tira daqui não é só a gravidade: é a <strong>hierarquia</strong>. As situações com mais evitação e menos ansiedade relatada são as candidatas ao primeiro roteiro; as com mais dos dois ficam para depois.</p>
"""),
        ('s2', 'Passo 3: escrever a cena', 'Passo 3: escrever a cena como um filme', u"""
<p>A exposição imaginada precisa de um roteiro, e o slide o define: é como escrever <strong>uma cena em um filme</strong> que descreva alguns minutos de ação. As regras:</p>
<ul class='key'><li>Escrever na <b>primeira pessoa</b>, usando "eu".</li><li>Escrever no <b>tempo presente</b> ("estou chegando em casa após um dia de trabalho").</li><li>Usar <b>detalhes sensoriais</b> para preencher a cena: sentimentos físicos de ansiedade (taquicardia), imagens detalhadas do entorno, outras sensações (sons, cheiros, toque).</li><li><b>Não listar preocupações</b> ("eu me preocupo com o que farei para ganhar dinheiro"). O objetivo é ir além da descrição verbal da ansiedade e criar uma imagem.</li><li>Tentar compreender o <b>significado do evento</b> ("isso significa que fracassei").</li></ul>
<p>O exemplo do slide é a cafeteria: o paciente escolhe uma mesa perto do balcão, reúne coragem, decide fazer um pedido simples; o coração acelera; a atendente sorri; quando tenta pedir um café preto, as palavras travam, a voz treme, saem inaudíveis; a expressão dela muda para confusão; a fila atrás fica impaciente; o rosto fica vermelho; ele tenta de novo, sai confuso; sai da fila, humilhado e derrotado.</p>
<div class='obs'><h4>Por que a cena inclui o pior</h4><p>Repare que o roteiro não termina bem: termina com a humilhação que o paciente teme. É de propósito. A exposição imaginada expõe ao <strong>significado</strong> temido ("isso significa que fracassei"), e não só à situação. Se a cena termina com o café servido e um sorriso, a pessoa não se expôs a nada. A curva só sobe, e só habitua, se o roteiro toca o que ela evita.</p></div>
"""),
        ('s3', 'Passo 4: conduzir', 'Passo 4: conduzir a exposição', u"""
<ul class='key'><li>Selecionar <b>um dos roteiros, de preferência o menos aversivo</b>, e pedir ao paciente que feche os olhos e <b>imagine a cena</b> como se estivesse acontecendo naquele momento.</li><li>Estimular a <b>concentração nos detalhes</b> que tornam a cena mais vívida: sentimentos físicos, o que vê, o que ouve, o significado.</li><li>Avaliar a <b>SUDS</b> de 0 a 100, ao longo da cena, para ver a curva subir e cair.</li><li><b>Gravar</b> o áudio da exposição e enviar como plano de ação: ouvir entre as sessões reforça a aprendizagem.</li></ul>
<div class='callout note'><div class='co-t'>O que o terapeuta observa</div>Duas coisas. Se a SUDS não sobe, a cena está verbal demais ou o paciente está se distraindo (que é a fuga do primeiro desenho, por dentro); pede-se mais detalhe sensorial. Se a SUDS sobe e não cai dentro da sessão, a cena está acima da hierarquia; repete-se uma menos aversiva. A gravação serve para a repetição diária que faz a família de curvas do segundo desenho.</div>
"""),
        ('s4', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<ul class='key'><li><b>A tela é o comportamento de fuga</b> da primeira curva, disponível no bolso em qualquer situação social. Expor é retirar dela a função de substituição que o vídeo 4 descreveu.</li><li><b>A avaliação dá a hierarquia</b>, que é a ordem de treino: evitação alta e ansiedade moderada primeiro.</li><li><b>O roteiro expõe ao significado</b>, e não só à situação: é o nó cognitivo ("fracassei") sendo tocado pela via emocional, o que o RPD e o continuum não alcançam sozinhos.</li><li><b>A SUDS é a medida da curva</b>, e a gravação é o que transforma uma exposição em dez. A habituação é o que faz a alça de fuga perder a função.</li><li><b>É o treino de "estar ali"</b> do vídeo 17, na imaginação; o ensaio comportamental (vídeo 19) é o mesmo treino ao vivo.</li></ul>
"""),
    ],
    'checklist': [
        'Expliquei as duas curvas com o desenho, e liguei a tela ao comportamento de fuga.',
        'Apliquei BSPS ou Liebowitz e montei a hierarquia pela evitação, não só pela ansiedade.',
        'Escrevi o roteiro com o paciente: primeira pessoa, presente, detalhes sensoriais, significado.',
        'Conferi que a cena toca o pior temido, e não termina bem.',
        'Comecei pelo roteiro menos aversivo.',
        'Medi a SUDS ao longo da cena e esperei a queda antes de encerrar.',
        'Quando a SUDS não subiu, pedi mais detalhe sensorial em vez de trocar de cena.',
        'Gravei a exposição e combinei a escuta diária como tarefa.',
    ],
    'questoes': [
        'Descreva as duas curvas do slide e o que cada uma diz sobre o uso da tela em situações sociais.',
        'Quais são os dois instrumentos de avaliação, o que cada um mede, e o que se tira deles além da gravidade?',
        'Quais são as cinco regras para escrever a cena, e por que ela não deve ser uma lista de preocupações?',
        'Por que o roteiro da cafeteria termina com humilhação, e não com o café servido?',
        'Como conduzir a exposição, e o que fazer se a SUDS não sobe ou não cai?',
        'Pense num paciente teu. Que situação social a tela evita, e como seriam as primeiras três linhas do roteiro dele?',
    ],
    'gabarito': {
     0: (C, u"Na primeira, o sofrimento sobe e a pessoa foge ou compensa no pico: a curva cai em linha reta, alívio agora e curva inteira na próxima vez. Na segunda, a pessoa suporta até a queda natural, e a cada repetição a curva começa e termina mais baixa (habituação). A tela no bolso é o comportamento de fuga da primeira curva em qualquer situação social; por isso a ansiedade social de quem usa muita tela não habitua."),
     1: (C, u"BSPS (Crippa et al., 2003): sete situações avaliadas em medo e esquiva, mais quatro sintomas fisiológicos, por entrevista. Liebowitz: 24 situações de desempenho e sociais, com nota de ansiedade e de evitação, e cortes de gravidade (até 54 pouco significativa; 96 ou mais muito grave). Além da gravidade, dão a hierarquia: as situações com mais evitação e ansiedade moderada são o primeiro roteiro."),
     2: (C, u"Primeira pessoa (\"eu\"); tempo presente; detalhes sensoriais (sensações físicas, imagens do entorno, sons, cheiros, toque); não listar preocupações; compreender o significado do evento (\"isso significa que fracassei\"). A lista de preocupações é verbal e não produz imagem; sem imagem a SUDS não sobe e não há o que habituar."),
     3: (C, u"Porque a exposição imaginada expõe ao significado temido, e não só à situação. Se a cena termina bem, a pessoa não tocou o que evita, a curva não sobe e nada habitua. O roteiro precisa incluir o pior (voz que trava, fila impaciente, humilhação) para que a habituação seja a esse significado."),
     4: (C, u"Escolher o roteiro menos aversivo, pedir que feche os olhos e imagine como se estivesse acontecendo, estimular os detalhes que tornam a cena vívida, medir a SUDS de 0 a 100 ao longo da cena, gravar e mandar como tarefa. Se a SUDS não sobe, a cena está verbal demais ou o paciente se distrai: mais detalhe sensorial. Se sobe e não cai na sessão, está acima da hierarquia: repetir uma menos aversiva."),
     5: (K, u"Não há resposta certa. Uma boa resposta nomeia uma situação concreta em que o paciente pega o celular para não estar (fila, mesa, reunião, corredor) e escreve três linhas na primeira pessoa e no presente, com ao menos um detalhe sensorial e o começo da ansiedade. O erro comum é escrever a cena em terceira pessoa, no passado, ou já com a solução dentro."),
    },
    'referencias': [
        "Crippa, J. A. S., Graeff, F. G., Zuardi, A. W., Hetem, L. A., Busatto, G. F., &amp; Loureiro, S. R. (2003). Brief Social Phobia Scale (BSPS): Tradução e adaptação para o português. (Conforme citado no instrumento.)",
        "Foa, E. B., Hembree, E. A., &amp; Rothbaum, B. O. (2007). <em>Prolonged exposure therapy for PTSD: Emotional processing of traumatic experiences. Therapist guide.</em> Oxford University Press.",
        "Heimberg, R. G., &amp; Becker, R. E. (2002). <em>Cognitive-behavioral group therapy for social phobia: Basic mechanisms and clinical strategies.</em> Guilford Press.",
        "Liebowitz, M. R. (1987). Social phobia. <em>Modern Problems of Pharmacopsychiatry, 22</em>, 141–173.",
        "Santos, L. F., Loureiro, S. R., Crippa, J. A. S., &amp; Os&oacute;rio, F. L. (2013). Psychometric validation study of the Liebowitz Social Anxiety Scale, self-reported version for Brazilian Portuguese. <em>PLoS ONE, 8</em>(7), e70235.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo oitavo vídeo de uma disciplina de pós-graduação; os ensaios comportamentais vêm no vídeo 19.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. As duas curvas foram redesenhadas a partir dos esboços à mão do slide. O roteiro da cafeteria foi resumido. Os quadros "por que a cena inclui o pior", "o que o terapeuta observa" e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina.<br><br><strong>Referências.</strong> As duas escalas trazem as fontes impressas no próprio instrumento (Crippa et al., 2003; Liebowitz, 1987; Santos et al., 2013), reproduzidas aqui como constam; a BSPS original é de Davidson (1995), como o rodapé do instrumento indica, e a referência completa da tradução não pôde ser conferida além do que o slide mostra. As regras de roteiro seguem a tradição da exposição prolongada (Foa) e da TCC para fobia social (Heimberg), citadas como respaldo.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'CURVAS': CURVAS}
DT18['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT18['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT18['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT18, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT18)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT18['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
