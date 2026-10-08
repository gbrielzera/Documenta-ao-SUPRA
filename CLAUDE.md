# Base de conhecimento do Supravizio

Esta pasta existe para responder perguntas e resolver demandas sobre o Supravizio (BPMS da Venki,
versão 19.1.1, banco Oracle neste cliente): uso do sistema, scripts IronPython, tarefas,
integrações/APIs, consultas SQL e análise dos fluxos exportados em XML. Responder em português.

## Comece por aqui (chat novo)

1. Ler `guias/contexto.md`: quem é o usuário, o ambiente, siglas, campos, papéis e tabelas recorrentes.
2. Ver se `guias/receitas.md` já resolve a pergunta.
3. Se for sobre um fluxo, achar o arquivo em `fluxos/_INDICE.md`.
4. Demandas em andamento ficam em `guias/demanda_*.md`: ler a correspondente antes de continuar.
5. Só então buscar (regra abaixo).

## Regras do usuário (valem sempre)

**Script mínimo.** Todo script pedido deve ser o menor e mais limpo que funciona:
- nada de funções auxiliares (`def Texto`, `def DefinirVisibilidade`...) quando o código cabe direto;
- nada de `import`/`clr.AddReference` além do estritamente necessário; o editor já insere
  `import clr`, `from System import *` e os imports de `Venki...Custom`;
- sem `try/except` defensivo, logs, contadores, mensagens de resumo ou comentários, a menos que
  sejam pedidos ou indispensáveis (ex.: chamada a API externa);
- sem variáveis intermediárias que só renomeiam um valor; sem código para casos não pedidos;
- se algo opcional for realmente recomendável (ex.: tratar campo vazio), citar em uma frase
  depois do script, sem colocá-lo no código.
Os fluxos existentes em `fluxos/` são verbosos e cheios de auxiliares: servem como prova de que um
método existe e funciona, não como modelo de estilo.

**Forma de visibilidade.** Preferir `Formulario["CAMPO"].Visivel = True` / `False` em `if/else`
explícito, que é como o usuário escreve.

## Regra de ouro: buscar, não ler tudo

Nunca abrir `raw/` nem os XMLs crus, e nunca varrer `docs/` inteiro. O caminho é:

1. `python -X utf8 tools/buscar.py "termos" [-t doc|fluxo|catalogo|guia] [-n 8]`
   devolve `arquivo:linha`, título e trecho. Sem acento e com prefixo já funcionam.
2. Ler só os 1 a 4 arquivos (ou trechos, com offset) que a busca apontou.
3. Para nome exato (função, tabela, campo), usar Grep em `docs/`, `fluxos/` ou `catalogo/`.

## O que há em cada pasta

| Pasta | Conteúdo |
|---|---|
| `guias/` | Leitura inicial. `contexto.md` (ambiente e usuário), `sql.md` (banco real: regras, índices, consultas), `consultas_banco.md` (consultas de leitura a pedir ao usuário), `receitas.md` (dúvidas já resolvidas), `scripts.md` (onde cada script roda), `api_scripts.md` (assinaturas reais dos objetos de script), `scripts_contexto.md` (uso real por tipo de script), `banco.md` (tabelas), `xml-fluxo.md` (estrutura do XML), `demanda_*.md` (demandas em andamento) |
| `docs/` | Documentação oficial em Markdown, 1 arquivo por tópico; `_INDICE.md` é o sumário em árvore |
| `fluxos/` | Resumo de cada XML de fluxo: grafo, atividades, campos, scripts completos; `_INDICE.md` lista todos |
| `catalogo/` | `api/<Classe>.md` (assinaturas das 300 classes da API de scripts, DLLs do Client v18.1.1); `biblioteca/*.py` (biblioteca de scripts do cliente); `campos.tsv` (campos customizados); `schema.txt` (colunas das tabelas oficiais, doc de 2018); `schema_real.tsv` (colunas reais de produção); `campos_banco.tsv` (mapa oficial de campos da produção); `campos_vs_banco.md`; `tabelas_customizadas.md`; `tabelas_usadas_em_sql.md` |
| `tools/` | Scripts de busca e manutenção |
| `XMLs para teste/`, `raw/`, `Supravizio Client3/`, `Supravizio.chm` | Fontes originais; só existem no PC do usuário e não devem ser lidas direto |

Prefixos úteis em `docs/`: `dados_<tabela>` (modelo de dados), `objetos_<classe>` (modelo de objetos),
`enum_<nome>` (enumerações), `prop_<classe>_<prop>` (uma propriedade), `db_*`, `ad_*`, `ldap_*`
(funções dos objetos de script), `tutorial_*`.

## Por tipo de pergunta

- **Como fazer X na tela / conceito**: buscar com `-t doc`.
- **Escrever ou revisar script**: aplicar a regra do script mínimo; `guias/scripts.md` diz onde o
  script roda e quais variáveis existem; conferir cada método e a assinatura em `guias/api_scripts.md`
  (ou `catalogo/api/<Classe>.md`); nomes de campo em `catalogo/campos.tsv`; se precisar de prova de uso,
  `buscar.py ... -t fluxo,catalogo`.
