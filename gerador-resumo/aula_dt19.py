# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 19: Ensaios comportamentais. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

RP = u"""<figure class='dg'><div class='dg-t'>O role play em três tempos</div>
<svg viewBox='0 0 720 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Três blocos em sequência: contextualização da cena, execução e debriefing, com o que fazer em cada um'>
<defs><marker id='rp' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='10' width='224' height='180' rx='11' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='14' y='36' %(F)s font-size='11.5' font-weight='800' fill='#2f2e24'>1 &middot; Contextualizar</text>
<text x='14' y='62' %(F)s font-size='10.5' fill='#2f2e24'>cenário e papéis: "tu está numa</text>
<text x='14' y='78' %(F)s font-size='10.5' fill='#2f2e24'>sala de aula e precisa fazer</text>
<text x='14' y='94' %(F)s font-size='10.5' fill='#2f2e24'>uma pergunta ao professor"</text>
<text x='14' y='122' %(F)s font-size='10.5' fill='#2f2e24'>tempo curto, 2 a 5 minutos,</text>
<text x='14' y='138' %(F)s font-size='10.5' fill='#2f2e24'>para manter o foco</text>
<path d='M228 100 L244 100' stroke='#8d876f' stroke-width='2' marker-end='url(#rp)'/>
<rect x='248' y='10' width='224' height='180' rx='11' fill='#43441f'/>
<text x='262' y='36' %(F)s font-size='11.5' font-weight='800' fill='#f0ede0'>2 &middot; Executar</text>
<text x='262' y='62' %(F)s font-size='10.5' fill='#f0ede0'>terapeuta ou colega faz o</text>
<text x='262' y='78' %(F)s font-size='10.5' fill='#f0ede0'>papel do "outro"</text>
<text x='262' y='102' %(F)s font-size='10.5' fill='#f0ede0'>o paciente age como faria</text>
<text x='262' y='118' %(F)s font-size='10.5' fill='#f0ede0'>na situação real</text>
<text x='262' y='146' %(F)s font-size='10.5' fill='#9ca575'>não interromper: silêncio e</text>
<text x='262' y='162' %(F)s font-size='10.5' fill='#9ca575'>hesitação são a exposição</text>
<path d='M476 100 L492 100' stroke='#8d876f' stroke-width='2' marker-end='url(#rp)'/>
<rect x='496' y='10' width='224' height='180' rx='11' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.3'/>
<text x='510' y='36' %(F)s font-size='11.5' font-weight='800' fill='#2f2e24'>3 &middot; Debriefing</text>
<text x='510' y='62' %(F)s font-size='10.5' fill='#2f2e24'>como tu se sentiu?</text>
<text x='510' y='80' %(F)s font-size='10.5' fill='#2f2e24'>que pensamentos passaram?</text>
<text x='510' y='98' %(F)s font-size='10.5' fill='#2f2e24'>o que tu acha que o outro</text>
<text x='510' y='114' %(F)s font-size='10.5' fill='#2f2e24'>percebeu de ti?</text>
<text x='510' y='146' %(F)s font-size='10.5' fill='#a05a3c'>gravar e avaliar cada</text>
<text x='510' y='162' %(F)s font-size='10.5' fill='#a05a3c'>momento da interação</text>
</svg>
<figcaption>Os três tempos do slide. O aviso do meio é o que separa ensaio de conversa: o silêncio que o terapeuta não preenche é a exposição acontecendo.</figcaption></figure>""" % dict(F=F)

