# Portal Lógica Psicológica

Site estático de materiais de estudo. Sem build: o que está no repositório é o que vai para o ar.

## Estrutura

```
index.html                  porta de entrada
assets/                     logo, foto, imagens compartilhadas
jornada/                    hub das Jornadas da Leitura
processos/                  trilha TBP (cap1…cap11)
psicoterapeutas-eficazes/   trilha Miller & Moyers (cap2…)
aulas/                      aulas livres
supervisoes/                supervisões clínicas
newsletter/                 edições numeradas, sem periodicidade fixa (pasta por data, ex.: 2026-09/)
```

Cada material é uma pasta com `index.html` e `resumo.pdf`.
As edições da newsletter têm `index.html` e `edicao-NN.pdf` (uma página A4).

Hoje: 32 materiais publicados, 201 perguntas com gabarito, 23 figuras.

## Publicação

Cloudflare Pages conectado a este repositório, branch `main`.
Push em `main` publica. Configuração do projeto:

- Comando de build: **(vazio)**
- Diretório de saída: **/** (raiz)
- Framework preset: **None**

## Ao acrescentar um material

1. Criar a pasta do material com `index.html` e `resumo.pdf`.
2. Trocar o card correspondente no `index.html` da trilha (de "em breve" para Abrir + PDF).
3. Atualizar o contador em `jornada/index.html`, quando for trilha da Jornada.
4. Atualizar, no `index.html` da raiz, o número no card da seção, a linha
   "Acervo atualizado em…" e o bloco do material mais recente.
5. Commit e push.

## Cuidado com os PDFs

Cada PDF tem ~400 KB e é binário. Regerar todos e commitar todos infla o histórico
em vários MB por commit, sem ganho. **Commite apenas os PDFs que mudaram.**

## Conferir antes de publicar

Os caminhos deste repositório são **absolutos** (`/assets/…`, `/aulas/`), como o
servidor exige. Abrir o `index.html` direto do disco por isso não funciona: o
navegador procura na raiz do drive, as imagens somem e os links de seção abrem
listagem de pasta.

Para conferir localmente existe uma **cópia de conferência** com caminhos
relativos, gerada à parte. Ela serve só para olhar e **não deve ser commitada** —
publicar caminhos relativos quebraria a navegação no ar.
