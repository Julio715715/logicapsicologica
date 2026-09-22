# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 9: Entrevista motivacional. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

ESTAGIOS = u"""<figure class='dg'><div class='dg-t'>Os estágios de mudança, e o que se pergunta em cada um</div>
<svg viewBox='0 0 720 300' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Seis estágios em ciclo: pré-contemplação, contemplação, preparação, ação, manutenção e recidiva, com a pergunta-alvo dos dois primeiros'>
<defs><marker id='es' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='8' width='226' height='86' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='12' y='30' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Pré-contemplação</text>
<text x='12' y='48' %(F)s font-size='10' fill='#6c6a55'>não há intenção de mudar</text>
<text x='12' y='68' %(F)s font-size='9.5' font-style='italic' fill='#a05a3c'>explorar negação, feedback social,</text>
<text x='12' y='82' %(F)s font-size='9.5' font-style='italic' fill='#a05a3c'>reação à ausência do comportamento</text>
<path d='M230 51 L262 51' stroke='#8d876f' stroke-width='1.8' marker-end='url(#es)'/>
<rect x='266' y='8' width='226' height='86' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='278' y='30' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Contemplação</text>
<text x='278' y='48' %(F)s font-size='10' fill='#6c6a55'>vê o problema, sem compromisso</text>
<text x='278' y='68' %(F)s font-size='9.5' font-style='italic' fill='#a05a3c'>levantar ambivalência, explorar</text>
<text x='278' y='82' %(F)s font-size='9.5' font-style='italic' fill='#a05a3c'>ganhos esperados com a mudança</text>
<path d='M496 51 L528 51' stroke='#8d876f' stroke-width='1.8' marker-end='url(#es)'/>
<rect x='532' y='8' width='188' height='86' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='544' y='30' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Preparação</text>
<text x='544' y='48' %(F)s font-size='10' fill='#6c6a55'>há intenção de tomar</text>
<text x='544' y='62' %(F)s font-size='10' fill='#6c6a55'>medidas para resolver</text>
<path d='M626 98 L626 130' stroke='#8d876f' stroke-width='1.8' marker-end='url(#es)'/>
<rect x='532' y='134' width='188' height='70' rx='10' fill='#43441f'/>
<text x='544' y='158' %(F)s font-size='11' font-weight='800' fill='#f0ede0'>Ação</text>
<text x='544' y='176' %(F)s font-size='10' fill='#9ca575'>mudança comportamental</text>
<path d='M528 169 L496 169' stroke='#8d876f' stroke-width='1.8' marker-end='url(#es)'/>
<rect x='266' y='134' width='226' height='70' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='278' y='158' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Manutenção</text>
<text x='278' y='176' %(F)s font-size='10' fill='#6c6a55'>mudança sustentada; o novo</text>
<path d='M262 169 L230 169' stroke='#8d876f' stroke-width='1.8' marker-end='url(#es)'/>
<rect x='0' y='134' width='226' height='70' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='12' y='158' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>Recidiva</text>
<text x='12' y='176' %(F)s font-size='10' fill='#6c6a55'>volta aos velhos padrões</text>
<path d='M60 130 L60 98' stroke='#8d876f' stroke-width='1.8' stroke-dasharray='5 4' marker-end='url(#es)'/>
<rect x='120' y='226' width='480' height='62' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='360' y='250' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>espiral ascendente: aprende com cada recidiva</text>
<text x='360' y='270' text-anchor='middle' %(F)s font-size='10' fill='#6c6a55'>a recidiva volta para trás, mas não para o mesmo lugar; cada volta é com mais informação</text>
</svg>
<figcaption>Em cima, os dois estágios que o instrumento do vídeo cobre, com o objetivo das perguntas. A recidiva não é o fim do ciclo: é uma volta com aprendizado.</figcaption></figure>""" % dict(F=F)