DT19 = {
    'slug': 'aula19',
    'titulo_txt': 'Ensaios comportamentais: direitos assertivos, role play em três tempos e dezoito cenas para treinar',
    'titulo_html': 'Ensaios comportamentais: direitos assertivos, role play em tr&ecirc;s tempos e dezoito cenas para treinar',
    'data': 'Vídeo 19',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 19',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 19 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 19',
    'chave': 'mat-Aula-DT19-',
    'arquivo': 'Aula-DT19-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo nono vídeo da "
              u"disciplina, sobre ensaios comportamentais para os déficits sociais que acompanham a dependência tecnológica. Não havia transcrição.</p></div>"),
    'tema': 'Do treino imaginado ao treino ao vivo: a psicoeducação dos dez direitos assertivos, o role play em contextualização, '
            'execução e debriefing, e a lista de dezoito cenas práticas para ensaiar em sessão.',
    'essencial': [
        ('Déficits sociais são comuns na dependência tecnológica.',
         'Anos de interação mediada por tela deixam o repertório presencial sem treino. O ensaio comportamental é o treino.'),
        ('Primeiro os direitos, depois a cena.',
         'Dizer não sem culpa, mudar de ideia, errar, não saber, ser respeitado, pedir, expressar emoção, não se justificar, se priorizar. Sem isso, o paciente ensaia sem acreditar que pode.'),
        ('Role play em três tempos: contextualizar, executar, debriefing.',
         'Cenário e papéis, 2 a 5 minutos; o outro feito pelo terapeuta, sem interromper; e três perguntas no fim.'),
        ('O silêncio é a exposição.',
         'Hesitação e pausa não são falha do ensaio; são o momento em que a ansiedade sobe e pode habituar. O terapeuta não preenche.'),
        ('Dezoito cenas, da apresentação ao pedido de ajuda.',
         'Escolhidas pela hierarquia do vídeo 18 e pelo que a tela mais evita neste paciente.'),
    ],
    'secoes': [
        ('s0', 'Direitos assertivos', 'Antes da cena: os direitos assertivos', u"""
<p>O vídeo abre com uma constatação: <strong>déficits sociais são comuns em pessoas com certo nível de dependência tecnológica</strong>. Faz sentido pelo que a disciplina já mostrou: a tela substitui a interação real por uma controlável (vídeo 4), e o que não é treinado não se desenvolve. Antes de ensaiar, o slide propõe uma psicoeducação: a exploração dos <strong>direitos assertivos básicos</strong>, em dez itens, cada um com uma frase para o paciente.</p>
<ul class='key'><li><b>Dizer "não" sem culpa</b>: recusar um pedido que não quer atender.</li><li><b>Mudar de ideia</b>: revisar uma decisão mesmo depois de ter dito sim.</li><li><b>Cometer erros e assumir responsabilidade</b>: errar é humano, sem justificativa excessiva.</li><li><b>Não saber algo</b>: não é obrigado a ter todas as respostas.</li><li><b>Ser tratado com respeito</b>: exigir que o tratem de forma respeitosa.</li><li><b>Fazer pedidos, mesmo que o outro possa recusar</b>: pedir não é imposição.</li><li><b>Se expressar emocionalmente</b>: tristeza, raiva, alegria, medo.</li><li><b>Dizer "não sei"</b>: sem inventar ou fingir conhecimento para agradar.</li><li><b>Não se justificar excessivamente</b>: explicações breves bastam.</li><li><b>Se priorizar em algumas situações</b>: colocar-se em primeiro lugar às vezes é necessário e saudável.</li></ul>
<div class='obs'><h4>Por que os direitos vêm antes</h4><p>Porque o paciente com déficit social costuma ensaiar sem acreditar que tem permissão para o que está ensaiando. Ele treina dizer não achando que não pode dizer não; o ensaio sai mecânico e a ansiedade não habitua, porque o significado ("estou fazendo algo errado") continua intacto. Ler os direitos primeiro, e pedir que ele marque os que não acredita ter, dá o alvo cognitivo do ensaio. Muitas vezes o direito que ele não se dá é exatamente o que a tela resolve: não precisar dizer não, não precisar pedir, não precisar ser visto errando.</p></div>
"""),
        ('s1', 'O role play', 'O role play em três tempos', u"""
{{RP}}
<ul class='key'><li><b>1. Contextualização da cena</b>: definir cenário e papéis ("tu está numa sala de aula e precisa fazer uma pergunta ao professor"); estabelecer tempo curto, 2 a 5 minutos, para manter o exercício focado.</li><li><b>2. Execução</b>: o terapeuta ou um colega faz o papel do "outro"; o paciente age como faria na situação real; e <strong>evitar interromper, mesmo que haja silêncio ou hesitação</strong>, porque esses momentos são parte da exposição.</li><li><b>3. Debriefing</b>: perguntar ao paciente como se sentiu, que pensamentos passaram pela cabeça, e o que ele acha que o outro percebeu dele. E gravar a encenação para avaliar pontualmente cada momento da interação.</li></ul>
<h3>O aviso do meio</h3>
<p>A instrução de não interromper é a que mais separa o ensaio de uma conversa terapêutica. O terapeuta que preenche o silêncio, sugere a frase ou alivia a pausa está fazendo, por dentro do ensaio, o que a tela faz por fora: cortando a curva no pico (vídeo 18). A hesitação é a SUDS subindo; deixar que ela passe é a habituação acontecendo em tempo real.</p>
<h3>A terceira pergunta do debriefing</h3>
<p>"O que tu acha que o outro percebeu de ti?" é a pergunta que expõe a crença. O paciente costuma responder com o pior ("que sou um idiota", "que não sei falar"), e o terapeuta, que fez o papel do outro, tem o dado de primeira mão para contrapor. É aqui que a gravação serve: mostrar o trecho em que ele achou que travou, e que durou dois segundos.</p>
"""),
        ('s2', 'As cenas', 'Dezoito cenas para ensaiar', u"""
<p>O último slide lista exemplos práticos, que aqui vão agrupados pelo que treinam.</p>
<ul class='key'><li><b>Se apresentar e sustentar a fala</b>: apresentação pessoal (nome, profissão, um interesse); apresentação curta de 2 minutos sobre um tema; leitura em voz alta de um parágrafo; explicar uma instrução (ensinar ao terapeuta como usar um aplicativo ou uma receita); apresentar um projeto para um "comitê"; defender trabalho acadêmico respondendo perguntas.</li><li><b>Iniciar e manter contato</b>: puxar assunto (clima, esportes, trabalho); telefone (ligar para uma pizzaria e pedir um sabor); conversar com pessoa atraente (paquera ou flerte).</li><li><b>Sustentar posição</b>: ser interrompido e continuar falando; responder a crítica sem se esquivar nem agredir; dizer não a um convite sem desculpas elaboradas; expressar opinião discordando com respeito numa reunião fictícia; falar com superior (pedir aumento ou negociar prazo).</li><li><b>Receber e pedir</b>: receber feedback de um professor ou chefe sobre um trabalho; pedir ajuda ou orientação a professor ou colega.</li></ul>
<div class='callout note'><div class='co-t'>Como escolher a cena</div>Pela hierarquia da Liebowitz (vídeo 18) e pelo que a tela evita neste paciente. Quem substitui amizade por jogo online começa por puxar assunto; quem evita o orientador (o caso dos vídeos 15 e 16) começa por pedir ajuda; quem não consegue recusar começa por dizer não. E cada cena se liga a um direito da primeira lista: dizer não é o primeiro direito, pedir ajuda é o sexto, discordar é o sétimo. O ensaio treina o comportamento, e o direito dá a permissão.</div>
"""),
        ('s3', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<ul class='key'><li><b>Os direitos assertivos trabalham o nó cognitivo</b> que a tela protege: a permissão que a pessoa não se dá. Sem ele, o ensaio é mecânico.</li><li><b>O role play é exposição ao vivo</b>, e o silêncio não preenchido é a curva subindo. É o treino de "estar ali" (vídeo 17) com corpo, e não só com imagem.</li><li><b>O debriefing junta os três domínios</b>: como se sentiu (afeto), que pensamentos passaram (cognição), o que o outro percebeu (self e contexto), e a gravação dá evidência contra a crença.</li><li><b>As dezoito cenas são repertório</b>, escolhidas pela hierarquia e pela função da tela. A cada cena ensaiada, uma situação real deixa de precisar do celular como saída.</li></ul>
"""),
    ],
    'checklist': [
        'Li os dez direitos assertivos com o paciente e pedi que marcasse os que não acredita ter.',
        'Liguei o direito que ele não se dá à função que a tela cumpre para ele.',
        'Contextualizei a cena com cenário, papéis e tempo curto antes de começar.',
        'Fiz o papel do outro e não interrompi silêncio nem hesitação.',
        'No debriefing, fiz as três perguntas, na ordem: sentiu, pensou, o que o outro percebeu.',
        'Gravei e usei a gravação para contrapor a percepção do paciente com o que aconteceu.',
        'Escolhi a cena pela hierarquia e pelo que a tela evita, e não pela lista em ordem.',
        'Liguei cada cena ensaiada a uma situação real da semana seguinte.',
    ],
    'questoes': [
        'Por que déficits sociais são comuns na dependência tecnológica, e por que a psicoeducação dos direitos assertivos vem antes do ensaio?',
        'Liste os dez direitos assertivos do slide.',
        'Descreva os três tempos do role play e o que o terapeuta faz em cada um.',
        'Por que não interromper o silêncio e a hesitação? Ligue à curva do vídeo 18.',
        'Quais são as três perguntas do debriefing, e o que a terceira expõe?',
        'Pense num paciente teu. Que direito ele não se dá, que cena da lista tu ensaiaria primeiro, e quem faria o outro?',
    ],
    'gabarito': {
     0: (C, u"Porque a tela substitui a interação presencial por uma controlável, e o que não é treinado não se desenvolve. Os direitos vêm antes porque o paciente com déficit costuma ensaiar sem acreditar que tem permissão para o que ensaia; o ensaio sai mecânico e o significado (\"estou fazendo algo errado\") fica intacto. Marcar os direitos que ele não se dá define o alvo cognitivo do ensaio."),
     1: (C, u"Dizer não sem culpa; mudar de ideia; cometer erros e assumir responsabilidade; não saber algo; ser tratado com respeito; fazer pedidos mesmo que o outro possa recusar; se expressar emocionalmente; dizer \"não sei\"; não se justificar excessivamente; se priorizar em algumas situações."),
     2: (C, u"Contextualização: cenário e papéis definidos, tempo de 2 a 5 minutos. Execução: terapeuta ou colega faz o outro, paciente age como faria na vida real, sem interrupção mesmo com silêncio ou hesitação. Debriefing: como se sentiu, que pensamentos passaram, o que o outro percebeu; gravar e avaliar cada momento."),
     3: (C, u"Porque o silêncio e a hesitação são a ansiedade subindo, e deixá-los passar é a habituação em tempo real. O terapeuta que preenche a pausa ou sugere a frase corta a curva no pico, que é exatamente o que a tela faz por fora: alívio agora, curva inteira na próxima vez."),
     4: (C, u"Como tu se sentiu; que pensamentos passaram pela tua cabeça; o que tu acha que o outro percebeu de ti. A terceira expõe a crença sobre como é visto (\"que sou um idiota\"), e o terapeuta, que fez o outro, tem o dado de primeira mão para contrapor, com a gravação como evidência."),
     5: (K, u"Não há resposta certa. Uma boa resposta identifica o direito que o paciente não se dá a partir do que a tela resolve para ele (não precisar recusar, pedir, ser visto errando), escolhe a cena da lista que treina esse direito na posição mais baixa da hierarquia, e define quem faz o outro (o terapeuta, ou um colega quando o terapeuta precisa observar). O erro comum é começar pela cena mais frequente na vida do paciente em vez da menos aversiva."),
    },
    'referencias': [
        "Caballo, V. E. (2003). <em>Manual de avaliação e treinamento das habilidades sociais.</em> Santos.",
        "Del Prette, Z. A. P., &amp; Del Prette, A. (2017). <em>Competência social e habilidades sociais: Manual teórico-prático.</em> Vozes.",
        "Heimberg, R. G., &amp; Becker, R. E. (2002). <em>Cognitive-behavioral group therapy for social phobia: Basic mechanisms and clinical strategies.</em> Guilford Press.",
        "Smith, M. J. (1975). <em>When I say no, I feel guilty.</em> Bantam.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo nono vídeo de uma disciplina de pós-graduação; a prevenção à recaída vem no vídeo 20.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. As dezoito cenas foram agrupadas pelo que treinam; no slide, aparecem em duas colunas sem agrupamento. Os quadros "por que os direitos vêm antes", "o aviso do meio", "como escolher a cena" e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina. As frases dos direitos foram adaptadas do "você" do slide para o registro do material, mantendo o conteúdo.<br><br><strong>Referências.</strong> Os slides não citam fontes. A lista de direitos assertivos remonta a Smith (1975) e está nos manuais de habilidades sociais de Caballo e de Del Prette; o role play com debriefing segue a tradição do treino de habilidades e da TCC para fobia social. Citados como respaldo.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'RP': RP}
DT19['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT19['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT19['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT19, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT19)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT19['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
