# Portal de resumos — Lógica Psicológica
## Como retomar o trabalho em outro chat

Este pacote contém **todas as ferramentas** usadas para gerar o portal.
O ambiente de execução é apagado entre sessões — sem estes arquivos,
tudo teria que ser reescrito do zero.

---

## O que fazer ao abrir o chat novo

1. **Abra o chat dentro do mesmo Projeto.** Os arquivos do projeto e a
   memória continuam disponíveis; um chat fora do projeto começa do zero.
2. **Anexe dois arquivos:** este pacote de ferramentas e o pacote mais
   recente do site (`site-portal-unificado-vNN.zip`).
3. **Diga o que quer fazer.** Ex.: "descompacta as ferramentas e o site em
   /home/claude, e vamos montar a supervisão do dia X".

O primeiro comando a rodar, sempre:

```bash
cd /home/claude && mkdir -p site && unzip -q site-portal-unificado-vNN.zip -d site \
  && unzip -q ferramentas-portal.zip -d . \
  && pip install pymupdf --break-system-packages -q \
  && mkdir -p /tmp/f && cd /tmp/f && npm pack @fontsource/plus-jakarta-sans >/dev/null \
  && tar xzf fontsource-plus-jakarta-sans-*.tgz \
  && mkdir -p /tmp/nf && cd /tmp/nf && npm pack @fontsource/newsreader >/dev/null \
  && tar xzf fontsource-newsreader-*.tgz && echo pronto
```

As fontes vêm do npm porque não ficam no repositório: Plus Jakarta Sans
(interface e corpo) e Newsreader (serifada dos títulos da newsletter).

---

## Estrutura do site

```
index.html                  home
assets/                     logo.png, logo-creme.png, julio.jpg
jornada/                    hub das trilhas de leitura
  processos/                11 encontros — Hofmann, Hayes & Lorscheid
  psicoterapeutas-eficazes/ 3 de 9 — Miller & Moyers
aulas/                      5 aulas livres
supervisoes/                12 casos, desidentificados
newsletter/                 edições numeradas (pasta por data: 2026-09/)
```

Cada material é uma pasta com `index.html` e `resumo.pdf`.
As edições da newsletter têm `index.html` e `edicao-01.pdf`.

**Números atuais:** 32 materiais, 201 perguntas com gabarito (100%),
26 figuras SVG, 3 itens na Edição 1 (definitiva, v44).

---

## As ferramentas

| Arquivo | Para que serve |
|---|---|
| `gen_resumo.py` | **Núcleo.** Gera o `resumo.pdf` branded: capa oliva, página da Comunidade, miolo com cabeçalho corrido, páginas de trabalho com campos AcroForm reais (checkbox e caixas de texto). |
| `sup_common.py` | Fonte única por material: `pagina(spec, base)` gera a página do site e `pdf(spec)` gera o dicionário do PDF. Aceita `desid` (caixa de desidentificação própria) e `gabarito`. |
| `reconstruir.py` | **Salva-vidas.** Remonta o dicionário do material a partir da **página publicada** — permite regerar qualquer PDF mesmo sem o arquivo-fonte. Também insere figuras por âncora de texto. |
| `gabarito.py` | Injeta gabarito expansível nas páginas e **anexa** as páginas de gabarito a PDFs já existentes, sem regerar. |
| `edicao.py` | Gera o PDF da edição da newsletter (uma página A4, direção editorial com retrato). |
| `jornal.py` | Versão anterior, formato de jornal antigo. Guardada como alternativa. |
| `revista.py` | Versão intermediária, cartões. Guardada como alternativa. |
| `referencias.py` | Gera as três direções de design (A editorial, B manifesto, C assimétrica) para comparação. |
| `build_local.py` | Gera a **cópia de conferência** com caminhos relativos, para abrir do disco. |
| `figs_tus.py`, `figs_aulas.py` | Figuras SVG das aulas. |
| `aula_*.py`, `sup_*.py` | Conteúdo dos materiais que ainda têm fonte. |
| `gab_*.py` | Gabaritos por trilha. |

---

## Convenções que precisam ser mantidas

**Desidentificação.** Casos de supervisão saem sem nome de supervisionanda
nem de participantes. Generaliza-se topografia e preserva-se função. Idade
vira faixa, ocupação e instituição saem, marcadores culturais saem. Cada
material abre com caixa dizendo o que foi generalizado. Menores recebem
desidentificação ampliada.

**Nota de método.** Todo material termina com uma, registrando: o que foi
desidentificado, quais artefatos de transcrição foram corrigidos, quais
moderações empíricas foram feitas e o que foi acrescentado por mim.
Referência nunca é inventada para preencher lacuna.

**Omissões de segurança.** Sem doses, pontos de corte, protocolos de pesagem,
nomes comerciais usados como método. **Nunca nomear meios ou métodos de
suicídio**, inclusive na restrição de acesso. Sem técnicas de desconforto
físico intenso como estratégia de regulação.

