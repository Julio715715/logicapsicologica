# -*- coding: utf-8 -*-
"""Aula livre: Aceitação em DBT (Descomplicando a DBT, 12/09/2026). Fonte: transcrição + anotações do Gemini."""
import io, re, sys
sys.path.insert(0, '/home/claude')
import sup_common, gen_resumo
from aula_tept import pagina_aula

C = 'comentario'
K = 'criterios'
F = 'font-family="Plus Jakarta Sans,sans-serif"'

ACEIT = u"""<figure class='dg'><div class='dg-t'>Aceitação não é resignação</div>
<svg viewBox='0 0 720 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Duas caixas: resignação fecha a porta para a mudança; aceitação aceita o que aconteceu e abre para o que ainda dá para mudar, e anda junto com validação e mudança'>
<defs><marker id='ac' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<rect x='0' y='10' width='300' height='120' rx='11' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='16' y='36' %(F)s font-size='11.5' font-weight='800' fill='#a05a3c'>RESIGNA&Ccedil;&Atilde;O</text>
<text x='16' y='60' %(F)s font-size='10.5' fill='#2f2e24'>"eu desisto; não vou mudar, as pessoas</text>
<text x='16' y='76' %(F)s font-size='10.5' fill='#2f2e24'>não vão mudar, aceito o mundo e deu"</text>
<text x='16' y='104' %(F)s font-size='10.5' font-style='italic' fill='#6c6a55'>porta fechada para a mudança</text>
<rect x='420' y='10' width='300' height='120' rx='11' fill='#f1ece0' stroke='#9ca575' stroke-width='1.4'/>
<text x='436' y='36' %(F)s font-size='11.5' font-weight='800' fill='#43441f'>ACEITA&Ccedil;&Atilde;O</text>
<text x='436' y='60' %(F)s font-size='10.5' fill='#2f2e24'>aceita o que aconteceu e o que está</text>
<text x='436' y='76' %(F)s font-size='10.5' fill='#2f2e24'>acontecendo; pergunta o que, dentro do</text>
<text x='436' y='92' %(F)s font-size='10.5' fill='#2f2e24'>contexto e das habilidades, ainda dá para mudar</text>
<text x='436' y='118' %(F)s font-size='10.5' font-style='italic' fill='#43441f'>porta aberta, sempre</text>
<text x='360' y='60' text-anchor='middle' %(F)s font-size='10' fill='#8d876f'>a fronteira é sutil:</text>
<text x='360' y='76' text-anchor='middle' %(F)s font-size='10' fill='#8d876f'>um "mas" no lugar de um "e"</text>
<rect x='150' y='150' width='420' height='40' rx='9' fill='#43441f'/>
<text x='360' y='175' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#f0ede0'>aceitação + validação + um passo de mudança, na mesma sessão</text>
</svg>
<figcaption>Nunca só aceitação e nunca só validação: sem um pequeno passo de mudança em cada sessão, o paciente escorrega para a resignação, e o terapeuta também.</figcaption></figure>""" % dict(F=F)

PERG = u"""<figure class='dg'><div class='dg-t'>A paciente faltou duas sessões e diz: "quase não vim de novo"</div>
<svg viewBox='0 0 720 250' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Duas colunas: afirmações que julgam e fecham, e perguntas que descrevem e abrem, com o efeito de cada uma'>
<rect x='0' y='8' width='350' height='196' rx='11' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='14' y='32' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>AFIRMA&Ccedil;&Atilde;O (JULGA)</text>
<text x='14' y='58' %(F)s font-size='10.5' font-style='italic' fill='#2f2e24'>"mas tu concordou com o plano, né?"</text>
<text x='14' y='78' %(F)s font-size='10.5' font-style='italic' fill='#2f2e24'>"isso é autossabotagem"</text>
<text x='14' y='98' %(F)s font-size='10.5' font-style='italic' fill='#2f2e24'>"se tu quer mesmo melhorar..."</text>
<text x='14' y='118' %(F)s font-size='10.5' font-style='italic' fill='#2f2e24'>"a gente já conversou que tem que fazer o plano"</text>
<text x='14' y='150' %(F)s font-size='10' fill='#6c6a55'>pressupõe má vontade; ignora a contingência</text>
<text x='14' y='166' %(F)s font-size='10' fill='#6c6a55'>(semana pesada, terapia que doeu, ritmo do</text>
<text x='14' y='182' %(F)s font-size='10' fill='#6c6a55'>terapeuta); a atenção vai para a ameaça</text>
<rect x='370' y='8' width='350' height='196' rx='11' fill='#f1ece0' stroke='#9ca575' stroke-width='1.4'/>
<text x='384' y='32' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#43441f'>PERGUNTA (DESCREVE E ABRE)</text>
<text x='384' y='58' %(F)s font-size='10.5' font-style='italic' fill='#2f2e24'>"tu quase não veio, e veio. como foi decidir vir?"</text>
<text x='384' y='78' %(F)s font-size='10.5' font-style='italic' fill='#2f2e24'>"o que teve no meio? o que tu pensou?"</text>
<text x='384' y='98' %(F)s font-size='10.5' font-style='italic' fill='#2f2e24'>"ficou pesado demais entre uma sessão e outra?"</text>
<text x='384' y='118' %(F)s font-size='10.5' font-style='italic' fill='#2f2e24'>"onde doeu? eu tô aqui pra isso"</text>
<text x='384' y='150' %(F)s font-size='10' fill='#6c6a55'>constata, não julga; descobre a motivação de</text>
<text x='384' y='166' %(F)s font-size='10' fill='#6c6a55'>ter vindo (e reforça: ação oposta); dá ao</text>
<text x='384' y='182' %(F)s font-size='10' fill='#6c6a55'>paciente a autonomia que ele não tem lá fora</text>
<text x='360' y='236' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#2f2e24'>curiosidade vem com pergunta, nunca com afirmação</text>
</svg>
<figcaption>Afirmação só para descrever o que o paciente falou ("entendi certo?"). O resto vira pergunta. É a mudança mais barata da aula e a que mais abre a sessão.</figcaption></figure>""" % dict(F=F)

MODOS = u"""<figure class='dg'><div class='dg-t'>Oito modos de invalidar sem perceber</div>
<svg viewBox='0 0 720 232' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Oito caixas com os modos de invalidação: argumentação, moralização, desaprovação, estigmatização, advertência, ironia, análise inoportuna e o mas'>
<g %(F)s font-size='10' fill='#2f2e24'>
<rect x='0' y='6' width='172' height='100' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/><text x='10' y='26' font-weight='800'>Argumentação</text><text x='10' y='46' fill='#6c6a55'>nunca tem pergunta no fim:</text><text x='10' y='60' fill='#6c6a55'>"não é bem assim, é assim"</text>
<rect x='182' y='6' width='172' height='100' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/><text x='192' y='26' font-weight='800'>Moralização</text><text x='192' y='46' fill='#6c6a55'>o que eu acho certo, que</text><text x='192' y='60' fill='#6c6a55'>naquela vida não faz sentido</text>
<rect x='364' y='6' width='172' height='100' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/><text x='374' y='26' font-weight='800'>Desaprovação</text><text x='374' y='46' fill='#6c6a55'>"não devia ter faltado";</text><text x='374' y='60' fill='#6c6a55'>"que bom que veio, porque</text><text x='374' y='74' fill='#6c6a55'>não é bom faltar"</text>
<rect x='546' y='6' width='174' height='100' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/><text x='556' y='26' font-weight='800'>Estigmatização</text><text x='556' y='46' fill='#6c6a55'>"borderline tem esse</text><text x='556' y='60' fill='#6c6a55'>padrão mesmo"; o rótulo</text><text x='556' y='74' fill='#6c6a55'>no lugar do contexto</text>
<rect x='0' y='120' width='172' height='100' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/><text x='10' y='140' font-weight='800'>Advertência</text><text x='10' y='160' fill='#6c6a55'>"já vou te adiantar que</text><text x='10' y='174' fill='#6c6a55'>ele vai te deixar"; como</text><text x='10' y='188' fill='#6c6a55'>se eu estivesse acima</text>
<rect x='182' y='120' width='172' height='100' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/><text x='192' y='140' font-weight='800'>Ironia</text><text x='192' y='160' fill='#6c6a55'>"desregulou essa semana?</text><text x='192' y='174' fill='#6c6a55'>nada de novo sob o sol"</text>
<rect x='364' y='120' width='172' height='100' rx='9' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.2'/><text x='374' y='140' font-weight='800'>Análise inoportuna</text><text x='374' y='160' fill='#6c6a55'>explicar ("isso é por causa</text><text x='374' y='174' fill='#6c6a55'>da tua mãe") enquanto a</text><text x='374' y='188' fill='#6c6a55'>pessoa chora na frente</text>
<rect x='546' y='120' width='174' height='100' rx='9' fill='#43441f'/><text x='556' y='140' font-weight='800' fill='#f0ede0'>O "mas"</text><text x='556' y='160' fill='#c9c6a8'>apaga tudo que veio antes</text><text x='556' y='174' fill='#c9c6a8'>e leva o olhar para a falta.</text><text x='556' y='188' fill='#c9c6a8'>Troca por "e".</text>
</g>
</svg>
<figcaption>Quase todos são afirmações. O oitavo é uma conjunção, e é o mais frequente.</figcaption></figure>""" % dict(F=F)

MAS_E = u"""<figure class='dg'><div class='dg-t'>O "mas" e o "e": a mesma devolutiva, duas leituras</div>
<svg viewBox='0 0 720 210' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Duas versões de uma devolutiva de supervisão: com mas, o olhar vai para a falta; com e mais proposta, a frase inteira é lida e a esperança fica'>
<rect x='0' y='8' width='350' height='150' rx='11' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='14' y='32' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>COM "MAS"</text>
<text x='14' y='58' %(F)s font-size='10.5' fill='#2f2e24'>"Tu tens um bom raciocínio, a condução tá</text>
<text x='14' y='74' %(F)s font-size='10.5' fill='#2f2e24'>boa, <tspan font-weight='800' fill='#a05a3c'>mas</tspan> acho que se tu focar mais no</text>
<text x='14' y='90' %(F)s font-size='10.5' fill='#2f2e24'>monitoramento..."</text>
<text x='14' y='120' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>o que fica: <tspan font-weight='800' fill='#a05a3c'>falta</tspan> algo em mim.</text>
<text x='14' y='136' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>a atenção vai para a ameaça e não lê o resto</text>
<rect x='370' y='8' width='350' height='150' rx='11' fill='#f1ece0' stroke='#9ca575' stroke-width='1.4'/>
<text x='384' y='32' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#43441f'>COM "E" + PROPOSTA</text>
<text x='384' y='58' %(F)s font-size='10.5' fill='#2f2e24'>"Tu tens um bom raciocínio, a condução tá</text>
<text x='384' y='74' %(F)s font-size='10.5' fill='#2f2e24'>muito boa, <tspan font-weight='800' fill='#43441f'>e</tspan> acho que a gente pode refinar</text>
<text x='384' y='90' %(F)s font-size='10.5' fill='#2f2e24'>isso juntos. <tspan font-weight='800' fill='#43441f'>Posso te propor?</tspan> O que tu acha?"</text>
<text x='384' y='120' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>nenhuma palavra negativa; a frase inteira</text>
<text x='384' y='136' %(F)s font-size='10' font-style='italic' fill='#6c6a55'>é lida; a esperança de melhorar fica de pé</text>
<text x='360' y='190' text-anchor='middle' %(F)s font-size='10.5' fill='#8d876f'>o mesmo vale para o paciente: descrever o que já vai bem, "e", pedir permissão para propor</text>
</svg>
<figcaption>O exemplo da aula é uma supervisão, de propósito: a gente sente na pele o que o "mas" faz antes de entender o que ele faz com o paciente.</figcaption></figure>""" % dict(F=F)