- **SQL**: ler `guias/sql.md` primeiro (regras de desempenho, tamanhos, índices, valores de domínio e
  consultas prontas). Colunas **reais** de produção: `grep -P "^TABELA	" catalogo/schema_real.tsv`
  (só 4 tabelas por enquanto; as demais seguem a doc de 2018 em `catalogo/schema.txt` e `docs/dados_<tabela>.md`).
  Tabela e coluna física de um campo: `grep -P "\tNOME_DO_CAMPO\t" catalogo/campos_banco.tsv` (mapa oficial da produção; `campos.tsv`, dos XMLs, pode divergir: `catalogo/campos_vs_banco.md`). Sintaxe Oracle.
  Se faltar informação do banco, pedir ao usuário (só tem SELECT) uma consulta de `guias/consultas_banco.md`.
- **Integração / API / web service**: `docs/web_services.md`, `docs/webservices.md`,
  `docs/iniciador_por_mensagem.md`, tutoriais 13 e 14; exemplos REST reais em `catalogo/biblioteca/api*.py`.
- **Entender ou alterar um fluxo (XML)**: ler `fluxos/<nome>.md` (começar pelo `## Grafo do fluxo`);
  estrutura do XML em `guias/xml-fluxo.md`; detalhe de um nó com
  `python -X utf8 tools/fluxo.py bruto "<xml>" <Id|NOME_CAMPO>` (só no PC, exige o XML).
- **Demanda inteira (novo fluxo ou mudança)**: ler o fluxo original; procurar um fluxo parecido já
  feito (`fluxos/_INDICE.md` marca grid, aprovação, lote, API...); listar as regras de negócio
  extraídas dos scripts; propor o desenho; apontar o que depende de documento ou decisão; registrar
  em `guias/demanda_<nome>.md` se o trabalho continuar depois.

## Honestidade

- Citar a fonte de cada afirmação (arquivo em `docs/`, fluxo ou catálogo).
- Três níveis de evidência para script: documentado (`docs/`), assinatura confirmada nas DLLs
  (`guias/api_scripts.md`, versão 18.1.1; os fluxos são 19.1.1) e observado em fluxos do cliente.
  Dizer qual é qual. Assinatura confirmada não garante comportamento: sugerir teste em Qualidade.
- O usuário normalmente não consegue testar na hora: dizer o que não foi testado.
- A lista de variáveis disponíveis em cada tipo de script não está nas DLLs de forma legível
  (código ofuscado, não descompilar); usar `guias/scripts.md` e `guias/scripts_contexto.md`.
- Não inventar função, propriedade, tabela ou coluna. Se a busca não achar, dizer isso.
- O schema real de produção foi extraído só para `CP_PESSOA`, `CP_ORDEM_SERVICO`, `CPE_CSC` e
  `CAD_FUNCIONARIO_V`; para as demais tabelas o modelo vem da documentação de 2018 e pode divergir.

## Aprender com o uso

Quando o usuário confirmar, corrigir ou ensinar algo, atualizar `guias/receitas.md` (receita nova ou
ajuste, com a fonte: [doc], [api], [fluxo] ou [usuário]) e, se for sobre o ambiente,
`guias/contexto.md`. No PC, rodar `tools/indexar.py`; para publicar, `tools/mascarar.py`, commit e
push (só com o pedido do usuário).

## Manutenção (no PC do usuário)

```
python -X utf8 tools/baixar.py                 # baixa/atualiza raw/ (retomável)
python -X utf8 tools/importar_chm.py <pasta>   # tópicos que só existem no Supravizio.chm -> raw/
python -X utf8 tools/converter.py              # raw/ -> docs/
python -X utf8 tools/fluxo.py resumir --todos  # XMLs -> fluxos/
python -X utf8 tools/fluxo.py catalogo         # XMLs -> catalogo/
python -X utf8 tools/guias.py                  # guias/banco.md, scripts_contexto.md, schema.txt, fluxos/_INDICE.md
powershell -ExecutionPolicy Bypass -File tools\extrair_api.ps1   # DLLs do Client -> catalogo/api/_api.json
python -X utf8 tools/api.py                    # _api.json -> catalogo/api/*.md e guias/api_scripts.md
python -X utf8 tools/schema_real.py <export>   # export de ALL_TAB_COLUMNS -> catalogo/schema_real.tsv
python -X utf8 tools/campos_banco.py <export>  # export de SV_CUSTOM_PROPERTY -> catalogo/campos_banco.tsv e campos_vs_banco.md
python -X utf8 tools/mascarar.py               # OBRIGATÓRIO antes de commitar: mascara senhas/tokens
python -X utf8 tools/indexar.py                # recria kb.sqlite (rodar por último)
```

Novo XML: copiar para `XMLs para teste/`, rodar `fluxo.py resumir "<arquivo>"`, `guias.py`,
`mascarar.py` e `indexar.py`.
Escritos à mão: `CLAUDE.md`, `guias/contexto.md`, `receitas.md`, `scripts.md`, `xml-fluxo.md` e
`demanda_*.md`, `sql.md` e `consultas_banco.md`. Os demais arquivos são gerados e não devem ser editados.

## Ambiente na nuvem / clone do GitHub

O repositório é privado e não inclui as fontes originais nem `kb.sqlite` (ver `.gitignore`).
`tools/buscar.py` recria o índice sozinho na primeira busca. Credenciais aparecem como
`***MASCARADO***`: nunca pedir nem reconstituir os valores.
