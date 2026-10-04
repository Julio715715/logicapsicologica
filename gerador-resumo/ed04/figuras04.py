# -*- coding: utf-8 -*-
"""Figuras SVG da Edição 4 (molde Bagual: viewBox 720 x 190-240, Plus Jakarta Sans)."""
import io, os
F = "font-family='Plus Jakarta Sans,sans-serif'"
OL, OL2, GILT, TERRA, TINTA, MUDO, CINZA = '#3d411f', '#5a5e2e', '#bcae56', '#a05a3c', '#2f2e24', '#6c6a55', '#c9c2a8'
AQUI = os.path.dirname(os.path.abspath(__file__))


def t(x, y, s, size=12, fill=TINTA, w='', anchor='start', extra=''):
    return "<text x='%s' y='%s' text-anchor='%s' %s font-size='%s'%s fill='%s'%s>%s</text>" % (
        x, y, anchor, F, size, (" font-weight='%s'" % w) if w else '', fill, extra, s)


# Figura 1: o que a evidência comparou (tamanhos de efeito com IC) e onde o projeto está
def fig1():
    # escala: 0 em x=250, 1,0 em x=550 (300 px por unidade)
    def X(v): return 250 + v * 300
    s = ["<svg viewBox='0 0 720 236' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Dois tamanhos de efeito: não especialista contra profissional, 0,09, intervalo cruzando o zero; não especialista contra controle, 0,49, intervalo de 0,36 a 0,62. Abaixo, o caminho do PL 2.386 no Congresso.'>",
         t(20, 26, 'O QUE A EVIDÊNCIA COMPAROU', 11, GILT, 800, extra=" letter-spacing='1.4'"),
         "<line x1='%s' y1='40' x2='%s' y2='130' stroke='%s' stroke-width='1' stroke-dasharray='3 3'/>" % (X(0), X(0), CINZA),
         t(X(0), 146, 'efeito zero', 10, MUDO, anchor='middle'),
         t(X(1), 146, 'g = 1,0', 10, MUDO, anchor='middle'),
         # linha 1: Cochrane
         t(20, 66, 'Não especialista × profissional', 12.5, TINTA, 800),
         t(20, 82, 'Cochrane, 5 estudos, 106 pessoas', 10.5, MUDO),
         "<line x1='%s' y1='70' x2='%s' y2='70' stroke='%s' stroke-width='3' stroke-linecap='round'/>" % (X(-0.23), X(0.40), CINZA),
         "<circle cx='%s' cy='70' r='6' fill='%s'/>" % (X(0.09), TERRA),
         t(X(0.40) + 12, 74, 'SMD 0,09 (IC −0,23 a 0,40)', 11, TERRA, 800),
         # linha 2: Singla
         t(20, 112, 'Não especialista × controle', 12.5, TINTA, 800),
         t(20, 128, '27 ensaios, países de renda baixa e média', 10.5, MUDO),
         "<line x1='%s' y1='116' x2='%s' y2='116' stroke='%s' stroke-width='3' stroke-linecap='round'/>" % (X(0.36), X(0.62), CINZA),
         "<circle cx='%s' cy='116' r='6' fill='%s'/>" % (X(0.49), OL2),
         t(X(0.62) + 12, 120, 'g 0,49 (IC 0,36 a 0,62)', 11, OL2, 800),
         # trilha do PL
         "<rect x='20' y='166' width='680' height='52' rx='8' fill='#efe7d3'/>",
         t(36, 186, 'PL 2.386/2023 · ONDE ESTÁ', 10.5, GILT, 800, extra=" letter-spacing='1.2'"),
         ]
    etapas = [('Comissão de Saúde', True), ('CCJ', False), ('Plenário da Câmara', False), ('Senado', False), ('Sanção', False)]
    x = 36
    for i, (n, on) in enumerate(etapas):
        s.append("<circle cx='%d' cy='204' r='5' fill='%s'/>" % (x + 5, TERRA if on else CINZA))
        s.append(t(x + 16, 208, n, 11, TINTA if on else MUDO, 800 if on else ''))
        x += 150 if i == 0 else 120
    s.append(t(690, 186, 'relatório de maio de 2026, aguarda votação', 10, MUDO, anchor='end'))
    s.append('</svg>')
    return '\n'.join(s)