REAT = u"""<figure class='dg'><div class='dg-t'>Reatância: o conselho certo dado do jeito errado</div>
<svg viewBox='0 0 720 236' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Duas sequências: em cima, conselho não pedido leva a ameaça à autonomia e modo opositor; embaixo, coletar a função, validar, pedir permissão e propor em aberto'>
<defs><marker id='re' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<text x='0' y='20' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#a05a3c'>O QUE GERA REAT&Acirc;NCIA</text>
<g %(F)s font-size='10' fill='#2f2e24' text-anchor='middle'>
<rect x='0' y='30' width='210' height='64' rx='9' fill='#fffdf7' stroke='#a05a3c'/><text x='105' y='52' font-weight='800'>conselho não pedido</text><text x='105' y='70' fill='#6c6a55' font-style='italic'>"que tal parar de beber?"</text>
<path d='M214 62 L246 62' stroke='#8d876f' stroke-width='2' marker-end='url(#re)'/>
<rect x='250' y='30' width='210' height='64' rx='9' fill='#fffdf7' stroke='#a05a3c'/><text x='355' y='52' font-weight='800'>ameaça à autonomia</text><text x='355' y='70' fill='#6c6a55'>"como se eu não fosse capaz sozinho"</text>
<path d='M464 62 L496 62' stroke='#8d876f' stroke-width='2' marker-end='url(#re)'/>
<rect x='500' y='30' width='220' height='64' rx='9' fill='#fffdf7' stroke='#a05a3c'/><text x='610' y='52' font-weight='800'>modo opositor</text><text x='610' y='70' fill='#6c6a55'>e o terapeuta "confirma" que ele não faz</text>
</g>
<text x='0' y='128' %(F)s font-size='10' font-weight='800' letter-spacing='1.2' fill='#43441f'>O QUE ABRE</text>
<g %(F)s font-size='10' fill='#2f2e24' text-anchor='middle'>
<rect x='0' y='138' width='166' height='84' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='83' y='160' font-weight='800'>1 · função</text><text x='83' y='178' fill='#6c6a55'>"como é para ti quando</text><text x='83' y='192' fill='#6c6a55'>tu bebe? o que sente?"</text>
<path d='M170 180 L182 180' stroke='#8d876f' stroke-width='2' marker-end='url(#re)'/>
<rect x='186' y='138' width='166' height='84' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='269' y='160' font-weight='800'>2 · validação</text><text x='269' y='178' fill='#6c6a55'>"faz sentido; no teu lugar</text><text x='269' y='192' fill='#6c6a55'>talvez eu fizesse o mesmo"</text>
<path d='M356 180 L368 180' stroke='#8d876f' stroke-width='2' marker-end='url(#re)'/>
<rect x='372' y='138' width='166' height='84' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='455' y='160' font-weight='800'>3 · permissão</text><text x='455' y='178' fill='#6c6a55'>"tem uma coisa que já</text><text x='455' y='192' fill='#6c6a55'>funcionou. posso te propor?"</text>
<path d='M542 180 L554 180' stroke='#8d876f' stroke-width='2' marker-end='url(#re)'/>
<rect x='558' y='138' width='162' height='84' rx='9' fill='#43441f'/><text x='639' y='160' font-weight='800' fill='#f0ede0'>4 · proposta aberta</text><text x='639' y='178' fill='#c9c6a8'>"essa é uma; tem outras.</text><text x='639' y='192' fill='#c9c6a8'>qual te parece melhor?"</text>
</g>
</svg>
<figcaption>A proposta é a mesma. O que muda é que a segunda não ameaça a única autonomia que o paciente tem, e deixa que ele chegue à conclusão, que vale mais quando é dele.</figcaption></figure>""" % dict(F=F)

NIVEIS = u"""<figure class='dg'><div class='dg-t'>Os seis níveis de validação, no exemplo da aula</div>
<svg viewBox='0 0 720 300' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Escada de seis degraus com os níveis de validação e a fala correspondente do terapeuta para o relato: mandei e-mail pro meu chefe, ele não respondeu e passei a noite acordada'>
<rect x='0' y='6' width='720' height='34' rx='8' fill='#43441f'/>
<text x='360' y='28' text-anchor='middle' %(F)s font-size='10.5' font-style='italic' fill='#f0ede0'>"Mandei e-mail pro meu chefe, ele não respondeu, e passei a noite toda acordada."</text>
<g %(F)s font-size='10' fill='#2f2e24'>
<rect x='0' y='52' width='720' height='38' rx='7' fill='#f1ece0' stroke='#9ca575'/><text x='10' y='68' font-weight='800'>1 · silêncio atento</text><text x='10' y='83' fill='#6c6a55'>atenção plena ao que ela fala, à postura, ao ritmo; não interrompe, não se adianta, nenhum comentário jocoso</text>
<rect x='0' y='94' width='720' height='38' rx='7' fill='#f1ece0' stroke='#9ca575'/><text x='10' y='110' font-weight='800'>2 · descrever</text><text x='10' y='125' fill='#6c6a55' font-style='italic'>"entendi: mandou o e-mail, ele não respondeu até agora e tu não conseguiu dormir"</text>
<rect x='0' y='136' width='720' height='38' rx='7' fill='#f1ece0' stroke='#9ca575'/><text x='10' y='152' font-weight='800'>3 · ler o que não foi dito</text><text x='10' y='167' fill='#6c6a55' font-style='italic'>"quando tu me diz que não dormiu, fico pensando se surgiu o medo de ter feito algo errado, como a gente já viu aqui"</text>
<rect x='0' y='178' width='720' height='38' rx='7' fill='#f1ece0' stroke='#9ca575'/><text x='10' y='194' font-weight='800'>4 · validar pela história</text><text x='10' y='209' fill='#6c6a55' font-style='italic'>"na tua casa, silêncio era o lugar seguro e do teu pai vinha bronca; faz sentido uma falta de resposta dar medo"</text>
<rect x='0' y='220' width='720' height='38' rx='7' fill='#f1ece0' stroke='#9ca575'/><text x='10' y='236' font-weight='800'>5 · validar pelo presente (normalizar)</text><text x='10' y='251' fill='#6c6a55' font-style='italic'>"a maioria das pessoas ficaria ansiosa sem resposta de algo importante"</text>
<rect x='0' y='262' width='720' height='38' rx='7' fill='#43441f'/><text x='10' y='278' font-weight='800' fill='#f0ede0'>6 · genuinidade radical (autorrevelação)</text><text x='10' y='293' fill='#c9c6a8' font-style='italic'>"eu já perdi sono com isso num lugar em que trabalhei; foi doloroso" (ou: "nem sei como eu reagiria")</text>
</g>
</svg>
<figcaption>O relato não tem emoção explícita. Uma pessoa que passa a noite acordada sentiu algo: o nível 3 é isso, e o ideal é abrir para ela nomear antes de nomear por ela.</figcaption></figure>""" % dict(F=F)

VALIDAR = u"""<figure class='dg'><div class='dg-t'>O que se valida e o que não se valida</div>
<svg viewBox='0 0 720 170' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Três caixas: o desejo e a emoção se validam; o contexto se valida; o comportamento nocivo não se valida, e a pergunta sobre ele fica em aberto'>
<rect x='0' y='30' width='226' height='100' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='113' y='54' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#43441f'>VALIDA: o desejo, a emoção</text>
<text x='113' y='78' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>"faz sentido querer se anestesiar,</text>
<text x='113' y='94' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>se apagar; rede de apoio é</text>
<text x='113' y='110' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>uma coisa que precisa"</text>
<rect x='247' y='30' width='226' height='100' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='360' y='54' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#43441f'>VALIDA: o contexto</text>
<text x='360' y='78' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>"diante desse término, eu nem</text>
<text x='360' y='94' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>imagino o vazio; é um impulso</text>
<text x='360' y='110' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>esperado de se livrar da dor"</text>
<rect x='494' y='30' width='226' height='100' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/>
<text x='607' y='54' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>N&Atilde;O VALIDA: o comportamento</text>
<text x='607' y='78' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>não "vai beber com teus amigos".</text>
<text x='607' y='94' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>e sim: "até que ponto isso te afasta</text>
<text x='607' y='110' text-anchor='middle' %(F)s font-size='10' fill='#2f2e24'>da dor? já tentou outra coisa?"</text>
<text x='360' y='156' text-anchor='middle' %(F)s font-size='10' font-style='italic' fill='#8d876f'>o mesmo vale para a autolesão: valida-se o vazio e o impulso; nunca o ato</text>
</svg>
<figcaption>Se o terapeuta valida o comportamento, o paciente ou desconfia da postura ou passa a achar que tudo tem aval. E quando recai, o terapeuta entra na conta.</figcaption></figure>""" % dict(F=F)

