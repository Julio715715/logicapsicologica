# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 20: Prevenção à recaída. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

RISCO = u"""<figure class='dg'><div class='dg-t'>Fatores de risco e de proteção, por dimensão</div>
<svg viewBox='0 0 720 270' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Tabela de quatro dimensões, psicossocial, comportamental, cognitiva e emocional, ambiental, com o fator de risco e o fator de proteção correspondente do exemplo'>
<rect x='0' y='6' width='120' height='24' rx='5' fill='#43441f'/><text x='60' y='22' text-anchor='middle' %(F)s font-size='9.5' font-weight='800' fill='#f0ede0'>DIMENS&Atilde;O</text>
<rect x='126' y='6' width='290' height='24' rx='5' fill='#a05a3c'/><text x='271' y='22' text-anchor='middle' %(F)s font-size='9.5' font-weight='800' fill='#fff'>RISCO</text>
<rect x='422' y='6' width='298' height='24' rx='5' fill='#9ca575'/><text x='571' y='22' text-anchor='middle' %(F)s font-size='9.5' font-weight='800' fill='#fff'>PROTE&Ccedil;&Atilde;O</text>
<g %(F)s font-size='10' fill='#2f2e24'>
<text x='6' y='56' font-weight='800'>Psicossocial</text>
<text x='132' y='50'>carga horária de trabalho</text><text x='132' y='64'>semanal excessiva</text>
<text x='428' y='50'>atividades valorosas para equilibrar o</text><text x='428' y='64'>orçamento corporal; sono e alimentação</text>
<line x1='0' y1='78' x2='720' y2='78' stroke='#d9d3c1'/>
<text x='6' y='104' font-weight='800'>Comportamental</text>
<text x='132' y='98'>fazer tudo sozinho, tirando tempo</text><text x='132' y='112'>do sono; evitar situações temidas</text>
<text x='428' y='98'>apoio de profissionais, consultoria,</text><text x='428' y='112'>estagiário; solução de problemas,</text><text x='428' y='126'>adiamento da preocupação, exposição</text>
<line x1='0' y1='140' x2='720' y2='140' stroke='#d9d3c1'/>
<text x='6' y='166' font-weight='800'>Cognitivo e</text><text x='6' y='180' font-weight='800'>emocional</text>
<text x='132' y='160'>alta sensibilidade ao estresse nas</text><text x='132' y='174'>interações com clientes; intolerância</text><text x='132' y='188'>à incerteza</text>
<text x='428' y='160'>habilidade de regulação emocional;</text><text x='428' y='174'>contestação cognitiva</text>
<line x1='0' y1='202' x2='720' y2='202' stroke='#d9d3c1'/>
<text x='6' y='232' font-weight='800'>Ambiental</text>
<text x='132' y='226'>estressores ocupacionais: a escolha</text><text x='132' y='240'>da profissão (advocacia ou concurso)</text>
<text x='428' y='226'>escolha e manutenção de um projeto</text><text x='428' y='240'>de vida baseado nos valores</text>
</g>
</svg>
<figcaption>A tabela do slide, para um paciente advogado. Cada risco tem uma proteção na mesma linha, e as proteções são as técnicas dos vídeos anteriores com o nome do paciente.</figcaption></figure>""" % dict(F=F)

