# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 15: Análise de desfechos e solução de problemas. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

DESF = u"""<figure class='dg'><div class='dg-t'>Análise de desfechos: o problema do exemplo</div>
<svg viewBox='0 0 720 236' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Uma régua de zero a cem entre o melhor e o pior desfecho de pedir dinheiro ao pai para a matrícula atrasada, com o plano de ação no meio'>
<rect x='0' y='6' width='720' height='40' rx='8' fill='#43441f'/>
<text x='360' y='23' text-anchor='middle' %(F)s font-size='9.5' font-weight='800' letter-spacing='1.2' fill='#9ca575'>PROBLEMA</text>
<text x='360' y='38' text-anchor='middle' %(F)s font-size='11' fill='#f0ede0'>precisa pedir dinheiro ao pai para a matrícula atrasada, e ele não sabe</text>
<line x1='40' y1='90' x2='680' y2='90' stroke='#2f2e24' stroke-width='2'/>
<g %(F)s font-size='9.5' fill='#6c6a55' text-anchor='middle'>
<line x1='40' y1='82' x2='40' y2='98' stroke='#2f2e24' stroke-width='1.6'/><text x='40' y='112'>0</text>
<line x1='200' y1='84' x2='200' y2='96' stroke='#2f2e24' stroke-width='1.2'/><text x='200' y='112'>25</text>
<line x1='360' y1='84' x2='360' y2='96' stroke='#2f2e24' stroke-width='1.2'/><text x='360' y='112'>50</text>
<line x1='520' y1='84' x2='520' y2='96' stroke='#2f2e24' stroke-width='1.2'/><text x='520' y='112'>75</text>
<line x1='680' y1='82' x2='680' y2='98' stroke='#2f2e24' stroke-width='1.6'/><text x='680' y='112'>100</text>
</g>
<rect x='0' y='128' width='210' height='100' rx='9' fill='#f1ece0' stroke='#9ca575' stroke-width='1.2'/>
<text x='12' y='150' %(F)s font-size='10' font-weight='800' letter-spacing='1' fill='#43441f'>MELHOR DESFECHO</text>
<text x='12' y='172' %(F)s font-size='10.5' fill='#2f2e24'>o pai não reage mal e ajuda</text>
<text x='12' y='188' %(F)s font-size='10.5' fill='#2f2e24'>a resolver o problema</text>
<rect x='255' y='128' width='210' height='100' rx='9' fill='#fffdf7' stroke='#8d876f' stroke-width='1.2'/>
<text x='267' y='150' %(F)s font-size='10' font-weight='800' letter-spacing='1' fill='#8d876f'>PLANO DE A&Ccedil;&Atilde;O</text>
<text x='267' y='170' %(F)s font-size='10.5' fill='#2f2e24'>terapia · conversa aberta com o</text>
<text x='267' y='186' %(F)s font-size='10.5' fill='#2f2e24'>pai · relevância daqui a 5 anos</text>
<text x='267' y='202' %(F)s font-size='10.5' fill='#2f2e24'>· apoio de parentes ou amigos</text>
<rect x='510' y='128' width='210' height='100' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.3'/>
<text x='522' y='150' %(F)s font-size='10' font-weight='800' letter-spacing='1' fill='#a05a3c'>PIOR DESFECHO</text>
<text x='522' y='172' %(F)s font-size='10.5' fill='#2f2e24'>o pai xinga, rejeita, não quer</text>
<text x='522' y='188' %(F)s font-size='10.5' fill='#2f2e24'>ajudar, se decepciona, deserda</text>
<path d='M465 178 L510 178' stroke='#a05a3c' stroke-width='1.6' stroke-dasharray='4 3'/>
</svg>
<figcaption>A régua obriga o paciente a colocar o desfecho provável entre os dois extremos, e o plano de ação é escrito para o pior. Quando o pior tem plano, ele deixa de ser o fim do mundo.</figcaption></figure>""" % dict(F=F)