PRINC = u"""<figure class='dg'><div class='dg-t'>Os cinco princípios da postura, e o que cada um pede na clínica</div>
<svg viewBox='0 0 720 300' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Cinco caixas: consciência do momento presente, desapego, interexistência, impermanência e o mundo é perfeito como é, cada uma com o que o princípio pede do terapeuta e do paciente'>
<g %(F)s font-size='10' fill='#2f2e24'>
<rect x='0' y='6' width='232' height='136' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='12' y='28' font-size='11' font-weight='800'>1 · Momento presente</text>
<text x='12' y='50' fill='#6c6a55'>atenção a cada palavra e gesto.</text><text x='12' y='64' fill='#6c6a55'>quando o paciente chora: "o que tá</text><text x='12' y='78' fill='#6c6a55'>acontecendo aqui entre nós agora?",</text><text x='12' y='92' fill='#6c6a55'>em vez de apaziguar. deixar que ele</text><text x='12' y='106' fill='#6c6a55'>sinta no lugar seguro por um minuto.</text>
<text x='12' y='130' font-style='italic' fill='#a05a3c'>armadilha: regular a dor dele por causa da minha</text>
<rect x='244' y='6' width='232' height='136' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='256' y='28' font-size='11' font-weight='800'>2 · Desapego</text>
<text x='256' y='50' fill='#6c6a55'>apego é exigir que a realidade fosse</text><text x='256' y='64' fill='#6c6a55'>outra: "não devia ter sido assim". é a</text><text x='256' y='78' fill='#6c6a55'>ruminação. adiar a ruminação, agir</text><text x='256' y='92' fill='#6c6a55'>apesar dela (ação oposta), e não</text><text x='256' y='106' fill='#6c6a55'>discutir com quem briga.</text>
<text x='256' y='130' font-style='italic' fill='#a05a3c'>armadilha: meu apego a reduzir sintoma rápido</text>
<rect x='488' y='6' width='232' height='136' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='500' y='28' font-size='11' font-weight='800'>3 · Interexistência</text>
<text x='500' y='50' fill='#6c6a55'>ninguém existe isolado; eu e o</text><text x='500' y='64' fill='#6c6a55'>paciente somos contingência um</text><text x='500' y='78' fill='#6c6a55'>do outro. atraso, distância, silêncio</text><text x='500' y='92' fill='#6c6a55'>são dado clínico, e não ataque</text><text x='500' y='106' fill='#6c6a55'>pessoal: pergunta-se pela função.</text>
<text x='500' y='130' font-style='italic' fill='#a05a3c'>armadilha: minha impaciência veio do meu dia</text>
<rect x='122' y='158' width='232' height='136' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/>
<text x='134' y='180' font-size='11' font-weight='800'>4 · Impermanência</text>
<text x='134' y='202' fill='#6c6a55'>emoção e contexto mudam sozinhos.</text><text x='134' y='216' fill='#6c6a55'>a crise "durou o dia inteiro": hora a</text><text x='134' y='230' fill='#6c6a55'>hora, não durou. só existe bom</text><text x='134' y='244' fill='#6c6a55'>porque existe ruim; a melhora também</text><text x='134' y='258' fill='#6c6a55'>não é permanente: lombada, não muro.</text>
<text x='134' y='282' font-style='italic' fill='#a05a3c'>armadilha: fugir cedo e nunca aprender a tolerar</text>
<rect x='366' y='158' width='232' height='136' rx='10' fill='#43441f'/>
<text x='378' y='180' font-size='11' font-weight='800' fill='#f0ede0'>5 · O mundo é perfeito como é</text>
<text x='378' y='202' fill='#c9c6a8'>perfeito = levado até o fim pelas</text><text x='378' y='216' fill='#c9c6a8'>variáveis, e não bom nem justo.</text><text x='378' y='230' fill='#c9c6a8'>"não devia ter acontecido" (moral) e</text><text x='378' y='244' fill='#c9c6a8'>"aconteceu, dadas as condições"</text><text x='378' y='258' fill='#c9c6a8'>(aceitação) são as duas verdades.</text>
<text x='378' y='282' font-style='italic' fill='#d59a4b'>armadilha: virar destino, plano divino ou conformismo</text>
</g>
</svg>
<figcaption>Os cinco se amarram: um abre espaço para o outro. E a aula insiste: se o terapeuta não vive isso, não passa para o paciente. É para isso que existe o grupo de consultoria.</figcaption></figure>""" % dict(F=F)

HORA = u"""<figure class='dg'><div class='dg-t'>Impermanência: a crise que "durou o dia inteiro", hora a hora</div>
<svg viewBox='0 0 720 210' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Gráfico de intensidade do sofrimento ao longo de um dia: pico às 14h, queda às 15h quando falou com alguém, 50 por cento às 16h; o paciente atenta só para o pico'>
<line x1='50' y1='20' x2='50' y2='170' stroke='#2f2e24' stroke-width='1.4'/><line x1='50' y1='170' x2='690' y2='170' stroke='#2f2e24' stroke-width='1.4'/>
<text x='24' y='100' %(F)s font-size='9' fill='#6c6a55' transform='rotate(-90 24 100)' text-anchor='middle'>sofrimento</text>
<g %(F)s font-size='9.5' fill='#6c6a55' text-anchor='middle'>
<text x='110' y='188'>12h</text><text x='210' y='188'>13h</text><text x='310' y='188'>14h</text><text x='410' y='188'>15h</text><text x='510' y='188'>16h</text><text x='610' y='188'>17h</text>
</g>
<polyline points='110,140 210,110 310,35 410,80 510,105 610,120' fill='none' stroke='#a05a3c' stroke-width='2.6'/>
<g fill='#a05a3c'><circle cx='110' cy='140' r='4'/><circle cx='210' cy='110' r='4'/><circle cx='310' cy='35' r='6'/><circle cx='410' cy='80' r='4'/><circle cx='510' cy='105' r='4'/><circle cx='610' cy='120' r='4'/></g>
<text x='310' y='24' text-anchor='middle' %(F)s font-size='9.5' font-weight='800' fill='#a05a3c'>"insuportável"</text>
<text x='410' y='70' text-anchor='middle' %(F)s font-size='9.5' fill='#2f2e24'>falou com alguém</text>
<text x='510' y='96' text-anchor='middle' %(F)s font-size='9.5' fill='#2f2e24'>"uns 50%%"</text>
<rect x='270' y='20' width='80' height='150' fill='#a05a3c' opacity='0.08'/>
<text x='600' y='45' text-anchor='end' %(F)s font-size='10' font-style='italic' fill='#8d876f'>o viés atencional guarda só o pico;</text>
<text x='600' y='60' text-anchor='end' %(F)s font-size='10' font-style='italic' fill='#8d876f'>reconstruir hora a hora mostra o resto</text>
</svg>
<figcaption>O pedido é simples: "me conta como foi das 12h às 18h, hora por hora". A curva aparece sozinha, e com ela a pergunta: o que ficaria possível fazer se isso não precisasse ser resolvido agora?</figcaption></figure>""" % dict(F=F)

LOMB = u"""<figure class='dg'><div class='dg-t'>Lombada ou muro</div>
<svg viewBox='0 0 720 150' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='À esquerda, uma estrada com lombadas: o carro reduz e segue; à direita, um muro: o carro para'>
<line x1='20' y1='110' x2='340' y2='110' stroke='#2f2e24' stroke-width='2'/>
<path d='M70 110 q 25 -28 50 0' fill='#9ca575' opacity='0.7'/><path d='M170 110 q 25 -28 50 0' fill='#9ca575' opacity='0.7'/><path d='M270 110 q 25 -28 50 0' fill='#9ca575' opacity='0.7'/>
<text x='180' y='40' text-anchor='middle' %(F)s font-size='11' font-weight='800' fill='#43441f'>LOMBADA</text>
<text x='180' y='58' text-anchor='middle' %(F)s font-size='10' fill='#6c6a55'>às vezes bom, às vezes ruim; vai lento,</text>
<text x='180' y='72' text-anchor='middle' %(F)s font-size='10' fill='#6c6a55'>e não para de andar. a segunda já se passa melhor</text>
<line x1='380' y1='110' x2='700' y2='110' stroke='#2f2e24' stroke-width='2'/>
<rect x='560' y='40' width='16' height='70' fill='#a05a3c'/>
<text x='540' y='40' text-anchor='end' %(F)s font-size='11' font-weight='800' fill='#a05a3c'>MURO</text>
<text x='540' y='58' text-anchor='end' %(F)s font-size='10' fill='#6c6a55'>"já tá bom aqui, chega" ou</text>
<text x='540' y='72' text-anchor='end' %(F)s font-size='10' fill='#6c6a55'>"já tá ruim aqui, chega":</text>
<text x='540' y='86' text-anchor='end' %(F)s font-size='10' fill='#6c6a55'>paralisa e não deixa viver a oscilação</text>
<text x='360' y='140' text-anchor='middle' %(F)s font-size='10' font-style='italic' fill='#8d876f'>a dor não é permanente, e a melhora também não; quem sabe disso é menos derrubado quando a curva desce</text>
</svg>
<figcaption>O paciente que diz "se vou melhorar e depois piorar, para que seguir?" está certo sobre a impermanência e errado sobre o muro.</figcaption></figure>""" % dict(F=F)

HIER = u"""<figure class='dg'><div class='dg-t'>Hierarquia de alvos e as quatro funções</div>
<svg viewBox='0 0 720 260' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='À esquerda, quatro degraus da hierarquia de alvos da DBT; à direita, os quatro episódios de autolesão da Camila, topografia idêntica e quatro funções diferentes'>
<g %(F)s font-size='10' fill='#2f2e24'>
<rect x='0' y='10' width='330' height='46' rx='8' fill='#a05a3c'/><text x='12' y='30' font-weight='800' fill='#fff'>1 · ameaçam a vida</text><text x='12' y='46' fill='#fff'>tentativa, autolesão, ideação: sempre primeiro</text>
<rect x='0' y='62' width='330' height='46' rx='8' fill='#c9a48c'/><text x='12' y='82' font-weight='800' fill='#2f2e24'>2 · interferem na terapia</text><text x='12' y='98' fill='#2f2e24'>faltar, atrasar, não trazer a tarefa: aqui, comigo, agora</text>
<rect x='0' y='114' width='330' height='46' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='12' y='134' font-weight='800'>3 · interferem na qualidade de vida</text><text x='12' y='150' fill='#6c6a55'>relacionamento, substância, moradia, trabalho</text>
<rect x='0' y='166' width='330' height='46' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='12' y='186' font-weight='800'>4 · aumento de habilidades</text><text x='12' y='202' fill='#6c6a55'>o projeto de vida propriamente dito</text>
<text x='0' y='240' font-style='italic' fill='#8d876f'>não é sugestão: recaída num alvo acima interrompe o de baixo</text>
<rect x='370' y='10' width='350' height='30' rx='7' fill='#43441f'/><text x='545' y='30' text-anchor='middle' font-weight='800' fill='#f0ede0'>Camila: quatro episódios, mesma topografia</text>
<rect x='370' y='48' width='170' height='58' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='380' y='68' font-weight='800'>baixar a emoção</text><text x='380' y='84' fill='#6c6a55'>a tensão cai em segundos</text><text x='380' y='98' fill='#6c6a55'>(reforço negativo)</text>
<rect x='550' y='48' width='170' height='58' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='560' y='68' font-weight='800'>sair de uma exigência</text><text x='560' y='84' fill='#6c6a55'>no dia seguinte ela não vai;</text><text x='560' y='98' fill='#6c6a55'>a demanda se afasta</text>
<rect x='370' y='114' width='170' height='58' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='380' y='134' font-weight='800'>trazer alguém de volta</text><text x='380' y='150' fill='#6c6a55'>a pessoa pede desculpa,</text><text x='380' y='164' fill='#6c6a55'>fica à noite, cuida</text>
<rect x='550' y='114' width='170' height='58' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='560' y='134' font-weight='800'>sentir alguma coisa</text><text x='560' y='150' fill='#6c6a55'>no meio da anestesia, o corpo</text><text x='560' y='164' fill='#6c6a55'>volta e ela sai do vazio</text>
<text x='545' y='200' text-anchor='middle' font-style='italic' fill='#8d876f'>cada comportamento tem função; a topografia não diz qual.</text>
<text x='545' y='216' text-anchor='middle' font-style='italic' fill='#8d876f'>só a análise em cadeia, uma por episódio, diz.</text>
</g>
</svg>
<figcaption>Reduzir emoção, evitar algo do ambiente, fazer alguém não abandonar, ou sentir alguma coisa: quase toda função cai numa das quatro. O padrão aparece depois de muitas cadeias.</figcaption></figure>""" % dict(F=F)