DT20 = {
    'slug': 'aula20',
    'titulo_txt': 'Prevenção à recaída: seis passos e uma tabela de riscos e proteções',
    'titulo_html': 'Preven&ccedil;&atilde;o &agrave; reca&iacute;da: seis passos e uma tabela de riscos e prote&ccedil;&otilde;es',
    'data': 'Vídeo 20',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 20',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 20 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 20',
    'chave': 'mat-Aula-DT20-',
    'arquivo': 'Aula-DT20-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do vigésimo vídeo da "
              u"disciplina, sobre a fase final: prevenção à recaída. Não havia transcrição.</p>"
              u"<p>A tabela de riscos e proteções é o exemplo do slide para um paciente advogado, e foi mantida como vinheta.</p></div>"),
    'tema': 'A fase final em seis passos: avaliar fatores de risco, conscientizar, desenvolver habilidades de enfrentamento, '
            'plano de ação personalizado, monitoramento contínuo e reforço de conquistas; e a tabela que junta tudo por dimensão.',
    'essencial': [
        ('Prevenção de recaída começa pela avaliação de risco.',
         'Estressores, padrões de pensamento e situações disparadoras deste paciente, antes de qualquer estratégia.'),
        ('O plano de ação é para quando os sintomas voltarem.',
         'Passos concretos em caso de sinais específicos ou situações difíceis. Um guia, e não uma promessa.'),
        ('Monitoramento contínuo pega o sinal cedo.',
         'Diários, escalas de humor, acompanhamento regular. É a EMA do vídeo 7 mantida depois da alta.'),
        ('Reforçar conquistas é fortalecer autoeficácia.',
         'Celebrar o progresso, por menor que seja, é o que sustenta a crença de superar desafios.'),
        ('Cada risco tem uma proteção na mesma linha.',
         'Psicossocial, comportamental, cognitivo-emocional, ambiental. A tabela é a formulação de manutenção do paciente.'),
    ],
    'secoes': [
        ('s0', 'Os seis passos', 'A fase final: seis passos', u"""
<p>A fase final tem por objetivo consolidar mudanças, manter ganhos e prevenir recaídas. O quadro lista o que a compõe: reforço da autoeficácia; planejamento de situações de risco; plano de ação em caso de recaída; discussão sobre o uso funcional da internet; rotina saudável; acompanhamento do progresso com tarefas entre sessões. Os dois slides seguintes organizam o trabalho em seis passos.</p>
<ul class='key'><li><b>1. Avaliação de fatores de risco.</b> Antes de implementar estratégias, uma avaliação minuciosa dos fatores de risco individuais: eventos estressores, padrões de pensamento disfuncionais e situações desencadeadoras que aumentam a vulnerabilidade à recaída.</li><li><b>2. Conscientização e psicoeducação.</b> Promover a conscientização do paciente sobre a própria condição e os desencadeadores; educar sobre os sinais precoces e sobre as estratégias de enfrentamento eficazes.</li><li><b>3. Desenvolvimento de habilidades de enfrentamento.</b> Regulação emocional, resolução de problemas e manejo do estresse; habilidades sociais, para fortalecer os relacionamentos.</li><li><b>4. Plano de ação personalizado.</b> Em colaboração com o paciente, um plano com passos concretos a seguir em caso de surgimento de sintomas específicos ou situações desafiadoras: um guia prático para enfrentar potenciais desafios.</li><li><b>5. Monitoramento contínuo.</b> Um sistema para identificar precocemente sinais de alerta: diários, escalas de avaliação de humor e acompanhamento regular das mudanças nos padrões.</li><li><b>6. Reforço de conquistas e autoeficácia.</b> Reforçar as conquistas alcançadas durante a terapia; celebrar os progressos, por menores que sejam, contribui para a motivação contínua e a crença de superar desafios.</li></ul>
<div class='obs'><h4>O que os seis passos têm de novo</h4><p>Quase nada, e é essa a lição. Regulação emocional é o vídeo 12; solução de problemas, o 15; habilidades sociais, o 19; monitoramento, o 7; sinais precoces, o 14. A prevenção de recaída não é uma técnica nova; é a organização das anteriores em torno de uma pergunta: o que este paciente vai fazer, sem o terapeuta, quando a situação de risco aparecer? O passo 4 é a resposta escrita, e o passo 1 é o que diz quais situações são essas.</p></div>
"""),
        ('s1', 'A tabela', 'A tabela de riscos e proteções', u"""
{{RISCO}}
<p>O último slide junta tudo numa tabela para um paciente específico, um advogado, em quatro dimensões.</p>
<ul class='key'><li><b>Psicossocial</b>. Risco: estressores significativos, especificamente carga horária de trabalho semanal excessiva. Proteção: atividades valorosas para equilibrar o orçamento corporal; hábitos de sono e alimentação regulares.</li><li><b>Comportamental</b>. Risco: fazer tudo sozinho, mesmo que implique usar tempo que não possui (retira tempo do sono); evitação de situações temidas. Proteção: apoio de profissionais mais habilitados, consultoria, estagiário; aplicação de solução de problemas, adiamento da preocupação e exposição direta, sempre que possível.</li><li><b>Cognitivo e emocional</b>. Risco: alta sensibilidade ao estresse, principalmente nas interações com clientes, gerando ansiedade; intolerância à incerteza. Proteção: habilidade de regulação emocional; contestação cognitiva.</li><li><b>Ambiental</b>. Risco: estressores ocupacionais em relação à escolha da profissão (manter-se na advocacia ou fazer concurso). Proteção: escolha e manutenção de um projeto de vida baseado nos valores.</li></ul>
<p>Três coisas para notar. Primeira: cada risco tem a proteção <strong>na mesma linha</strong>, e a proteção é uma técnica da disciplina com o nome do paciente ("estagiário" é solução de problemas aplicada; "projeto de vida baseado nos valores" é o vídeo 13). Segunda: a tabela não menciona a tela em nenhuma linha. O risco de recaída deste paciente não é o celular; é a carga horária, o fazer tudo sozinho, a sensibilidade ao cliente e a dúvida sobre a profissão. A tela é onde ele vai parar se esses quatro voltarem. Terceira: a dimensão ambiental tem a proteção mais lenta (um projeto de vida), e é a que mais sustenta as outras.</p>
<div class='callout note'><div class='co-t'>Como montar a tabela com o paciente</div>Uma linha por sessão, nas últimas sessões. Começar pelo risco: "quando tu recaiu ou quase recaiu, o que estava acontecendo?" A resposta cai numa das quatro dimensões. Depois a proteção: "e o que, de tudo que a gente fez, teria segurado?" A resposta é uma técnica que ele já conhece. A tabela pronta vai com ele, e o plano de ação (passo 4) é a coluna da direita em ordem: o que fazer primeiro quando o sinal da esquerda aparecer.</div>
"""),
        ('s2', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<ul class='key'><li><b>A tabela é a formulação de manutenção</b>: os riscos são os antecedentes que reativam a alça velha, e as proteções são as respostas alternativas que a rede nova já tem. Não há técnica nova porque não há nó novo; há a mesma rede sem o terapeuta.</li><li><b>O risco não é a tela.</b> É o contexto (carga horária), o comportamento (fazer sozinho), a cognição e o afeto (sensibilidade, incerteza) e o projeto de vida. A tela é o destino da alça, e não o gatilho.</li><li><b>O monitoramento contínuo é a discriminação</b> que permite agir no primeiro elo e não no último. Os sinais do vídeo 14 são o que se monitora.</li><li><b>Autoeficácia é o nó de self</b> que sustenta a manutenção quando a novidade acaba. Reforçar conquistas pequenas é alimentar esse nó com evidência.</li><li><b>Uso funcional da internet</b> é a meta realista: a rede nova inclui a tela, no lugar certo e com a função certa.</li></ul>
"""),
    ],
    'checklist': [
        'Avaliei os fatores de risco deste paciente (estressores, pensamentos, situações) antes de propor estratégias.',
        'Ensinei os sinais precoces de recaída, a partir da lista que o paciente deu no vídeo 14.',
        'Conferi que as habilidades de enfrentamento foram treinadas, e não só explicadas.',
        'Escrevi com o paciente o plano de ação: o que fazer primeiro quando cada sinal aparecer.',
        'Deixei um sistema de monitoramento (diário, escala, EMA) funcionando depois da alta.',
        'Reforcei conquistas concretas e nomeei a autoeficácia que elas mostram.',
        'Montei a tabela de riscos e proteções nas quatro dimensões, com uma proteção por risco.',
        'Conferi que a tabela fala do contexto do paciente, e não só da tela.',
        'Combinei o que é uso funcional de internet para este paciente.',
    ],
    'questoes': [
        'Liste os seis passos da prevenção à recaída e o que cada um envolve.',
        'Por que a prevenção de recaída "quase não tem técnica nova", e o que ela tem de específico?',
        'Descreva as quatro dimensões da tabela do slide, com o risco e a proteção de cada uma.',
        'Por que a tabela do exemplo não menciona a tela, e o que isso diz sobre onde está o risco?',
        'Como montar a tabela com o paciente, e como ela vira o plano de ação?',
        'Pense num paciente teu perto da alta. Preenche as quatro linhas: um risco e uma proteção por dimensão.',
    ],
    'gabarito': {
     0: (C, u"1, avaliação de fatores de risco: estressores, pensamentos disfuncionais, situações disparadoras. 2, conscientização e psicoeducação: condição, desencadeadores, sinais precoces, estratégias. 3, habilidades de enfrentamento: regulação emocional, solução de problemas, manejo do estresse, habilidades sociais. 4, plano de ação personalizado: passos concretos em caso de sintomas ou situações difíceis. 5, monitoramento contínuo: diários, escalas de humor, acompanhamento regular. 6, reforço de conquistas e autoeficácia: celebrar progressos, por menores que sejam."),
     1: (C, u"Porque regulação, solução de problemas, habilidades sociais, monitoramento e sinais precoces já foram trabalhados nos vídeos anteriores. O específico é a pergunta que organiza tudo: o que este paciente vai fazer, sem o terapeuta, quando a situação de risco aparecer. O passo 1 diz quais situações são essas e o passo 4 é a resposta escrita."),
     2: (C, u"Psicossocial: carga horária excessiva; atividades valorosas, sono e alimentação regulares. Comportamental: fazer tudo sozinho tirando tempo do sono, evitar situações temidas; apoio de profissionais, consultoria, estagiário, solução de problemas, adiamento da preocupação, exposição direta. Cognitivo e emocional: sensibilidade ao estresse com clientes, intolerância à incerteza; regulação emocional, contestação cognitiva. Ambiental: dúvida entre advocacia e concurso; projeto de vida baseado nos valores."),
     3: (C, u"Porque o risco de recaída não é o celular: é a carga horária, o fazer tudo sozinho, a sensibilidade ao cliente e a dúvida sobre a profissão. A tela é onde ele vai parar se esses quatro voltarem, ou seja, é o destino da alça, e não o gatilho. Prevenir recaída é proteger os quatro, e não vigiar a tela."),
     4: (C, u"Uma linha por sessão, nas últimas sessões. Começar pelo risco (\"quando tu quase recaiu, o que estava acontecendo?\"), que cai numa das dimensões; depois a proteção (\"o que, de tudo que a gente fez, teria segurado?\"), que é uma técnica já conhecida. A tabela vai com o paciente, e o plano de ação é a coluna da direita em ordem: o que fazer primeiro quando o sinal da esquerda aparecer."),
     5: (K, u"Não há resposta certa. Uma boa resposta preenche as quatro dimensões com riscos específicos do contexto do paciente (e não com \"usar o celular\") e com proteções que são técnicas já treinadas com ele, uma por linha, escritas de um jeito que ele reconheça. O erro comum é colocar a tela como risco em todas as linhas e \"reduzir o uso\" como proteção, o que não protege de nada."),
    },
    'referencias': [
        "Marlatt, G. A., &amp; Donovan, D. M. (Eds.). (2005). <em>Relapse prevention: Maintenance strategies in the treatment of addictive behaviors</em> (2nd ed.). Guilford Press.",
        "Witkiewitz, K., &amp; Marlatt, G. A. (2004). Relapse prevention for alcohol and drug problems: That was Zen, this is Tao. <em>American Psychologist, 59</em>(4), 224–235.",
        "W&ouml;lfling, K., M&uuml;ller, K. W., Dreier, M., Ruckes, C., Deuster, O., Batra, A., Mann, K., Musalek, M., Sch&uuml;tz, C., Hanke, S., &amp; Beutel, M. E. (2019). Efficacy of short-term treatment of internet and computer game addiction: A randomized clinical trial. <em>JAMA Psychiatry, 76</em>(10), 1018–1025.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o vigésimo vídeo de uma disciplina de pós-graduação; a psicoeducação para cuidadores e familiares vem no vídeo 21.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. A tabela foi redesenhada com o conteúdo do slide. Os quadros "o que os seis passos têm de novo", "como montar a tabela com o paciente" e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina. O exemplo do advogado é vinheta didática do slide.<br><br><strong>Referências.</strong> Os slides não citam fontes. O modelo de prevenção de recaída é o de Marlatt, citado como respaldo; a estrutura da fase final corresponde à do protocolo STICA (vídeo 8).<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'RISCO': RISCO}
DT20['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT20['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT20['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT20, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT20)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT20['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
