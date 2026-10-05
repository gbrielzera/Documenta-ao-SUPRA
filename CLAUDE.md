# Base de conhecimento do Supravizio

Esta pasta existe para responder perguntas sobre o Supravizio (BPMS da Venki, versão 19.1.1,
banco Oracle neste cliente): uso do sistema, scripts IronPython, tarefas, integrações/APIs,
consultas SQL e análise dos fluxos exportados em XML. Responder em português.

## Regra de ouro: buscar, não ler tudo

Nunca abrir `raw/` nem os XMLs crus, e nunca varrer `docs/` inteiro. O caminho é:

1. `python -X utf8 tools/buscar.py "termos" [-t doc|fluxo|catalogo|guia] [-n 8]`
   devolve `arquivo:linha`, título e trecho. Sem acento e com prefixo já funcionam.
2. Ler só os 1 a 4 arquivos (ou trechos, com offset) que a busca apontou.
3. Para nome exato (função, tabela, campo), usar Grep em `docs/`, `fluxos/` ou `catalogo/`.

## O que há em cada pasta

| Pasta | Conteúdo |
|---|---|
| `guias/` | Resumos para começar: `receitas.md` (dúvidas frequentes já resolvidas), `scripts.md`, `scripts_contexto.md`, `banco.md`, `xml-fluxo.md` |
| `docs/` | Documentação oficial (help.supravizio.com) em Markdown, 1 arquivo por tópico; `_INDICE.md` é o sumário em árvore |
| `fluxos/` | Resumo de cada XML de fluxo: grafo, atividades, campos, scripts completos |
| `catalogo/` | Extraído dos XMLs: `biblioteca/*.py` (biblioteca de scripts), `campos.tsv` (campos customizados), `schema.txt` (colunas das tabelas oficiais), `tabelas_customizadas.md`, `tabelas_usadas_em_sql.md` |
| `XMLs para teste/` | XMLs originais exportados (não ler direto) |
| `raw/` | HTML original da documentação (não ler) |
| `tools/` | Scripts de manutenção |

Prefixos úteis em `docs/`: `dados_<tabela>` (modelo de dados), `objetos_<classe>` (modelo de objetos),
`enum_<nome>` (enumerações), `prop_<classe>_<prop>` (uma propriedade), `db_*`, `ad_*`, `ldap_*`
(funções dos objetos de script), `tutorial_*`.

## Por tipo de pergunta

- **Antes de tudo**: ver se `guias/receitas.md` já resolve (importar fluxo, criar campo/papel,
  visibilidade, grids, gateway de aprovação, API REST, validação...). Ao resolver uma dúvida nova
  e recorrente, acrescentar a receita lá com a fonte ([doc] ou [fluxo]) e rodar `tools/indexar.py`.

- **Como fazer X na tela / conceito**: buscar com `-t doc`.
- **Escrever ou revisar script**: ler `guias/scripts.md`; depois a seção do tipo de script em
  `guias/scripts_contexto.md`; depois um exemplo real com `buscar.py ... -t fluxo,catalogo`.
- **SQL**: `guias/banco.md` para achar a tabela; `grep -i '^TABELA:' catalogo/schema.txt` para as
  colunas; `docs/dados_<tabela>.md` para o significado. Campos customizados: `catalogo/campos.tsv`
  dá tabela e coluna físicas. Sintaxe Oracle.
- **Integração / API / web service**: `docs/web_services.md`, `docs/webservices.md`,
  `docs/iniciador_por_mensagem.md`, tutoriais 13 e 14; exemplos REST reais em `catalogo/biblioteca/api*.py`.
- **Entender ou alterar um fluxo (XML)**: ler `fluxos/<nome>.md` (começar pelo `## Grafo do fluxo`);
  estrutura do XML em `guias/xml-fluxo.md`; detalhe de um nó com
  `python -X utf8 tools/fluxo.py bruto "<xml>" <Id|NOME_CAMPO>`.

## Honestidade

- Citar a fonte de cada afirmação (arquivo em `docs/`, fluxo ou catálogo).
- A documentação oficial cobre pouco dos objetos de script (ex.: `Criticas`, `Mensagem`,
  `OrdemServico.GetCustom`). O que só aparece nos fluxos reais deve ser apresentado como
  "observado em fluxos do cliente", não como documentado.
- Não inventar função, propriedade, tabela ou coluna. Se a busca não achar, dizer isso.
- O schema real do banco ainda não foi extraído; o modelo vem da documentação e pode divergir.

## Manutenção

```
python -X utf8 tools/baixar.py                 # baixa/atualiza raw/ (retomável)
python -X utf8 tools/converter.py              # raw/ -> docs/
python -X utf8 tools/fluxo.py resumir --todos  # XMLs -> fluxos/
python -X utf8 tools/fluxo.py catalogo         # XMLs -> catalogo/
python -X utf8 tools/guias.py                  # guias/banco.md, scripts_contexto.md, schema.txt
python -X utf8 tools/mascarar.py               # OBRIGATÓRIO antes de commitar: mascara senhas/tokens
python -X utf8 tools/indexar.py                # recria kb.sqlite (rodar por último)
```

Novo XML: copiar para `XMLs para teste/`, rodar `fluxo.py resumir "<arquivo>"`, `mascarar.py` e `indexar.py`.

## Ambiente na nuvem / clone do GitHub

O repositório é privado e não inclui `XMLs para teste/`, `raw/` nem `kb.sqlite` (ver `.gitignore`).
`tools/buscar.py` recria o índice sozinho na primeira busca. Sem os XMLs, `fluxo.py bruto` não
funciona: usar os resumos em `fluxos/`. Credenciais aparecem como `***MASCARADO***`: nunca pedir
nem reconstituir os valores; indicar que ficam no Supravizio/cofre da empresa.
`guias/scripts.md` e `guias/xml-fluxo.md` são escritos à mão; os demais arquivos gerados não devem ser editados.