PADRAO = u"""<figure class='dg'><div class='dg-t'>Três cadeias, um padrão, e onde o plano de segurança entra</div>
<svg viewBox='0 0 720 214' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Três linhas com situações diferentes: chefe não responde, amiga cancela, namorado dorme sem avisar; todas passam por vergonha, leitura de rejeição, isolamento e ruminação, e chegam à autolesão; o plano de segurança corta entre a ruminação e o ato'>
<defs><marker id='pd' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0 L8,4 L0,8 z' fill='#8d876f'/></marker></defs>
<g %(F)s font-size='9.5' fill='#2f2e24'>
<text x='0' y='36' font-weight='800'>chefe não responde</text>
<text x='0' y='86' font-weight='800'>amiga cancela</text>
<text x='0' y='136' font-weight='800'>namorado dorme cedo</text><text x='0' y='150' font-weight='800'>e não avisa</text>
<g stroke='#8d876f' stroke-width='1.6'><path d='M130 32 L164 62' fill='none' marker-end='url(#pd)'/><path d='M130 82 L164 82' fill='none' marker-end='url(#pd)'/><path d='M130 132 L164 102' fill='none' marker-end='url(#pd)'/></g>
<rect x='170' y='56' width='110' height='52' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='225' y='78' text-anchor='middle' font-weight='800'>vergonha</text><text x='225' y='96' text-anchor='middle' fill='#6c6a55'>medo, culpa</text>
<path d='M284 82 L304 82' stroke='#8d876f' stroke-width='1.6' marker-end='url(#pd)'/>
<rect x='310' y='56' width='110' height='52' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='365' y='78' text-anchor='middle' font-weight='800'>"é rejeição"</text><text x='365' y='96' text-anchor='middle' fill='#6c6a55'>a leitura</text>
<path d='M424 82 L444 82' stroke='#8d876f' stroke-width='1.6' marker-end='url(#pd)'/>
<rect x='450' y='56' width='110' height='52' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='505' y='78' text-anchor='middle' font-weight='800'>isola, rumina</text><text x='505' y='96' text-anchor='middle' fill='#6c6a55'>e a dor sobe</text>
<path d='M564 82 L584 82' stroke='#a05a3c' stroke-width='2' marker-end='url(#pd)'/>
<rect x='590' y='56' width='130' height='52' rx='8' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.4'/><text x='655' y='78' text-anchor='middle' font-weight='800' fill='#a05a3c'>autolesão</text><text x='655' y='96' text-anchor='middle' fill='#6c6a55'>para aliviar</text>
<line x1='575' y1='40' x2='575' y2='124' stroke='#43441f' stroke-width='2.4' stroke-dasharray='5 3'/>
<text x='575' y='30' text-anchor='middle' font-weight='800' fill='#43441f'>plano de segurança corta aqui</text>
<rect x='170' y='160' width='550' height='46' rx='8' fill='#43441f'/>
<text x='445' y='178' text-anchor='middle' fill='#f0ede0' font-weight='800'>o elo do meio é onde a intervenção cabe</text>
<text x='445' y='196' text-anchor='middle' fill='#c9c6a8'>o ambiente muda toda hora e o viés atencional não vê; o elo cognitivo e o isolamento, sim, dá para mexer</text>
</g>
</svg>
<figcaption>Situações diferentes, funções iguais. Depois de muitas cadeias o padrão vai para o papel, volta para o paciente em forma de pergunta ("faz sentido na tua vida?"), e o elo se escolhe junto: o mais acessível, com desconforto tolerável.</figcaption></figure>""" % dict(F=F)

QUATRO = u"""<figure class='dg'><div class='dg-t'>Quatro categorias de procedimento, e a flexibilidade na fidelidade</div>
<svg viewBox='0 0 720 232' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Quatro caixas com as categorias operacionais da DBT e quando cada uma entra; embaixo, três pacientes e o que cada um pede'>
<g %(F)s font-size='10' fill='#2f2e24'>
<rect x='0' y='6' width='172' height='96' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='10' y='26' font-weight='800'>Treino de habilidades</text><text x='10' y='46' fill='#6c6a55'>não tem repertório: chega</text><text x='10' y='60' fill='#6c6a55'>desregulado, sem saber o</text><text x='10' y='74' fill='#6c6a55'>que fazer às 23h. costuma</text><text x='10' y='88' fill='#6c6a55'>ser o começo.</text>
<rect x='182' y='6' width='172' height='96' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='192' y='26' font-weight='800'>Modificação cognitiva</text><text x='192' y='46' fill='#6c6a55'>tem repertório e a emoção</text><text x='192' y='60' fill='#6c6a55'>é forte demais: "eu sei</text><text x='192' y='74' fill='#6c6a55'>racionalmente, mas não</text><text x='192' y='88' fill='#6c6a55'>consigo". apego.</text>
<rect x='364' y='6' width='172' height='96' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='374' y='26' font-weight='800'>Manejo de contingências</text><text x='374' y='46' fill='#6c6a55'>o ambiente mantém o</text><text x='374' y='60' fill='#6c6a55'>comportamento. o mais difícil</text><text x='374' y='74' fill='#6c6a55'>de início: pouca variação,</text><text x='374' y='88' fill='#6c6a55'>mais punição que reforço.</text>
<rect x='546' y='6' width='174' height='96' rx='9' fill='#f1ece0' stroke='#9ca575'/><text x='556' y='26' font-weight='800'>Exposição</text><text x='556' y='46' fill='#6c6a55'>esquiva da vergonha, da</text><text x='556' y='60' fill='#6c6a55'>culpa, de ser vista como</text><text x='556' y='74' fill='#6c6a55'>ruim: tolerância ao mal-estar</text><text x='556' y='88' fill='#6c6a55'>e regulação entram aqui.</text>
<rect x='0' y='118' width='720' height='30' rx='7' fill='#43441f'/><text x='360' y='138' text-anchor='middle' font-weight='800' fill='#f0ede0'>flexibilidade na fidelidade: o alvo mais urgente puxa o módulo de volta</text>
<text x='0' y='172' font-weight='800'>Camila</text><text x='70' y='172' fill='#6c6a55'>quinta à noite, faz algo para baixar a emoção; não sabia o que fazer &rarr; treino de habilidades + coach telefônico</text>
<text x='0' y='194' font-weight='800'>Marcos</text><text x='70' y='194' fill='#6c6a55'>liga para a ex para trazer alguém perto; sabe as habilidades e não usa &rarr; contingência ou modificação cognitiva</text>
<text x='0' y='216' font-weight='800'>Beatriz</text><text x='70' y='216' fill='#6c6a55'>entra dizendo que vai parar &rarr; para a solução, sobe o alvo (interfere na terapia), volta ao comprometimento</text>
</g>
</svg>
<figcaption>Demandas parecidas (todos afastam algo), percursos diferentes. Se o paciente chega com autolesão na quinta, a cadeia da quinta vem antes da solução que estava em curso; se chega dissociado, para tudo e foca na dissociação.</figcaption></figure>""" % dict(F=F)

HAB = u"""<figure class='dg'><div class='dg-t'>Seis habilidades de aceitação e as duas metades do módulo</div>
<svg viewBox='0 0 720 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Seis habilidades: aceitação radical, redirecionamento, estar disposto, meio sorriso, mãos dispostas, permitir a mente; embaixo, as duas metades do módulo de tolerância ao mal-estar: sobreviver à crise e aceitar a realidade'>
<g %(F)s font-size='10' fill='#2f2e24' text-anchor='middle'>
<rect x='0' y='6' width='112' height='60' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='56' y='30' font-weight='800'>aceitação</text><text x='56' y='46' font-weight='800'>radical</text>
<rect x='122' y='6' width='112' height='60' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='178' y='30' font-weight='800'>redirecio-</text><text x='178' y='46' font-weight='800'>namento</text>
<rect x='244' y='6' width='112' height='60' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='300' y='30' font-weight='800'>estar</text><text x='300' y='46' font-weight='800'>disposto</text>
<rect x='366' y='6' width='112' height='60' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='422' y='30' font-weight='800'>meio</text><text x='422' y='46' font-weight='800'>sorriso</text>
<rect x='488' y='6' width='112' height='60' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='544' y='30' font-weight='800'>mãos</text><text x='544' y='46' font-weight='800'>dispostas</text>
<rect x='610' y='6' width='110' height='60' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='665' y='30' font-weight='800'>permitir</text><text x='665' y='46' font-weight='800'>a mente</text>
<text x='178' y='84' font-size='9.5' font-style='italic' fill='#8d876f'>com os princípios &middot; com atenção plena</text>
<text x='544' y='84' font-size='9.5' font-style='italic' fill='#8d876f'>com o corpo: postura e entonação modulam a fisiologia</text>
<rect x='0' y='104' width='350' height='84' rx='10' fill='#fffdf7' stroke='#a05a3c' stroke-width='1.3'/><text x='175' y='128' font-weight='800' fill='#a05a3c'>SOBREVIVER &Agrave; CRISE</text><text x='175' y='150' fill='#6c6a55'>distração, autoacalmar, melhorar o momento,</text><text x='175' y='166' fill='#6c6a55'>prós e contras: atravessar o hoje</text>
<rect x='370' y='104' width='350' height='84' rx='10' fill='#f1ece0' stroke='#9ca575' stroke-width='1.3'/><text x='545' y='128' font-weight='800' fill='#43441f'>ACEITAR A REALIDADE</text><text x='545' y='150' fill='#6c6a55'>a postura que fica depois da regulação: lidar</text><text x='545' y='166' fill='#6c6a55'>com o que não vai mudar nunca</text>
</g>
</svg>
<figcaption>As duas metades servem para a hora difícil. Só sobreviver à crise, sem entrar na aceitação, não dá chance de tolerar a emoção; e é quando o paciente para de tentar mudar o ambiente que as crises costumam diminuir. É paradoxal, e é a linha mestra.</figcaption></figure>""" % dict(F=F)

EQUIV = u"""<figure class='dg'><div class='dg-t'>Quatro equívocos da aceitação radical, e a correção</div>
<svg viewBox='0 0 720 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Quatro pares: aceitar o comportamento de risco versus aceitar a emoção; eu sou assim e pronto versus e estamos aqui para mudar; autoindulgência versus observar para verificar; passividade e sem perfil versus construir o perfil'>
<g %(F)s font-size='10' fill='#2f2e24'>
<rect x='0' y='6' width='350' height='42' rx='8' fill='#fffdf7' stroke='#a05a3c'/><text x='10' y='24' font-weight='800' fill='#a05a3c'>"tá tudo bem tu te cortar"</text><text x='10' y='40' fill='#6c6a55'>aceitou o comportamento</text>
<rect x='370' y='6' width='350' height='42' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='380' y='24' font-weight='800' fill='#43441f'>"faz sentido esse vazio e esse impulso"</text><text x='380' y='40' fill='#6c6a55'>aceitou a emoção e o contexto, e abriu outra via</text>
<rect x='0' y='56' width='350' height='42' rx='8' fill='#fffdf7' stroke='#a05a3c'/><text x='10' y='74' font-weight='800' fill='#a05a3c'>"eu sou assim e pronto"</text><text x='10' y='90' fill='#6c6a55'>resignação (do paciente, ou do terapeuta: "ele cansa todo mundo")</text>
<rect x='370' y='56' width='350' height='42' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='380' y='74' font-weight='800' fill='#43441f'>"tu é assim, e estamos aqui juntos para mudar"</text><text x='380' y='90' fill='#6c6a55'>"qual frase te soa melhor? o que tu mudaria nela?"</text>
<rect x='0' y='106' width='350' height='42' rx='8' fill='#fffdf7' stroke='#a05a3c'/><text x='10' y='124' font-weight='800' fill='#a05a3c'>"então vou procrastinar com gosto"</text><text x='10' y='140' fill='#6c6a55'>autoindulgência: ouviu o aval e não o resto</text>
<rect x='370' y='106' width='350' height='42' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='380' y='124' font-weight='800' fill='#43441f'>"adiar a ruminação essa semana, e observar o que muda"</text><text x='380' y='140' fill='#6c6a55'>não é permissão; é experimento com registro</text>
<rect x='0' y='156' width='350' height='42' rx='8' fill='#fffdf7' stroke='#a05a3c'/><text x='10' y='174' font-weight='800' fill='#a05a3c'>"nem vou tentar, não tenho perfil"</text><text x='10' y='190' fill='#6c6a55'>passividade: define-se pelo déficit</text>
<rect x='370' y='156' width='350' height='42' rx='8' fill='#f1ece0' stroke='#9ca575'/><text x='380' y='174' font-weight='800' fill='#43441f'>"hoje não tem, e com treino a gente constrói. como soa?"</text><text x='380' y='190' fill='#6c6a55'>valida o agora, abre o depois</text>
</g>
</svg>
<figcaption>Em todos, a correção mantém a primeira parte (é verdade) e acrescenta a segunda com "e". A aceitação radical é abertura aos fatos, sempre voltada à mudança.</figcaption></figure>""" % dict(F=F)

