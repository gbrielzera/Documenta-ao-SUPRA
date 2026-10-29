---
name: supravizio
description: Base de conhecimento do Supravizio (BPMS da Venki) no ambiente da empresa do usuário, com a documentação oficial, resumos de 76 fluxos reais, a API de scripts IronPython, o schema Oracle real e os códigos de erro. Use SEMPRE que o usuário falar de Supravizio, Ordem de Serviço (OS), fluxo ou processo no Editor de Processos, papel, gateway/desvio, Entrada de Dados, campo customizado, grid, aprovação, subprocesso, Link Inicial, importação de fluxo ou XML exportado, scripts (Início, Validação, Fim, Modificado, Formulário carregado, Seleção de Atores, Evento) usando Formulario, OrdemServico, DB, Utils, Criticas, Atores ou Mensagem, consultas SQL em tabelas como OCORRENCIA, CP_ORDEM_SERVICO, CPE_*, CP_PESSOA ou CAD_FUNCIONARIO_V, ou mensagens de erro com código SV/PR/RH/CF/PT, mesmo que a palavra Supravizio não apareça. Cobre escrever scripts mínimos, montar SQL, desenhar fluxos, entender XMLs, chamar APIs e explicar erros.
---

# Supravizio

Esta skill reúne o que foi levantado sobre o Supravizio **do ambiente real da empresa do usuário** (versão 19.1.1, banco
Oracle): ela é mais confiável que o conhecimento geral para qualquer pergunta sobre o produto, porque traz nomes de campos,
tabelas, papéis e padrões que existem de fato lá. Responda em português.

O usuário é estagiário e desenvolve fluxos e scripts no Supravizio. Costuma consultar longe do computador e testa depois:
entregue respostas prontas para colar e diga o que não foi testado.

## Primeiro passo
Leia `references/guias/contexto.md` (ambiente, siglas, campos, papéis e tabelas recorrentes, divergências da
documentação). Depois veja se `references/guias/receitas.md` já resolve a pergunta; ele cobre as dúvidas mais comuns.

## Onde está cada coisa
Os guias citam caminhos como na pasta do projeto original. Aqui eles ficam assim:

| Caminho citado nos guias | Onde ler na skill |
|---|---|
| `guias/*.md` | `references/guias/` (arquivos soltos) |
| `catalogo/*.tsv`, `catalogo/erros_supravizio.md`, `schema.txt`... | `references/catalogo/` (use `grep`) |
| `docs/*.md` (documentação oficial, 3.300 páginas) | banco: `python scripts/kb.py ler docs/<arquivo>.md` |
| `fluxos/*.md` (resumo de cada fluxo real) | banco: `python scripts/kb.py ler fluxos/<arquivo>.md`; índice em `references/fluxos/_INDICE.md` |
| `catalogo/api/<Classe>.md`, `catalogo/biblioteca/*.py` | banco: `python scripts/kb.py ler catalogo/api/OrdemServico.md` |
| sumário da documentação | `references/docs/_INDICE.md` |

Busca (rode a partir da pasta da skill):

```
python scripts/kb.py buscar "termos" [-t doc,fluxo,catalogo,guia] [-n 8]
python scripts/kb.py ler docs/objeto_db.md [--de 1 --ate 120]
python scripts/kb.py listar fluxos/
```

A busca devolve `arquivo:linha`, título e trecho; leia só os 1 a 4 resultados relevantes com `ler`. Não varra pastas inteiras
nem leia tudo: a base é grande, e o ganho está em achar o trecho certo. Para um nome exato (campo, tabela, método), use `grep`
em `references/catalogo/` ou `buscar` com o nome.

## Como atender cada tipo de pedido
- **Como fazer X na tela / conceito**: `buscar ... -t doc`.
- **Escrever ou revisar script**: leia `references/guias/scripts.md` (onde cada script roda e as variáveis disponíveis);
  confira cada método em `references/guias/api_scripts.md`; ache o nome do campo e sua tabela com
  `grep -P "\tNOME\t" references/catalogo/campos_banco.tsv`; se precisar de prova de uso real, `buscar ... -t fluxo,catalogo`.
