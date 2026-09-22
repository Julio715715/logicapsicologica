# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 8: Etapas do processo interventivo. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

FASES = u"""<figure class='dg'><div class='dg-t'>As três fases do processo interventivo</div>
<svg viewBox='0 0 720 262' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Três fases em sequência: psicoeducação, intervenções e prevenção de recaídas, com objetivo e conteúdo de cada uma'>
<defs><marker id='fs' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<line x1='0' y1='250' x2='720' y2='250' stroke='#9ca575' stroke-width='2'/>
<circle cx='115' cy='250' r='7' fill='#43441f'/><circle cx='360' cy='250' r='7' fill='#43441f'/><circle cx='605' cy='250' r='7' fill='#43441f'/>
<rect x='0' y='6' width='230' height='230' rx='12' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='14' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a8894f'>FASE INICIAL</text>
<text x='14' y='50' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>Psicoeducação</text>
<text x='14' y='70' %(F)s font-size='9.5' font-style='italic' fill='#6c6a55'>conscientizar sobre o transtorno e</text>
<text x='14' y='84' %(F)s font-size='9.5' font-style='italic' fill='#6c6a55'>os mecanismos de manutenção</text>
<text x='14' y='108' %(F)s font-size='10.5' fill='#2f2e24'>educação: aprendizagem e</text>
<text x='14' y='123' %(F)s font-size='10.5' fill='#2f2e24'>reforço, ciclo da dependência,</text>
<text x='14' y='138' %(F)s font-size='10.5' fill='#2f2e24'>impacto neurobiológico</text>
<text x='14' y='162' %(F)s font-size='10.5' fill='#2f2e24'>técnicas: entrevista motivacional,</text>
<text x='14' y='177' %(F)s font-size='10.5' fill='#2f2e24'>vantagens e desvantagens do</text>
<text x='14' y='192' %(F)s font-size='10.5' fill='#2f2e24'>comportamento atual, metas</text>
<text x='14' y='207' %(F)s font-size='10.5' fill='#2f2e24'>terapêuticas realistas</text>
<rect x='245' y='6' width='230' height='230' rx='12' fill='#43441f'/>
<text x='259' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#9ca575'>FASE INTERMEDI&Aacute;RIA</text>
<text x='259' y='50' %(F)s font-size='12' font-weight='800' fill='#f0ede0'>Intervenções</text>
<text x='259' y='70' %(F)s font-size='9.5' font-style='italic' fill='#c9c6a8'>modificar padrões de pensamento</text>
<text x='259' y='84' %(F)s font-size='9.5' font-style='italic' fill='#c9c6a8'>e comportamento desadaptativos</text>
<text x='259' y='108' %(F)s font-size='10.5' fill='#f0ede0'>comportamentais: monitorar uso e</text>
<text x='259' y='123' %(F)s font-size='10.5' fill='#f0ede0'>humor, reduzir gradualmente,</text>
<text x='259' y='138' %(F)s font-size='10.5' fill='#f0ede0'>substituir por offline, expor ao evitado</text>
<text x='259' y='162' %(F)s font-size='10.5' fill='#f0ede0'>habilidades: solução de problemas,</text>
<text x='259' y='177' %(F)s font-size='10.5' fill='#f0ede0'>comunicação e assertividade, tempo</text>
<text x='259' y='201' %(F)s font-size='10.5' fill='#f0ede0'>cognitivas: reestruturação</text>
<rect x='490' y='6' width='230' height='230' rx='12' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='504' y='30' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>FASE FINAL</text>
<text x='504' y='50' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>Prevenção de recaídas</text>
<text x='504' y='70' %(F)s font-size='9.5' font-style='italic' fill='#6c6a55'>consolidar mudanças, manter</text>
<text x='504' y='84' %(F)s font-size='9.5' font-style='italic' fill='#6c6a55'>ganhos e prevenir recaídas</text>
<text x='504' y='108' %(F)s font-size='10.5' fill='#2f2e24'>reforço da autoeficácia</text>
<text x='504' y='123' %(F)s font-size='10.5' fill='#2f2e24'>situações de risco planejadas</text>
<text x='504' y='138' %(F)s font-size='10.5' fill='#2f2e24'>plano de ação para a recaída</text>
<text x='504' y='153' %(F)s font-size='10.5' fill='#2f2e24'>uso funcional da internet</text>
<text x='504' y='168' %(F)s font-size='10.5' fill='#2f2e24'>rotina saudável</text>
<text x='504' y='183' %(F)s font-size='10.5' fill='#2f2e24'>tarefas entre sessões</text>
</svg>
<figcaption>As três fases do slide. A ordem é didática; na prática, a psicoeducação volta sempre que a motivação cai, e a prevenção de recaídas começa na primeira redução que dá certo.</figcaption></figure>""" % dict(F=F)

