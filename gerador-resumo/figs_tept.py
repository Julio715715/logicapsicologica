# -*- coding: utf-8 -*-
"""Figuras SVG da aula 'Tratando o TEPT complexo'."""
F = 'font-family="Plus Jakarta Sans,sans-serif"'

REDE = u"""<figure class='dg'><div class='dg-t'>A rede de memória traumática</div>
<svg viewBox='0 0 720 236' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Cinco elementos da memória traumática ligados entre si; um gatilho ativa um elemento e a rede inteira responde'>
<line x1='150' y1='70' x2='360' y2='118' stroke='#c9c2a8' stroke-width='2'/>
<line x1='150' y1='70' x2='570' y2='70' stroke='#c9c2a8' stroke-width='2'/>
<line x1='150' y1='70' x2='210' y2='190' stroke='#c9c2a8' stroke-width='2'/>
<line x1='570' y1='70' x2='360' y2='118' stroke='#c9c2a8' stroke-width='2'/>
<line x1='570' y1='70' x2='510' y2='190' stroke='#c9c2a8' stroke-width='2'/>
<line x1='210' y1='190' x2='360' y2='118' stroke='#c9c2a8' stroke-width='2'/>
<line x1='510' y1='190' x2='360' y2='118' stroke='#c9c2a8' stroke-width='2'/>
<line x1='210' y1='190' x2='510' y2='190' stroke='#c9c2a8' stroke-width='2'/>
<rect x='84' y='46' width='132' height='48' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='150' y='66' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>sensorial</text>
<text x='150' y='83' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>sufocamento, náusea</text>
<rect x='504' y='46' width='132' height='48' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='570' y='66' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>cognitivo</text>
<text x='570' y='83' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>“a culpa foi minha”</text>
<rect x='294' y='94' width='132' height='48' rx='10' fill='#43441f'/>
<text x='360' y='114' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#f0ede0'>emocional</text>
<text x='360' y='131' text-anchor='middle' %(F)s font-size='10.5' fill='#9ca575'>medo, vergonha, nojo</text>
<rect x='144' y='166' width='132' height='48' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='210' y='186' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>corporal</text>
<text x='210' y='203' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>tensão, paralisia</text>
<rect x='444' y='166' width='132' height='48' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='510' y='186' text-anchor='middle' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>comportamental</text>
<text x='510' y='203' text-anchor='middle' %(F)s font-size='10.5' fill='#6c6a55'>fugir, apagar, machucar-se</text>
<path d='M14 70 L78 70' stroke='#a05a3c' stroke-width='2.4' marker-end='url(#gt)'/>
<text x='14' y='56' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>gatilho</text>
<defs><marker id='gt' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#a05a3c'/></marker></defs>
<text x='660' y='140' %(F)s font-size='10.5' font-style='italic' fill='#8d876f'>sem começo,</text>
<text x='660' y='156' %(F)s font-size='10.5' font-style='italic' fill='#8d876f'>meio e fim</text>
</svg>
<figcaption>A memória não fica guardada como história, mas como elementos ligados entre si. Basta um gatilho tocar um deles para a rede inteira acender, e a pessoa revive no presente.</figcaption></figure>""" % dict(F=F)

