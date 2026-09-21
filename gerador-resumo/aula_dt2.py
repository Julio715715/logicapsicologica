# -*- coding: utf-8 -*-
"""Trilha Dependências tecnológicas, vídeo 2: Desenvolvimento de produtos baseados
em princípios evolutivos e neuronais. Fonte: slides da aula (sem transcrição)."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from pe_cap5 import pagina_jornada

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

GANCHOS = u"""<figure class='dg'><div class='dg-t'>Seis mecanismos antigos, seis ganchos de design</div>
<svg viewBox='0 0 720 318' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Seis pares: mecanismo evolutivo e o recurso de design que o explora'>
<rect x='0' y='8' width='226' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='16' y='30' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>1 · RECOMPENSA IMEDIATA</text>
<text x='16' y='52' %(F)s font-size='11' fill='#2f2e24'>alimento e informação eram raros</text>
<text x='16' y='76' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>likes, notificações, reforço variável</text>
<rect x='247' y='8' width='226' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='263' y='30' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>2 · ATENÇÃO AO SOCIAL</text>
<text x='263' y='52' %(F)s font-size='11' fill='#2f2e24'>rosto, status e coesão do grupo</text>
<text x='263' y='76' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>feed, reações, comparação constante</text>
<rect x='494' y='8' width='226' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='510' y='30' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>3 · NOVIDADE</text>
<text x='510' y='52' %(F)s font-size='11' fill='#2f2e24'>curiosidade achava recurso e abrigo</text>
<text x='510' y='76' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>rolagem infinita, aleatoriedade</text>
<rect x='0' y='116' width='226' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='16' y='138' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>4 · AUTOMATISMO</text>
<text x='16' y='160' %(F)s font-size='11' fill='#2f2e24'>automatizar poupava energia</text>
<text x='16' y='184' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>uso rápido, repetido, sem reflexão</text>
<rect x='247' y='116' width='226' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='263' y='138' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>5 · HIERARQUIA</text>
<text x='263' y='160' %(F)s font-size='11' fill='#2f2e24'>posição no grupo dava recurso</text>
<text x='263' y='184' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>rankings, medalhas, seguidores</text>
<rect x='494' y='116' width='226' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='510' y='138' %(F)s font-size='10.5' font-weight='800' letter-spacing='1.2' fill='#a8894f'>6 · ESTÍMULO PREPARADO</text>
<text x='510' y='160' %(F)s font-size='11' fill='#2f2e24'>rosto, olho, movimento, cor viva</text>
<text x='510' y='184' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>ícones com face, cores, animação</text>
<rect x='120' y='232' width='480' height='70' rx='11' fill='#43441f'/>
<text x='360' y='260' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#f0ede0'>o que o design faz: pega um mecanismo que já existe</text>
<text x='360' y='282' text-anchor='middle' %(F)s font-size='11' fill='#9ca575'>e entrega o estímulo em dose, frequência e forma que o ambiente ancestral nunca entregou</text>
</svg>
<figcaption>Nenhum dos seis foi inventado pelo produto. O produto só sabe onde apertar. Na clínica, a pergunta é qual deles sustenta o uso deste paciente.</figcaption></figure>""" % dict(F=F)

ALCA = u"""<figure class='dg'><div class='dg-t'>A alça que os seis ganchos alimentam</div>
<svg viewBox='0 0 720 150' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Alça: pista, ação, recompensa variável, retorno à pista'>
<defs><marker id='al' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='30' width='200' height='70' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='100' y='58' text-anchor='middle' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>pista</text>
<text x='100' y='80' text-anchor='middle' %(F)s font-size='11' fill='#6c6a55'>notificação, tédio, rosto no ícone</text>
<path d='M204 65 L252 65' stroke='#8d876f' stroke-width='2' marker-end='url(#al)'/>
<rect x='260' y='30' width='200' height='70' rx='10' fill='#fffdf7' stroke='#43441f' stroke-width='1.5'/>
<text x='360' y='58' text-anchor='middle' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>ação barata</text>
<text x='360' y='80' text-anchor='middle' %(F)s font-size='11' fill='#6c6a55'>desbloquear, rolar, tocar</text>
<path d='M464 65 L512 65' stroke='#8d876f' stroke-width='2' marker-end='url(#al)'/>
<rect x='520' y='30' width='200' height='70' rx='10' fill='#43441f'/>
<text x='620' y='58' text-anchor='middle' %(F)s font-size='12.5' font-weight='800' fill='#f0ede0'>recompensa variável</text>
<text x='620' y='80' text-anchor='middle' %(F)s font-size='11' fill='#9ca575'>às vezes vem, às vezes não</text>
<path d='M620 104 L620 128 L100 128 L100 106' fill='none' stroke='#a05a3c' stroke-width='2' marker-end='url(#al)'/>
<text x='360' y='142' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#a05a3c'>a incerteza da recompensa é o que fortalece a alça, como na máquina caça-níqueis</text>
</svg>
<figcaption>Reforço em esquema variável: o comportamento que às vezes é recompensado resiste mais à extinção do que o que é sempre recompensado. É o esquema do jogo de azar, e é o do feed.</figcaption></figure>""" % dict(F=F)

DT2 = {
    'slug': 'aula2',
    'titulo_txt': 'Como os produtos exploram o que a evolução deixou: seis ganchos do design digital',
    'titulo_html': 'Como os produtos exploram o que a evolu&ccedil;&atilde;o deixou: seis ganchos do design digital',
    'data': 'Vídeo 2',
    'meta': 'Prof. Júlio Gonçalves · Disciplina Avaliação e tratamento das dependências tecnológicas · Vídeo 2',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; AVALIA&Ccedil;&Atilde;O E TRATAMENTO DAS DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS<br>V&Iacute;DEO 2 &middot; JORNADA DA LEITURA',
    'header_dir': 'DEPEND&Ecirc;NCIAS TECNOL&Oacute;GICAS &middot; V&Iacute;DEO 2',
    'chave': 'mat-Aula-DT2-',
    'arquivo': 'Aula-DT2-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir dos slides do segundo vídeo da "
              u"disciplina, que apresenta seis mecanismos evolutivos e o recurso de design que explora cada um. Não havia "
              u"transcrição; onde o slide era telegráfico, o texto desenvolve o raciocínio e diz que está desenvolvendo.</p>"
              u"<p>Como o vídeo 1, este conteúdo serve também como <strong>psicoeducação</strong>: é o mapa da arquitetura em que o "
              u"paciente vive. Duas moderações empíricas estão sinalizadas no corpo do texto.</p></div>"),
    'tema': 'O design digital não inventa desejo: ele encontra mecanismos que a seleção natural deixou prontos e entrega o estímulo '
            'em dose e frequência que o ambiente ancestral nunca entregou. Seis desses mecanismos, e o que fazer com eles na formulação.',
    'essencial': [
        ('O produto não cria o mecanismo; ele sabe onde apertar.',
         'Recompensa, atenção ao social, novidade, automatismo, hierarquia e estímulo preparado já existiam. O design só mudou a dose.'),
        ('Reforço variável é o motor.',
         'Likes e notificações que às vezes vêm e às vezes não seguem o esquema da máquina caça-níqueis, o mais resistente à extinção.'),
        ('A rolagem infinita vende novidade, e o cérebro compra.',
         'A curiosidade que achava recurso e abrigo hoje acha mais um vídeo. Sempre há algo novo, por desenho.'),
        ('O hábito é o objetivo do produto.',
         'Uso rápido, repetido e sem reflexão. Desbloquear o celular sem perceber é sucesso de design, e é o que a clínica precisa desmontar.'),
        ('Na formulação, a pergunta é qual gancho sustenta este uso.',
         'Comparação social, tédio, status, novidade. O mesmo aplicativo prende pacientes diferentes por mecanismos diferentes.'),
    ],
    'secoes': [
        ('s0', 'O que o UX design faz com a evolução', 'O que o UX design faz com a evolução', u"""
