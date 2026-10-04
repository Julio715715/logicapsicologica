# -*- coding: utf-8 -*-
"""Ilustração da Ed. 4: placa de porta 'Psicoterapia' com o campo do registro em branco."""
import io, os, shutil, subprocess, time
from playwright.sync_api import sync_playwright
AQUI = os.path.dirname(os.path.abspath(__file__))
FONTES = '/home/claude/bagual/modelo-jornal-bagual/fontes'
W = '/home/claude/tabloidework/ilu4'
if os.path.exists(W): shutil.rmtree(W)
os.makedirs(W + '/f')
for f in os.listdir(FONTES):
    shutil.copy(os.path.join(FONTES, f), W + '/f/' + f)
css_f = """
@font-face{font-family:'Jak';src:url('f/plus-jakarta-sans-latin-800-normal.woff2');font-weight:800;}
@font-face{font-family:'Jak';src:url('f/plus-jakarta-sans-latin-500-normal.woff2');font-weight:500;}
@font-face{font-family:'Play';src:url('f/playfair-display-latin-700-normal.woff2');font-weight:700;}
"""
html = u"""<!doctype html><meta charset='utf-8'><style>%s
body{margin:0;width:660px;height:580px;overflow:hidden;background:#2F2E24;font-family:'Jak',sans-serif;position:relative;}
.wall{position:absolute;inset:0;background:linear-gradient(160deg,#3a3930,#23221b);}
.door{position:absolute;left:90px;top:-40px;width:480px;height:700px;background:linear-gradient(90deg,#43441F,#383a18 60%%,#2f3014);border:6px solid #1f2010;box-shadow:inset 0 0 60px rgba(0,0,0,.4);}
.panel{position:absolute;left:40px;right:40px;top:70px;height:430px;border:3px solid rgba(248,243,230,.12);}
.plate{position:absolute;left:135px;top:190px;width:390px;height:150px;background:linear-gradient(135deg,#d9c77a,#bcae56 50%%,#a8964a);border-radius:6px;box-shadow:0 10px 30px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.5);padding:26px 28px;box-sizing:border-box;color:#2a2a16;}
.plate .k{font-size:11px;letter-spacing:.3em;font-weight:800;opacity:.8;}
.plate .n{font-family:'Play',serif;font-size:40px;font-weight:700;letter-spacing:.02em;margin-top:6px;line-height:1;}
.plate .crp{margin-top:18px;font-size:14px;font-weight:800;letter-spacing:.14em;display:flex;align-items:baseline;gap:10px;}
.plate .crp span{display:inline-block;width:180px;border-bottom:2px solid #2a2a16;height:14px;}
.screw{position:absolute;width:10px;height:10px;border-radius:50%%;background:#6b5e2a;box-shadow:inset 0 1px 2px rgba(255,255,255,.6);}
.knob{position:absolute;left:520px;top:400px;width:34px;height:34px;border-radius:50%%;background:radial-gradient(circle at 35%% 35%%,#e2d08a,#8f7c35);box-shadow:0 4px 10px rgba(0,0,0,.5);}
</style><div class='wall'></div><div class='door'><div class='panel'></div></div>
<div class='plate'><div class='screw' style='left:8px;top:8px'></div><div class='screw' style='right:8px;top:8px'></div><div class='screw' style='left:8px;bottom:8px'></div><div class='screw' style='right:8px;bottom:8px'></div>
<div class='k'>CONSULTÓRIO</div><div class='n'>Psicoterapia</div><div class='crp'>CRP <span></span></div></div><div class='knob'></div>""" % css_f
io.open(W + '/i.html', 'w', encoding='utf-8').write(html)
srv = subprocess.Popen(['python3', '-m', 'http.server', '8983', '-d', W], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 660, 'height': 580}, device_scale_factor=2)
        pg.goto('http://localhost:8983/i.html'); pg.wait_for_timeout(900)
        pg.screenshot(path=os.path.join(AQUI, 'capa.png')); b.close()
finally:
    srv.terminate()
print('capa.png')
