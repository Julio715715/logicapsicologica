# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 14: Fases da ação e da manutenção. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

DOIS = u"""<figure class='dg'><div class='dg-t'>Ação e manutenção: o que muda na pergunta e na intervenção</div>
<svg viewBox='0 0 720 240' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Duas colunas: ação e manutenção, com a frase do paciente, o foco das perguntas e o foco da intervenção em cada uma'>
<rect x='0' y='6' width='350' height='228' rx='12' fill='#43441f'/>
<text x='16' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#9ca575'>4 &middot; A&Ccedil;&Atilde;O</text>
<text x='16' y='52' %(F)s font-size='11' font-style='italic' fill='#f0ede0'>"Estou fazendo mudanças concretas."</text>
<text x='16' y='82' %(F)s font-size='10' font-weight='800' fill='#c9c6a8'>PERGUNTAS OLHAM PARA O QUE EST&Aacute; SENDO FEITO</text>
<text x='16' y='100' %(F)s font-size='10.5' fill='#f0ede0'>o que já faz de diferente · o que funciona</text>
<text x='16' y='116' %(F)s font-size='10.5' fill='#f0ede0'>o que é mais difícil · mantém o planejado?</text>
<text x='16' y='132' %(F)s font-size='10.5' fill='#f0ede0'>o que ajuda e o que atrapalha</text>
<text x='16' y='162' %(F)s font-size='10' font-weight='800' fill='#c9c6a8'>INTERVEN&Ccedil;&Atilde;O</text>
<text x='16' y='180' %(F)s font-size='10.5' fill='#f0ede0'>reforçar progressos · monitorar dificuldades</text>
<text x='16' y='196' %(F)s font-size='10.5' fill='#f0ede0'>ajustar estratégias conforme os obstáculos</text>
<text x='16' y='212' %(F)s font-size='10.5' fill='#f0ede0'>aparecem</text>
<rect x='370' y='6' width='350' height='228' rx='12' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='386' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a8894f'>5 &middot; MANUTEN&Ccedil;&Atilde;O</text>
<text x='386' y='52' %(F)s font-size='11' font-style='italic' fill='#2f2e24'>"Mantenho a mudança, mas preciso me cuidar."</text>
<text x='386' y='82' %(F)s font-size='10' font-weight='800' fill='#6c6a55'>PERGUNTAS OLHAM PARA O RISCO</text>
<text x='386' y='100' %(F)s font-size='10.5' fill='#2f2e24'>o que tem ajudado a manter · já recaiu?</text>
<text x='386' y='116' %(F)s font-size='10.5' fill='#2f2e24'>como lidou com a recaída</text>
<text x='386' y='132' %(F)s font-size='10.5' fill='#2f2e24'>que sinais avisam que está voltando</text>
<text x='386' y='162' %(F)s font-size='10' font-weight='800' fill='#6c6a55'>INTERVEN&Ccedil;&Atilde;O</text>
<text x='386' y='180' %(F)s font-size='10.5' fill='#2f2e24'>prevenção de recaídas · identidade de</text>
<text x='386' y='196' %(F)s font-size='10.5' fill='#2f2e24'>alguém em mudança · relembrar conquistas</text>
<text x='386' y='212' %(F)s font-size='10.5' fill='#2f2e24'>e revalidar as razões para mudar</text>
</svg>
<figcaption>Na ação, o terapeuta olha para o que está sendo feito; na manutenção, para o que pode desfazer. A pergunta sobre sinais de retorno é a que prepara o plano de recaída.</figcaption></figure>""" % dict(F=F)