<p>O vídeo 1 terminou com uma promessa: mostrar como a armadilha é montada. Este vídeo cumpre. A tese é simples e vale guardar inteira: o <strong>design de experiência do usuário</strong> (UX) explora mecanismos evolutivos. Nenhum dos mecanismos foi inventado por uma empresa; todos foram selecionados ao longo de milhares de anos porque resolviam problemas de sobrevivência e de reprodução. O que o produto faz é identificar o mecanismo e entregar o estímulo que o dispara em dose, frequência e forma que o ambiente ancestral nunca entregou.</p>
{{GANCHOS}}
<p>Os slides organizam seis desses pares, sempre no mesmo formato: o contexto evolutivo de um lado, o recurso de design do outro. O texto segue a mesma ordem.</p>
"""),
        ('s1', '1. Sensibilidade à recompensa imediata', '1. Sensibilidade à recompensa imediata', u"""
<p><strong>Contexto evolutivo.</strong> No ambiente ancestral, encontrar alimento ou informação nova era vital e raro. O cérebro passou a valorizar essas experiências com liberação de dopamina, marcando o evento como algo a repetir.</p>
<p><strong>No design digital.</strong> Likes, notificações, mensagens novas e conquistas em jogos ativam o mesmo sistema. E são <strong>reforçadores intermitentes</strong>: o modelo é o do reforço variável, o mesmo do jogo de azar. Não é a recompensa que prende; é a incerteza de quando ela vem.</p>
{{ALCA}}
<div class='obs'><h4>Uma moderação</h4><p>Vale repetir a distinção do vídeo 1. A dopamina responde mais ao <em>querer</em> e à antecipação do que ao prazer consumado. É por isso que a recompensa variável funciona tão bem: o sistema dispara na expectativa, e a expectativa nunca se resolve. Dizer ao paciente que ele "busca dopamina" está certo; dizer que ele busca prazer explica mal o uso que segue sem prazer nenhum.</p></div>
"""),
        ('s2', '2. Atenção seletiva a estímulos sociais', '2. Atenção seletiva a estímulos sociais', u"""
