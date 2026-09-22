# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 13: Valores e programação de atividades. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

GAP = u"""<figure class='dg'><div class='dg-t'>Importância e ação: onde está a distância</div>
<svg viewBox='0 0 720 300' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Gráfico de barras pareadas: para cada área de vida, a nota de importância e a nota de ação do exemplo do slide; as maiores distâncias aparecem em família, relacionamento, educação e sociedade'>
<g %(F)s font-size='9.5' fill='#6c6a55'>
<text x='0' y='34'>Família</text><text x='0' y='58'>Relacionamento</text><text x='0' y='82'>Ser pai ou mãe</text><text x='0' y='106'>Amizades</text><text x='0' y='130'>Trabalho</text><text x='0' y='154'>Finanças</text><text x='0' y='178'>Educação</text><text x='0' y='202'>Lazer</text><text x='0' y='226'>Espiritualidade</text><text x='0' y='250'>Vida em sociedade</text><text x='0' y='274'>Autocuidado</text>
</g>
<g>
<rect x='110' y='22' width='432' height='7' fill='#9ca575'/><rect x='110' y='31' width='192' height='7' fill='#a05a3c'/>
<rect x='110' y='46' width='432' height='7' fill='#9ca575'/><rect x='110' y='55' width='240' height='7' fill='#a05a3c'/>
<rect x='110' y='70' width='288' height='7' fill='#9ca575'/><rect x='110' y='79' width='288' height='7' fill='#a05a3c'/>
<rect x='110' y='94' width='288' height='7' fill='#9ca575'/><rect x='110' y='103' width='240' height='7' fill='#a05a3c'/>
<rect x='110' y='118' width='192' height='7' fill='#9ca575'/><rect x='110' y='127' width='480' height='7' fill='#a05a3c'/>
<rect x='110' y='142' width='480' height='7' fill='#9ca575'/><rect x='110' y='151' width='480' height='7' fill='#a05a3c'/>
<rect x='110' y='166' width='384' height='7' fill='#9ca575'/><rect x='110' y='175' width='48' height='7' fill='#a05a3c'/>
<rect x='110' y='190' width='240' height='7' fill='#9ca575'/><rect x='110' y='199' width='96' height='7' fill='#a05a3c'/>
<rect x='110' y='214' width='288' height='7' fill='#9ca575'/><rect x='110' y='223' width='240' height='7' fill='#a05a3c'/>
<rect x='110' y='238' width='192' height='7' fill='#9ca575'/><rect x='110' y='247' width='96' height='7' fill='#a05a3c'/>
<rect x='110' y='262' width='288' height='7' fill='#9ca575'/><rect x='110' y='271' width='192' height='7' fill='#a05a3c'/>
</g>
<rect x='600' y='22' width='10' height='7' fill='#9ca575'/><text x='614' y='29' %(F)s font-size='9.5' fill='#2f2e24'>importância</text>
<rect x='600' y='36' width='10' height='7' fill='#a05a3c'/><text x='614' y='43' %(F)s font-size='9.5' fill='#2f2e24'>ação</text>
<text x='600' y='180' %(F)s font-size='9.5' font-style='italic' fill='#a05a3c'>educação: 8 contra 1</text>
<text x='600' y='194' %(F)s font-size='9.5' font-style='italic' fill='#a05a3c'>trabalho: 4 contra 10</text>
</svg>
<figcaption>As notas do exemplo do slide. A distância entre as duas barras é o que interessa: onde a importância é alta e a ação é baixa está o alvo; onde a ação passa da importância (trabalho) está o que consome o tempo.</figcaption></figure>""" % dict(F=F)