DBT = {
    'slug': 'dbt-aceitacao-validacao',
    'titulo_txt': 'Aceitação em DBT: postura do terapeuta, validação e os cinco princípios',
    'titulo_html': 'Aceita&ccedil;&atilde;o em DBT: postura do terapeuta, valida&ccedil;&atilde;o e os cinco princ&iacute;pios',
    'data': '12/09/2026',
    'meta': 'Prof. Júlio Gonçalves · Descomplicando a DBT, com Andressa Juliana · 12/09/2026',
    'meta_capa': 'PROF. J&Uacute;LIO GON&Ccedil;ALVES &middot; DESCOMPLICANDO A DBT<br>12 DE SETEMBRO DE 2026 &middot; AULA LIVRE',
    'header_dir': 'AULA LIVRE &middot; 12/09/2026',
    'chave': 'mat-Aula-DBT-Aceit-',
    'arquivo': 'Aula-DBT-aceitacao-respostas.txt',
    'desid': (u"<div class='obs' style='margin-bottom:18px'><h4>Sobre este material</h4>"
              u"<p>Material de estudo <strong>dirigido a psicólogos</strong>, escrito a partir da transcrição da aula do curso "
              u"Descomplicando a DBT de 12/09/2026 (a aula anterior, com Andressa Juliana, tratou de plano de tratamento e formulação; a seguinte trata de análise em cadeia).</p>"
              u"<p>Os exemplos (Camila, Rafael, Marcos, Beatriz, a supervisão da Andressa) são vinhetas didáticas da aula. Dúvidas dos participantes foram incorporadas ao texto sem identificação. "
              u"Menções à autolesão aparecem como exemplo de análise funcional, sem descrição de método.</p></div>"),
    'tema': 'O que a DBT pede do terapeuta antes de qualquer intervenção: aceitar antes de mudar, perguntar em vez de afirmar, trocar o "mas" pelo "e", '
            'validar em seis níveis sem validar o comportamento nocivo, sustentar cinco princípios de postura, e só então entrar na hierarquia de alvos e nas cadeias.',
    'essencial': [
        ('Aceitação não é resignação.',
         'Resignação fecha a porta; aceitação aceita o que aconteceu e pergunta o que ainda dá para mudar. Sempre com validação e um passo de mudança na mesma sessão.'),
        ('Pergunta, não afirmação.',
         'Afirmação só para descrever o que o paciente disse. O resto vira pergunta. Curiosidade vem com pergunta; moralização, argumentação e desaprovação vêm com afirmação.'),
        ('O "mas" apaga o que veio antes.',
         'Trocar por "e", tirar a palavra negativa e pedir permissão para propor. O olhar lê a frase inteira e a esperança fica.'),
        ('Seis níveis de validação, e um cuidado.',
         'Silêncio atento, descrever, ler o não dito, história, presente, genuinidade. Valida-se o desejo, a emoção e o contexto; nunca o comportamento nocivo.'),
        ('Cinco princípios que o terapeuta precisa viver.',
         'Momento presente, desapego, interexistência, impermanência, o mundo é perfeito como é. Se não vive, não passa. Para isso existe o grupo de consultoria.'),
        ('Só depois: hierarquia, função e cadeia.',
         'Vida, terapia, qualidade de vida, habilidades. Cada comportamento tem função; a topografia não diz qual. O elo do meio é onde se mexe.'),
    ],
    'secoes': [
        ('s0', 'Aceitar antes de mudar', 'Aceitar antes de mudar', u"""
{{ACEIT}}
<p>A aula abre com uma confissão que serve de diagnóstico da formação em psicologia: a gente é ensinado a produzir mudança. Centenas de protocolos, avaliação e intervenção já no estágio, questionário de distorções, diagnóstico e intervenção antes de a relação terapêutica existir. Olhando para trás, o professor chama isso do que é: iatrogênico e invalidante. A DBT inverte a ordem. Antes da mudança, o processo de <strong>aceitação</strong>, que atravessa todos os módulos e se fixa no de atenção plena; é a linha em que tudo se assenta.</p>
<p>A definição é simples e a fronteira é fina. Aceitar é aceitar o que aconteceu e o que está acontecendo; mudar é fazer, dentro do contexto e das habilidades do paciente, o que ainda dá para mudar. <strong>Resignação</strong> parece igual e é o oposto: "eu desisto, não vou mudar, as pessoas não vão mudar, aceito o mundo e deu". Aceitação sempre abre para a mudança, e a mudança se traduz na síntese dos dilemas dialéticos: mudar é muito difícil, e é aí que entra a gradação e a validação que instila esperança nas pequenas mudanças que o paciente já faz.</p>
<div class='obs'><h4>A aceitação também é do terapeuta</h4><p>A gente também está na equação. Somos modelados por cultura, formação e família, e o paciente modula nosso comportamento o tempo todo: ele é contingência para as nossas dores e para os nossos modelos parentais. A parte mais séria da postura, na fala do professor, é não desregular e não ir para o polo do apego às próprias crenças quando o paciente toca em algum lugar da gente, porque é aí que a invalidação sai sem a gente perceber.</p></div>
<h3>Uma definição para começar</h3>
<p>A aula parte de uma definição que atribui a Struck: aceitar é <strong>ouvir sem pré-julgamento e sem condenação</strong>, em três níveis. <strong>Cordialidade</strong>: corpo, ritmo, como a gente se entrega ao paciente. <strong>Comunicação</strong>: as palavras, muitas vezes uma quebra de formalidade ("pode me chamar de Júlio"). <strong>Consideração positiva</strong>: independente de quem está na frente, algo ali tem valor. A terceira é a mais difícil (a aula lembra abusadores e assassinos como limite), e fica mais fácil num público de desregulação, porque ninguém escolhe desregular: por mais trivial que a sociedade julgue o estímulo, há um processo muito mais complexo por trás. E a <strong>afirmação</strong>: sintetizar o que o paciente trouxe e devolver de forma organizada, sempre perguntando se faz sentido. Os seis níveis de validação são o caminho até ela.</p>
"""),
        ('s1', 'Pergunta, não afirmação', 'Pergunta, não afirmação: as falas que impedem avanço', u"""
{{PERG}}
<p>O exemplo é uma paciente que faltou duas sessões e chega dizendo "bá, quase não vim de novo". As falas que impedem avanço são as que ninguém acha que faz e todo mundo faz em variações: "mas tu concordou com o plano", "isso é autossabotagem", "se tu quer mesmo melhorar", "a gente já conversou que tem que fazer o plano senão não melhora". O objetivo é honesto e a forma está toda errada, por dois motivos. É uma afirmativa. E pressupõe que faltar foi má vontade, quando provavelmente estava controlado por uma contingência: a terapia virou estressor, o terapeuta acelerou, a semana foi pesada e pensar na terapia levava para o lugar da dor.</p>
<p>As perguntas que abrem não emitem julgamento; descrevem e devolvem. "Tu quase não veio, e veio: como foi decidir vir? O que teve no meio? O que tu pensou?" Isso descobre a motivação de ter vindo (e a gente reforça: "eu vim porque sabia que tinha que vir", ação oposta, e isso é útil para a gente aqui). "Ficou pesado demais entre uma sessão e outra? Faz sentido não querer entrar aqui quando dói tanto. Onde doeu? Eu tô aqui para isso." Curiosidade sempre vem com pergunta, nunca com afirmação.</p>
<div class='callout note'><div class='co-t'>A regra prática</div>Reduzir a afirmação ao máximo. Afirmação é só para descrever o que o paciente falou: "o que chegou para mim foi isso; entendi certo?" Se não entendeu, pergunta. Isso dá ao paciente, dentro do consultório, um poder e uma autonomia que ele não tem lá fora. Só transformar em pergunta já liga o modo curiosidade, e a abertura terapêutica que aparece é grande.</div>
"""),
        ('s2', 'Modos de invalidar', 'Os modos de invalidar que a gente não percebe', u"""
{{MODOS}}
<p>Quase todas as afirmativas caem num desses oito. A <strong>argumentação</strong> nunca tem pergunta no fim. A <strong>moralização</strong> incute o que eu considero certo e que, para aquele paciente naquela vida, não faz sentido nenhum. A <strong>desaprovação</strong> pode ser explícita ("não devia ter faltado") ou disfarçada de elogio ("que bom que tu veio, porque não é bom faltar mesmo"). A <strong>estigmatização</strong> substitui o contexto pelo rótulo ("borderline tem esse padrão mesmo"), e a aula lembra que Linehan não fez a DBT para borderline: pensou num conjunto transdiagnóstico de processos que não tem nome, e com o paciente a gente não precisa nomear. A <strong>advertência</strong> me põe acima do paciente ("já vou te adiantar que ele vai te deixar"). A <strong>ironia</strong> dispensa exemplo. A <strong>análise inoportuna</strong> é explicar ("isso é por causa da tua mãe") enquanto a pessoa se debulha em choro, em vez de vivenciar a emoção com ela; psicoeducar tem hora. E o <strong>"mas"</strong>.</p>
{{MAS_E}}
<p>O exemplo do "mas" é uma supervisão, de propósito. "Tu tens um bom raciocínio, Andressa, a condução tá boa, <em>mas</em> acho que se tu focar mais no monitoramento..." O que fica? A falta. A atenção vai para a ameaça ("falta algo em mim") e não processa o resto. A versão com "e": "Tu tens um bom raciocínio, a condução tá muito boa, e acho que a gente pode aprimorar isso juntos. Posso te propor? O que tu acha?" Nenhuma palavra negativa, nenhuma afirmativa, total liberdade, e a primeira parte fica de pé. O professor cita, sem atribuir à DBT, estudos de que termos negativos pioram a percepção da pessoa sobre o próprio processo. São pequenos movimentos.</p>
"""),
        ('s3', 'Estilo e reatância', 'Estilo do terapeuta e reatância', u"""
<h3>Dois estilos, dois prognósticos</h3>
<p>Há estudos, apresentados como complemento, de que o estilo <strong>afetuoso, receptivo, humano e democrático</strong> (baseado em pergunta, em avaliar decisões juntos, em errar e corrigir, em deixar o paciente ativo) tem prognóstico um pouco melhor, e o <strong>diretivo, moralista, disciplinador, frio e severo</strong> (que cobra execução, categoriza demais, mantém distância "técnica") tem prognóstico pessimista. "Mas tem paciente que prefere o psicólogo direto." Sim, e a explicação é a aula inteira: costuma ser o paciente controlador, que sente que o psicólogo faz o mesmo que ele faz na vida, ou seja, o psicólogo o reforça e a mudança fica no campo do conforto. Se o psicólogo fala por ele, ele nunca adquire assertividade nem repertório próprio. O democrático, implicitamente, força o paciente a ser autônomo, com a presença do terapeuta, que é muito mais seguro. Imagina ter tido pais assim.</p>
<div class='callout note'><div class='co-t'>O ciclo que estraga o caso</div>O nosso julgamento afeta o desfecho. Paciente difícil, "não tá dando nada", troco a intervenção, ele responde mal, troco de novo, responde mal, entro em reatância dele e confirmo minha regra de que ele não faz. É o paciente que não dá vontade de atender. E talvez a ativação seja minha: mudanças que não passaram pela aceitação, intervenções escolhidas no protocolo e colocadas antes de ele estar pronto. O modelo biossocial vale aqui também: paciente que melhora deixa o terapeuta mais caloroso, e o ciclo se retroalimenta nos dois sentidos.</div>
{{REAT}}
<p><strong>Reatância cognitiva e comportamental</strong> é o que acontece quando a gente dá ou fala coisas que o paciente poderia alcançar sozinho, principalmente em quem tem histórico de humilhação, baixa autonomia e invalidação, em que nada podia ser expresso: ele aprendeu a ficar quieto e agora, adulto, tem um pouco de poder sobre isso. O conselho pode estar certo ("parar de beber vai ajudar na tua regulação; que tal tentar na próxima semana?") e a pergunta está toda mal feita: eu não coletei a função de beber de forma neutra (beber anestesia alguma coisa), e não abri para o paciente pensar o que, além do álcool ou junto com ele, o deixa melhor. É como a criança que já ia lavar a louça e a gente manda lavar: barra na hora, porque bate na crença de não ser capaz sozinho e entra o modo opositor da vida inteira.</p>
<p>A ordem que abre: coletar a função; validar ("faz sentido; no teu lugar talvez eu fizesse o mesmo"); pedir permissão ("tem uma coisa que já funcionou comigo num contexto parecido; posso te propor para ver o que tu acha?"); e propor em aberto ("essa é uma; tem outras; qual te parece?"). O paciente pode chegar sozinho ("parar de beber me desregula"), e aí vale mais. Se não tem repertório para chegar, a gente orienta sem ditar a regra.</p>
"""),
        ('s4', 'Seis níveis', 'Os seis níveis de validação', u"""
{{NIVEIS}}
<p>A validação é regra e algoritmo, para ter anotado e aplicar sempre: o paciente traz dor para a clínica o tempo todo, e o tempo todo a gente entra no modo de validação. Com o aviso repetido: validação para gerar aceitação <em>e</em> mudança. Nunca só validação, senão é resignação. Por isso toda sessão promove algum pequeno passo de mudança.</p>
<p>O exemplo é a Camila: "mandei e-mail para o meu chefe, ele não respondeu, e passei a noite toda acordada". Não há emoção explícita; ela descreveu a situação. Mas uma pessoa que passa a noite acordada sentiu algo. O <strong>silêncio atento</strong> é o primeiro nível e é treino: atenção plena ao que ela fala, à postura, ao ritmo; não interromper, não se adiantar, nenhum comentário jocoso ("bá, de novo esse teu chefe", que foca no estímulo e não no sofrimento). Depois <strong>descrever</strong>. Depois <strong>ler o que não foi dito</strong>, ligando à formulação. Depois <strong>validar pela história</strong> (casa em silêncio, bronca do pai, medo até para pegar um copo de água: faz sentido uma falta de resposta dar medo). Depois <strong>validar pelo presente</strong> (a maioria das pessoas ficaria ansiosa). E a <strong>genuinidade radical</strong>, com autorrevelação nos dois polos: "eu já perdi sono com isso" ou "nunca passei por nada perto disso, e fico imaginando o quanto deve ser difícil; nem sei como eu reagiria".</p>
<div class='obs'><h4>A dúvida da turma: quem nomeia a emoção?</h4><p>Uma participante perguntou se, no nível 3, a gente atribui a emoção antes de o paciente dizê-la. A resposta: o ideal é abrir para ele nomear ("tu não dormiu; o que tu acha que aconteceu no teu corpo?"). Se não acessa o repertório, a gente amarra com a formulação ("uma coisa que tu já me disse é que tem medo de ter feito algo errado; é algo nessa linha?"). E há pacientes que de fato não sabem nomear, ou que na desregulação não acessam (às vezes é dissociação): nomear é um dos estágios do tratamento, e aí a formulação prévia ajuda. Quanto mais aberto, melhor; o princípio é aprofundar o que não foi dito.</p></div>
{{VALIDAR}}
<p>E o cuidado de <strong>validar o inválido</strong>. "Diante desse término, vou beber com meus amigos no fim de semana para reduzir o estresse." "É mesmo, é um momento de ter rede de apoio, vai beber com teus amigos, tu precisa relaxar." Qual a chance de o paciente ficar com o pé atrás com a postura, ou de achar que tudo tem aval, ou de recair e concluir que o psicólogo o mandou beber e ele não melhora? A saída é validar o <strong>desejo</strong> (faz sentido querer se anestesiar; rede de apoio é preciso) e deixar o comportamento em pergunta ("até que ponto isso é uma forma de se afastar da dor? como é para ti?"). Vale igual para a autolesão: valida-se o vazio e o impulso, empatiza-se com o que aconteceu, e nunca o ato; e abre-se outra via ("já tentou alguma outra coisa?").</p>
"""),
        ('s5', 'Cinco princípios', 'Os cinco princípios da postura', u"""
{{PRINC}}
<p>Os princípios organizam a postura do terapeuta e a do paciente. A condição, repetida na aula: se tu não tenta viver isso, não consegue passar para o paciente. Não dá para ensinar atenção plena sem experiência dela. Por isso o grupo de consultoria, em que os princípios são promovidos.</p>
<h3>1. Consciência do momento presente</h3>
<p>Camila conta a briga de domingo, tu formula a intervenção enquanto ela fala, ela começa a chorar e tu não sabe em que momento nem por quê. A consciência do presente exige atenção a cada palavra, ao rosto, à postura, e não a escuta passiva enquanto se faz outra coisa. Imerso, dá para pegar o momento: "vivencia um pouquinho e me diz o que está acontecendo aqui, agora, entre a gente; em que parte?" O erro é o modo apaziguador: "faz sentido chorar, não é fácil", para o paciente parar de desregular, porque a dor é minha e não dele. Vem dos nossos apegos: reduzir sintoma, tratar bem, não deixar desregular. E tira do paciente a chance de experienciar a emoção no lugar seguro.</p>
<p>Pelo lado do paciente, o princípio pede observar e descrever sensação, criar repertório sensorial e emocional e antecipar impulsos: quem não sabe descrever não modula a resposta. E pede <strong>sentir</strong>: o paciente que chora e desregula na sessão, sobretudo no começo, está no ambiente controlado, comigo. Não custa eu suportar a minha dor de vê-lo sofrer por um minuto, e esse minuto ensina a tolerar. Depois: "foi tão horrível assim? como foi eu ter ficado aqui contigo?" É, não morri; passou; não foi eterno. E a pergunta que ajuda quem sente e não sabe explicar: "a vergonha vai te matar? vai fazer algo cruel a ponto de tu nunca mais funcionar?" Não, é só ruim a sensação.</p>
<div class='callout note'><div class='co-t'>O terapeuta também é puxado para fora do presente</div>Pelo sintoma ("quero ver do sintoma"), pelo passado do paciente ("que droga, como a gente muda isso, que tal se afastar dessa mãe?"), pela solução rápida sem checar se ele tem a habilidade. Quando sentir que está sendo arrastado pela história e querendo resolver rápido, voltar por aqui: "o que está acontecendo aqui, agora, entre nós?"</div>
<h3>2. Desapego</h3>
<p>Apego é a exigência de que a realidade seja outra: "não era para ter sido assim; e se fosse diferente?" É a ruminação, e a briga é do paciente com um fato já fechado. O nosso papel não é "já foi, não tem o que fazer, nem foi tua culpa"; é abrir: o que ficaria possível fazer, em que contexto, se tu não precisasse resolver isso primeiro? Quando o treino de atenção plena entra, essa segunda coisa vira a primeira, porque ao trazer para o presente a ruminação perde força. O exemplo pessoal do professor é o ombro deslocado aos vinte anos, que ainda dói e que puxa a atenção para "por que fui fazer aquilo"; num paciente com trauma recorrente, a mesma ruminação vai para sobrecarga, sono ruim, cansaço, irritação, atenção estreita, mais ruminação, e o comportamento desadaptado é o último elo, consequência de tudo isso. A prática: adiar a ruminação, seguir fazendo o que importa apesar dela (ação oposta), e não entrar na discussão com quem briga; às vezes o oposto, um abraço, regula mais.</p>
<p>E o <strong>nosso</strong> apego, que a aula diz ser a lição maior para nós: querer melhora rápida, não querer ser alvo da raiva do paciente, a mentalidade de redução de sintoma ("apagar incêndio"). O Rafael terminou há duas semanas e passa a sessão listando o que faria diferente e checando o perfil dela. Eu quero que ele pare de checar e de sofrer: sinal de que me apeguei a uma norma social e não ao sofrimento dele. Se eu ficar dando solução para parar de checar, estou tentando resolver rápido como ele faz com a ruminação, e discutir possibilidades é ruminação viva; ensino que ruminar resolve. Quando a ansiedade do terapeuta bate ("tem que fazer algo senão ele me abandona e me julga"), a saída é reorganizar: "vamos cinco minutos para a gente se regular; eu vou tomar uma água", e retomar o fio pela função: "tu me diz que quer parar de checar; o que acontece quando tu checa? o que vem antes?"</p>
<h3>3. Interexistência</h3>
<p>Ninguém existe isolado: tira-se família, escola, sociedade e não sobra nada (o princípio dialético da polarização). No modelo biossocial, não dá para dizer se a desregulação da criança vem da mãe ou a da mãe da criança; para ser filho tem que ter mãe. Na clínica, a versão simples: eu estou sujeito à contingência do paciente e ele à minha. O paciente que diz "todo mundo cansa de mim" começa a atrasar, e eu começo a cansar, e a ficar impaciente: isso é apego meu às minhas crenças entrando na clínica. Se olho como funcionamento, o atraso é sobre o caso e não sobre mim; é <strong>dado clínico</strong>, nunca ataque pessoal. Avalia-se a função: "como foi hoje para ti estar aqui? aconteceu alguma coisa? tem algo na própria terapia que pode estar te afastando?" Até com autorrevelação: "fiquei pensando se um formato mais quieto de terapia não pode ser coisa minha; entendi certo?"</p>
<p>E a biofisiologia: impaciência que veio antes do paciente, por noite mal dormida, carro arranhado, fim de dia. É sutil; adrenalina com cortisol faz a gente achar que está bem e dar a patada, invalidar. Por isso as orientações de não atender dezenas por dia, o grupo de consultoria, as práticas de saúde e uma agenda que dê para manter sem cansaço: é o mínimo para trabalhar com DBT. Transação: pessoa e ambiente se produzem mutuamente.</p>
<h3>4. Impermanência</h3>
{{HORA}}
<p>O paciente entrega um trabalho às duas, almoça com a mãe às três, o pai grita às cinco, e só o grito fica. A crise "durou o dia inteiro, faz semanas". Pede-se para reconstruir hora a hora e não durou: às 14h insuportável, às 15h falou com alguém, às 16h já em 50%. O viés atencional, característico do espectro, atenta só para o pico. E o princípio: só existe bom porque existe ruim, e quando estiver ruim eu lembro do bom e vou buscá-lo. Isso se psicoeduca quando couber, e está nas fichas de aceitação de cada módulo.</p>
<p>Fugir cedo demais da emoção baixa rápido e ensina a não tolerar. A fisiologia se move sozinha: quem entrou na aula com empolgação 9 ou 10 está, depois de uma hora e meia, um pouco mais denso; é questão de minutos. E aqui o paciente pode entrar na resignação: "se vou melhorar e depois piorar, para que seguir? deixa eu me livrar da dor de uma vez". A validação é concordar: sim, se uma coisa melhora, outra piora, porque ambiente e critério mudam (o sushi do interior fica pior depois do de Itajaí, e o de Itajaí fica pior depois de um famoso).</p>
{{LOMB}}
<p>A questão é aceitar que as oscilações ocorrem: vira lombada. Às vezes bom, às vezes ruim, vai lento e não para de andar; a primeira lombada quase quebra o carro, depois de dez anos ninguém entra rápido nela. O problema é o muro: "já está bom aqui, chega" ou "já está ruim aqui, chega". A dor não é permanente e a melhora também não; quem entende isso é menos derrubado quando a curva desce.</p>
<h3>5. O mundo é perfeito como é</h3>
<p>Perfeito não é bom, justo, simétrico ou eterno. É <strong>levado até o fim</strong> pelas variáveis: dadas as condições, o resultado vem inteiro. A aula usa o exemplo chocante que Linehan usa, de um acidente fatal com uma criança, para dizer que, com aquela velocidade, aquela curva, aquele ponto cego, aquele fio de tarde escurecendo, não tinha como ser diferente; e "tinha que" não é desejo, é a leitura de todas as variáveis. Na clínica: se juntar tudo o que veio antes, o comportamento de hoje faz sentido. Agora, como mexer nas variáveis?</p>
<p>Duas leituras a evitar, no paciente e em nós. A <strong>moral</strong> ("o mundo é bom como é", ou ruim como é) vira resignação e conformismo. A <strong>espiritual</strong> ("tudo acontece por um motivo, é destino, é plano") é perigosa, e não há nada na DBT sobre isso: é contingência. A leitura que fica é a <strong>causal e correlacional</strong>. O exemplo: a negligência de uma paciente na infância <em>não deveria ter acontecido</em> (verdade moral, e válida: ninguém deveria passar por uma invalidação daquele tamanho) <em>e aconteceu</em> (verdade que permite a aceitação): dentro daquela mãe, daquela família, daquele contexto, talvez não tivesse como ser diferente; e também não tem como ser diferente o teu sofrimento de hoje, com o que tu trouxe até aqui; e a gente vai juntos buscar possibilidades de lidar com isso.</p>
"""),
        ('s6', 'Habilidades e cuidados', 'Seis habilidades de aceitação e os equívocos comuns', u"""
{{HAB}}
<p>Dos princípios saem seis habilidades que aumentam o senso de liberdade: <strong>aceitação radical</strong> (considerar os princípios para decidir), <strong>redirecionamento</strong> e <strong>estar disposto</strong> (ligados à atenção plena), <strong>meio sorriso</strong>, <strong>mãos dispostas</strong> e <strong>permitir a mente</strong> (postura). A aula lembra a discussão de <em>O erro de Descartes</em> (se emoção, pensamento ou postura vêm primeiro, ainda não se sabe, e todas produzem algo) e um estudo com uma cantora de ópera que, só fazendo o gesto de cantar num ambiente neutro, teve a mesma resposta fisiológica de quando canta. Mudar entonação e postura é uma habilidade para se apoiar no momento.</p>
<p>O módulo tem duas metades. <strong>Sobreviver à crise</strong>: distração, autoacalmar, melhorar o momento, prós e contras, para quando o paciente chega desregulado, com ideação ou autolesão. <strong>Aceitar a realidade</strong>: a postura que fica quando a regulação chega, para o que não vai mudar nunca (a mãe que hoje volta a invalidar). O professor conta que aprendeu com a Andressa: ficava só na primeira metade. Só sobreviver à crise não dá chance de tolerar a emoção e caminhar para a aceitação; e é quando o paciente para de tentar mudar o ambiente que as crises costumam diminuir. Paradoxal, difícil, e é a linha mestra.</p>
<div class='obs'><h4>A ordem e o treino</h4><p>Paciente debulhado, chorando no quarto escuro há três dias sem banho: primeiro regulação; quando a ativação baixa, os princípios. E nenhuma habilidade se aprende na crise, como ninguém aprende a andar de bicicleta no dia da corrida. Treina-se no contexto de calma, ainda que "agora não faça sentido", para que na hora o repertório esteja acessível. Por isso passar por todos os módulos importa: são complementares.</p></div>
{{EQUIV}}
<p>Os equívocos mais comuns da aceitação radical: confundi-la com aceitar o comportamento de risco (valida-se o vazio e o impulso, nunca o ato); a <strong>resignação</strong> ("eu sou assim e pronto", e o professor responde concordando e acrescentando: "e estamos aqui juntos para produzir mudança e te aproximar dos teus valores; qual frase te soa melhor?"), que também é do terapeuta ("ele cansa todo mundo, pronto"); a <strong>autoindulgência</strong> (a paciente que ouviu "essa semana vamos só procrastinar" como aval, quando a proposta era adiar a ruminação sobre a procrastinação e observar o que muda); e a <strong>passividade</strong> ("nem vou tentar, não tenho perfil", que não se invalida: "hoje não tem, e com treino e orientação a gente constrói; como soa?").</p>
"""),
        ('s7', 'Estratégias de mudança', 'Estratégias de mudança: hierarquia, função, cadeia e procedimento', u"""
{{HIER}}
<p>A parte final ficou "no radar" para a aula seguinte, de análise em cadeia. Os processos de mudança acontecem nos módulos; aqui, o desenho geral. Começa pela <strong>hierarquia de alvos</strong>, que não é sugestão: comportamentos que ameaçam a vida primeiro; depois os que interferem na terapia (para quem viveu humilhação e baixa autonomia, o terapeuta também é fonte aversiva desconhecida: vai ter falta, atraso, e o alvo é aqui, comigo, agora, e não intervir na família); depois os que interferem na qualidade de vida (relacionamento, substância, moradia); e só então aumento de habilidades, o projeto de vida. Cada problema é ruim no longo prazo e funciona no curto: por isso a cadeia.</p>
<p><strong>Cada comportamento tem função.</strong> A Camila tem quatro episódios de autolesão com topografia idêntica e função diferente: baixar a emoção (a tensão cai em segundos), sair de uma exigência (no dia seguinte ela não vai, e a demanda afastada reforça), trazer alguém de volta (a pessoa pede desculpa e fica à noite), sentir alguma coisa (no meio da anestesia o corpo volta). Quase toda função cai numa das quatro: reduzir emoção, evitar algo do ambiente, fazer as pessoas não abandonarem, sentir. Olha-se cada episódio pontualmente, naquele dia e hora.</p>
{{PADRAO}}
<p>Com muitas cadeias, o padrão aparece: chefe não responde, amiga cancela, namorado dorme sem avisar; vergonha, leitura de rejeição, isolamento e ruminação para reduzir a dor (que às vezes a aumentam até escalar), autolesão para aliviar. O padrão vai para o papel, volta para o paciente em pergunta ("posso te mostrar o que eu pensei? faz sentido na tua vida?"; ele quase sempre se reconhece), e a gente escolhe o elo juntos: onde é mais acessível, com desconforto tolerável. Se está no alvo mais alto, a escolha já vem amarrada ("onde tu acha que dá para mexer no cuidado com a tua vida essa semana?"); "queria melhorar meu namoro" não é por onde se começa quando há autolesão. O elo do meio é onde a intervenção cabe: o ambiente muda toda hora e o viés atencional não vê; o elo cognitivo, o isolamento, o apego, o baixo senso de impermanência, sim.</p>
<p>Gera-se várias soluções para o elo, e nem toda opção do paciente serve: ligar para a psicóloga (longe; coach telefônico é delimitado), para a amiga (longe, trabalha demais), para a mãe (ambiente invalidante, reforça o sofrimento). Avalia-se acesso e se o ambiente não será mais aversivo ainda. Aí ensaia-se na sessão (tolerância ao mal-estar, efetividade interpessoal, plano de segurança), antecipa-se o que pode dar errado, e combina-se como experimento curto, até semana que vem, sem expectativa altíssima para quem já vive sob pressão. Seis soluções do exemplo: checar os fatos (excluir que foi rejeição), ação oposta à vergonha (ficar na sala em vez de ir para o quarto), ligar para a irmã que sempre atende, mandar mensagem em vez de esperar, autoacalmar por vinte minutos e reavaliar, coach telefônico. Tudo isso pode constar no plano de segurança quando há autolesão.</p>
{{QUATRO}}
<p>Toda solução entra numa das <strong>quatro categorias operacionais</strong>: treinamento de habilidades (nos quatro módulos; costuma ser o começo, para quem chega sem repertório), modificação cognitiva (para quem sabe racionalmente e emocionalmente não consegue; a tolerância ao mal-estar prepara), manejo de contingências (o mais difícil de início, quando o ambiente tem pouca variação e mais punição que reforço; o objetivo é chegar a qualidade de vida e habilidades para conseguir manejá-lo) e exposição (à vergonha, à culpa, a ser vista como ruim; tolerância, mindfulness e regulação entram como exposição e controle de estímulo). Três pré-requisitos: psicoeducação, devolutiva da formulação e análise em cadeia feita; sem isso, qualquer orientação vira ordem, e com esses pacientes ordem não funciona (reatância). E não esperar que a solução venha pronta: mais provável é que os comportamentos que interferem na terapia (não trazer feito) voltem a interagir, e aí se volta ao alvo dois e ao comprometimento.</p>
<div class='callout note'><div class='co-t'>Flexibilidade na fidelidade</div>Linehan não diz que se faz uma coisa de cada vez. Se estou em qualidade de vida e há recaída em interferir na terapia, volto. Se estou em interferir na terapia e o paciente se cortou na quinta, deixo o resto e vou para a cadeia da quinta. Se chega sem disposição, paro a solução e volto ao comprometimento. Se dissocia, paro tudo e foco na dissociação. E a demanda de última hora, o incêndio, quase sempre já está em alguma cadeia feita: pego a demanda e volto ao padrão. É assim que se gera comprometimento: focando no que aconteceu, sem ser sequestrado.</div>
<h3>Treinar com simulação</h3>
<p>A aula fecha com a sugestão de treinar com inteligência artificial: pedir uma simulação de caso, "avalie meu atendimento a partir dos princípios da DBT", e receber devolutiva ("aqui chegou numa validação cinco, aqui foi três e não teve mudança"). O erro que apareceu nos treinos do professor e de uma colega foi o mesmo: os dois validam bem, e quando chega o lado da mudança, ou o paciente traz algo emocional, surge o professor e a gente começa a explicar. É o modo explicativo e diretivo que a aula inteira ensina a segurar. E a orientação final para a turma: pegar um paciente, abrir mais a curiosidade, explicar levemente impermanência e apego se não estiver em crise, e trazer o que travou para o grupo. É uma árvore de decisão grande, e tem fim.</p>
"""),
    ],
    'checklist': [
        'Na sessão, contei quantas afirmações fiz que não eram descrição do que o paciente disse, e troquei por pergunta.',
        'Devolvi o que entendi com "entendi certo?" antes de qualquer outra coisa.',
        'Tirei o "mas" das devolutivas e usei "e" mais pedido de permissão para propor.',
        'Antes de sugerir algo, coletei a função ("como é para ti quando...") e validei.',
        'Passei pelos seis níveis com ao menos um relato: silêncio, descrever, o não dito, história, presente, genuinidade.',
        'Validei desejo, emoção e contexto, e deixei o comportamento nocivo em pergunta.',
        'Quando o paciente chorou, perguntei "o que está acontecendo aqui agora entre nós" em vez de apaziguar.',
        'Reconstruí uma crise hora a hora com o paciente e mostrei a curva.',
        'Tratei atraso, silêncio e distância como dado clínico, e perguntei pela função.',
        'Conferi se a minha impaciência veio antes do paciente (sono, dia, agenda).',
        'Fiz um passo de mudança na mesma sessão em que validei, para não escorregar para a resignação.',
        'Escolhi o alvo pela hierarquia e o elo pela acessibilidade, junto com o paciente.',
    ],
    'questoes': [
        'Diferencie aceitação de resignação e explique por que a aula insiste em "aceitação, validação e um passo de mudança" na mesma sessão.',
        'Por que "pergunta, não afirmação" é a mudança mais barata da aula? Reescreva "mas tu concordou com o plano" em três perguntas.',
        'Liste os oito modos de invalidar e explique, com o exemplo da supervisão, o que o "mas" faz com a atenção de quem ouve.',
        'O que é reatância, em que pacientes ela é mais provável, e qual é a ordem (função, validação, permissão, proposta aberta) que a evita?',
        'Aplique os seis níveis de validação a um relato sem emoção explícita de um paciente teu.',
        'Escolha dois dos cinco princípios e descreva a armadilha do terapeuta em cada um, com um exemplo da tua clínica.',
        'Explique a hierarquia de alvos e por que o elo do meio é onde a intervenção cabe. Use o padrão das três cadeias.',
        'O que é flexibilidade na fidelidade? Dê um exemplo em que tu interromperia a solução em curso.',
    ],
    'gabarito': {
     0: (C, u"Resignação é fechar a porta: \"eu desisto, não vou mudar, aceito o mundo e deu\". Aceitação aceita o que aconteceu e o que está acontecendo e pergunta o que, dentro do contexto e das habilidades, ainda dá para mudar; sempre abre. A aula insiste nos três juntos porque só validação e só aceitação levam o paciente (e o terapeuta) à resignação; um pequeno passo de mudança por sessão é o que mantém a porta aberta."),
     1: (C, u"Porque não exige técnica nova, só trocar o modo da frase, e porque afirmação é onde moram argumentação, moralização, desaprovação e julgamento; pergunta é onde mora a curiosidade e dá ao paciente uma autonomia que ele não tem lá fora. Por exemplo: \"tu quase não veio, e veio; como foi decidir vir?\", \"o que teve no meio entre uma sessão e outra?\", \"ficou pesado demais? onde doeu?\"."),
     2: (C, u"Argumentação, moralização, desaprovação, estigmatização, advertência, ironia, análise inoportuna e o \"mas\". No exemplo (\"tu tens um bom raciocínio, a condução tá boa, mas se tu focar mais no monitoramento...\"), o \"mas\" apaga a primeira parte e leva a atenção para a falta (\"falta algo em mim\"), como ameaça; o ouvinte não processa o resto. Com \"e\" e pedido de permissão, a frase inteira é lida e a esperança fica de pé."),
     3: (C, u"Reatância é o modo opositor que aparece quando o terapeuta dá ou fala o que o paciente poderia alcançar sozinho, ameaçando a pouca autonomia que ele tem; mais provável em quem tem histórico de humilhação, invalidação e baixa autonomia. A ordem: coletar a função de forma neutra (\"como é para ti quando bebe?\"), validar (\"faz sentido; talvez eu fizesse o mesmo\"), pedir permissão (\"tem algo que já funcionou; posso te propor?\") e propor em aberto (\"essa é uma, tem outras; qual te parece?\")."),
     4: (K, u"Não há resposta certa. Uma boa resposta parte de um relato que descreve situação sem nomear emoção, e percorre: silêncio atento (sem interromper, sem comentário sobre o estímulo), descrição (\"entendi: aconteceu X e tu ficou Y\"), leitura do não dito abrindo para o paciente nomear antes de nomear por ele, validação pela história (ligada à formulação), validação pelo presente (o que a maioria sentiria) e genuinidade (autorrevelação de experiência ou de não ter passado por aquilo). O erro comum é pular o silêncio e ir direto à explicação."),
     5: (K, u"Não há resposta certa. Uma boa resposta nomeia a armadilha de cada princípio escolhido (momento presente: apaziguar a dor do paciente por causa da minha; desapego: querer reduzir sintoma rápido e virar bombeiro; interexistência: ler atraso como ataque pessoal, ou levar para a sessão a impaciência do meu dia; impermanência: fugir cedo e ensinar a não tolerar; mundo perfeito: deslizar para leitura moral ou espiritual) e traz um momento real em que ela apareceu. O erro comum é descrever o princípio para o paciente e não para si."),
     6: (C, u"Vida, terapia, qualidade de vida, habilidades, nessa ordem e sem ser sugestão. O elo do meio (vergonha, leitura de rejeição, isolamento e ruminação) é onde a intervenção cabe porque o ambiente (chefe, amiga, namorado) muda toda hora e o viés atencional não vê; o cognitivo, o isolamento, o apego e o baixo senso de impermanência são acessíveis. Nas três cadeias, situações diferentes passam pelo mesmo meio e chegam ao mesmo fim; o plano de segurança corta entre a ruminação e o ato."),
     7: (C, u"É alterar o módulo e o alvo conforme o paciente apresenta algo mais urgente ligado a um alvo acima, sem abandonar o protocolo: se estou em qualidade de vida e há recaída em interferir na terapia, volto; se estou trabalhando interferência na terapia e ele se cortou na quinta, vou para a cadeia da quinta; se chega sem disposição, paro a solução e volto ao comprometimento; se dissocia, paro tudo e foco na dissociação. Exemplo aceitável: qualquer um desses com um paciente real."),
    },
    'referencias': [
        "Damásio, A. R. (2012). <em>O erro de Descartes: Emoção, razão e o cérebro humano.</em> Companhia das Letras.",
        "Koerner, K. (2012). <em>Doing dialectical behavior therapy: A practical guide.</em> Guilford Press.",
        "Linehan, M. M. (1993). <em>Cognitive-behavioral treatment of borderline personality disorder.</em> Guilford Press.",
        "Linehan, M. M. (1997). Validation and psychotherapy. In A. C. Bohart &amp; L. S. Greenberg (Eds.), <em>Empathy reconsidered: New directions in psychotherapy</em> (pp. 353–392). American Psychological Association.",
        "Linehan, M. M. (2015). <em>DBT skills training manual</em> (2nd ed.). Guilford Press.",
    ],
    'nota': u"""Material dirigido a psicólogos, feito da transcrição completa da aula de 12/09/2026 do curso Descomplicando a DBT (Júlio Gonçalves e Andressa Juliana), com apoio das anotações automáticas da reunião. A aula anterior tratou de plano de tratamento e formulação; a seguinte, de análise em cadeia, para onde a parte final desta foi deixada "no radar".<br><br><strong>O que é da aula e o que é do material.</strong> Os exemplos, as frases de paciente e de terapeuta, os cinco princípios, os seis níveis, as seis habilidades, a hierarquia, as quatro funções, as três cadeias e os três percursos são da aula. As figuras foram construídas a partir da fala, e não de slides (o material não teve acesso aos slides). As posições dos elementos e os títulos das figuras são do autor do material. A intervenção de uma participante sobre quem nomeia a emoção foi incorporada sem identificação.<br><br><strong>Fontes.</strong> A definição de aceitação em três níveis é atribuída na aula a \"Struck\", nome como consta na transcrição, que não pôde ser conferido; o material a apresenta como a aula a apresenta. Os estudos citados de passagem (termos negativos e percepção do processo; estilo do terapeuta e prognóstico; a cantora de ópera) não foram identificados e ficaram sem referência, com a ressalva do próprio professor de que são complemento e não DBT. Os seis níveis de validação e a hierarquia de alvos seguem Linehan (1993, 1997); os princípios e as habilidades de aceitação estão no manual de habilidades (2015). O exemplo do acidente com a criança, que a aula credita a Linehan, foi mantido sem detalhe.<br><br><strong>Segurança.</strong> A autolesão aparece como exemplo de análise funcional e de plano de segurança, sem qualquer descrição de método. O exemplo do álcool foi mantido como a aula o usa: validação do desejo, não do comportamento.<br><br>Nenhuma citação foi construída para preencher lacuna.""",
}