<p><strong>Contexto evolutivo.</strong> Estar atento a expressões faciais, a status e a relações interpessoais aumentava a coesão do grupo, e a coesão do grupo era sobrevivência. Quem lia mal o rosto do outro ficava de fora.</p>
<p><strong>No design digital.</strong> As redes sociais amplificam essas pistas com fotos, reações, seguidores e algoritmos que priorizam conteúdo de alta interação. O resultado é <strong>comparação social constante</strong>, que o slide liga a compulsão, ansiedade e baixa autoestima.</p>
<div class='obs'><h4>Uma moderação</h4><p>O mecanismo é bem descrito, mas a ligação entre uso de redes e sofrimento é menos forte na literatura do que a intuição sugere: em amostras grandes, a associação entre tempo de tela e bem-estar é pequena, e a direção causal é disputada. O que se sustenta melhor é o efeito da <em>comparação</em> e do uso passivo, e não do tempo em si. Na clínica isso muda a pergunta: em vez de quanto o paciente usa, o que ele faz e com quem se compara enquanto usa.</p></div>
"""),
        ('s3', '3. Busca por novidade e exploração', '3. Busca por novidade e exploração', u"""
<p><strong>Contexto evolutivo.</strong> Curiosidade e exploração ajudavam a encontrar recursos, abrigo e aliados. O organismo que parava de explorar cedo perdia para o que seguia olhando.</p>
<p><strong>No design digital.</strong> A rolagem infinita, as recomendações automáticas e a <strong>aleatoriedade</strong> dos feeds exploram exatamente essa tendência: sempre há algo novo para descobrir, e o fim nunca chega. Repare que a aleatoriedade aqui é o mesmo ingrediente do mecanismo 1: novidade imprevisível é recompensa variável com outro nome.</p>
<div class='callout note'><div class='co-t'>Para a sessão</div>O paciente que "só ia dar uma olhada" e ficou uma hora não falhou em força de vontade. Ele entrou num ambiente desenhado para não ter ponto de parada. Nomear isso reduz a culpa e abre a intervenção óbvia: criar o ponto de parada que o produto tirou.</div>
"""),
        ('s4', '4. Economia cognitiva e automatismo', '4. Economia cognitiva e automatismo', u"""
