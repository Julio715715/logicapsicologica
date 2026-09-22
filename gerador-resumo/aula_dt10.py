# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 10: Fase da pré-contemplação. Fonte: slides (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

CRENCAS = u"""<figure class='dg'><div class='dg-t'>Três famílias de crenças que sustentam a aposta</div>
<svg viewBox='0 0 720 214' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Três caixas: persistência, previsão e plano, com as frases típicas do paciente, e embaixo o alvo: manejo das expectativas e psicoeducação do acaso'>
<rect x='0' y='6' width='226' height='140' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='12' y='30' %(F)s font-size='11.5' font-weight='800' fill='#2f2e24'>Persistência</text>
<text x='12' y='54' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>"se eu insistir, uma hora a</text>
<text x='12' y='68' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>sorte vira para o meu lado"</text>
<text x='12' y='90' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>"minha habilidade tá melhorando"</text>
<text x='12' y='112' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>"sou brasileiro, não desisto nunca"</text>
<rect x='247' y='6' width='226' height='140' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='259' y='30' %(F)s font-size='11.5' font-weight='800' fill='#2f2e24'>Previsão</text>
<text x='259' y='54' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>"se eu estudar os resultados,</text>
<text x='259' y='68' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>vou achar um padrão"</text>
<rect x='494' y='6' width='226' height='140' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='506' y='30' %(F)s font-size='11.5' font-weight='800' fill='#2f2e24'>Plano</text>
<text x='506' y='54' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>"nada é por acaso, é só observar</text>
<text x='506' y='68' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>os padrões e apostar do jeito certo"</text>
<text x='506' y='90' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>"meu pai é sortudo, vou colocar</text>
<text x='506' y='104' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>a data de aniversário dele"</text>
<rect x='120' y='162' width='480' height='46' rx='10' fill='#43441f'/>
<text x='360' y='182' text-anchor='middle' %(F)s font-size='11.5' font-weight='800' fill='#f0ede0'>alvo: manejo das expectativas e psicoeducação do acaso</text>
<text x='360' y='199' text-anchor='middle' %(F)s font-size='10' fill='#9ca575'>as três são a ilusão de controle do vídeo 5 em roupas diferentes</text>
</svg>
<figcaption>As frases dos slides, agrupadas. Persistência nega a independência do acaso; previsão nega a imprevisibilidade; plano nega a incontrolabilidade. São as três propriedades do vídeo 5, cada uma negada por uma crença.</figcaption></figure>""" % dict(F=F)

