# Modelo do Jornal Bagual

Gerador do Jornal Bagual (Lógica Psicológica). Monta o PDF A4 sempre no mesmo molde:

- **Página 1, capa:** nome do jornal, "Ao leitor", índice, matéria em destaque e chamadas das outras.
- **Páginas 2, 3 e 4:** uma matéria completa por página.
- **Fim da última página:** nota de método e anúncio da comunidade.

O texto se ajusta sozinho pra caber na página.

## Como gerar uma edição

1. Escreve o conteúdo em `edicao.json`, no formato de `exemplo/edicao.json`.
2. Põe a imagem da capa e as figuras (SVG) na mesma pasta do JSON.
3. Roda:

```
pip install playwright pyphen beautifulsoup4 pymupdf pillow
python3 gerar_jornal.py caminho/edicao.json Jornal-Bagual-Edicao-04.pdf
```

Ao lado do PDF saem prévias PNG de cada página. Se o terminal avisar "ATENÇÃO: alguma matéria não coube", encurta o texto dessa matéria e gera de novo.

## Campos do JSON

### Da edição

| Campo | O que é |
|---|---|
| `numero` | número da edição (vai em "Ano I · Nº 4") |
| `mes` | por extenso, ex. "outubro de 2026" |
| `ao_leitor` | o parágrafo de abertura da edição (60 a 90 palavras) |
| `destaque` | qual matéria vai em destaque na capa: 0 = primeira, 1 = segunda, 2 = terceira |
| `foto_capa` | arquivo da imagem (jpg ou png). Opcional. Sem foto, a capa usa o gráfico da matéria em destaque. |
| `foto_materia` | a qual matéria a foto pertence. Se for diferente do `destaque`, a foto aparece pequena na chamada dessa matéria. |
| `legenda_foto` | texto curto embaixo da foto |
| `nota_metodo` | opcional. Se ficar vazio, usa a nota padrão. |
| `materias` | sempre 3 |

### De cada matéria

| Campo | O que é |
|---|---|
| `retranca` | etiqueta acima do título, ex. "Umbrella review · Clinical Psychology Review" |
| `titulo` | a manchete, até umas 14 palavras |
| `linha_fina` | o resumo do achado, 50 a 90 palavras. Aceita `<strong>` no número principal. |
| `ficha` | 4 ou 5 pares, como `["Desenho", "ECR, 210 adultos"]` |
| `figura_svg` | nome do arquivo .svg (ou o SVG inteiro) |
| `legenda_figura` | 1 ou 2 frases |
| `muda_na_clinica` | 3 itens, até 70 palavras cada |
| `nao_autoriza_dizer` | 3 itens, até 55 palavras cada |
| `acao_para_a_clinica` | 60 a 90 palavras |
| `pergunta` | uma pergunta só, até 30 palavras |
| `referencia` | referência APA da fonte |

### Figuras

- SVG com `viewBox` de 720 de largura e 190 a 240 de altura.
- Fonte `Plus Jakarta Sans`.
- Cores da marca: oliva `#3d411f` e `#5a5e2e`, dourado `#bcae56`, terracota `#a05a3c` e texto `#2f2e24`.

Os SVGs de `exemplo/` servem de modelo.

## Texto pra colar no chat que gera o jornal

> Anexei o pacote modelo-jornal-bagual.zip. A edição sai sempre por ele, sem mudar layout, fontes nem cores. O teu trabalho é escrever o `edicao.json` com o conteúdo da edição, no formato de `exemplo/edicao.json`, respeitando os tamanhos do LEIA-ME.md:
> - 3 matérias, cada uma com ficha, figura SVG, 3 itens de "Muda na clínica", 3 de "Não autoriza dizer", ação para a clínica e uma pergunta;
> - figuras no estilo das de `exemplo/`.
>
> Depois roda `python3 gerar_jornal.py edicao.json Jornal-Bagual-Edicao-NN.pdf`, confere as prévias PNG e, se alguma matéria estourar, encurta o texto dela e gera de novo. No fim me entrega o PDF.
> O texto vai na minha voz, tratando o leitor por "tu" (conjugação gaúcha: "tu atende", "tu acha"). Nada de travessão, nada de "não é X, é Y" e nada de frase de efeito no fim.