<p><strong>Contexto evolutivo.</strong> Automatizar comportamentos poupava energia para lidar com ameaças e com decisões complexas. Hábito é o cérebro economizando para o que importa.</p>
<p><strong>No design digital.</strong> Os aplicativos são otimizados para uso rápido e repetitivo, criando hábitos e rotinas automáticas sem reflexão crítica. O exemplo do slide é preciso: <strong>desbloquear o celular sem perceber</strong>. Do ponto de vista do produto, isso é o objetivo alcançado; do ponto de vista clínico, é o comportamento que precisa voltar a passar pela consciência antes de qualquer outra coisa.</p>
<p>Hábito, na definição da psicologia, é comportamento disparado por pista de contexto, com pouca dependência de intenção. Por isso a intervenção que começa por motivação costuma falhar: o gesto acontece antes da motivação entrar em cena. O que funciona é mexer na pista e no atrito.</p>
"""),
        ('s5', '5. Competição e hierarquia', '5. Competição e hierarquia', u"""
<p><strong>Contexto evolutivo.</strong> Estar em boa posição no grupo garantia acesso a recursos e a parceiros. Status era moeda antes de existir moeda.</p>
<p><strong>No design digital.</strong> Rankings, curtidas, conquistas e medalhas simulam status e prestígio, reforçando o engajamento. O jogo entrega hierarquia visível a cada partida; a rede entrega seguidores como placar. É a mesma busca por "algo valioso" do vídeo 1, com o status como o valioso da vez.</p>
"""),
        ('s6', '6. Estímulos visuais preparados', '6. Estímulos visuais preparados', u"""
<p><strong>Contexto evolutivo.</strong> A espécie desenvolveu sensibilidade a estímulos visuais biologicamente relevantes: rostos, olhos, movimento súbito, cores vivas. Esses elementos indicavam perigo ou oportunidade social, e a atenção a eles vinha pronta, sem aprendizagem.</p>
<p><strong>No design digital.</strong> Interfaces usam cores chamativas, ícones com olhos ou faces e elementos em movimento para capturar atenção, explorando essa predisposição. Ícones de notificação e emojis são o exemplo do slide: um rosto minúsculo no canto da tela ainda é um rosto para o sistema que o detecta.</p>
<p>Esse é o mecanismo mais difícil de contornar por decisão, porque opera antes da decisão. Daí as intervenções de ambiente que funcionam melhor do que as de intenção: tela em escala de cinza, ícones sem selo, notificações visuais desligadas.</p>
"""),
        ('s7', 'O que fazer com isso na formulação', 'O que fazer com isso na formulação', u"""
