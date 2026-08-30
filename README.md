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
```

Cada material é uma pasta com `index.html` e `resumo.pdf`.

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
4. Commit e push.

## Cuidado com os PDFs

Cada PDF tem ~400 KB e é binário. Regerar todos e commitar todos infla o histórico
em vários MB por commit, sem ganho. **Commite apenas os PDFs que mudaram.**