- **SQL**: leia `references/guias/sql.md` antes (regras de desempenho, índices, valores de domínio, consultas prontas).
  Colunas reais de produção: `grep -P "^TABELA\t" references/catalogo/schema_real.tsv` (776 tabelas, 2026-10-26); `dicionario_dll.tsv` e
  `docs/dados_<tabela>.md` ajudam a entender o significado. Sintaxe Oracle.
- **Desenhar ou montar um fluxo / demanda inteira**: leia `references/guias/desenho_fluxos.md` (formato da proposta e regras);
  procure um fluxo parecido em `references/fluxos/_INDICE.md` (marca grid, aprovação, lote, API, planilha); veja
  `references/guias/exemplo_lote_perfil_especialidade.md` para um exemplo completo de análise.
- **Dúvida de conceito ou comportamento** (aprovação, ANS/ANO, chamada assíncrona, papéis, importação, mensagens, Timer/Regra,
  pesquisa de satisfação): `references/guias/aulas_resumo.md`, organizado por tema e com a fonte de cada afirmação.
- **Entender um XML de fluxo**: o XML cru não está aqui; use o resumo em `fluxos/` e `references/guias/xml-fluxo.md`.
- **Integração, API, web service**: `references/guias/receitas.md` (receitas de API REST e de lote) e os módulos
  `catalogo/biblioteca/api*.py` via `ler`.
- **Mensagem de erro** (`PR0011`, "Associação não configurada"): `buscar "código ou texto" -t catalogo`, ou
  `references/catalogo/erros_supravizio.md`.

## Regras do usuário (valem sempre)
- **Script mínimo.** Todo script pedido deve ser o menor e mais limpo que funcione: sem funções auxiliares quando o código cabe
  direto, sem `import`/`clr.AddReference` além do necessário (o editor já insere `import clr`, `from System import *` e os imports
  de `Venki...Custom`), sem `try/except` defensivo, logs, contadores, mensagens de resumo ou comentários, a menos que ele peça ou
  seja indispensável (chamada a API externa). O que for opcional mas recomendável vira uma frase depois do código. Os fluxos
  reais são verbosos: servem de prova de que um método existe, não de modelo de estilo.
- **Visibilidade de campo**: use `Formulario["CAMPO"].Visivel = True` / `False` em `if/else` explícito, como o usuário escreve.

## Honestidade
- Cite a fonte de cada afirmação (página da documentação, fluxo, catálogo ou guia).
- Há três níveis de evidência para script: **documentado** (`docs/`), **assinatura confirmada nas DLLs** (`api_scripts.md`,
  versão 18.1.1, enquanto os fluxos são 19.1.1) e **observado em fluxos do cliente**. Diga qual é qual. Assinatura confirmada não
  garante comportamento: recomende teste em Qualidade.
- A documentação oficial tem inconsistências (veja "Divergências conhecidas" em `contexto.md`): não use uma dessas páginas como
  prova isolada. Os XMLs analisados parecem vir de Qualidade e trazem campos que a produção não tem; o mapa
  `campos_banco.tsv` (produção) é a verdade para tabela e coluna.
- Não invente método, propriedade, tabela, coluna ou campo. Se a busca não achar, diga que não encontrou. O schema real
  de produção está em `schema_real.tsv`.
- O usuário normalmente não consegue testar na hora: diga o que ficou sem teste.

## Dados sensíveis
Credenciais aparecem como `***MASCARADO***`; nunca peça nem reconstitua os valores reais. `CAD_FUNCIONARIO_V` tem CPF, salário,
endereço e outros dados pessoais: em scripts, selecione só o que o campo precisa; não cole resultados com pessoas reais. O usuário
tem apenas `SELECT` nos bancos de homologação e produção: consultas que você sugerir para ele rodar devem ser só de leitura.
Se faltar informação do banco, `references/guias/consultas_banco.md` lista consultas de leitura que ele pode rodar.

## Limites desta skill
Ela é uma fotografia (outubro de 2026): não vê o ambiente atual, os XMLs originais nem o banco. Quando o usuário trouxer algo
novo (campo, regra, correção), use a informação dele na resposta e sugira registrá-la no projeto de origem, onde estão as
ferramentas de atualização (esta skill é só leitura).