FASES = u"""<figure class='dg'><div class='dg-t'>As quatro fases do DBT-PTSD</div>
<svg viewBox='0 0 720 150' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Quatro fases em sequência: preparação e habilidades, exposição, vida de valor, despedida'>
<rect x='0' y='16' width='168' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='84' y='42' text-anchor='middle' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a8894f'>1 · PREPARAÇÃO</text>
<text x='84' y='64' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>psicoeducação, acordos,</text>
<text x='84' y='80' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>mente sábia, plano de crise,</text>
<text x='84' y='96' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>valores e metas</text>
<path d='M172 62 L180 62' stroke='#8d876f' stroke-width='2'/>
<rect x='184' y='16' width='168' height='92' rx='10' fill='#43441f'/>
<text x='268' y='42' text-anchor='middle' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#9ca575'>2 · EXPOSIÇÃO</text>
<text x='268' y='64' text-anchor='middle' %(F)s font-size='11' fill='#f0ede0'>in vivo, à invalidação,</text>
<text x='268' y='80' text-anchor='middle' %(F)s font-size='11' fill='#f0ede0'>à mente sábia</text>
<text x='268' y='96' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#9ca575'>pela pior memória primeiro</text>
<path d='M356 62 L364 62' stroke='#8d876f' stroke-width='2'/>
<rect x='368' y='16' width='168' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='452' y='42' text-anchor='middle' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a8894f'>3 · VIDA DE VALOR</text>
<text x='452' y='64' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>corpo e sexualidade,</text>
<text x='452' y='80' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>metas, prevenção de</text>
<text x='452' y='96' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>nova violência</text>
<path d='M540 62 L548 62' stroke='#8d876f' stroke-width='2'/>
<rect x='552' y='16' width='168' height='92' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='636' y='42' text-anchor='middle' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a8894f'>4 · DESPEDIDA</text>
<text x='636' y='64' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>carta a si mesmo,</text>
<text x='636' y='80' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>sessões de reforço,</text>
<text x='636' y='96' text-anchor='middle' %(F)s font-size='11' fill='#2f2e24'>prevenção de recaída</text>
<text x='360' y='138' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#8d876f'>a passagem da fase 1 para a 2 é decidida com o time de consultoria, e o paciente apresenta o próprio modelo do trauma</text>
</svg>
<figcaption>Mente sábia e plano de crise entram antes da exposição, e não depois. É isso que torna o modelo mais compassivo do que a inundação sugere.</figcaption></figure>""" % dict(F=F)

TIPOS = u"""<figure class='dg'><div class='dg-t'>Três formatos de exposição, três alvos</div>
<svg viewBox='0 0 720 176' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Exposição in vivo, exposição à invalidação traumática e exposição à mente sábia, com o alvo de cada uma'>
<rect x='0' y='10' width='226' height='156' rx='11' fill='#fffdf7' stroke='#9ca575' stroke-width='1.3'/>
<text x='18' y='36' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a8894f'>IN VIVO</text>
<text x='18' y='60' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>alvo: a memória do evento</text>
<text x='18' y='84' %(F)s font-size='11' fill='#6c6a55'>narrar a pior memória, olhos</text>
<text x='18' y='100' %(F)s font-size='11' fill='#6c6a55'>fechados, sem esquiva nem</text>
<text x='18' y='116' %(F)s font-size='11' fill='#6c6a55'>dissociação; sessão gravada</text>
<text x='18' y='146' %(F)s font-size='10.5' font-style='italic' fill='#43441f'>aprendizagem inibitória</text>
<rect x='247' y='10' width='226' height='156' rx='11' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='265' y='36' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>À INVALIDAÇÃO</text>
<text x='265' y='60' %(F)s font-size='12' font-weight='800' fill='#2f2e24'>alvo: o que veio depois</text>
<text x='265' y='84' %(F)s font-size='11' fill='#6c6a55'>a tentativa de contar e não</text>
<text x='265' y='100' %(F)s font-size='11' fill='#6c6a55'>ser acreditado, ser punido,</text>
<text x='265' y='116' %(F)s font-size='11' fill='#6c6a55'>ou nunca ter contado</text>
<text x='265' y='146' %(F)s font-size='10.5' font-style='italic' fill='#a05a3c'>falha do ambiente, não da pessoa</text>
<rect x='494' y='10' width='226' height='156' rx='11' fill='#43441f'/>
<text x='512' y='36' %(F)s font-size='11' font-weight='800' letter-spacing='1.2' fill='#9ca575'>À MENTE SÁBIA</text>
<text x='512' y='60' %(F)s font-size='12' font-weight='800' fill='#f0ede0'>alvo: o autoconceito</text>
<text x='512' y='84' %(F)s font-size='11' fill='#ddd8c4'>o adulto, em mente sábia,</text>
<text x='512' y='100' %(F)s font-size='11' fill='#ddd8c4'>observa a cena na cadeira</text>
<text x='512' y='116' %(F)s font-size='11' fill='#ddd8c4'>vazia e reprocessa o sentido</text>
<text x='512' y='146' %(F)s font-size='10.5' font-style='italic' fill='#9ca575'>culpa, vergonha, autoaversão</text>
</svg>
<figcaption>A exposição in vivo cuida da memória. As outras duas cuidam do que o TEPT complexo acrescenta ao TEPT clássico: a invalidação e o self construído em volta do trauma.</figcaption></figure>""" % dict(F=F)