**Gabarito.** Duas etiquetas: *Ver comentário* para pergunta conceitual,
*Ver critérios* para pergunta de aplicação pessoal — esta abre com "não há
resposta certa" e lista o que uma boa resposta contempla, incluindo o erro
comum. Na página é `<details>`; no PDF, seção ao final.

**Newsletter.** Cada item tem: ficha do estudo em etiquetas, figura quando
couber, duas colunas (*muda na clínica* × *não autoriza dizer*), e um bloco
oliva com **ação para a clínica formulada em processos** mais uma pergunta
crítica. Sem tom de IA. Edições são numeradas, sem periodicidade fixa.

**Artefatos de transcrição recorrentes do Gemini:**
Reis/Hoffman → Hayes/Hofmann · Fambern → Fairburn · ara Cooper → Zafra Cooper ·
Dalgala Rondo → Dalgalarrondo · PEBAT → PBAT · OK45 → OQ-45 · DAS21 → DASS-21 ·
AQ2 → AAQ-II · hipotivação → hipoativação · metas Smart → SMART

---

## Publicação

- **Publicar:** conteúdo do `site-portal-unificado-vNN.zip` na **raiz** do
  repositório. Caminhos absolutos (`/assets/`), como o servidor exige.
- **Nunca publicar:** `site-conferencia-local.zip` — tem caminhos relativos
  e quebraria a navegação no ar.
- **Cloudflare Pages** conectado ao repositório, branch `main`. Sem comando
  de build, diretório de saída `/`.
- **Cuidado com os PDFs:** 13 dos 15 MB do repositório, binários. Commite
  **apenas os que mudaram**; regerar todos infla o histórico em ~13 MB por
  commit. Alternativa estrutural: `git lfs track "*.pdf"`.
- Se algo não atualizar no ar: *Purge Everything* em Caching. E confira se
  **Auto Minify** e **Rocket Loader** estão desligados — reescrevem HTML na
  borda e já causaram um problema aqui.

---

## Armadilhas que já custaram tempo

1. **`re.sub` com CSS na string de substituição.** `\\2212` vira escape octal
   e grava caractere de controle no arquivo. O Chromium tolera local; o
   Cloudflare pode truncar a folha de estilo ali. Use `str.replace`.
2. **Dupla formatação com `%`.** CSS tem `100%` literal; formatar a string
   duas vezes quebra. Use `.replace('@MARCA@', valor)`.
3. **Substituição de CSS que falha em silêncio.** Sempre confira se a regra
   entrou de fato, e renderize antes de publicar.
4. **`doc.save` do PyMuPDF sobre o próprio arquivo** exige `tmp` + `os.replace`.
5. **Abrir o site do disco** não funciona com caminhos absolutos — use a
   cópia de conferência.
6. As páginas dos PDFs fecham com **folga zero**: qualquer texto a mais joga
   para a segunda página. Os geradores reportam a folga a cada rodada.

---

## O que ficou pendente

- **Figuras**, primeiro lote: cap. 11 da trilha de processos e as cinco
  supervisões cuja espinha é a rede do caso (perfeccionismo e vergonha,
  defeito e culpa, fusão e rigidez, ansiedade e desesperança, desconfiança
  e incerteza).
- **Newsletter (resolvido em 08/09/2026).** A seção passou a se chamar
  **O que vale ler** (trocado em todas as páginas). A **Edição 1 definitiva**
  substituiu por completo os quatro itens de teste em `newsletter/2026-09/`:
  Artmed Experience (15 a 17/10/2026), o experimento de caso único de
  Lavefjord et al. (2026) sobre a hipótese da centralidade, e a trend das
  fotos anos 80 lida pela pesquisa sobre nostalgia (Sedikides & Wildschut).
  Geradores: `edicao01_site.py` (página, índice, home, nome da seção; roda
  sobre a página **original** de teste, não é idempotente) e
  `edicao01_pdf.py` (PDF de uma página, folga zero).
  O fluxo segue: eu levanto a pauta, você aprova, eu escrevo.
  Candidatos ainda na gaveta para a Edição 2: o ensaio randomizado do chatbot
  Therabot e a carta que o contesta; a reação do público a esse ensaio; o
  ensaio de TBP contra TCC de rotina, ainda sem resultados; a **parte 2** da
  revisão sobre neurobiologia da agressão; e a metanálise "Principles of
  nostalgia" (JESP, 2026), que não consegui abrir.

- **O formato da newsletter está fechado** e é o que deve ser reaproveitado:
  ficha do estudo em etiquetas, figura quando couber, duas colunas
  (*muda na clínica* × *não autoriza dizer*), bloco oliva com ação em
  processos mais pergunta crítica, e o PDF de uma página na direção
  editorial (`edicao.py` / `edicao01_pdf.py`), com miniatura clicável no alto da página.

- **Trilha Psicoterapeutas Eficazes:** 6 capítulos ainda sem material.
- **Consentimento** para uso dos casos de supervisão em material público:
  decisão sua, anterior ao deploy.