# Figura 2: oferta de sites ilegais: pedidos, bloqueados, novos numa semana
def fig2():
    dados = [('5.209', 'domínios com pedido de derrubada', 5209, OL2),
             ('2.387', 'já bloqueados pela Anatel', 2387, OL),
             ('6.401', 'sites ilegais novos entre 22 e 28 de setembro', 6401, TERRA)]
    mx = 6401.0
    s = ["<svg viewBox='0 0 720 220' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Três barras: 5.209 domínios com pedido de derrubada, 2.387 bloqueados pela Anatel e 6.401 sites ilegais novos numa semana.'>",
         t(20, 26, 'A OFERTA, EM SITES', 11, GILT, 800, extra=" letter-spacing='1.4'")]
    y = 48
    for n, rot, v, cor in dados:
        w = int(300 * v / mx)
        s.append("<rect x='120' y='%d' width='%d' height='22' rx='5' fill='%s'/>" % (y, w, cor))
        s.append(t(110, y + 16, n, 15, cor, 800, anchor='end'))
        s.append(t(128 + w, y + 15, rot, 11, TINTA))
        y += 40
    s.append("<rect x='20' y='172' width='680' height='36' rx='8' fill='#efe7d3'/>")
    s.append(t(36, 195, 'Pico: 3.094 endereços novos num só dia, logo depois do anúncio da MP. Dado de oferta (quantos sites), não de demanda (quantos apostam).', 10.5, MUDO))
    s.append('</svg>')
    return '\n'.join(s)


# Figura 3: o que a lei alcança e o que o paciente usa
def fig3():
    def caixa(x, n, l1, l2, cor='#efe7d3', tcor=OL):
        return ("<rect x='%d' y='44' width='150' height='96' rx='8' fill='%s'/>" % (x, cor)
                + t(x + 75, 92, n, 26, tcor, 800, anchor='middle')
                + t(x + 75, 114, l1, 10.5, TINTA, anchor='middle')
                + t(x + 75, 128, l2, 10.5, TINTA, anchor='middle'))
    s = ["<svg viewBox='0 0 720 258' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Quatro números: 19 por cento dos jovens pediram conselho a um chatbot, 63 por cento não contaram a ninguém, 28 intervenções humanas no ensaio do Therabot, e 0,15 por cento dos usuários semanais do ChatGPT com sinais de ideação suicida. Abaixo: o projeto de lei alcança pessoas, não aplicativos.'>",
         t(20, 26, 'O QUE O PACIENTE JÁ USA', 11, GILT, 800, extra=" letter-spacing='1.4'"),
         caixa(20, '19%', 'dos 12 a 21 anos pediram', 'conselho a um chatbot'),
         caixa(190, '63%', 'desses, não contaram', 'a ninguém', '#f7ede7', TERRA),
         caixa(360, '28', 'intervenções humanas', 'em 8 semanas de Therabot'),
         caixa(530, '0,15%', 'dos usuários semanais com', 'sinais de ideação suicida', '#f7ede7', TERRA),
         "<rect x='20' y='160' width='680' height='84' rx='8' fill='%s'/>" % OL,
         t(36, 182, 'O PL 2.386 ALCANÇA', 10.5, GILT, 800, extra=" letter-spacing='1.2'"),
         t(200, 182, 'o coach, o terapeuta holístico, quem cobra por “psicoterapia” sem registro.', 12, '#f8f3e6'),
         t(36, 222, 'NÃO ALCANÇA', 10.5, GILT, 800, extra=" letter-spacing='1.2'"),
         t(200, 222, 'o aplicativo que a tua paciente abre às 2 da manhã.', 12, '#f8f3e6', 800),
         '</svg>']
    return '\n'.join(s)


if __name__ == '__main__':
    for n, f in [('figura1.svg', fig1), ('figura2.svg', fig2), ('figura3.svg', fig3)]:
        io.open(os.path.join(AQUI, n), 'w', encoding='utf-8').write(f())
        print(n)
