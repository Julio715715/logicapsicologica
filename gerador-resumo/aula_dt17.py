# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 17: Continuum cognitivo. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

CONT = u"""<figure class='dg'><div class='dg-t'>O continuum cognitivo do exemplo</div>
<svg viewBox='0 0 720 236' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Régua de zero a cem entre sou um fracasso e sou um sucesso, com cinco pessoas de referência distribuídas ao longo dela e a pergunta: tu está onde'>
<line x1='40' y1='120' x2='680' y2='120' stroke='#2f2e24' stroke-width='2'/>
<g %(F)s font-size='9.5' fill='#6c6a55' text-anchor='middle'>
<line x1='40' y1='112' x2='40' y2='128' stroke='#2f2e24' stroke-width='1.6'/><text x='40' y='142'>0</text>
<line x1='360' y1='114' x2='360' y2='126' stroke='#2f2e24' stroke-width='1.2'/><text x='360' y='142'>50</text>
<line x1='680' y1='112' x2='680' y2='128' stroke='#2f2e24' stroke-width='1.6'/><text x='680' y='142'>100</text>
</g>
<g %(F)s font-size='10' fill='#2f2e24' text-anchor='middle'>
<circle cx='90' cy='120' r='6' fill='#a05a3c'/><text x='90' y='98' font-weight='800'>Ricardo</text><text x='90' y='84' font-size='8.5' fill='#6c6a55'>sem família, sem modelo</text>
<circle cx='200' cy='120' r='6' fill='#a05a3c'/><text x='200' y='98' font-weight='800'>Ju</text><text x='200' y='84' font-size='8.5' fill='#6c6a55'>abandonou, mora sozinha</text>
<circle cx='330' cy='120' r='6' fill='#8d876f'/><text x='330' y='98' font-weight='800'>Robson</text><text x='330' y='84' font-size='8.5' fill='#6c6a55'>competente, sem constância</text>
<circle cx='530' cy='120' r='6' fill='#9ca575'/><text x='530' y='98' font-weight='800'>Fer</text><text x='530' y='84' font-size='8.5' fill='#6c6a55'>família unida, estudou de novo</text>
<circle cx='640' cy='120' r='6' fill='#43441f'/><text x='640' y='98' font-weight='800'>Sara</text><text x='640' y='84' font-size='8.5' fill='#6c6a55'>tudo a favor, apoio do marido</text>
</g>
<rect x='0' y='166' width='220' height='62' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.3'/>
<text x='12' y='186' %(F)s font-size='10' font-weight='800' fill='#a05a3c'>SOU UM FRACASSO</text>
<text x='12' y='202' %(F)s font-size='9.5' fill='#6c6a55'>despreocupado, vive em função</text>
<text x='12' y='216' %(F)s font-size='9.5' fill='#6c6a55'>de vícios, não é responsável</text>
<rect x='500' y='166' width='220' height='62' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='512' y='186' %(F)s font-size='10' font-weight='800' fill='#43441f'>SOU UM SUCESSO</text>
<text x='512' y='202' %(F)s font-size='9.5' fill='#6c6a55'>formada, trabalha, honra as</text>
<text x='512' y='216' %(F)s font-size='9.5' fill='#6c6a55'>responsabilidades, tem dinheiro</text>
<text x='360' y='200' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Após o exercício: tu está onde?</text>
</svg>
<figcaption>Cinco pessoas, de quem tem tudo contra a quem tem tudo a favor, e o paciente se colocando entre elas. As posições são ilustrativas; no exercício, é o paciente quem posiciona cada uma.</figcaption></figure>""" % dict(F=F)