<p>Os seis mecanismos servem a duas coisas na clínica.</p>
<p>A primeira é <strong>psicoeducação</strong>, no sentido exato do vídeo 1: mostrar ao paciente que o uso dele apoia-se em mecanismos que todo mundo tem, e que o produto foi construído para apertá-los. Isso desloca a culpa do caráter para o contexto sem tirar a responsabilidade pela mudança.</p>
<p>A segunda é <strong>formulação</strong>. O mesmo aplicativo prende pacientes diferentes por mecanismos diferentes: um está preso pela comparação social, outro pela novidade que preenche o tédio, outro pelo status do ranking, outro por hábito puro que já não entrega nada. A pergunta de avaliação é qual gancho sustenta o uso deste paciente, porque a intervenção muda conforme a resposta. Para o gancho 4, atrito e pista; para o 2, o que ele faz enquanto usa e com quem se compara; para o 1 e o 3, ponto de parada e substituição da recompensa variável por recompensa previsível.</p>
<div class='callout note'><div class='co-t'>Leitura em processos</div>Na rede do caso, o uso de tela raramente é o nó central. Ele costuma ser a saída barata de um processo que está antes: evitação de tédio, de solidão, de tarefa aversiva, de comparação que dói. Os seis ganchos explicam por que a saída é tão barata; a formulação precisa achar de que o paciente está saindo.</div>
<h3>O que vem no próximo vídeo</h3>
<p>Um alinhamento conceitual do que é, afinal, dependência tecnológica: onde termina o uso intenso e começa o transtorno.</p>
"""),
    ],
    'checklist': [
        'Identifiquei qual dos seis ganchos sustenta o uso deste paciente, em vez de tratar "tela" como um alvo único.',
        'Perguntei o que ele faz enquanto usa, e não só quanto usa.',
        'Distingui querer de gostar ao ouvir o relato: o uso ainda entrega prazer ou só antecipação?',
        'Mapeei as pistas de contexto que disparam o gesto automático.',
        'Propus intervenções de ambiente (atrito, ponto de parada, notificações) antes de contar com motivação.',
        'Usei os mecanismos para reduzir culpa sem retirar a responsabilidade pela mudança.',
        'Procurei, na rede do caso, de que o paciente está saindo quando entra na tela.',
    ],
    'questoes': [
        'Explique por que o reforço variável é o motor de likes, notificações e feeds, e o que ele tem em comum com o jogo de azar.',
        'Quais dos seis mecanismos operam antes da decisão consciente, e por que isso muda o tipo de intervenção?',
        'Por que o slide liga a atenção seletiva ao social a ansiedade e baixa autoestima, e que ressalva a literatura pede?',
        'Descreva um paciente teu com uso problemático de tela. Qual gancho sustenta o uso dele, e como tu chegou a essa resposta?',
        'Como tu explicaria a um paciente a ideia de que o produto não inventa o desejo, sem que ele saia da sessão se sentindo vítima?',
        'Que intervenção de ambiente tu proporia para o gancho do automatismo, e como testaria se funcionou?',
    ],
    'gabarito': {
     0: (C, u"No esquema de reforço variável, a recompensa vem em intervalos ou proporções imprevisíveis. O comportamento reforçado assim é o mais resistente à extinção: a pessoa continua porque a próxima pode ser a que vem. Likes, notificações e a rolagem entregam recompensa exatamente desse jeito, às vezes sim, às vezes não. É o esquema da máquina caça-níqueis, e o sistema dopaminérgico dispara na antecipação, não no prêmio."),
     1: (C, u"O <b>automatismo</b> (o gesto disparado pela pista, antes da intenção) e os <b>estímulos preparados</b> (rosto, olho, cor, movimento, que capturam atenção sem aprendizagem). Como operam antes da decisão, intervenções que dependem de decidir melhor chegam atrasadas. O que funciona é mexer no ambiente: atrito, pista, cor da tela, notificações, ponto de parada."),
     2: (C, u"Porque redes sociais amplificam pistas de status e induzem comparação social constante, e a comparação para baixo custa autoestima. A ressalva: em amostras grandes, a associação entre tempo de uso e bem-estar é pequena e de direção disputada; o que se sustenta melhor é o efeito da comparação e do uso passivo. A pergunta clínica útil é o que a pessoa faz e com quem se compara enquanto usa."),
     3: (K, u"Não há resposta certa. Uma boa resposta nomeia um gancho principal (ou dois) e diz como chegou lá: pelo que o paciente relata sentir logo antes de pegar o celular, pelo que faz quando está dentro, pelo que acontece quando a recompensa não vem. O erro comum é responder pelo aplicativo (\"é o Instagram\") em vez de pelo mecanismo, ou listar os seis sem escolher."),
     4: (K, u"Não há resposta certa. Uma boa resposta explica que o mecanismo é de todo mundo e que o produto foi desenhado para apertá-lo, e no mesmo movimento mostra que conhecer o mecanismo é o que permite escolher o ambiente e as regras. A responsabilidade sai do caráter e vai para o manejo do contexto. O erro comum é parar na primeira metade e deixar o paciente com a conclusão de que não há o que fazer."),
     5: (K, u"Não há resposta certa. Uma boa resposta propõe algo que muda a pista ou o atrito (celular fora do quarto, ícone fora da tela inicial, senha longa, tela em cinza) e define o teste antes: um registro simples de quantas vezes o gesto aconteceu por dia, comparando a semana anterior com a seguinte. O erro comum é propor a intervenção sem medida, e concluir pelo relato geral."),
    },
    'referencias': [
        "Alter, A. (2017). <em>Irresistible: The rise of addictive technology and the business of keeping us hooked.</em> Penguin Press.",
        "Berridge, K. C., &amp; Robinson, T. E. (2016). Liking, wanting, and the incentive-sensitization theory of addiction. <em>American Psychologist, 71</em>(8), 670–679.",
        "Eyal, N. (2014). <em>Hooked: How to build habit-forming products.</em> Portfolio.",
        "Ferster, C. B., &amp; Skinner, B. F. (1957). <em>Schedules of reinforcement.</em> Appleton-Century-Crofts.",
        "Li, N. P., van Vugt, M., &amp; Colarelli, S. M. (2018). The evolutionary mismatch hypothesis: Implications for psychological science. <em>Current Directions in Psychological Science, 27</em>(1), 38–44.",
        "Montag, C., Lachmann, B., Herrlich, M., &amp; Zweig, K. (2019). Addictive features of social media/messenger platforms and freemium games against the background of psychological and economic theories. <em>International Journal of Environmental Research and Public Health, 16</em>(14), 2612.",
        "Orben, A., &amp; Przybylski, A. K. (2019). The association between adolescent well-being and digital technology use. <em>Nature Human Behaviour, 3</em>(2), 173–182.",
        "Seligman, M. E. P. (1971). Phobias and preparedness. <em>Behavior Therapy, 2</em>(3), 307–320.",
        "Wood, W., &amp; Rünger, D. (2016). Psychology of habit. <em>Annual Review of Psychology, 67</em>, 289–314.",
    ],
    'nota': u"""Material dirigido a psicólogos. É o segundo vídeo de uma disciplina de pós-graduação e trata de fundamentos; avaliação e intervenção vêm nos vídeos seguintes.<br><br><strong>Fonte.</strong> Este resumo foi escrito a partir dos <b>slides</b> do vídeo, sem transcrição da fala. Os seis pares (contexto evolutivo e recurso de design) reproduzem o conteúdo dos slides em paráfrase; os trechos que ligam os mecanismos entre si, a definição de hábito e a seção final sobre formulação foram desenvolvidos pelo autor do material a partir da lógica da aula, e o texto assume isso onde ocorre.<br><br><strong>Duas moderações empíricas, sinalizadas no texto.</strong> Primeira: a "liberação de dopamina" dos slides foi lida pela distinção entre querer e gostar (Berridge e Robinson), porque é ela que explica o poder do reforço variável e o uso sem prazer. Segunda: a ligação entre redes sociais e ansiedade ou baixa autoestima foi mantida como mecanismo plausível, com a ressalva de que a associação entre tempo de uso e bem-estar é pequena nas amostras grandes (Orben e Przybylski) e de que o efeito mais bem sustentado é o da comparação e do uso passivo.<br><br><strong>Acréscimos.</strong> As referências foram acrescentadas para dar respaldo formal ao que os slides afirmam sem citação: os esquemas de reforço, o modelo do gancho de produto, o descompasso evolutivo, a psicologia do hábito, a preparação biológica para certos estímulos e a análise dos recursos aditivos das plataformas. Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'GANCHOS': GANCHOS, 'ALCA': ALCA}
DT2['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DT2['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/psicoterapeutas-eficazes/cap4/index.html', encoding='utf-8').read()
    dest = SITE + '/dependencias-tecnologicas/' + DT2['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_jornada(DT2, base).replace('/psicoterapeutas-eficazes/', '/dependencias-tecnologicas/'))
    c = sup_common.pdf(DT2)
    c['kicker'] = 'RESUMO DE AULA &middot; JORNADA DA LEITURA'
    c['gabarito'] = DT2['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
