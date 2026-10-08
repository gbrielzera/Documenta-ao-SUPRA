# Consultas de leitura que o usuário pode rodar para melhorar este projeto
Caminho: Guias > Consultas para extrair do banco

O usuário tem `SELECT` em homologação e produção (sem insert/update/delete). Um chat que precisar de
informação do banco que o repositório não tem deve pedir uma destas consultas (copiar o bloco).
Regras: trazer só **estrutura, contagens e valores de código**; nunca linhas com nome, CPF, matrícula
ou e-mail reais. **Pedir que o resultado seja salvo em arquivo .txt e anexado com `@caminho`**: colar
resultados grandes na conversa é pesado e já fez um resultado sumir. Depois de receber:
`python -X utf8 tools/schema_real.py <arquivo>` (colunas de tabelas), `python -X utf8 tools/campos_banco.py <arquivo>`
(mapa de campos), ou editar `guias/sql.md` para o resto, e registrar abaixo a data.

## Já feitas (produção, 2026-10-08)
- Colunas de `CP_PESSOA`, `CP_ORDEM_SERVICO`, `CPE_CSC`, `CAD_FUNCIONARIO_V` → `catalogo/schema_real.tsv`.
- Mapa oficial de campos customizados (`SV_CUSTOM_PROPERTY`, 3.451 campos) → `catalogo/campos_banco.tsv`.
- Lista de tabelas e views do schema com nº de colunas → resumida em `guias/sql.md`.
- Tabelas com mais de 100 mil linhas, índices de `CP_PESSOA`, `PESSOA`, `OCORRENCIA`, `CP_ORDEM_SERVICO`, `CPE_CSC`,
  `ORDEM_SERVICO`, `CLASSE_SUB_PROCESSO`, `APROVACAO`, `ASSUNTO_APROVACAO`, `SERVICO`, `ORGAO` → `guias/sql.md`.
- Valores de `OCORRENCIA.SITUACAO`, `OCORRENCIA.CLASSE_NEGOCIO`, `APROVACAO.SITUACAO`, `CAD_FUNCIONARIO_V.STATUS_MATRICULA`
  e `TIPO_COLABORADOR` → `guias/sql.md`.
- Contagem de `CP_PESSOA`, `PESSOA`, `ORGAO`, `CAD_FUNCIONARIO_V` → `guias/sql.md`.
- Colunas de `CPE_CONTRATOS`, `CPE_CONTRATOS02`, `CPE_BOOTCAMP` (coladas no chat, não salvas em arquivo): conferidas
  contra o mapa de campos; os tipos delas ainda não estão em `schema_real.tsv`.
- `all_views` para `CAD_FUNCIONARIO_V`: vazio (o objeto é de outro schema, ver abaixo).

## Pendentes, por prioridade

### 1. Valores de código de PESSOA (a consulta rodou sem resultado colado)
```sql
SELECT 'PESSOA.ATIVO' AS col, NVL(TO_CHAR(ativo), '[NULO]') AS valor, COUNT(*) AS n FROM pessoa GROUP BY ativo
UNION ALL SELECT 'PESSOA.TIPO_COLABORADOR', NVL(TO_CHAR(tipo_colaborador), '[NULO]'), COUNT(*) FROM pessoa GROUP BY tipo_colaborador
UNION ALL SELECT 'PESSOA.TIPO', NVL(TO_CHAR(tipo), '[NULO]'), COUNT(*) FROM pessoa GROUP BY tipo;
```

### 2. De quem são `CAD_FUNCIONARIO_V`, `SV_PARAM` e as demais tabelas que os fluxos usam
Os fluxos consultam objetos que não estão no schema do Supravizio; isto mostra o dono e o tipo (tabela, view, sinônimo).
```sql
SELECT owner, object_name, object_type FROM all_objects
WHERE object_name IN ('CAD_FUNCIONARIO_V','SV_PARAM','CIDADE_V','ESTADO_V','DEPENDENTES_BENEFICIOS_V','CRONOGRAMA_DOD','COB_GL_CENTRO')
ORDER BY object_name, owner;
SELECT synonym_name, table_owner, table_name FROM all_synonyms
WHERE synonym_name IN ('CAD_FUNCIONARIO_V','SV_PARAM','CIDADE_V','ESTADO_V','DEPENDENTES_BENEFICIOS_V','CRONOGRAMA_DOD','COB_GL_CENTRO');
```

### 3. Colunas de outras tabelas (trocar a lista; salvar em arquivo)
Prioridade: as que os fluxos mais usam e ainda não temos: `CPE_FINANCEIRO`, `CPE_PESSOAS`, `CPE_NEGOCIOS`, `CPE_CONTRATOS`,
`CPE_CONTRATOS02`, `CPE_BOOTCAMP`, `SV_CAD_PESSOAS_V`, `SV_CAD_FUNC_HIERARQ_V`, `VW_SV_CAD_FORNECEDOR`; depois as nucleares
para conferir a documentação de 2018: `OCORRENCIA`, `ORDEM_SERVICO`, `CLASSE_SUB_PROCESSO`, `SERVICO`, `APROVACAO`,
`ASSUNTO_APROVACAO`, `PESSOA`, `ORGAO`.
```sql
SELECT table_name, column_name, data_type, data_length, nullable
FROM all_tab_columns WHERE owner = USER AND table_name IN ('CPE_CONTRATOS','CPE_CONTRATOS02','CPE_BOOTCAMP')
ORDER BY table_name, column_id;
```

### 4. Chaves estrangeiras e restrições das tabelas centrais
```sql
SELECT c.table_name, c.constraint_name, c.constraint_type, cc.column_name, c.r_constraint_name
FROM all_constraints c INNER JOIN all_cons_columns cc ON cc.constraint_name = c.constraint_name AND cc.owner = c.owner
WHERE c.owner = USER AND c.table_name IN ('OCORRENCIA','ORDEM_SERVICO','APROVACAO','ASSUNTO_APROVACAO','PESSOA','CP_PESSOA')
ORDER BY c.table_name, c.constraint_name, cc.position;
```

### 5. Valores de código de outras tabelas
`ATIVIDADE.TIPO`, `GRUPO_TRABALHO`, `CLASSE_SUB_PROCESSO.ATIVO`, `SERVICO.ATIVO`. Formato:
`SELECT 'TABELA.COLUNA', coluna, COUNT(*) FROM tabela GROUP BY coluna`.

### 6. Duplicidade de matrícula na view do RH
Mostra se uma matrícula aparece em mais de uma linha (necessário para usá-la como chave).
```sql
SELECT COUNT(*) AS matriculas_repetidas FROM (
  SELECT matricula FROM cad_funcionario_v GROUP BY matricula HAVING COUNT(*) > 1);
```

### 7. Plano de execução de uma consulta pesada (se tiver permissão)
Existe `PLAN_TABLE` no schema, mas `EXPLAIN PLAN` grava nela (insert): pode ser negado.
```sql
EXPLAIN PLAN FOR <a consulta>;
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```