DT9 = {
    'slug': 'aula9',
    'titulo_txt': 'Entrevista motivacional: os estágios de mudança e a pergunta certa para cada um',
    'titulo_html': 'Entrevista motivacional: os est&aacute;gios de mudan&ccedil;a e a pergunta certa para cada um',
    'data': 'Vídeo 9',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 9',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 9 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 9',
    'chave': 'mat-Aula-DT9-',
    'arquivo': 'Aula-DT9-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do nono vídeo da "
              u"disciplina, sobre entrevista motivacional na fase inicial do tratamento. Não havia transcrição.</p>"
              u"<p>O vídeo é curto: dois slides de conteúdo, um roteiro de perguntas por estágio e o ciclo dos estágios de mudança. "
              u"O material os desenvolve e acrescenta uma moderação sobre o modelo de estágios.</p></div>"),
    'tema': 'A entrevista motivacional como técnica da fase inicial, o roteiro de perguntas por estágio de mudança, os seis estágios '
            'do ciclo e a espiral que aprende com cada recidiva.',
    'essencial': [
        ('A entrevista motivacional é a primeira técnica da fase inicial.',
         'Antes de reduzir qualquer coisa, a mudança precisa ser do paciente. É isso que ela faz: evoca as razões dele, em vez de dar as do terapeuta.'),
        ('A pergunta muda com o estágio.',
         'Na pré-contemplação, perguntas que abrem a percepção do problema. Na contemplação, perguntas que dão voz à ambivalência e aos ganhos esperados.'),
        ('Seis estágios, em ciclo.',
         'Pré-contemplação, contemplação, preparação, ação, manutenção, recidiva. A recidiva volta ao começo, mas com mais informação.'),
        ('Perguntar é diferente de convencer.',
         'As perguntas do roteiro não têm resposta certa. Servem para o paciente ouvir a si mesmo dizendo o que o uso custa.'),
        ('O estágio é uma leitura, não um rótulo.',
         'Serve para escolher a pergunta de hoje. O modelo tem críticas, e a entrevista motivacional funciona sem ele.'),
    ],
    'secoes': [
        ('s0', 'Onde a EM entra', 'Onde a entrevista motivacional entra', u"""
<p>O vídeo retoma a fase inicial do processo interventivo, a psicoeducação, cujo objetivo é conscientizar o paciente sobre o transtorno e os mecanismos de manutenção do comportamento aditivo. A primeira das três técnicas dessa fase é a <strong>entrevista motivacional</strong>; as outras duas, análise de vantagens e desvantagens e metas realistas, dependem dela, porque uma balança feita com um paciente que não quer mudar pende sempre para o mesmo lado.</p>
<p>Entrevista motivacional, na definição de quem a criou, é um estilo de conversa colaborativo para fortalecer a motivação e o compromisso da própria pessoa com a mudança. O terapeuta não argumenta a favor da mudança; ele faz perguntas que levam o paciente a argumentar. Nas dependências tecnológicas, isso importa mais que em outras demandas, porque o paciente costuma chegar trazido pela família ou pela escola, e a primeira reação a qualquer argumento do terapeuta é defender o uso.</p>
"""),
        ('s1', 'O roteiro por estágio', 'O roteiro: uma pergunta para cada estágio', u"""
<p>O slide mostra o instrumento <strong>Entrevista Motivacional para Dependência Tecnológica</strong>: uma tabela com estágio de mudança, objetivo da pergunta, pergunta sugerida e espaço para a resposta. As linhas visíveis cobrem os dois primeiros estágios.</p>
<h3>Pré-contemplação</h3>
<ul class='key'><li><b>Explorar negação e ausência de percepção do problema</b>: "Você já pensou que o tempo que passa usando celular, internet ou jogando pode estar te atrapalhando em alguma área da sua vida?"</li><li><b>Investigar o feedback social recebido</b>: "Alguém já te disse que você usa tecnologia ou joga demais? O que você acha disso?"</li><li><b>Avaliar reações à ausência do comportamento</b>: "O que você sente quando está desconectado ou não pode jogar?"</li></ul>
<h3>Contemplação</h3>
<ul class='key'><li><b>Levantar a ambivalência sobre a mudança</b>: "Quais são as coisas boas e as coisas ruins de passar tanto tempo online ou jogando?"</li><li><b>Explorar os ganhos esperados com a mudança</b>: "O que você acredita que poderia melhorar na sua vida se você usasse menos tecnologia?"</li><li>A tabela segue com o objetivo de <b>identificar</b> (o slide corta aqui), presumivelmente as barreiras à mudança, e com as linhas dos estágios seguintes.</li></ul>
<div class='obs'><h4>O que essas perguntas fazem</h4><p>Repare que nenhuma delas afirma que há um problema. A primeira pergunta se o paciente já pensou nisso; a segunda pergunta o que ele acha do que os outros dizem; a terceira pede que ele descreva a abstinência com as próprias palavras, sem chamá-la assim. Na contemplação, a pergunta das coisas boas e ruins pede as boas primeiro, de propósito: o paciente que sente que o terapeuta reconhece o que o uso lhe dá fica mais disposto a falar do que ele custa. A pergunta seguinte já aponta para frente. É a sequência clássica da entrevista motivacional: perceber, ambivalência, ganhos, e só depois plano.</p></div>
"""),
        ('s2', 'Os estágios de mudança', 'Os seis estágios de mudança', u"""
{{ESTAGIOS}}
<p>O segundo slide é o ciclo dos estágios de mudança do modelo transteórico. <strong>Pré-contemplação</strong>: não há intenção de mudar de comportamento. <strong>Contemplação</strong>: tem consciência do problema, mas sem comprometimento em relação a atitudes. <strong>Preparação</strong>: há intenção de tomar medidas para resolver o problema. <strong>Ação</strong>: mudança comportamental. <strong>Manutenção</strong>: mudança sustentada; o novo. <strong>Recidiva</strong>: volta aos velhos padrões de comportamento, e daí de novo para a pré-contemplação.</p>
<p>No centro do ciclo, a <strong>espiral ascendente</strong>: a pessoa aprende com cada recidiva. É o que transforma o ciclo em espiral: a volta é para trás, mas não para o mesmo lugar, porque agora o paciente sabe o que precipitou a recaída, quanto tempo a manutenção durou e o que faltou. Para o terapeuta, é a atitude que evita tratar a recaída como fracasso do tratamento; ela é o material da próxima volta, e o plano de ação da fase final (vídeo 8) existe para isso.</p>
<div class='obs'><h4>Uma moderação sobre o modelo</h4><p>O modelo de estágios é útil como leitura clínica: ajuda a escolher a pergunta de hoje, e é assim que o vídeo o usa. Vale saber que ele tem críticas sérias na literatura: os estágios não são discretos, a pessoa oscila entre eles dentro de uma mesma semana, e intervenções "casadas" com o estágio não mostraram vantagem consistente sobre intervenções sem esse pareamento. A própria entrevista motivacional, nas edições mais recentes do manual de Miller e Rollnick, deixou de se organizar pelos estágios e passou a se organizar pelos seus quatro processos (engajar, focar, evocar, planejar). Na prática: use o estágio para ler a prontidão de agora, e não para rotular o paciente por meses.</p></div>
"""),
        ('s3', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>A entrevista motivacional é, de todas as técnicas da disciplina, a que mais naturalmente se lê em processos, porque ela não trata o comportamento: trata a relação da pessoa com o próprio comportamento.</p>
<ul class='key'><li><b>Motivação</b> é um nó da rede, e não um pré-requisito externo a ela. As perguntas do roteiro o ativam com o material do próprio paciente.</li><li><b>A ambivalência</b> é o estado normal, e não um obstáculo. A pergunta das coisas boas e ruins a coloca na mesa inteira, e é dali que sai a mudança, quando o lado dos custos passa a pesar mais na fala do paciente.</li><li><b>O feedback social</b> (segunda pergunta da pré-contemplação) traz o contexto para dentro: o que a família e a escola dizem é parte da rede, e o que o paciente faz com isso também.</li><li><b>A reação à ausência</b> (terceira pergunta) é a função disfarçada: o que o paciente sente desconectado é o que a tela estava regulando.</li><li><b>Os estágios</b> são uma leitura de prontidão, variável e reversível, e a recidiva é informação sobre a alça de manutenção.</li></ul>
<p>Na prática: antes de qualquer meta, as perguntas deste roteiro. E de novo toda vez que a motivação cair, porque ela cai.</p>
"""),
    ],
    'checklist': [
        'Li o estágio de prontidão do paciente antes de propor qualquer meta, e reli nas sessões seguintes.',
        'Na pré-contemplação, fiz perguntas que abrem a percepção, e não afirmações de que há um problema.',
        'Perguntei o que os outros dizem do uso e o que o paciente acha disso, sem tomar partido.',
        'Pedi que ele descreva o que sente quando está desconectado, com as palavras dele.',
        'Na contemplação, pedi as coisas boas do uso antes das ruins, e ouvi as boas de verdade.',
        'Deixei o paciente dizer o que poderia melhorar se usasse menos, em vez de dizer por ele.',
        'Tratei a recaída como informação para a próxima volta, e não como fracasso.',
        'Não usei o estágio como rótulo: usei para escolher a pergunta de hoje.',
    ],
    'questoes': [
        'Por que a entrevista motivacional é a primeira técnica da fase inicial, e o que as outras duas dependem dela?',
        'Quais são as três perguntas sugeridas para a pré-contemplação, e o que cada uma busca?',
        'Quais são as duas perguntas da contemplação, e por que a ordem (coisas boas antes das ruins) importa?',
        'Descreva os seis estágios de mudança e explique o que a espiral ascendente acrescenta ao ciclo.',
        'Qual é a moderação sobre o modelo de estágios, e como usar o modelo mesmo assim?',
        'Pense num paciente teu que chegou trazido pela família. Em que estágio ele está, e qual seria a tua primeira pergunta, com as tuas palavras?',
    ],
    'gabarito': {
     0: (C, u"Porque a mudança precisa ser do paciente antes que qualquer redução seja proposta, e a entrevista motivacional é o que evoca as razões dele em vez de impor as do terapeuta. A análise de vantagens e desvantagens só funciona com um paciente disposto a olhar os dois lados, e as metas realistas só se sustentam se forem metas dele; as duas dependem da motivação que a entrevista trabalha."),
     1: (C, u"\"Você já pensou que o tempo que passa usando celular, internet ou jogando pode estar te atrapalhando em alguma área da sua vida?\", para explorar negação e ausência de percepção do problema. \"Alguém já te disse que você usa tecnologia ou joga demais? O que você acha disso?\", para investigar o feedback social recebido. \"O que você sente quando está desconectado ou não pode jogar?\", para avaliar reações à ausência do comportamento, que é a abstinência descrita pelo paciente sem esse nome."),
     2: (C, u"\"Quais são as coisas boas e as coisas ruins de passar tanto tempo online ou jogando?\", para levantar a ambivalência; e \"O que você acredita que poderia melhorar na sua vida se você usasse menos tecnologia?\", para explorar os ganhos esperados. As boas vêm antes porque o paciente que sente o terapeuta reconhecendo o que o uso lhe dá fica mais disposto a falar do que ele custa; começar pelos custos coloca o paciente na defesa do uso."),
     3: (C, u"Pré-contemplação (sem intenção de mudar), contemplação (consciência do problema sem compromisso), preparação (intenção de tomar medidas), ação (mudança comportamental), manutenção (mudança sustentada) e recidiva (volta aos velhos padrões), que leva de novo à pré-contemplação. A espiral ascendente acrescenta que cada recidiva traz aprendizado: a volta é para trás, mas com mais informação sobre o que precipitou a recaída e o que faltou, e por isso não é para o mesmo lugar."),
     4: (C, u"Os estágios não são discretos, a pessoa oscila entre eles em dias, e intervenções pareadas ao estágio não mostraram vantagem consistente; a própria entrevista motivacional, nas edições recentes, se organiza pelos seus quatro processos (engajar, focar, evocar, planejar) e não pelos estágios. Mesmo assim, o modelo serve como leitura de prontidão de agora, para escolher a pergunta de hoje, desde que não vire rótulo."),
     5: (K, u"Não há resposta certa. Uma boa resposta reconhece que o paciente trazido costuma estar em pré-contemplação (ou em contemplação defensiva), escolhe uma pergunta que abre a percepção sem afirmar o problema e a reescreve na voz do próprio terapeuta, com o vocabulário do paciente (o jogo dele, o app dele, o que a família disse). O erro comum é começar pela psicoeducação sobre o transtorno, que para um paciente em pré-contemplação soa como o discurso da família repetido por outra pessoa."),
    },
    'referencias': [
        "Miller, W. R., &amp; Rollnick, S. (2023). <em>Entrevista motivacional: Ajudando pessoas a mudar e crescer</em> (4. ed.). Artmed.",
        "Prochaska, J. O., &amp; DiClemente, C. C. (1983). Stages and processes of self-change of smoking: Toward an integrative model of change. <em>Journal of Consulting and Clinical Psychology, 51</em>(3), 390–395.",
        "Prochaska, J. O., DiClemente, C. C., &amp; Norcross, J. C. (1992). In search of how people change: Applications to addictive behaviors. <em>American Psychologist, 47</em>(9), 1102–1114.",
        "West, R. (2005). Time for a change: Putting the Transtheoretical (Stages of Change) Model to rest. <em>Addiction, 100</em>(8), 1036–1039.",
        "Yakovenko, I., Quigley, L., Hemmelgarn, B. R., Hodgins, D. C., &amp; Ronksley, P. (2015). The efficacy of motivational interviewing for disordered gambling: Systematic review and meta-analysis. <em>Addictive Behaviors, 43</em>, 72–82.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o nono vídeo de uma disciplina de pós-graduação; a fase de pré-contemplação é o tema do vídeo 10.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. O vídeo tem dois slides de conteúdo: o roteiro de perguntas por estágio (as linhas visíveis cobrem pré-contemplação e contemplação; a tabela continua fora do enquadramento) e o ciclo dos estágios de mudança. A definição de entrevista motivacional, a leitura do que cada pergunta faz, a moderação sobre o modelo de estágios e a seção final em processos foram desenvolvidas pelo autor do material a partir da lógica da disciplina e da literatura citada.<br><br><strong>Uma moderação, sinalizada no texto.</strong> O modelo transteórico de estágios é apresentado como leitura clínica de prontidão, com a ressalva de que a literatura o critica como modelo de estágios discretos (West, 2005) e de que as edições recentes de Miller e Rollnick organizam a entrevista motivacional por processos, e não por estágios. As perguntas do roteiro foram transcritas como estão no slide, com "você", porque são o instrumento do professor e não texto na voz dele.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'ESTAGIOS': ESTAGIOS}
DT9['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DT9['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT9['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT9, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT9)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT9['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
