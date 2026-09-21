# -*- coding: utf-8 -*-
"""Figuras SVG da aula sobre bases evolutivas do comportamento lúdico."""
F = 'font-family="Plus Jakarta Sans,sans-serif"'

BENEFICIOS = u"""<figure class='dg'><div class='dg-t'>O que o brincar treina</div>
<svg viewBox='0 0 720 214' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Seis ganhos do comportamento lúdico na infância: motor, emocional, regras, cultura, funções executivas e habilidades sociais'>
<rect x='0' y='10' width='226' height='88' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='18' y='36' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>Refinamento motor</text>
<text x='18' y='58' %(F)s font-size='11' fill='#6c6a55'>engatinhar até o brinquedo,</text>
<text x='18' y='74' %(F)s font-size='11' fill='#6c6a55'>apoiar-se, alcançar, equilibrar</text>
<rect x='247' y='10' width='226' height='88' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='265' y='36' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>Expressão emocional</text>
<text x='265' y='58' %(F)s font-size='11' fill='#6c6a55'>os primeiros movimentos de</text>
<text x='265' y='74' %(F)s font-size='11' fill='#6c6a55'>mostrar o que sente ao ambiente</text>
<rect x='494' y='10' width='226' height='88' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='512' y='36' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>Regras e moral</text>
<text x='512' y='58' %(F)s font-size='11' fill='#6c6a55'>o que pode, o que não pode,</text>
<text x='512' y='74' %(F)s font-size='11' fill='#6c6a55'>o que põe a vida em risco</text>
<rect x='0' y='116' width='226' height='88' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='18' y='142' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>Apropriação cultural</text>
<text x='18' y='164' %(F)s font-size='11' fill='#6c6a55'>o que importa nessa família,</text>
<text x='18' y='180' %(F)s font-size='11' fill='#6c6a55'>como se veste, como se porta</text>
<rect x='247' y='116' width='226' height='88' rx='10' fill='#fffdf7' stroke='#43441f' stroke-width='1.5'/>
<text x='265' y='142' %(F)s font-size='12.5' font-weight='800' fill='#2f2e24'>Funções executivas</text>
<text x='265' y='164' %(F)s font-size='11' fill='#6c6a55'>atenção, memória, planejamento,</text>
<text x='265' y='180' %(F)s font-size='11' fill='#6c6a55'>controle inibitório, flexibilidade</text>
<rect x='494' y='116' width='226' height='88' rx='10' fill='#43441f'/>
<text x='512' y='142' %(F)s font-size='12.5' font-weight='800' fill='#f0ede0'>Habilidades sociais</text>
<text x='512' y='164' %(F)s font-size='11' fill='#ddd8c4'>empatia, altruísmo, teoria da</text>
<text x='512' y='180' %(F)s font-size='11' fill='#ddd8c4'>mente: o que o outro está pensando</text>
</svg>
<figcaption>A infância como arena de simulação da vida adulta. As duas últimas caixas são as que mais interessam ao clínico: são elas que a tela substitui mal.</figcaption></figure>""" % dict(F=F)

VALIOSO = u"""<figure class='dg'><div class='dg-t'>A mesma busca, dois ambientes</div>
<svg viewBox='0 0 720 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='O algoritmo de buscar algo valioso não mudou; o ambiente passou a entregar coisas valiosas o tempo todo'>
<rect x='236' y='16' width='248' height='60' rx='12' fill='#43441f'/>
<text x='360' y='40' text-anchor='middle' %(F)s font-size='13' font-weight='800' fill='#f0ede0'>buscar algo valioso</text>
<text x='360' y='60' text-anchor='middle' %(F)s font-size='11' fill='#9ca575'>prazer, status, vínculo, recurso</text>
<defs><marker id='va' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<path d='M300 80 L170 112' stroke='#8d876f' stroke-width='2' marker-end='url(#va)'/>
<path d='M420 80 L550 112' stroke='#8d876f' stroke-width='2' marker-end='url(#va)'/>
<rect x='0' y='118' width='330' height='74' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='18' y='142' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a8894f'>ANTES</text>
<text x='18' y='162' %(F)s font-size='11.5' fill='#2f2e24'>pedras, gravetos, árvores, corrida, lutinha,</text>
<text x='18' y='180' %(F)s font-size='11.5' fill='#2f2e24'>quem pega a fruta primeiro. Recompensa escassa.</text>
<rect x='390' y='118' width='330' height='74' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.5'/>
<text x='408' y='142' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>AGORA</text>
<text x='408' y='162' %(F)s font-size='11.5' fill='#2f2e24'>cartas, cassinos, games, rolagem infinita,</text>
<text x='408' y='180' %(F)s font-size='11.5' fill='#2f2e24'>moeda dentro do jogo. Recompensa o tempo todo.</text>
</svg>
<figcaption>O que mudou foi a oferta, e não o algoritmo. É essa diferença que a próxima aula explora: como os produtos são desenhados em cima dele.</figcaption></figure>""" % dict(F=F)