_FIGS = {'ACEIT': ACEIT, 'PERG': PERG, 'MODOS': MODOS, 'MAS_E': MAS_E, 'REAT': REAT, 'NIVEIS': NIVEIS, 'VALIDAR': VALIDAR,
         'PRINC': PRINC, 'HORA': HORA, 'LOMB': LOMB, 'HIER': HIER, 'PADRAO': PADRAO, 'QUATRO': QUATRO, 'HAB': HAB, 'EQUIV': EQUIV}
DBT['secoes'] = [(sid, nav, tit, re.sub(r'\{\{(\w+)\}\}', lambda m: _FIGS[m.group(1)], corpo))
                 for sid, nav, tit, corpo in DBT['secoes']]

if __name__ == '__main__':
    import os
    SITE = '/home/claude/site'
    base = io.open(SITE + '/aulas/transdiagnostico-substancias/index.html', encoding='utf-8').read()
    dest = SITE + '/aulas/' + DBT['slug']
    os.makedirs(dest, exist_ok=True)
    io.open(dest + '/index.html', 'w', encoding='utf-8').write(pagina_aula(DBT, base))
    c = sup_common.pdf(DBT)
    c['kicker'] = 'RESUMO DE AULA &middot; AULA LIVRE'
    c['gabarito'] = DBT['gabarito']
    gen_resumo.gerar(c, dest + '/resumo.pdf')
    import pymupdf
    d = pymupdf.open(dest + '/resumo.pdf')
    print('página e PDF gerados: %d páginas, %.0f KB' % (d.page_count, os.path.getsize(dest + '/resumo.pdf') / 1024))