DT17 = {
    'slug': 'aula17',
    'titulo_txt': 'Continuum cognitivo: de "sou um fracasso" a "tu está onde?"',
    'titulo_html': 'Continuum cognitivo: de &ldquo;sou um fracasso&rdquo; a &ldquo;tu est&aacute; onde?&rdquo;',
    'data': 'Vídeo 17',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 17',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 17 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 17',
    'chave': 'mat-Aula-DT17-',
    'arquivo': 'Aula-DT17-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo sétimo vídeo da "
              u"disciplina, sobre o continuum cognitivo aplicado à crença nuclear do caso. Não havia transcrição.</p>"
              u"<p>Os cinco personagens do exercício são figuras didáticas dos slides.</p></div>"),
    'tema': 'A técnica para a crença nuclear: definir os dois polos, distribuir pessoas reais ou compostas ao longo da régua, '
            'e perguntar ao paciente onde ele está. E o que fazer quando a resposta é "nunca estive lá".',
    'essencial': [
        ('O continuum é para a crença nuclear, e não para o pensamento automático.',
         '"Decepcionei meu pai" foi para o RPD (vídeo 16). "Sou um fracasso" vem para cá, porque é sobre a pessoa, e não sobre um evento.'),
        ('Os polos precisam de definição.',
         'Fracasso: despreocupado com a vida, vive em função de vícios, não é responsável. Sucesso: formada, trabalha, honra responsabilidades, tem dinheiro próprio. Sem definição, a régua não mede nada.'),
        ('As pessoas de referência fazem o trabalho.',
         'Ricardo, Ju, Robson, Fer, Sara. Distribuí-las obriga o paciente a usar critérios, e os critérios dele são o que muda a posição dele.'),
        ('"Tu está onde?" só depois das cinco.',
         'A pergunta vem no fim, quando a régua já tem gente e o paciente já viu que ninguém está no zero nem no cem.'),
        ('"Nunca treinei estar aqui" é o resultado esperado.',
         'Se o paciente diz que está longe do sucesso porque nunca esteve lá, a resposta é exposição: a próxima técnica da disciplina.'),
    ],
    'secoes': [
        ('s0', 'A técnica', 'O continuum cognitivo: para que serve', u"""
<p>O vídeo fecha o bloco das intervenções cognitivas com a técnica para a <strong>crença nuclear</strong>. No RPD (vídeo 16), o pensamento era "decepcionei meu pai", ligado a um evento; na reatribuição, "sou o culpado por tudo", ligado a uma situação. Aqui, o alvo é <em>"sou um fracasso"</em>: uma afirmação sobre a pessoa inteira, sem evento, e por isso imune a evidências pontuais. Quem se acha um fracasso não muda de ideia porque acertou uma coisa.</p>
<p>O continuum funciona por outro caminho: em vez de discutir se a crença é verdadeira, mostra que ela é <strong>dicotômica</strong>, e que a realidade não é. A sinopse do baralho mostrado no slide resume: as crenças nucleares, quando rígidas e extremas, comprometem a autoestima e mantêm quadros comuns na clínica; o continuum é uma das técnicas mais usadas para flexibilizá-las, e não é incomum que terapeutas tenham dificuldade em aplicá-la. O vídeo mostra como.</p>
"""),
        ('s1', 'Passo a passo', 'Passo a passo, com o exemplo do slide', u"""
{{CONT}}
<h3>1. Definir os polos</h3>
<p>O primeiro erro comum é colocar "fracasso" e "sucesso" nas pontas sem dizer o que são. O slide define os dois. <strong>Sou um fracasso</strong>: despreocupado com a vida, vive a vida em função de vícios, não é responsável. <strong>Sou um sucesso</strong>: formada, que trabalha, que honra as responsabilidades, possui o próprio dinheiro. As definições são do paciente, e vale escrevê-las antes de qualquer outra coisa, porque é contra elas que tudo vai ser medido.</p>
<h3>2. Distribuir pessoas de referência</h3>
<p>Cinco pessoas, com uma linha de história cada. <strong>Ricardo</strong>: sem família, vida sofrida, sem modelo de educação. <strong>Ju</strong>: abandonou a faculdade, sem ajuda dos pais, mora sozinha, história de vida complicada. <strong>Robson</strong>: é competente, mas tem dificuldades emocionais e não mantém constância; se virou sozinho desde sempre. <strong>Fer</strong>: família de muito trabalho, bem unidos, se apoiam, tem bons amigos, estudou desde nova. <strong>Sara</strong>: pai empresário, faculdade particular, boas condições financeiras, estudo no exterior, apoio do marido. O paciente posiciona cada uma na régua de 0 a 100.</p>
<p>É aqui que a técnica trabalha. Para posicionar Robson (competente, mas sem constância) o paciente precisa decidir quanto vale competência e quanto vale constância; para posicionar Sara ele precisa decidir se ter tudo a favor conta como mérito. Cada decisão dessas é um critério, e os critérios que ele usa para os outros são os que vai ter que usar para si.</p>
<h3>3. "Tu está onde?"</h3>
<p>Só depois das cinco. A pergunta do slide: <em>"Após o exercício: tu estás onde?"</em> A régua já tem gente; o paciente já viu que ninguém está no zero nem no cem, que Ju e Ricardo têm circunstâncias que ele não tem, e que Sara teve vantagens que ele não teve. A posição que ele se dá agora é comparativa, e não absoluta.</p>
"""),
        ('s2', 'A resposta que vale a sessão', 'A resposta que vale a sessão', u"""
<p>O slide traz uma fala de paciente, com duas setas apontando para o polo do sucesso: <em>"Talvez esteja aqui porque nunca treinou estar aqui, ou seja, será preciso se expor e sentir o que é estar aqui."</em></p>
<p>É o melhor desfecho possível do exercício, e é o que liga o continuum ao resto da fase intermediária. Quando o paciente entende que está longe do polo do sucesso não porque <em>é</em> um fracasso, mas porque <strong>nunca treinou</strong> as coisas que definem o sucesso (trabalhar, honrar responsabilidades, ter dinheiro próprio), a crença muda de natureza: deixa de ser identidade e vira <strong>repertório que falta</strong>. E repertório que falta se treina. É por isso que o vídeo seguinte é exposição imaginada e o outro é ensaio comportamental: são o treino de "estar ali".</p>
<div class='obs'><h4>Como conduzir sem forçar</h4><p>O terapeuta não empurra o paciente para a direita; ele pergunta pelos critérios. "O que fez tu colocar o Robson no 50?" "E o que ele tem que tu não tem?" "E o que tu tem que ele não tem?" As perguntas sobre os outros são seguras, e as respostas viram a régua do próprio paciente. O erro mais comum é o terapeuta discordar da posição que o paciente se deu; a posição não importa, os critérios importam, e eles mudam sozinhos quando o paciente os aplica a cinco pessoas diferentes.</p></div>
<p>O slide mostra também o baralho <em>Além dos extremos</em>, de intervenção para crenças nucleares, com formulários digitais, como recurso para o terapeuta que quer o passo a passo com cartas. É material do professor e de coautora, e está aqui como o slide o apresenta.</p>
"""),
        ('s3', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<ul class='key'><li><b>A crença nuclear é um nó de self</b>, e é o mais rígido da rede porque não depende de evento. Evidências pontuais (o RPD) não o movem; o continuum o move porque troca a pergunta: de "é verdade?" para "é a única forma de ver?".</li><li><b>As pessoas de referência são a intervenção de flexibilidade</b>: o paciente aplica critérios a cinco casos e descobre que os critérios dele não sustentam a dicotomia.</li><li><b>"Nunca treinei estar aqui" é a formulação certa</b>: transforma identidade em repertório, e repertório é o que a exposição (vídeo 18) e o ensaio (vídeo 19) constroem.</li><li><b>A técnica fecha o bloco cognitivo</b> e abre o comportamental: depois de flexibilizar, a pessoa precisa sentir o que é estar do outro lado. Sem isso, a régua volta para onde estava.</li></ul>
"""),
    ],
    'checklist': [
        'Reservei o continuum para a crença sobre a pessoa, e não para o pensamento sobre o evento.',
        'Escrevi a definição dos dois polos nas palavras do paciente antes de qualquer posicionamento.',
        'Usei pessoas de referência com histórias suficientemente diferentes para forçar critérios.',
        'Perguntei pelos critérios de cada posição ("o que fez tu colocar ele ali?") em vez de discordar da posição.',
        'Deixei a pergunta "tu está onde?" para o fim, depois das cinco pessoas.',
        'Anotei a posição que o paciente se deu e os critérios que usou, para retomar mais adiante.',
        'Quando apareceu "nunca treinei estar ali", liguei à exposição e ao ensaio, e não a mais discussão.',
    ],
    'questoes': [
        'Por que o continuum é a técnica para "sou um fracasso" e não o RPD?',
        'Quais são as definições dos dois polos no exemplo, e por que elas precisam vir antes de tudo?',
        'Descreva as cinco pessoas de referência e explique o que posicionar cada uma exige do paciente.',
        'Por que a pergunta "tu está onde?" vem só no fim?',
        'O que significa a fala "talvez esteja aqui porque nunca treinou estar aqui", e o que ela muda no tratamento?',
        'Pense num paciente teu. Qual é a crença nuclear dele, como tu definiria os polos com ele, e que cinco pessoas tu usaria?',
    ],
    'gabarito': {
     0: (C, u"Porque \"sou um fracasso\" é uma crença sobre a pessoa inteira, sem evento, e por isso imune a evidências pontuais: quem se acha um fracasso não muda de ideia por ter acertado uma coisa. O RPD testa pensamentos ligados a eventos (\"decepcionei meu pai\"); o continuum mostra que a crença é dicotômica e a realidade não é."),
     1: (C, u"Fracasso: despreocupado com a vida, vive em função de vícios, não é responsável. Sucesso: formada, que trabalha, honra as responsabilidades, possui o próprio dinheiro. Precisam vir antes porque são a régua: sem definição, o paciente se posiciona por sentimento, e não por critério, e o exercício não mede nada."),
     2: (C, u"Ricardo (sem família, sem modelo), Ju (abandonou a faculdade, sozinha, história complicada), Robson (competente, sem constância, se virou sozinho), Fer (família unida, bons amigos, estudou desde nova), Sara (tudo a favor, pai empresário, estudo fora, apoio do marido). Posicionar cada uma exige decidir critérios: quanto vale competência sem constância, se vantagem herdada conta como mérito, quanto pesa a circunstância. Os critérios que o paciente usa para os outros são os que vai usar para si."),
     3: (C, u"Porque antes das cinco pessoas a posição do paciente seria absoluta e vinda da crença (zero). Depois, a régua tem gente, ele viu que ninguém está nas pontas, e a posição que se dá é comparativa, feita com os critérios que ele mesmo acabou de usar."),
     4: (C, u"Que a distância até o polo do sucesso não é identidade (\"sou um fracasso\") e sim repertório que falta (\"nunca treinei trabalhar, honrar responsabilidades, ter meu dinheiro\"). Repertório se treina, e por isso o tratamento segue para exposição imaginada e ensaio comportamental: são o treino de \"estar ali\", e sem eles a régua volta para onde estava."),
     5: (K, u"Não há resposta certa. Uma boa resposta identifica uma crença sobre a pessoa (e não sobre um evento), define os polos com as palavras do paciente, e escolhe cinco pessoas (reais, compostas ou fictícias) com histórias diferentes o bastante para exigir critérios: uma com tudo contra, uma com tudo a favor, e três no meio com combinações diferentes de competência, circunstância e constância. O erro comum é usar pessoas que o paciente admira ou despreza, o que dá posições prontas sem critério."),
    },
    'referencias': [
        "Beck, J. S. (2022). <em>Terapia cognitivo-comportamental: Teoria e prática</em> (3. ed.). Artmed.",
        "Gonçalves, J., &amp; Sampaio, N. <em>Além dos extremos: Baralho de intervenção para crenças nucleares.</em> Sinopsys.",
        "Padesky, C. A. (1994). Schema change processes in cognitive therapy. <em>Clinical Psychology &amp; Psychotherapy, 1</em>(5), 267–278.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo sétimo vídeo de uma disciplina de pós-graduação; a exposição imaginada vem no vídeo 18.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. As posições dos personagens na figura são ilustrativas (o slide mostra a régua vazia; no exercício, é o paciente quem posiciona). O quadro "como conduzir sem forçar", a leitura de "nunca treinei estar aqui" como ponte para a exposição e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina.<br><br><strong>Referências.</strong> O baralho <em>Além dos extremos</em> é do professor e de coautora e está no slide como recurso; entrou nas referências como o slide o apresenta, sem ano. O continuum cognitivo tem formulação em Padesky (1994) e nos manuais de Judith Beck, citados como respaldo.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'CONT': CONT}
DT17['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT17['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT17['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT17, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT17)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT17['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