DT10 = {
    'slug': 'aula10',
    'titulo_txt': 'Pré-contemplação: o ciclo, as crenças sobre o acaso e o que a neurobiologia diz (e o que não diz)',
    'titulo_html': 'Pr&eacute;-contempla&ccedil;&atilde;o: o ciclo, as cren&ccedil;as sobre o acaso e o que a neurobiologia diz (e o que n&atilde;o diz)',
    'data': 'Vídeo 10',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 10',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 10 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 10',
    'chave': 'mat-Aula-DT10-',
    'arquivo': 'Aula-DT10-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do décimo vídeo da "
              u"disciplina, sobre a fase de pré-contemplação. Não havia transcrição.</p>"
              u"<p>O vídeo desdobra os três conteúdos da psicoeducação (ciclo, crenças, neurobiologia) e fecha com a ficha do estágio. "
              u"Há uma moderação sobre as afirmações neurobiológicas, sinalizada no texto.</p></div>"),
    'tema': 'O paciente que não vê problema: o que ensinar (ciclo da dependência, crenças sobre o acaso, neurobiologia), '
            'como perguntar sem julgar, e o cuidado para que a psicoeducação não vire discurso.',
    'essencial': [
        ('Pré-contemplação: "eu nem vejo isso como um problema".',
         'O paciente não reconhece o comportamento como prejudicial, pode estar defensivo ou achar que todo mundo faz isso. A intervenção é informação sem julgamento.'),
        ('O ciclo é o primeiro conteúdo da psicoeducação.',
         'Precipitante, cognição permissiva, comportamento, reforço, consequência, emoção reativa. Mostrar o ciclo com o material do paciente já é intervenção.'),
        ('As crenças sobre o acaso se agrupam em três.',
         'Persistência, previsão e plano. Cada uma nega uma propriedade do acaso: independente, imprevisível, incontrolável.'),
        ('A neurobiologia entra como explicação, não como sentença.',
         'Reforço positivo e negativo, tolerância, controle pré-frontal imaturo no adolescente. Vale ensinar, com a dose certa.'),
        ('Perguntas antes de informação.',
         'As três perguntas do vídeo 9 abrem a percepção; a informação neuropsicológica vem depois, e só se o paciente quiser ouvir.'),
    ],
    'secoes': [
        ('s0', 'A ficha do estágio', 'Pré-contemplação: a ficha do estágio', u"""
<p>O vídeo abre a série de um vídeo por estágio de mudança. O primeiro é a <strong>pré-contemplação</strong>, que o slide resume na frase do paciente: <em>"Eu nem vejo isso como um problema."</em></p>
<ul class='key'><li><b>Características</b>: o paciente não reconhece o comportamento como prejudicial. Pode estar defensivo, desinteressado, ou acreditar que "todo mundo faz isso". Resiste à ideia de mudança.</li><li><b>Perguntas</b> (as três do roteiro do vídeo 9): se já pensou que o tempo de uso pode estar atrapalhando alguma área da vida; se alguém já disse que ele usa ou joga demais, e o que ele acha disso; o que sente quando está desconectado ou não pode jogar.</li><li><b>Intervenção</b>: fornecer informações sem julgamento, principalmente sobre os aspectos neuropsicológicos e os impactos na saúde mental.</li></ul>
<p>O resto do vídeo é o conteúdo dessa informação, nos três blocos que a fase inicial lista: ciclo da dependência, modelos de aprendizagem e reforço, impacto neurobiológico. Antes de entrar neles, vale fixar a ordem: <strong>perguntas primeiro, informação depois</strong>. Informação dada a quem não perguntou vira o discurso da família com outra voz.</p>
"""),
        ('s1', 'O ciclo, de novo', 'O ciclo da dependência, agora como psicoeducação', u"""
<p>O ciclo sucessivo de feedback (vídeo 6) volta aqui com outra função. No vídeo 6 ele era ferramenta do terapeuta para formular; agora é conteúdo para ensinar ao paciente. As seis etapas são as mesmas: precipitantes (tédio, estresse, briga familiar), cognições ("só vou jogar dez minutos", "preciso checar o que estão dizendo"), comportamento (horas de jogo, apostas, verificação), reforço (prazer ou alívio, sensação de controle, distração dos problemas), consequências (culpa, perda de tempo, insônia, isolamento) e emoções negativas reativas (tristeza, frustração, vergonha), que reabrem o ciclo.</p>
<div class='obs'><h4>Como ensinar o ciclo a quem não vê problema</h4><p>Não como diagrama pronto. Pedindo o último episódio: o que estava acontecendo antes, o que passou pela cabeça, o que fez, o que sentiu na hora, o que aconteceu depois, e como ficou. O paciente monta o ciclo com o material dele, e o terapeuta só dá nome às etapas. Para o pré-contemplador, é a intervenção mais poderosa do vídeo, porque ele descobre o problema descrevendo, e não ouvindo.</p></div>
"""),
        ('s2', 'As crenças sobre o acaso', 'As cognições no jogo de azar: persistência, previsão e plano', u"""
{{CRENCAS}}
<p>O slide seguinte abre a etapa "cognições" do ciclo para o caso do jogo de azar, e agrupa as frases do paciente em três famílias.</p>
<ul class='key'><li><b>Persistência</b>: "se eu persistir e insistir, uma hora a sorte vira para o meu lado"; "minha habilidade tá melhorando"; "sou brasileiro, não desisto nunca". É a negação da independência do acaso: a pessoa acredita que as rodadas anteriores acumulam algo a favor dela.</li><li><b>Previsão</b>: "se eu estudar os resultados, vou achar um padrão". É a negação da imprevisibilidade: tratar uma sequência aleatória como se tivesse estrutura.</li><li><b>Plano</b>: "nada é por acaso, é só observar os padrões e fazer a aposta do jeito certo"; "meu pai é sortudo, vou colocar a data de aniversário dele". É a negação da incontrolabilidade: método, ritual, talismã.</li></ul>
<p>O alvo, escrito no slide: <strong>manejo das expectativas e psicoeducação do acaso</strong>. É a primeira tarefa clínica do vídeo 5, agora com a lista de frases para reconhecer na fala do paciente. Note que a frase "sou brasileiro, não desisto nunca" mostra como uma virtude cultural (persistência) é recrutada pelo jogo: o que serve para treinar e trabalhar não serve para a roleta, porque a roleta não aprende que a pessoa insiste.</p>
"""),
        ('s3', 'A neurobiologia', 'O impacto neurobiológico: o que ensinar', u"""
<p>Dois slides tratam da base neurobiológica. O primeiro, com a figura do celular e do cérebro: a notificação chega e a área tegmental ventral libera dopamina; a dopamina vai ao núcleo accumbens (prazer) e ao córtex pré-frontal (impulsividade). Ao lado, três pontos: no <strong>sistema dopaminérgico</strong>, a liberação no circuito de recompensa aumenta com o uso repetido, e quanto mais a pessoa joga ou navega, maior a necessidade de estímulo para o mesmo prazer (tolerância); na <strong>imaturidade pré-frontal do adolescente</strong>, a região que regula controle inibitório e julgamento ainda está em desenvolvimento, o que o torna mais vulnerável a comportamentos compulsivos; e nas <strong>mudanças estruturais e funcionais</strong>, estudos de neuroimagem mostraram ativação semelhante à de usuários de drogas, com prejuízo em planejamento, tomada de decisão, inibição de impulsos e regulação emocional.</p>
<p>O segundo slide resume o modelo: o uso excessivo produz picos rápidos de dopamina, semelhantes aos de substâncias psicoativas, gerando <strong>reforço positivo</strong> (prazer imediato) e <strong>reforço negativo</strong> (redução de tédio ou ansiedade), o que mantém o comportamento. Na dependência tecnológica haveria hipofunção do córtex pré-frontal (menos autocontrole), hiperativação da amígdala diante de gatilhos digitais, envolvimento do hipocampo na associação de recompensas e participação do cerebelo e da ínsula na integração emocional e na fissura. O desequilíbrio entre recompensa hiperativa e controle executivo hipoativo dificulta a interrupção mesmo com prejuízo, o que justifica intervenções voltadas ao fortalecimento do autocontrole, como mindfulness e autorregulação.</p>
<div class='obs'><h4>Uma moderação, e a dose certa para o paciente</h4><p>O que se sustenta bem: reforço positivo e negativo, tolerância como fenômeno comportamental, e a maturação tardia do controle pré-frontal no adolescente. O que pede cautela: a comparação com substâncias. Os picos de dopamina de uma notificação são ordens de grandeza menores que os de uma droga, e os estudos de neuroimagem em dependência tecnológica são em geral pequenos, transversais e concentrados em jogos pela internet; mostram semelhança de padrão, não equivalência. Dizer ao paciente que "o celular sequestra o cérebro como a cocaína" tem dois problemas: é impreciso, e tira a agência de quem precisa dela para mudar. A dose certa na psicoeducação é a do reforço: o aparelho entrega recompensa rápida e alívio rápido, o cérebro aprende isso depressa, e por isso parar custa. Verdadeiro, suficiente, e deixa o paciente no lugar de quem pode fazer algo.</p></div>
"""),
        ('s4', 'Lendo em processos', 'Lendo o vídeo em processos', u"""
<p>A pré-contemplação, lida em processos, não é um estágio do paciente; é um estado da relação dele com o próprio ciclo.</p>
<ul class='key'><li><b>O que falta não é informação, é discriminação.</b> O paciente pré-contemplador em geral sabe que usa muito. O que ele não fez foi ligar o uso ao que perde. Ensinar o ciclo com o material dele cria essa ligação.</li><li><b>As crenças sobre o acaso são o nó cognitivo mais barato de mexer</b>, porque são falsas de um jeito demonstrável. Mas só depois que o paciente quer olhar; antes disso, corrigir a crença é discutir com a defesa.</li><li><b>A neurobiologia serve para tirar culpa, não para tirar responsabilidade.</b> "Teu cérebro aprendeu isso rápido porque a recompensa é rápida" alivia a vergonha, que é a emoção que fecha o ciclo. "Teu cérebro está sequestrado" alimenta a impotência, que é a emoção que sustenta o coping.</li><li><b>As três perguntas do roteiro</b> são intervenção sobre autoconhecimento e sobre contexto (o que os outros dizem), e a terceira, sobre a função (o que sente sem a tela).</li></ul>
<p>Na prática: perguntar, deixar descrever o último episódio, nomear as etapas, e só então oferecer a informação que o paciente pediu com a própria descrição.</p>
"""),
    ],
    'checklist': [
        'Fiz as três perguntas do roteiro antes de dar qualquer informação.',
        'Pedi o último episódio e deixei o paciente montar o ciclo com o material dele.',
        'Reconheci na fala dele as crenças de persistência, previsão e plano, e anotei as frases.',
        'Não corrigi a crença sobre o acaso antes de o paciente querer olhar para ela.',
        'Ensinei reforço positivo e negativo e tolerância com exemplos do uso dele, e não em abstrato.',
        'Evitei a comparação direta com drogas e a imagem de cérebro sequestrado.',
        'Usei a neurobiologia para reduzir vergonha, e conferi se ela não aumentou a sensação de impotência.',
        'Saí da sessão com uma ligação nova entre o uso e algo que o paciente perde, dita por ele.',
    ],
    'questoes': [
        'Descreva a ficha da pré-contemplação: características, perguntas e intervenção.',
        'Por que a ordem "perguntas primeiro, informação depois" importa nesse estágio?',
        'Quais são as três famílias de crenças sobre o acaso do slide, e que propriedade do acaso cada uma nega?',
        'O que os slides afirmam sobre a neurobiologia da dependência tecnológica, e qual é a moderação?',
        'Como ensinar o ciclo da dependência a um paciente que não vê problema?',
        'Pense num paciente teu em pré-contemplação. Que informação neurobiológica tu daria, com que palavras, e o que tu deixaria de fora?',
    ],
    'gabarito': {
     0: (C, u"Características: não reconhece o comportamento como prejudicial; pode estar defensivo, desinteressado ou achar que todo mundo faz isso; resiste à ideia de mudança. Perguntas: se já pensou que o tempo de uso atrapalha alguma área da vida; se alguém já disse que usa demais e o que acha disso; o que sente quando está desconectado. Intervenção: informação sem julgamento, sobretudo sobre aspectos neuropsicológicos e impactos na saúde mental."),
     1: (C, u"Porque o paciente pré-contemplador não pediu a informação e tende a ouvi-la como o discurso da família com outra voz, o que ativa a defesa do uso. As perguntas abrem a percepção com o material dele; quando ele descreve o que perde ou o que sente sem a tela, a informação passa a responder a uma pergunta que ele mesmo fez."),
     2: (C, u"Persistência (\"se eu insistir a sorte vira\", \"minha habilidade tá melhorando\"): nega a independência do acaso. Previsão (\"se eu estudar os resultados acho um padrão\"): nega a imprevisibilidade. Plano (\"é só observar os padrões e apostar do jeito certo\", \"vou usar a data do meu pai que é sortudo\"): nega a incontrolabilidade. O alvo é o manejo das expectativas e a psicoeducação do acaso."),
     3: (C, u"Que o uso produz picos de dopamina semelhantes aos de substâncias, com reforço positivo e negativo e tolerância; que o adolescente tem controle pré-frontal imaturo; e que neuroimagem mostra ativação semelhante à de usuários de drogas, com hipofunção pré-frontal, hiperativação da amígdala e participação de hipocampo, cerebelo e ínsula. A moderação: reforço, tolerância e maturação pré-frontal se sustentam bem; a comparação com substâncias é imprecisa (magnitudes muito menores, estudos pequenos e transversais, semelhança de padrão e não equivalência) e, dita ao paciente, tira a agência que ele precisa para mudar."),
     4: (C, u"Não como diagrama pronto, e sim pedindo o último episódio: o que acontecia antes, o que passou pela cabeça, o que fez, o que sentiu na hora, o que veio depois, como ficou. O paciente monta o ciclo com o material dele e o terapeuta nomeia as etapas. O pré-contemplador descobre o problema descrevendo, o que não ativa a defesa que a informação pronta ativa."),
     5: (K, u"Não há resposta certa. Uma boa resposta escolhe a dose do reforço (recompensa rápida, alívio rápido, aprendizado rápido, por isso parar custa), diz isso com as palavras do uso daquele paciente e deixa de fora a comparação com drogas e a imagem de cérebro sequestrado. O erro comum é usar a neurobiologia para impressionar, o que costuma produzir ou descrédito (\"não é tão grave assim\") ou impotência (\"então não adianta\")."),
    },
    'referencias': [
        "Brand, M., Young, K. S., Laier, C., W&ouml;lfling, K., &amp; Potenza, M. N. (2016). Integrating psychological and neurobiological considerations regarding the development and maintenance of specific Internet-use disorders: An Interaction of Person-Affect-Cognition-Execution (I-PACE) model. <em>Neuroscience &amp; Biobehavioral Reviews, 71</em>, 252–266.",
        "Clark, L. (2010). Decision-making during gambling: An integration of cognitive and psychobiological approaches. <em>Philosophical Transactions of the Royal Society B, 365</em>(1538), 319–330.",
        "Ladouceur, R., Sylvain, C., Boutin, C., &amp; Doucet, C. (2002). <em>Understanding and treating the pathological gambler.</em> Wiley.",
        "Miller, W. R., &amp; Rollnick, S. (2023). <em>Entrevista motivacional: Ajudando pessoas a mudar e crescer</em> (4. ed.). Artmed.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o décimo vídeo de uma disciplina de pós-graduação; a fase de contemplação vem no vídeo 11.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. O quadro sobre como ensinar o ciclo, a leitura das três famílias de crenças pelas propriedades do acaso, a "dose certa" da psicoeducação e a seção final em processos foram desenvolvidos pelo autor do material a partir da lógica da disciplina.<br><br><strong>Uma moderação, sinalizada no texto.</strong> Os slides afirmam picos de dopamina "semelhantes aos observados em substâncias psicoativas" e ativação em neuroimagem "semelhante à de usuários de drogas". O material mantém o que se sustenta (reforço positivo e negativo, tolerância como fenômeno comportamental, maturação pré-frontal tardia) e modera a comparação com substâncias: magnitudes muito menores, estudos pequenos e transversais, concentrados em jogos pela internet, mostrando semelhança de padrão e não equivalência. O modelo I-PACE (Brand et al., 2016) está nas referências como a síntese mais citada dessa literatura. Os slides não citam fontes para as afirmações neurobiológicas.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'CRENCAS': CRENCAS}
DT10['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                  for sid, nav, tit, corpo in DT10['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT10['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT10, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT10)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT10['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