DT14 = {
    'slug': 'aula14',
    'titulo_txt': 'Ação e manutenção: reforçar o que funciona, ajustar o que não, e ler os sinais de retorno',
    'titulo_html': 'A&ccedil;&atilde;o e manuten&ccedil;&atilde;o: refor&ccedil;ar o que funciona, ajustar o que n&atilde;o, e ler os sinais de retorno',
    'data': 'Vídeo 14',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 14',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 14 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 14',
    'chave': 'mat-Aula-DT14-',
    'arquivo': 'Aula-DT14-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo quarto vídeo da "
              u"disciplina, que fecha a série dos estágios de mudança com ação e manutenção. Não havia transcrição.</p>"
              u"<p>O vídeo é curto: duas fichas de estágio. O material as desenvolve e as liga ao que veio antes.</p></div>"),
    'tema': 'Os dois últimos estágios: na ação, reforçar o que funciona e ajustar conforme os obstáculos aparecem; na manutenção, '
            'trabalhar a prevenção de recaídas, a identidade de quem mudou e os sinais que avisam do retorno.',
    'essencial': [
        ('Ação: "estou fazendo mudanças concretas".',
         'O paciente altera ativamente o padrão e ainda sente vontade de voltar. As perguntas olham para o que está sendo feito; a intervenção reforça e ajusta.'),
        ('Reforçar o progresso é intervenção, e não elogio.',
         'O que o terapeuta nota e nomeia é o que o paciente repete. Reforçar o específico (a quarta que não cumpriu e a quinta que voltou) vale mais que o geral.'),
        ('Manutenção: "mantenho a mudança, mas preciso me cuidar".',
         'Semanas ou meses de novo padrão, com risco de recaída diante de estressores. As perguntas olham para o risco; a intervenção é prevenção.'),
        ('A pergunta dos sinais é a mais importante da fase.',
         '"Que sinais tu observa quando percebe que pode estar voltando?" transforma a recaída de evento em processo, com aviso prévio.'),
        ('Identidade de alguém em mudança.',
         'Relembrar conquistas e revalidar as razões pessoais é o que sustenta a mudança quando o reforço da novidade acaba.'),
    ],
    'secoes': [
        ('s0', 'Ação', 'Ação: a ficha do estágio', u"""
{{DOIS}}
<p>O quarto estágio, na frase do paciente: <em>"Estou fazendo mudanças concretas no meu comportamento."</em></p>
<ul class='key'><li><b>Características</b>: o paciente altera ativamente seu padrão de comportamento. Pode ainda sentir vontade de voltar ao hábito antigo.</li><li><b>Perguntas</b>: o que ele já está fazendo de diferente em relação ao uso; o que tem funcionado bem até agora; o que tem sido mais difícil; se está conseguindo manter o que planejou; o que ajuda e o que atrapalha.</li><li><b>Intervenção</b>: reforçar progressos; monitorar dificuldades; ajustar estratégias conforme os obstáculos aparecem.</li></ul>
<p>Repare na ordem das perguntas: primeiro o que ele faz de diferente e o que funciona; só depois o que é difícil. É a mesma lógica da balança do vídeo 11, agora aplicada ao esforço: o paciente que ouve o terapeuta notar o que deu certo fica mais disposto a contar o que não deu.</p>
<div class='obs'><h4>Reforçar é específico</h4><p>"Parabéns, tu está indo bem" reforça pouco, porque não diz o que repetir. "Tu não cumpriu na quarta e na quinta voltou, sem esperar a semana seguinte" reforça a conduta que importa: retomar. O que o terapeuta nota e nomeia é o que o paciente aprende a notar em si. E o ajuste vem do mesmo material: cada "o que atrapalhou" é uma mudança na agenda, e não uma falha do paciente.</p></div>
"""),
        ('s1', 'Manutenção', 'Manutenção: a ficha do estágio', u"""
<p>O quinto estágio, na frase do paciente: <em>"Estou conseguindo manter a mudança, mas preciso me cuidar."</em></p>
<ul class='key'><li><b>Características</b>: o paciente já mantém o novo padrão há semanas ou meses. O risco de recaída ainda existe, principalmente diante de estressores.</li><li><b>Perguntas</b>: o que tem ajudado a manter o controle sobre o uso; se já teve alguma recaída e como lidou com ela; que sinais ele observa quando percebe que pode estar voltando ao padrão antigo.</li><li><b>Intervenção</b>: trabalhar prevenção de recaídas; reforçar a identidade da pessoa como alguém em mudança; relembrar conquistas e revalidar as razões pessoais para mudar.</li></ul>
<h3>A pergunta dos sinais</h3>
<p>Das três perguntas, a terceira é a que vale a sessão. "Que sinais tu observa quando percebe que pode estar voltando?" faz o paciente descrever a recaída como <strong>processo</strong>, e não como evento. Ele costuma responder com coisas pequenas: deixar o celular no quarto de novo, pular a caminhada, dormir mais tarde, "só dar uma olhada" no jogo. Esses sinais viram a lista de alerta do plano de recaída (vídeo 20), e o plano só funciona porque a lista é dele.</p>
<h3>Identidade</h3>
<p>A intervenção que o slide chama de "reforçar a identidade da pessoa como alguém em mudança" responde a um problema concreto: o reforço da novidade acaba. Nas primeiras semanas, mudar é interessante; depois de meses, é só rotina, e a rotina antiga continua disponível a um toque. O que sustenta é a pessoa se ver como alguém que fez isso, com as conquistas na frente e as razões revalidadas. Vale voltar aos caminhos da vida do vídeo 11 e perguntar em qual dos dois ela está andando agora.</p>
"""),
        ('s2', 'Os cinco estágios', 'Os cinco estágios, vistos juntos', u"""
<p>Com os vídeos 10 a 14, a série dos estágios fecha. Vale ver o desenho inteiro, porque cada estágio muda o que o terapeuta faz com a mesma técnica.</p>
<ul class='key'><li><b>Pré-contemplação</b>: perguntas abrem a percepção; informação sem julgamento, só depois.</li><li><b>Contemplação</b>: balança de vantagens e desvantagens, caminhos da vida, "o que te impede".</li><li><b>Preparação</b>: meta SMART, escala de alcance, agenda com o que entra no lugar, arranjo do ambiente.</li><li><b>Ação</b>: reforçar o específico, monitorar, ajustar a agenda a cada obstáculo.</li><li><b>Manutenção</b>: sinais de retorno, plano de recaída, identidade e razões.</li></ul>
<p>E a recidiva, quando vem, devolve o paciente a um estágio anterior, com mais informação, como o vídeo 9 mostrou. O terapeuta que sabe em qual estágio o paciente está hoje sabe qual pergunta fazer hoje; é para isso que o modelo serve, com a ressalva que já foi feita: leitura de prontidão, e não rótulo.</p>
"""),
        ('s3', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<ul class='key'><li><b>Na ação, o alvo é a alça nova.</b> O comportamento planejado precisa ser reforçado até que a consequência natural (bem-estar, competência, pertencimento) assuma o lugar do reforço do terapeuta. Reforçar o específico acelera essa transferência.</li><li><b>Na manutenção, o alvo é a alça velha.</b> Ela não sumiu; está disponível. Os sinais de retorno são os primeiros elos dela se reativando, e por isso a pergunta dos sinais é intervenção sobre discriminação.</li><li><b>Identidade é um nó de self</b>, e é o que faz a mudança durar depois que a novidade acaba. Relembrar conquistas e razões é alimentar esse nó.</li><li><b>O modelo de estágios</b> serve para escolher a técnica; a rede serve para saber por que ela funciona. Os dois juntos evitam aplicar protocolo em quem não está pronto e evitar técnica em quem está.</li></ul>
"""),
    ],
    'checklist': [
        'Na ação, perguntei primeiro o que está funcionando, e só depois o que é difícil.',
        'Reforcei condutas específicas (retomar depois de um dia ruim), e não o esforço em geral.',
        'Transformei cada "o que atrapalhou" em ajuste da agenda, e não em falha do paciente.',
        'Na manutenção, perguntei pelos sinais que avisam o retorno, com as palavras do paciente.',
        'Anotei esses sinais como lista de alerta para o plano de recaída.',
        'Perguntei pela recaída que já houve e por como o paciente lidou, sem julgamento.',
        'Relembrei conquistas concretas e revalidei as razões dele para mudar.',
        'Voltei aos caminhos da vida e perguntei em qual ele está andando agora.',
    ],
    'questoes': [
        'Descreva a ficha da ação: características, perguntas e intervenção.',
        'Por que reforçar o específico vale mais que reforçar o esforço em geral? Dê um exemplo.',
        'Descreva a ficha da manutenção: características, perguntas e intervenção.',
        'O que a pergunta sobre sinais de retorno faz com a ideia de recaída, e para que serve a resposta?',
        'Resuma o que o terapeuta faz em cada um dos cinco estágios.',
        'Pense num paciente teu em manutenção. Quais seriam os três primeiros sinais de que ele está voltando, e o que tu combinaria para cada um?',
    ],
    'gabarito': {
     0: (C, u"Características: altera ativamente o padrão e ainda pode sentir vontade de voltar. Perguntas: o que já faz de diferente, o que funciona, o que é mais difícil, se mantém o planejado, o que ajuda e o que atrapalha. Intervenção: reforçar progressos, monitorar dificuldades e ajustar estratégias conforme os obstáculos aparecem."),
     1: (C, u"Porque o reforço específico diz ao paciente o que repetir, e o geral não. \"Tu não cumpriu na quarta e na quinta voltou\" reforça a conduta de retomar; \"tu está indo bem\" não reforça nada em particular. O que o terapeuta nota e nomeia é o que o paciente passa a notar em si."),
     2: (C, u"Características: mantém o novo padrão há semanas ou meses, com risco de recaída diante de estressores. Perguntas: o que tem ajudado a manter, se já recaiu e como lidou, que sinais observa quando pode estar voltando. Intervenção: prevenção de recaídas, identidade como alguém em mudança, relembrar conquistas e revalidar razões."),
     3: (C, u"Transforma a recaída de evento (aconteceu ou não) em processo (está começando, com aviso prévio). A resposta, que costuma ser uma lista de coisas pequenas (celular no quarto, pular a caminhada, dormir tarde), vira a lista de alerta do plano de recaída, e o plano funciona porque a lista é do paciente."),
     4: (C, u"Pré-contemplação: perguntas que abrem a percepção, informação depois. Contemplação: balança, caminhos da vida, o que impede. Preparação: meta SMART, escala de alcance, agenda com substituição, ambiente arranjado. Ação: reforçar o específico, monitorar, ajustar. Manutenção: sinais de retorno, plano de recaída, identidade e razões."),
     5: (K, u"Não há resposta certa. Uma boa resposta lista sinais concretos e precoces desse paciente (mudanças de horário, de lugar do aparelho, de sono, uma atividade que ele para de fazer) e combina uma resposta para cada um, proporcional e imediata, de preferência a que já funcionou antes. O erro comum é listar sinais tardios (jogou o dia inteiro), quando a recaída já aconteceu."),
    },
    'referencias': [
        "Marlatt, G. A., &amp; Donovan, D. M. (Eds.). (2005). <em>Relapse prevention: Maintenance strategies in the treatment of addictive behaviors</em> (2nd ed.). Guilford Press.",
        "Miller, W. R., &amp; Rollnick, S. (2023). <em>Entrevista motivacional: Ajudando pessoas a mudar e crescer</em> (4. ed.). Artmed.",
        "Prochaska, J. O., DiClemente, C. C., &amp; Norcross, J. C. (1992). In search of how people change: Applications to addictive behaviors. <em>American Psychologist, 47</em>(9), 1102–1114.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo quarto vídeo de uma disciplina de pós-graduação; análise de desfechos e solução de problemas vêm no vídeo 15.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. O vídeo tem dois slides de conteúdo, as fichas de ação e de manutenção. O quadro "reforçar é específico", a seção sobre a pergunta dos sinais e a identidade, a síntese dos cinco estágios e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina. As perguntas do roteiro foram transcritas como estão no slide, com "você", porque são instrumento do professor.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'DOIS': DOIS}
DT14['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT14['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT14['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT14, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT14)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT14['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