DT13 = {
    'slug': 'aula13',
    'titulo_txt': 'Valores e programação de atividades: o que importa, o que se faz, e a agenda que repõe a função',
    'titulo_html': 'Valores e programa&ccedil;&atilde;o de atividades: o que importa, o que se faz, e a agenda que rep&otilde;e a fun&ccedil;&atilde;o',
    'data': 'Vídeo 13',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 13',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 13 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 13',
    'chave': 'mat-Aula-DT13-',
    'arquivo': 'Aula-DT13-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo terceiro vídeo da "
              u"disciplina, sobre valores e programação de atividades. Não havia transcrição.</p>"
              u"<p>Três instrumentos: a escala de importância e ação por área de vida, a programação de eventos agradáveis e a agenda semanal preenchida. Os exemplos são vinhetas dos slides.</p></div>"),
    'tema': 'Três ferramentas para responder à pergunta da preparação, o que entra no lugar da tela: a escala de valores por área, '
            'a lista de eventos agradáveis para quem não sabe o que gosta, e a agenda semanal com o antes e o depois.',
    'essencial': [
        ('Valor é importância menos ação.',
         'A escala pede duas notas por área, o quanto importa e o quanto a pessoa age. O alvo está onde a distância é maior.'),
        ('Quando o insight é baixo, a lista resolve.',
         'A programação de eventos agradáveis (Lewinsohn) pergunta frequência e prazer de cada atividade no último mês. Serve para descobrir o que a pessoa gostava e parou.'),
        ('A agenda mostra o antes e o depois na mesma célula.',
         'Redes sociais das 10h às 12h vira preparação do almoço; vídeos tediosos às 22h vira rotina noturna. A tela sai do horário e algo entra.'),
        ('A atividade se escolhe pela função e pelo valor.',
         'Caminhada de manhã e leitura no almoço não são aleatórias: cobrem autocuidado e educação, as áreas com maior distância na escala.'),
        ('A conclusão da semana é dado, e não nota.',
         'Totalmente, parcialmente, não cumpri. Serve para revisar a agenda, e não para julgar o paciente.'),
    ],
    'secoes': [
        ('s0', 'A escala de importância e ação', 'A escala de importância e ação por área de vida', u"""
{{GAP}}
<p>O vídeo abre com o instrumento que liga os vídeos anteriores à agenda: uma escala de onze áreas de vida, cada uma com duas notas de 1 a 10. A primeira é a <strong>importância</strong> (de nada importante a muito importante); a segunda é a <strong>ação</strong> (de baixa a alta). As áreas: relações familiares (sem contar cônjuge e filhos), casamento ou relacionamento afetivo, ser pai ou mãe, amizades, trabalho e carreira, finanças, educação e aprendizagem, lazer e hobbies, espiritualidade e sentido da vida, vida em sociedade e cidadania, autocuidado (descansar, dormir, exercício, alimentação).</p>
<p>No exemplo do slide, o paciente dá 9 para família e 4 de ação; 9 para relacionamento e 5; 8 para educação e 1; 5 para lazer e 2. E dá 4 para trabalho com 10 de ação. A leitura é direta: a pessoa está agindo muito onde importa pouco e pouco onde importa muito. O trabalho consome o tempo; família, relacionamento e educação ficam com a sobra, e a tela ocupa a sobra.</p>
<div class='obs'><h4>Como usar a escala</h4><p>Não é para somar. É para subtrair, área por área, e ordenar pela distância. As duas ou três áreas com maior distância entre importância e ação são as candidatas à agenda. E vale olhar também o sentido contrário: onde a ação passa muito da importância (trabalho, no exemplo, ou a própria tela, se ela entrasse na lista), é de onde o tempo vai sair.</p></div>
"""),
        ('s1', 'Eventos agradáveis', 'Quando o paciente não sabe o que gosta: a programação de eventos agradáveis', u"""
<p>O segundo slide resolve o problema mais comum da fase: o paciente que quer mudar, sabe que precisa fazer outra coisa, e não faz ideia do quê. Anos de tela costumam apagar o repertório de lazer. O slide diz: se o insight sobre que atividades fazer for baixo, opte pela <strong>programação de atividades agradáveis</strong>.</p>
<p>O instrumento mostrado é a <strong>Programação de Eventos Agradáveis</strong>, adaptada de Lewinsohn e Libet (1972). É uma lista longa de atividades, eventos e experiências (estar no campo, vestir roupa boa, contribuir com um grupo, conversar sobre esportes, conhecer alguém, e assim por diante), que a pessoa avalia duas vezes: primeiro, com que <strong>frequência</strong> cada uma aconteceu nos últimos 30 dias (nenhuma, algumas vezes, sete ou mais); depois, quanto <strong>prazer</strong> cada uma dá ou daria (nenhum, talvez, muito). Não há resposta certa.</p>
<p>O cruzamento das duas respostas é o que serve. Atividades com prazer alto e frequência zero são o achado: coisas que a pessoa gosta e parou de fazer. Elas entram na agenda antes de qualquer atividade nova, porque já têm o reforço garantido e não pedem que o paciente aprenda a gostar de nada.</p>
"""),
        ('s2', 'A agenda semanal', 'A agenda semanal: o antes e o depois', u"""
<p>O último slide é a agenda de um paciente, de segunda a sexta, em sete faixas de horário. Em cada célula, duas linhas: a primeira é o que <strong>acontecia</strong>, e a segunda é o que foi <strong>planejado</strong>. O que muda de uma linha para a outra é o tratamento inteiro.</p>
<ul class='key'><li><b>7h às 10h</b>: rotina matutina passa a incluir caminhada ou bicicleta de 20 minutos.</li><li><b>10h às 12h</b>: <em>uso de redes sociais</em> vira preparação do almoço.</li><li><b>12h às 14h30</b>: almoço sem celular, e leitura livre.</li><li><b>14h30 às 15h30</b>: <em>videogame</em> (segunda, quarta e sexta) vira preparação dos estudos; terça e quinta, estágio.</li><li><b>16h às 17h30</b>: revisão dos estudos para a faculdade, mantida.</li><li><b>17h30 às 22h</b>: faculdade, mantida.</li><li><b>22h às 23h</b>: <em>vídeos tediosos</em> vira rotina noturna.</li></ul>
<p>Na coluna final, a conclusão de cada dia: totalmente (segunda e sexta), parcialmente (terça e quinta), não cumpri (quarta). E, no rodapé, o que sustenta a agenda. <strong>Valores</strong>: estar mais conectado com as pessoas, poder fazer atividades diferentes como arte marcial, pintura e design, sentir-se menos ansioso, mais leve, mais ativo na vida. <strong>Consequência positiva</strong>: bem-estar, sensação de competência, pertencer a algum lugar.</p>
<div class='obs'><h4>Três coisas que a agenda faz bem</h4><p>Primeira: ela não tira a tela do dia inteiro; tira dos três horários em que ela era a resposta ao vazio (meio da manhã, meio da tarde, fim da noite), que são os quadrantes desagradáveis do vídeo 12. Segunda: o que entra em cada horário responde à escala: caminhada é autocuidado, leitura é educação, preparar o almoço é rotina que vira o dia, e as três eram áreas com distância grande. Terceira: a "consequência positiva" do rodapé é a função da tela (competência, pertencimento) reposta por outra via. É a balança do vídeo 11 fechando: as vantagens percebidas do uso agora têm outro fornecedor.</p></div>
"""),
        ('s3', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>Este vídeo é a ponte entre a formulação e o plano semanal, e cada instrumento responde a uma pergunta da rede.</p>
<ul class='key'><li><b>A escala de valores responde "para quê".</b> É o R do SMART, agora medido: as áreas de maior distância são os valores que o comportamento está deixando de servir.</li><li><b>A lista de eventos agradáveis responde "o quê".</b> Repõe repertório sem exigir insight, o que importa em quem passou anos com um único reforçador.</li><li><b>A agenda responde "quando e no lugar de quê".</b> Cada troca é uma substituição funcional no horário exato em que a tela entrava.</li><li><b>A conclusão diária é o monitoramento</b> do vídeo 7, na escala do vídeo 12, e a pergunta seguinte é sempre a mesma: o que impediu na quarta?</li></ul>
<p>Na prática: escala para escolher as áreas, lista para escolher as atividades, agenda para colocá-las no horário da tela, e revisão semanal do que foi cumprido.</p>
"""),
    ],
    'checklist': [
        'Apliquei a escala de importância e ação e ordenei as áreas pela distância entre as duas notas.',
        'Olhei também onde a ação passa da importância, para saber de onde o tempo vai sair.',
        'Quando o paciente não soube dizer o que gosta, usei a lista de eventos agradáveis em vez de insistir.',
        'Cruzei prazer alto com frequência zero e comecei por essas atividades.',
        'Montei a agenda com as duas linhas por célula: o que acontecia e o que entra.',
        'Coloquei atividade nos horários em que a tela era a resposta, e não em horários vazios.',
        'Escrevi os valores e a consequência positiva no rodapé da agenda, nas palavras do paciente.',
        'Revisei a conclusão de cada dia como dado para ajustar, e não como nota.',
    ],
    'questoes': [
        'Como funciona a escala de importância e ação, e o que se faz com as duas notas de cada área?',
        'No exemplo do slide, quais áreas têm a maior distância, e o que a nota de trabalho revela?',
        'Quando e por que usar a programação de eventos agradáveis, e como ler o cruzamento entre frequência e prazer?',
        'Descreva a agenda do slide: em que horários a tela saiu e o que entrou em cada um?',
        'Por que o rodapé da agenda (valores e consequência positiva) importa para a manutenção?',
        'Pense num paciente teu. Que área teria a maior distância na escala, e que atividade tu colocaria no horário em que ele mais usa a tela?',
    ],
    'gabarito': {
     0: (C, u"Onze áreas de vida, cada uma com nota de 1 a 10 para importância e para ação. Não se soma: subtrai-se área por área e ordena-se pela distância. As áreas com importância alta e ação baixa são candidatas à agenda; as com ação muito acima da importância mostram de onde o tempo vai sair."),
     1: (C, u"Educação (8 de importância, 1 de ação), família (9 e 4), relacionamento (9 e 5) e vida em sociedade (4 e 2, em proporção). Trabalho tem 4 de importância e 10 de ação: é o que consome o tempo, e o que sobra vai para a tela. A agenda do slide confirma: as substituições são em autocuidado, educação e rotina."),
     2: (C, u"Quando o insight sobre que atividades fazer é baixo, o que é comum depois de anos com um único reforçador. A lista pergunta frequência no último mês e prazer de cada atividade; as que têm prazer alto e frequência zero são o que a pessoa gostava e parou, e entram primeiro na agenda porque já têm reforço garantido."),
     3: (C, u"Redes sociais das 10h às 12h viraram preparação do almoço; videogame das 14h30 às 15h30 virou preparação dos estudos; vídeos tediosos das 22h às 23h viraram rotina noturna. Além disso, caminhada ou bicicleta de 20 minutos entrou na rotina matutina, e o almoço passou a ser sem celular, com leitura livre depois."),
     4: (C, u"Porque a agenda sem o para quê dura até a primeira semana ruim. Os valores (conexão, atividades diferentes, menos ansiedade) são o R da meta; a consequência positiva (bem-estar, competência, pertencimento) é a função que a tela cumpria, agora reposta por outra via. Sem isso, a agenda é uma lista de obrigações; com isso, é o caminho sonhado do vídeo 11 em horários."),
     5: (K, u"Não há resposta certa. Uma boa resposta identifica uma área específica com importância alta e ação baixa, localiza o horário de maior uso da tela (que costuma ser um quadrante desagradável) e propõe para esse horário uma atividade dessa área que o paciente já gostou um dia, com o valor escrito ao lado. O erro comum é escolher a atividade pelo que o terapeuta acha saudável, e não pela distância na escala do paciente."),
    },
    'referencias': [
        "Hayes, S. C., Strosahl, K. D., &amp; Wilson, K. G. (2012). <em>Acceptance and commitment therapy: The process and practice of mindful change</em> (2nd ed.). Guilford Press.",
        "Lewinsohn, P. M., &amp; Libet, J. (1972). Pleasant events, activity schedules, and depressions. <em>Journal of Abnormal Psychology, 79</em>(3), 291–295.",
        "Martell, C. R., Dimidjian, S., &amp; Herman-Dunn, R. (2010). <em>Behavioral activation for depression: A clinician's guide.</em> Guilford Press.",
        "Wilson, K. G., Sandoz, E. K., Kitchens, J., &amp; Roberts, M. (2010). The Valued Living Questionnaire: Defining and measuring valued action within a behavioral framework. <em>The Psychological Record, 60</em>(2), 249–272.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo terceiro vídeo de uma disciplina de pós-graduação; ação e manutenção vêm no vídeo 14.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. O gráfico de barras foi construído a partir das notas do exemplo do slide. Os quadros "como usar a escala", "três coisas que a agenda faz bem" e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina.<br><br><strong>Sobre os instrumentos.</strong> A escala de importância e ação por área segue a lógica do Valued Living Questionnaire (Wilson et al., 2010), citado como respaldo; o slide apresenta a escala como material do professor, para download, sem citar fonte. A Programação de Eventos Agradáveis está creditada no próprio slide a Lewinsohn e Libet (1972). O exemplo de agenda e as notas da escala são vinhetas dos slides, e não dados de paciente real.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'GAP': GAP}
DT13['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT13['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT13['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT13, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT13)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT13['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