DT8 = {
    'slug': 'aula8',
    'titulo_txt': 'Etapas do processo interventivo: fármacos, grupos de apoio, o protocolo STICA e as três fases',
    'titulo_html': 'Etapas do processo interventivo: f&aacute;rmacos, grupos de apoio, o protocolo STICA e as tr&ecirc;s fases',
    'data': 'Vídeo 8',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 8',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 8 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 8',
    'chave': 'mat-Aula-DT8-',
    'arquivo': 'Aula-DT8-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do oitavo vídeo da "
              u"disciplina, sobre as etapas do processo interventivo. Não havia transcrição.</p>"
              u"<p>A tabela de farmacologia foi mantida como os slides a apresentam, com uma moderação sobre o peso da evidência "
              u"de cada classe, sinalizada no texto. Psicólogo não prescreve; a seção serve para conversar com o psiquiatra.</p></div>"),
    'tema': 'O que a farmacologia oferece e com que evidência, o lugar dos grupos de apoio, o protocolo STICA e seu ensaio clínico, '
            'e as três fases do processo interventivo: psicoeducação, intervenções e prevenção de recaídas.',
    'essencial': [
        ('Fármaco é adjuvante, e a evidência é desigual.',
         'Antagonistas opioides têm o melhor apoio para jogo de azar; ISRS ajudam pela comorbidade; lítio, no bipolar; antipsicóticos, quase nunca.'),
        ('Jogadores Anônimos existe no Brasil e custa zero.',
         'Doze passos, reuniões presenciais, anonimato. Serve de rede para o paciente que não tem outra, e não substitui a terapia.'),
        ('STICA: 23 sessões em quatro meses, grupo mais individual.',
         'Protocolo cognitivo-comportamental para dependência de internet e jogos, testado em ensaio randomizado publicado no JAMA Psychiatry em 2019.'),
        ('Três fases, três objetivos.',
         'Psicoeducação para entender o ciclo e querer mudar; intervenções para mudar pensamento e comportamento; prevenção de recaídas para manter.'),
        ('A fase inicial é onde se perde o paciente.',
         'Entrevista motivacional, balança de vantagens e desvantagens e metas realistas vêm antes de qualquer redução. O vídeo 9 é sobre isso.'),
    ],
    'secoes': [
        ('s0', 'Farmacologia', 'Farmacologia: o que existe e com que evidência', u"""
<p>O vídeo abre com uma tabela de medicações usadas no jogo patológico. Ela está aqui como o slide a apresenta, seguida de uma moderação, porque o peso da evidência varia muito de uma linha para outra.</p>
<ul class='key'><li><b>Fluoxetina, paroxetina (ISRS)</b>: redução da compulsão e controle de impulsos; úteis quando há comorbidade com depressão ou ansiedade.</li><li><b>Naltrexona (antagonista opioide)</b>: reduz o prazer associado ao jogo e a frequência dos episódios; eficaz em pacientes com comportamento de jogo altamente recompensador.</li><li><b>Lítio (estabilizador de humor)</b>: redução de impulsividade e estabilização emocional; especialmente útil em pacientes com transtorno bipolar.</li><li><b>Topiramato (estabilizador de humor, anticonvulsivante)</b>: redução da excitação associada ao jogo; pode ajudar com impulsividade.</li><li><b>Quetiapina, olanzapina (antipsicóticos atípicos)</b>: indicados em casos com sintomas psicóticos ou comorbidades graves; uso limitado, geralmente adjuvante.</li></ul>
<div class='obs'><h4>Uma moderação, para conversar com o psiquiatra</h4><p>Nenhuma medicação tem aprovação específica para transtorno do jogo, e as metanálises mostram efeitos modestos. O que se sustenta melhor: os <strong>antagonistas opioides</strong> (naltrexona, nalmefeno) têm o corpo de ensaios mais consistente, sobretudo em quem tem fissura intensa ou história familiar de alcoolismo. Os <strong>ISRS</strong> têm resultados mistos quando o jogo é o alvo direto; funcionam melhor como tratamento da comorbidade. O <strong>lítio</strong> tem um ensaio positivo em jogadores com espectro bipolar, e é para esse subgrupo. O <strong>topiramato</strong> tem estudos pequenos. Os <strong>antipsicóticos</strong> não mostraram benefício sobre o jogo em si nos ensaios com olanzapina; a indicação da tabela é para a comorbidade psicótica, não para o jogo. Em resumo: fármaco é adjuvante, escolhido pela comorbidade e pela fissura, e a psicoterapia continua sendo o tratamento de primeira linha. As duas fontes citadas no slide (Weinstock e Ledgerwood, 2008; Júnior e Sousa, 2024) não puderam ser conferidas e ficaram fora das referências; a metanálise que sustenta esta moderação está lá.</p></div>
"""),
        ('s1', 'Jogadores Anônimos', 'Grupos de apoio: Jogadores Anônimos', u"""
<p>O segundo slide é o site dos <strong>Jogadores Anônimos</strong> no Brasil: os doze passos de recuperação, os doze de unidade, as vinte perguntas, literatura, depoimentos, anonimato, reuniões presenciais, e os endereços dos escritórios de serviço em São Paulo e no Rio de Janeiro. O vídeo o apresenta como recurso a indicar.</p>
<p>Vale saber o que ele é e o que não é. É uma irmandade de doze passos, no modelo dos Alcoólicos Anônimos, gratuita, com reuniões regulares e uma rede de pessoas que passaram pelo mesmo. Para o paciente que perdeu a rede social por causa do jogo (critério 8 do vídeo 6), isso tem valor que a terapia individual não consegue oferecer. O que ele não é: tratamento com evidência controlada. A adesão costuma ser baixa e a evasão, alta, e os estudos mostram resultado melhor quando o grupo é combinado com psicoterapia, e não usado sozinho.</p>
<div class='callout note'><div class='co-t'>Como indicar</div>Como complemento, e com expectativa ajustada: "é um lugar onde tu vai encontrar gente que entende, e onde ninguém vai te cobrar nada". Para o paciente cujo modelo de abstinência total combina com os doze passos, a adesão é maior. Para quem tem meta de uso controlado (mais comum nas dependências tecnológicas que no jogo de azar), a lógica do grupo pode entrar em conflito com o plano, e vale conversar sobre isso antes.</div>
"""),
        ('s2', 'O protocolo STICA', 'O protocolo STICA e o ensaio clínico', u"""
<p>O <strong>manual STICA</strong> (Short-term Treatment for Internet and Computer game Addiction) é baseado numa abordagem cognitivo-comportamental e combina sessões de terapia em grupo com atendimentos individuais. O protocolo compreende <strong>23 sessões ao longo de quatro meses</strong>. O slide mostra o artigo que o testou: Wölfling e colaboradores, ensaio clínico randomizado publicado no <em>JAMA Psychiatry</em> em 2019.</p>
<p>O que o ensaio mostrou, em resumo: adultos do sexo masculino com dependência de internet ou de jogos, tratados com o STICA, tiveram taxa de remissão bem maior que os do grupo em lista de espera ao fim dos quatro meses, com redução dos sintomas e do tempo de uso. É um dos poucos ensaios randomizados de porte na área, e por isso o protocolo serve de referência: não porque seja o único caminho, mas porque foi testado.</p>
<p>A estrutura dele é a que o vídeo desdobra na seção seguinte: uma fase de psicoeducação e motivação, uma fase de intervenções comportamentais, cognitivas e de habilidades, e uma fase de estabilização e prevenção de recaídas, com grupo para o treino e individual para o que é de cada um.</p>
"""),
        ('s3', 'As três fases', 'As três fases do processo interventivo', u"""
{{FASES}}
<h3>Fase inicial: psicoeducação</h3>
<p>Objetivo: conscientizar o paciente sobre o transtorno e os mecanismos de manutenção do comportamento aditivo. Educação sobre modelos de aprendizagem e reforço, sobre o ciclo da dependência (o do vídeo 6) e sobre o impacto neurobiológico. Técnicas: <strong>entrevista motivacional</strong>, <strong>análise de vantagens e desvantagens</strong> do comportamento atual, e <strong>estabelecimento de metas terapêuticas realistas</strong>.</p>
<p>É a fase em que se perde o paciente, e por um motivo simples: ele chegou trazido, ou chegou querendo parar de sofrer sem parar de usar. Antes de qualquer redução, é preciso que a mudança seja dele. Por isso a entrevista motivacional abre a lista, e por isso o vídeo 9 é inteiro sobre ela.</p>
<h3>Fase intermediária: intervenções</h3>
<p>Objetivo: modificar padrões de pensamento e comportamento desadaptativos. Três frentes.</p>
<ul class='key'><li><b>Intervenções comportamentais</b>: monitoramento do uso e do humor (a EMA do vídeo 7 continua aqui), redução gradual do tempo online, substituição por atividades offline, exposição gradual a situações evitadas, como atividades sociais.</li><li><b>Treinamento em habilidades</b>: solução de problemas, comunicação social e assertividade, organização e gestão do tempo. É aqui que se repõe o que a tela fazia pela pessoa: a interação controlável da ansiedade social, a fuga da tarefa difícil, a ocupação do tempo vazio.</li><li><b>Intervenções cognitivas</b>: reestruturação cognitiva, das cognições permissivas do ciclo ("só dez minutos") e, no jogo de azar, das crenças sobre o acaso (vídeo 5).</li></ul>
<h3>Fase final: prevenção de recaídas</h3>
<p>Objetivo: consolidar mudanças, manter ganhos e prevenir recaídas. Reforço da autoeficácia; planejamento de situações de risco; elaboração de plano de ação em caso de recaída; discussão sobre o <strong>uso funcional da internet</strong>, porque abstinência total de tela não é meta viável para quase ninguém; estabelecimento de rotina saudável; e acompanhamento do progresso com tarefas entre sessões.</p>
<div class='obs'><h4>Duas observações sobre a ordem</h4><p>Primeira: a sequência é didática. A psicoeducação volta sempre que a motivação cai, e a prevenção de recaídas começa na primeira redução que dá certo, porque é ali que aparece a primeira situação de risco real. Segunda: a "redução gradual do tempo online" é o item que mais tenta o terapeuta a começar por ele. O ciclo do vídeo 6 explica por que isso não segura sozinho: o comportamento é a única etapa que o ciclo repõe automaticamente. Reduzir horas sem repor a função é combinar recaída.</p></div>
"""),
        ('s4', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>As três fases mapeiam com folga numa formulação processual, e a leitura ajuda a decidir o que fazer com cada paciente, em vez de aplicar o protocolo em ordem.</p>
<ul class='key'><li><b>Psicoeducação e entrevista motivacional</b> trabalham o nó de motivação e o de self: a pessoa passar a ver o ciclo como dela, e a mudança como dela. Sem esse nó, o resto não engata.</li><li><b>Monitoramento e redução gradual</b> mexem na frequência do comportamento; <b>substituição e exposição</b> mexem no que ele evita; <b>habilidades</b> repõem a função. São três alvos diferentes, e o paciente costuma precisar mais de um que dos outros.</li><li><b>Reestruturação cognitiva</b> mira as cognições permissivas e, no jogo de azar, a ilusão de controle. É a alça cognitiva do ciclo.</li><li><b>Prevenção de recaídas</b> é o trabalho sobre a alça de manutenção: o que fazer quando a emoção reativa (vergonha, frustração) tentar reabrir o precipitante.</li><li><b>Fármaco e grupo de apoio</b> entram pelo contexto: comorbidade e fissura, de um lado; rede social perdida, de outro.</li></ul>
<p>Na prática: o protocolo dá a caixa de ferramentas e a ordem sugerida; a formulação diz qual ferramenta este paciente precisa primeiro.</p>
"""),
    ],
    'checklist': [
        'Quando há comorbidade ou fissura intensa, encaminhei ao psiquiatra com a formulação e a pergunta certa, e não com o pedido genérico de remédio.',
        'Apresentei o grupo de apoio como complemento, com expectativa ajustada e atenção ao conflito entre abstinência e uso controlado.',
        'Comecei pela psicoeducação e pela motivação, e não pela redução de horas.',
        'Fiz a balança de vantagens e desvantagens do comportamento atual com o paciente, e não para ele.',
        'Combinei metas realistas, incluindo o que é uso funcional de internet para esta pessoa.',
        'Para cada redução planejada, defini o que entra no lugar (atividade, habilidade, contato).',
        'Montei o plano de ação para a recaída antes da primeira situação de risco, e não depois.',
        'Mantive tarefas entre sessões e monitoramento do uso e do humor durante todo o tratamento.',
    ],
    'questoes': [
        'Descreva as cinco classes de medicação da tabela e diga, para cada uma, qual é o peso da evidência para o jogo de azar.',
        'O que os Jogadores Anônimos oferecem que a psicoterapia individual não oferece, e qual é o limite dessa indicação?',
        'O que é o protocolo STICA, como é estruturado e o que o ensaio de 2019 mostrou?',
        'Enumere as três fases do processo interventivo, com o objetivo e as principais técnicas de cada uma.',
        'Por que reduzir o tempo online sem repor a função costuma falhar? Use o ciclo do vídeo 6 na resposta.',
        'Pense num paciente teu. Em que fase ele está de fato, e qual ferramenta do protocolo ele precisa primeiro?',
    ],
    'gabarito': {
     0: (C, u"ISRS (fluoxetina, paroxetina): compulsão e impulsos, úteis na comorbidade; evidência mista quando o jogo é o alvo direto. Naltrexona: reduz prazer e frequência; é a classe com evidência mais consistente, sobretudo com fissura intensa. Lítio: impulsividade e estabilização; apoio em jogadores com espectro bipolar. Topiramato: excitação e impulsividade; estudos pequenos. Antipsicóticos atípicos: só para comorbidade psicótica ou grave; sem benefício sobre o jogo em si nos ensaios. Em todas, adjuvante; a psicoterapia é a primeira linha."),
     1: (C, u"Oferecem uma rede de pessoas que passaram pelo mesmo, gratuita, com reuniões regulares e anonimato, o que repõe parte da rede social que o jogo destruiu. O limite: não é tratamento com evidência controlada, a evasão é alta e o resultado é melhor combinado com psicoterapia; e o modelo de abstinência total pode conflitar com metas de uso controlado, o que pede conversa antes da indicação."),
     2: (C, u"Short-term Treatment for Internet and Computer game Addiction: protocolo cognitivo-comportamental de 23 sessões em quatro meses, combinando grupo e atendimentos individuais. O ensaio randomizado de Wölfling e colaboradores (JAMA Psychiatry, 2019) mostrou taxa de remissão maior no grupo tratado do que na lista de espera ao fim do tratamento, com redução de sintomas e de tempo de uso."),
     3: (C, u"Inicial, psicoeducação: conscientizar sobre o transtorno e o ciclo de manutenção; entrevista motivacional, balança de vantagens e desvantagens, metas realistas. Intermediária, intervenções: modificar pensamento e comportamento; monitoramento, redução gradual, substituição por offline, exposição ao evitado, habilidades (problemas, assertividade, tempo), reestruturação cognitiva. Final, prevenção de recaídas: consolidar e manter; autoeficácia, situações de risco, plano de ação para recaída, uso funcional da internet, rotina, tarefas entre sessões."),
     4: (C, u"Porque no ciclo o comportamento é a única etapa que se repõe sozinha: os precipitantes continuam acontecendo, as cognições permissivas continuam disponíveis e a função (reforço, alívio, controle) continua sem outra fonte. Reduzir horas tira o comportamento sem tirar o que o produz, e o ciclo o devolve na primeira noite de domingo. A redução funciona quando vem junto com a substituição, a habilidade ou a exposição que repõe a função."),
     5: (K, u"Não há resposta certa. Uma boa resposta localiza o paciente pela motivação e pela função, e não pelo tempo de tratamento (um paciente na décima sessão pode estar ainda na fase inicial), e escolhe a ferramenta pelo que falta: motivação, uma habilidade específica, uma crença, um plano para a recaída. O erro comum é seguir a ordem do protocolo com um paciente que ainda não decidiu mudar."),
    },
    'referencias': [
        "Goslar, M., Leibetseder, M., Muench, H. M., Hofmann, S. G., &amp; Laireiter, A.-R. (2019). Pharmacological treatments for disordered gambling: A meta-analysis. <em>Journal of Behavioral Addictions, 8</em>(2), 194–208.",
        "Petry, N. M. (2005). <em>Pathological gambling: Etiology, comorbidity, and treatment.</em> American Psychological Association.",
        "Potenza, M. N., Balodis, I. M., Derevensky, J., Grant, J. E., Petry, N. M., Verdejo-Garcia, A., &amp; Yip, S. W. (2019). Gambling disorder. <em>Nature Reviews Disease Primers, 5</em>, 51.",
        "Stevens, M. W. R., King, D. L., Dorstyn, D., &amp; Delfabbro, P. H. (2019). Cognitive-behavioral therapy for internet gaming disorder: A systematic review and meta-analysis. <em>Clinical Psychology &amp; Psychotherapy, 26</em>(2), 191–203.",
        "W&ouml;lfling, K., M&uuml;ller, K. W., Dreier, M., Ruckes, C., Deuster, O., Batra, A., Mann, K., Musalek, M., Sch&uuml;tz, C., Hanke, S., &amp; Beutel, M. E. (2019). Efficacy of short-term treatment of internet and computer game addiction: A randomized clinical trial. <em>JAMA Psychiatry, 76</em>(10), 1018–1025.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o oitavo vídeo de uma disciplina de pós-graduação; a entrevista motivacional vem no vídeo 9.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. A descrição do que o ensaio do STICA mostrou, a leitura dos Jogadores Anônimos como complemento, as duas observações sobre a ordem das fases e a seção final em processos foram desenvolvidas pelo autor do material a partir da lógica da disciplina e da literatura citada.<br><br><strong>Uma moderação, sinalizada no texto.</strong> A tabela de farmacologia foi mantida como o slide a apresenta, e o material acrescenta o peso da evidência por classe, com base na metanálise de Goslar e colaboradores (2019) e na revisão de Potenza e colaboradores (2019): antagonistas opioides com o apoio mais consistente, ISRS pela comorbidade, lítio no espectro bipolar, topiramato com estudos pequenos, antipsicóticos sem benefício sobre o jogo. As duas fontes citadas no slide (Weinstock e Ledgerwood, 2008; Júnior e Sousa, 2024) não puderam ser conferidas e ficaram fora das referências. Psicólogo não prescreve; a seção existe para a conversa com o psiquiatra.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'FASES': FASES}
DT8['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DT8['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT8['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT8, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT8)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT8['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
