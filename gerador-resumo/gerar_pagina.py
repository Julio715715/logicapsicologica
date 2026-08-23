#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera a página web de um encontro (processos/capN/index.html) a partir do mesmo
JSON usado no PDF, reaproveitando o <head> e o CSS de uma página já existente.

Uso:  python3 gerar_pagina.py conteudo/cap5.json modelo/index.html saida/index.html
"""

import html as H
import json, re, sys, unicodedata
from pathlib import Path


def slug(txt):
    t = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode()
    t = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-")
    return "-".join(p.capitalize() for p in t.split("-"))[:40]


def svg_fluxo(bloco):
    """três caixas ligadas por setas, no mesmo desenho do cap. 4"""
    passos, larg, gap = bloco["v"], 213.3, 30.0
    partes = [
        "<svg viewBox='0 0 720 132' xmlns='http://www.w3.org/2000/svg' role='img' "
        f"aria-label='{H.escape(bloco['rotulo'])}'><defs>"
        "<marker id='ar5' markerWidth='9' markerHeight='9' refX='7' refY='3' orient='auto'>"
        "<path d='M0,0 L0,6 L7,3 z' fill='#a8894f'/></marker></defs>"
    ]
    x = 10.0
    centros = []
    for i, p in enumerate(passos):
        if i:
            partes.append(f"<line x1='{x-gap+4:.1f}' y1='66' x2='{x-4:.1f}' y2='66' "
                          "stroke='#c3a468' stroke-width='1.6' marker-end='url(#ar5)'/>")
        cx = x + larg / 2
        centros.append(cx)
        partes.append(f"<rect x='{x:.1f}' y='24' width='{larg:.1f}' height='84' rx='12' "
                      "fill='#fffdf7' stroke='#9ca575' stroke-width='1.4'/>")
        partes.append(f"<text x='{cx:.1f}' y='48' text-anchor='middle' "
                      "font-family='Plus Jakarta Sans,sans-serif' font-size='10.5' "
                      "font-weight='800' letter-spacing='1.4' fill='#a8894f'>"
                      f"{H.escape(p['rotulo'])}</text>")
        linhas = quebra(p["texto"], 27)[:3]
        y0 = 70 if len(linhas) < 3 else 64
        for j, ln in enumerate(linhas):
            partes.append(f"<text x='{cx:.1f}' y='{y0 + j*16}' text-anchor='middle' "
                          "font-family='Plus Jakarta Sans,sans-serif' font-size='12' "
                          f"fill='#2f2e24'>{H.escape(ln)}</text>")
        x += larg + gap
    if bloco.get("ciclo"):
        partes.append(f"<path d='M{centros[-1]:.1f} 112 C{centros[-1]:.1f} 126, "
                      f"{centros[0]:.1f} 126, {centros[0]:.1f} 112' fill='none' stroke='#c3a468' "
                      "stroke-width='1.6' stroke-dasharray='4 4' marker-end='url(#ar5)'/>")
    partes.append("</svg>")
    return "".join(partes)


def quebra(txt, largura):
    linhas, atual = [], ""
    for pal in txt.split():
        if len(atual) + len(pal) + 1 > largura and atual:
            linhas.append(atual); atual = pal
        else:
            atual = (atual + " " + pal).strip()
    if atual:
        linhas.append(atual)
    return linhas


def corpo(d):
    """converte os blocos do JSON no HTML da página, abrindo uma <details> por h2"""
    saida, secoes, aberta, n = [], [], False, 0
    for b in d["blocos"]:
        t = b["t"]
        if t == "h2":
            if aberta:
                saida.append("</details>")
            atrib = " open" if n == 0 else ""
            saida.append(f"<details class='sec' id='s{n}'{atrib}><summary>"
                         f"<h2>{b['v']}</h2><span class='arw'>&#9656;</span></summary>")
            secoes.append((f"s{n}", b["v"]))
            aberta = True
            n += 1
        elif t == "h3":
            saida.append(f"<h3>{b['v']}</h3>")
        elif t == "p":
            saida.append(f"<p>{b['v']}</p>")
        elif t == "lista":
            itens = "".join(f"<li>{x}</li>" for x in b["v"])
            saida.append(f"<ul class='key'>{itens}</ul>")
        elif t == "callout":
            saida.append(f"<div class='callout note'><div class='co-t'>{b['rotulo']}</div>"
                         f"{b['v']}</div>")
        elif t == "cards":
            ds = "".join(f"<div class='d'><div class='dt'>{c['rotulo'].capitalize()}</div>"
                         f"<p>{c['texto']}</p></div>" for c in b["v"])
            saida.append(f"<div class='dial'>{ds}</div>")
        elif t == "fluxo":
            saida.append(f"<figure class='dg'><div class='dg-t'>{b['rotulo'].capitalize()}</div>"
                         f"{svg_fluxo(b)}<figcaption>{b['legenda']}</figcaption></figure>")
    if aberta:
        saida.append("</details>")
    # tags <b>/<i> do JSON viram <strong>/<em> na página
    corpo_html = "".join(saida)
    for de, para in (("<b>", "<strong>"), ("</b>", "</strong>"),
                     ("<i>", "<em>"), ("</i>", "</em>")):
        corpo_html = corpo_html.replace(de, para)
    return corpo_html, secoes


def montar(json_path, modelo_path, saida_path):
    d = json.loads(Path(json_path).read_text(encoding="utf-8"))
    modelo = Path(modelo_path).read_text(encoding="utf-8")
    cabeca = modelo.split("</style>", 1)[0] + "</style>"
    cabeca = re.sub(r"<title>.*?</title>",
                    f"<title>{d['titulo']} — Lógica Psicológica</title>", cabeca)

    conteudo, secoes = corpo(d)
    apelido = d.get("slug") or slug(d["titulo"])
    chave = f"mat-Proc{d['numero']}-{apelido}-"

    idx = "".join(f"<a href='#{i}'>{t}</a>" for i, t in secoes)
    ess = "".join(f"<li>{x}</li>" for x in d["essencial"]) \
        .replace("<b>", "<strong>").replace("</b>", "</strong>") \
        .replace("<i>", "<em>").replace("</i>", "</em>")
    chk = "".join("<label class='ck'><input type='checkbox'>"
                  f"<span>{x}</span></label>" for x in d["checklist"])
    qz = "".join(f"<div class='qz'><p>{i+1}. {q}</p>"
                 "<textarea placeholder='Sua resposta…'></textarea></div>"
                 for i, q in enumerate(d["perguntas"]))
    refs = "".join(f"<li>{r}</li>" for r in d["referencias"]) \
        .replace("<i>", "<em>").replace("</i>", "</em>")
    nmet = d["nota_metodo"].replace("<b>", "<strong>").replace("</b>", "</strong>") \
        .replace("<i>", "<em>").replace("</i>", "</em>")
    meta = d.get("meta_pagina") or d["meta_capa"]
    meta = meta.replace("<i>", "<em>").replace("</i>", "</em>")

    body = f"""</head><body><div class='topbar'><div class='in'><a href='/'><img alt='Lógica Psicológica' src='/assets/logo.png'></a><a class='backlink' href='/processos/' title='Voltar para Encontros'>&#8592; Voltar</a><div class='sp'></div><div class='tag'>Jornada da Leitura</div></div></div><div class='shell'><aside class='side' id='side'><a class='brand' href='/'><img alt='Lógica Psicológica' src='/assets/logo-creme.png'></a><div class='nav'><div class='st first'>Navegação</div><a class='home' href='/processos/'>&#8592; Encontros</a><a class='navlink' href='/'>Início do portal</a><div class='st'>Neste material</div><div class='idx'>{idx}</div></div><div class='sig'><img alt='Prof. Júlio Gonçalves' src='/assets/julio.jpg'><div class='who'>Prof. Júlio Gonçalves<span>MSc · CRP 12/17614</span></div></div><a class='sub' href='https://psicojulio.com/comunidade-logica-psicologica/' target='_blank' rel='noopener'>Inscreva-se</a></aside><main class='main'><div class='mhero'><div class='kick'>Resumo de aula · Jornada da Leitura</div><h1>{d['titulo']}</h1><div class='sub'>Capítulo {d['numero']}</div><div class='meta'>{meta}</div><p class='tema'>{d['subtitulo']}</p></div><div class='usar'><b>Como usar</b>Abra as seções que quiser ler, marque o que pretende aplicar e responda o que fizer sentido. Tudo fica salvo neste aparelho — ninguém mais vê.</div><a class='pdfbtn' href='resumo.pdf'>&#8681; Baixar em PDF</a><div class='ess'><div class='et'>O essencial</div><ul>{ess}</ul></div>{conteudo}<div class='tools'><div class='tool'><div class='tt'>Levar para a prática</div>{chk}</div><div class='tool'><div class='tt'>Para revisar — responda</div>{qz}</div></div><div class='savebar'><button id='exp'>Exportar respostas</button><button id='lmp'>Limpar</button><span class='saved' id='saved'>Salvo neste aparelho</span></div><div class='refs'><h2>Referências</h2><ol>{refs}</ol></div><div class='nmet'><b>Nota de método</b>{nmet}</div><div class='cta'><img class='ph' alt='Prof. Júlio Gonçalves' src='/assets/julio.jpg'><div class='in'><div class='k'>Aprenda muito mais na</div><h3>Comunidade Lógica Psicológica</h3><ul><li>Aprofundar o raciocínio clínico com ciência, processos e análise funcional.</li><li>Estruturar uma prática ética, com pensamento crítico e evidências atualizadas.</li><li>Desenvolver o self clínico com supervisão, leituras guiadas e rede.</li></ul><a class='go' href='https://psicojulio.com/comunidade-logica-psicologica/' target='_blank' rel='noopener'>Participar da comunidade &#8594;</a></div></div><div class='foot'><img class='foot-logo' alt='Lógica Psicológica' src='/assets/logo.png'><div class='contato'><a href='mailto:contato@psicojulio.com'>contato@psicojulio.com</a> &middot; <a href='tel:+5547999338021'>(47) 99933-8021</a><br>Rua Concórdia, 703, São Vicente, Itajaí — 88309-645<br><span class='cnpj'>CNPJ 49.649.803/0001-60</span></div></div></main></div><button class='toc-fab' id='fab'>&#9776; Seções</button><div class='overlay' id='ov'></div><script>