DT15 = {
    'slug': 'aula15',
    'titulo_txt': 'Análise de desfechos e solução de problemas: a fase intermediária começa pelo que a tela evitava',
    'titulo_html': 'An&aacute;lise de desfechos e solu&ccedil;&atilde;o de problemas: a fase intermedi&aacute;ria come&ccedil;a pelo que a tela evitava',
    'data': 'Vídeo 15',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 15',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 15 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 15',
    'chave': 'mat-Aula-DT15-',
    'arquivo': 'Aula-DT15-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo quinto vídeo da "
              u"disciplina, que abre a fase intermediária com o monitoramento das ativações, a análise de desfechos e a solução de problemas. Não havia transcrição.</p>"
              u"<p>O caso do TCC atrasado é vinheta didática dos slides.</p></div>"),
    'tema': 'A fase intermediária em quatro movimentos: monitorar as ativações a cada sessão, checar os recursos quando a adesão falha, '
            'usar a análise de desfechos para o problema que o paciente evita, e a solução de problemas com preocupação agendada.',
    'essencial': [
        ('O monitoramento das ativações é a cada sessão.',
         'Quanto conseguiu fazer, quão difícil foi, quanto melhorou o humor, o que impediu. Sem isso, a agenda do vídeo 13 vira papel.'),
        ('Adesão baixa pede checagem de recursos, e não de motivação.',
         'Atividade física não interessa à maioria. Se a ativação não pega, a primeira hipótese é que a atividade estava errada.'),
        ('A tela costuma esconder um problema com nome.',
         'No exemplo, o TCC atrasado escondia três: os prazos que ele tem vergonha de perguntar, a matrícula que o pai não sabe, o tema que não gosta.'),
        ('Análise de desfechos: melhor, pior e plano para o pior.',
         'A régua de 0 a 100 obriga a colocar o provável entre os extremos, e o plano de ação escrito para o pior tira dele o poder de paralisar.'),
        ('Preocupação com hora marcada, e produtiva.',
         'Vinte minutos por dia para as preocupações, e solução de problemas em cinco colunas: brainstorm, vantagens, desvantagens, escolha, primeiro passo.'),
    ],
    'secoes': [
        ('s0', 'A fase intermediária', 'A fase intermediária: o que ela tem e como se monitora', u"""
<p>O vídeo abre a fase intermediária, cujo objetivo é modificar padrões de pensamento e comportamento desadaptativos. O slide liga cada frente do quadro (vídeo 8) ao que já foi feito: o <strong>monitoramento e a redução gradual</strong> se fazem via HumanTrack ou EMA (vídeo 7); as <strong>atividades offline</strong> vêm da escala de valores mais ação oposta (vídeo 13); e o treinamento em habilidades traz <strong>estratégias de regulação emocional, enfrentamento do tédio com atividades valorosas, e exposição imaginada</strong> para os estímulos aversivos, como os sociais (vídeo 18).</p>
<h3>O monitoramento é a cada sessão</h3>
<p>À medida que as atividades são planejadas e executadas, o monitoramento de quatro perguntas deve ser feito <strong>a cada sessão</strong>: quanto conseguiu fazer? quão difícil foi? quanto melhorou o humor? o que impediu de ser feita? É a conclusão diária da agenda do vídeo 13, agora perguntada pelo terapeuta, e é o que transforma a agenda em tratamento em vez de tarefa.</p>
<div class='callout note'><div class='co-t'>Quando a adesão falha</div>O slide avisa: caso não esteja tendo adesão às ativações, é importante verificar os <strong>recursos disponíveis</strong> para a execução. O exemplo é direto: atividade física não é interessante para a maioria. A primeira hipótese para a ativação que não pega não é falta de motivação; é atividade errada, horário errado, ou uma habilidade que falta. A pergunta "o que impediu" é a que separa as três.</div>
"""),
        ('s1', 'O problema atrás da tela', 'O problema atrás da tela: o exemplo do TCC', u"""
<p>O slide seguinte mostra por que a fase intermediária precisa de solução de problemas. O exemplo: um paciente precisa <strong>começar a escrever o TCC</strong>. Atrás dessa tarefa, três problemas em cadeia. Ele não sabe os prazos e precisa perguntar ao orientador, mas tem vergonha. Precisa pedir dinheiro ao pai para renovar a matrícula atrasada, mas o pai não sabe. E o tema que o orientador quer não é atrativo, e ele tem pouca experiência.</p>
<p>É o retrato de como a tela funciona como evitação: o jogo não é o problema, é a resposta a três problemas que a pessoa não sabe como enfrentar. Enquanto eles não tiverem plano, a redução de horas devolve o paciente a três fontes de ansiedade sem nada no lugar. O slide liga isso a duas técnicas: <strong>solução de problemas</strong> (do treinamento em habilidades) e <strong>reestruturação cognitiva</strong> (das intervenções cognitivas), que o vídeo 16 vai trabalhar com o mesmo caso.</p>
"""),
        ('s2', 'Análise de desfechos', 'Análise de desfechos', u"""
{{DESF}}
<p>Para o problema do meio (pedir dinheiro ao pai), o slide aplica a <strong>análise de desfechos</strong>. Uma régua de 0 a 100; numa ponta, o <strong>melhor desfecho</strong>: o pai não ter uma reação negativa e ajudar a resolver. Na outra, o <strong>pior desfecho</strong>: o pai xingar, rejeitar, não querer ajudar, se decepcionar, deserdar. E, ligado ao pior, o <strong>plano de ação</strong>: terapia; conversa aberta com o pai sobre os problemas; a relevância disso daqui a cinco anos; apoio de outros parentes ou amigos.</p>
<p>A técnica faz duas coisas. Primeiro, obriga a pessoa a nomear os extremos, e o pior nomeado costuma ser menos catastrófico do que o pior imaginado (o "deserdar" fica evidentemente exagerado quando está escrito ao lado de "se decepcionar"). Segundo, e mais importante: o plano de ação é escrito <strong>para o pior</strong>. Quando o pior tem plano, ele deixa de ser o fim e vira um cenário com resposta, e a pessoa consegue agir mesmo sem garantia do melhor.</p>
<div class='obs'><h4>Como conduzir</h4><p>Pedir os dois extremos antes de qualquer probabilidade. Depois pedir que o paciente marque na régua onde ele acha que vai cair, e perguntar por que ali. Só então montar o plano para o pior, com pelo menos um item que não dependa da reação do pai (no exemplo: apoio de outros parentes, e a terapia). A pergunta "daqui a cinco anos, isso ainda seria difícil de suportar?" é a que redimensiona.</p></div>
"""),
        ('s3', 'Solução de problemas', 'Solução de problemas e a preocupação com hora marcada', u"""
<p>O último slide traz a ficha de solução de problemas, que abre com uma frase de contexto: as duas intervenções mais importantes para reduzir a ansiedade generalizada são o <strong>adiamento da preocupação</strong> e <strong>tornar a preocupação produtiva</strong>, por meio da solução de problemas. Dois passos.</p>
<ul class='key'><li><b>Passo 1</b>: reservar 20 minutos do dia para anotar as preocupações. Fazer uma lista de problemas e possíveis soluções, e todo dia acrescentar novas preocupações, se houver. Refletir sobre elas de forma atenta e consciente, sem precisar resolver nada. O exemplo de compromisso: "das 18h30 às 19h, de segunda a sexta, para me preocupar de forma produtiva; sempre que os pensamentos surgirem fora desse horário, vou me lembrar desse recado; se for difícil, exercícios de regulação emocional, distração ou outra atividade importante".</li><li><b>Passo 2</b>: qual é o problema? quais as consequências de não resolver? e os benefícios de resolver? Depois, a tabela de cinco colunas: <b>brainstorm</b> de soluções, sem julgar quão boas ou ruins; <b>vantagens</b> de cada uma; <b>desvantagens</b>; a <b>escolha</b> da melhor (ou da menos pior); e <b>o que precisa fazer</b> para colocá-la em ação.</li></ul>
<p>Para o paciente do exemplo, isso significa que os três problemas do TCC deixam de rodar no fundo o dia inteiro (que é quando a tela entra) e passam a ter meia hora com hora marcada e uma tabela. A frase "escolha a melhor solução ou a menos pior" é importante: para quem evita, a exigência de uma solução boa é o que mantém a evitação.</p>
"""),
        ('s4', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<ul class='key'><li><b>O monitoramento das ativações</b> é a medida da alça nova, e a pergunta "o que impediu" é o diagnóstico diferencial entre atividade errada, contexto errado e habilidade que falta.</li><li><b>O problema atrás da tela</b> é a função de evitação com nome. Encontrá-lo é o que permite tratar a causa em vez do sintoma.</li><li><b>A análise de desfechos</b> trabalha a intolerância à incerteza: o pior com plano é suportável, e agir sem garantia do melhor vira possível.</li><li><b>A preocupação agendada</b> retira o combustível da ruminação, que é o precipitante mais comum do uso noturno (vídeo 7). <b>A solução de problemas</b> repõe a habilidade que a tela substituía.</li></ul>
<p>Na prática: perguntar o que impediu, achar o problema atrás da tela, colocar o pior na régua com plano, e dar meia hora por dia à preocupação, com tabela.</p>
"""),
    ],
    'checklist': [
        'A cada sessão, perguntei quanto fez, quão difícil foi, quanto melhorou o humor e o que impediu.',
        'Quando a ativação não pegou, chequei recursos (atividade, horário, habilidade) antes de motivação.',
        'Procurei o problema com nome atrás do uso da tela, e a cadeia de problemas atrás dele.',
        'Na análise de desfechos, pedi os dois extremos antes de qualquer probabilidade.',
        'Escrevi o plano de ação para o pior desfecho, com ao menos um item que não depende do outro.',
        'Fiz a pergunta dos cinco anos para redimensionar o pior.',
        'Combinei um horário diário de preocupação, com o que fazer quando ela aparece fora dele.',
        'Usei a tabela de cinco colunas e aceitei a solução "menos pior" como escolha válida.',
    ],
    'questoes': [
        'Quais são as quatro perguntas do monitoramento das ativações, e por que devem ser feitas a cada sessão?',
        'O que fazer quando o paciente não adere às ativações, segundo o slide, e por quê?',
        'Descreva os três problemas em cadeia do exemplo do TCC e o que eles mostram sobre a função da tela.',
        'Explique a análise de desfechos e por que o plano de ação é escrito para o pior.',
        'Descreva os dois passos da ficha de solução de problemas e o papel da preocupação com hora marcada.',
        'Pense num paciente teu. Que problema com nome está atrás do uso, e como tu montaria a régua de desfechos para ele?',
    ],
    'gabarito': {
     0: (C, u"Quanto conseguiu fazer, quão difícil foi, quanto melhorou o humor e o que impediu de ser feita. A cada sessão, porque é o que transforma a agenda em tratamento: sem revisão, a agenda vira tarefa, e a pergunta \"o que impediu\" é o único jeito de ajustar a atividade, o horário ou a habilidade que falta."),
     1: (C, u"Verificar os recursos disponíveis para a execução, e não a motivação. O exemplo do slide: atividade física não é interessante para a maioria. A primeira hipótese para a ativação que não pega é que a atividade estava errada, o horário estava errado ou falta uma habilidade; a pergunta \"o que impediu\" separa as três."),
     2: (C, u"Não sabe os prazos e tem vergonha de perguntar ao orientador; precisa pedir dinheiro ao pai para a matrícula atrasada e o pai não sabe; o tema não é atrativo e ele tem pouca experiência. Mostram que a tela é evitação de problemas com nome: reduzir horas sem dar plano a esses três devolve a ansiedade sem nada no lugar."),
     3: (C, u"Régua de 0 a 100 entre o melhor desfecho (o pai não reage mal e ajuda) e o pior (xinga, rejeita, deserda); o paciente marca onde acha que vai cair; e o plano de ação (terapia, conversa aberta, relevância em cinco anos, apoio de outros) é escrito para o pior. Escrever para o pior tira dele o poder de paralisar: quando o pior tem resposta, a pessoa consegue agir sem garantia do melhor."),
     4: (C, u"Passo 1: reservar 20 minutos por dia para anotar e refletir sobre as preocupações, com compromisso de horário e um recado para quando elas aparecem fora dele (regulação, distração, outra atividade). Passo 2: definir o problema, as consequências de não resolver e os benefícios de resolver, e preencher cinco colunas: brainstorm sem julgar, vantagens, desvantagens, escolha da melhor ou menos pior, e o que fazer para colocá-la em ação. A hora marcada tira a ruminação do dia inteiro, que é quando a tela entra."),
     5: (K, u"Não há resposta certa. Uma boa resposta nomeia um problema concreto e evitado (uma conversa, um prazo, uma dívida, uma decisão), escreve o melhor e o pior desfecho nas palavras do paciente, e monta um plano para o pior com ao menos um item que não dependa da reação de terceiros. O erro comum é montar a régua sobre o uso da tela em vez de sobre o problema que ela evita."),
    },
    'referencias': [
        "Borkovec, T. D., Wilkinson, L., Folensbee, R., &amp; Lerman, C. (1983). Stimulus control applications to the treatment of worry. <em>Behaviour Research and Therapy, 21</em>(3), 247–251.",
        "D'Zurilla, T. J., &amp; Nezu, A. M. (2007). <em>Problem-solving therapy: A positive approach to clinical intervention</em> (3rd ed.). Springer.",
        "Dugas, M. J., &amp; Robichaud, M. (2007). <em>Cognitive-behavioral treatment for generalized anxiety disorder: From science to practice.</em> Routledge.",
        "Martell, C. R., Dimidjian, S., &amp; Herman-Dunn, R. (2010). <em>Behavioral activation for depression: A clinician's guide.</em> Guilford Press.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo quinto vídeo de uma disciplina de pós-graduação; RPD e reatribuição vêm no vídeo 16.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. Os quadros "quando a adesão falha" (a partir do aviso do slide), "como conduzir" e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina. A régua de desfechos foi redesenhada com os elementos do slide.<br><br><strong>Referências.</strong> Os slides não citam fontes. O adiamento da preocupação remonta a Borkovec e colaboradores (1983) e está no protocolo de Dugas para ansiedade generalizada; a solução de problemas segue D'Zurilla e Nezu. As obras estão nas referências como respaldo, não como fonte dos slides. O caso do TCC é vinheta didática.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'DESF': DESF}
DT15['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT15['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT15['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT15, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT15)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT15['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