(function(){{
  var K='{chave}';
  document.querySelectorAll('.ck input').forEach(function(c,i){{
    var k=K+'ck'+i;
    try{{ if(localStorage.getItem(k)==='1'){{c.checked=true;c.closest('.ck').classList.add('done');}} }}catch(e){{}}
    c.addEventListener('change',function(){{
      c.closest('.ck').classList.toggle('done',c.checked);
      try{{ localStorage.setItem(k,c.checked?'1':'0'); }}catch(e){{}} flag();
    }});
  }});
  document.querySelectorAll('.qz textarea').forEach(function(t,i){{
    var k=K+'q'+i;
    try{{ var v=localStorage.getItem(k); if(v)t.value=v; }}catch(e){{}}
    t.addEventListener('input',function(){{ try{{ localStorage.setItem(k,t.value); }}catch(e){{}} flag(); }});
  }});
  var s=document.getElementById('saved'),tm;
  function flag(){{ if(!s)return; s.classList.add('on'); clearTimeout(tm); tm=setTimeout(function(){{s.classList.remove('on');}},1600); }}
  var b=document.getElementById('exp');
  if(b) b.addEventListener('click',function(){{
    var out='RESPOSTAS — {d["titulo"]}\\n\\n';
    document.querySelectorAll('.qz').forEach(function(q){{
      out+= q.querySelector('p').innerText+'\\n'+(q.querySelector('textarea').value||'(sem resposta)')+'\\n\\n';
    }});
    var a=document.createElement('a');
    a.href=URL.createObjectURL(new Blob([out],{{type:'text/plain'}}));
    a.download='{apelido}-respostas.txt'; a.click();
  }});
  var l=document.getElementById('lmp');
  if(l) l.addEventListener('click',function(){{
    if(!confirm('Apagar suas anotações deste material?'))return;
    try{{ Object.keys(localStorage).filter(function(k){{return k.indexOf(K)===0;}}).forEach(function(k){{localStorage.removeItem(k);}}); }}catch(e){{}}
    location.reload();
  }});
  var f=document.getElementById('fab'),o=document.getElementById('ov'),sd=document.getElementById('side');
  if(f)f.onclick=function(){{sd.classList.toggle('open');o.classList.toggle('open');}};
  if(o)o.onclick=function(){{sd.classList.remove('open');o.classList.remove('open');}};
}})();
</script></body></html>
"""
    Path(saida_path).parent.mkdir(parents=True, exist_ok=True)
    Path(saida_path).write_text(cabeca + body, encoding="utf-8")
    return saida_path, len(secoes)


if __name__ == "__main__":
    caminho, n = montar(sys.argv[1], sys.argv[2], sys.argv[3])
    print(f"gerado: {caminho} ({n} seções)")
