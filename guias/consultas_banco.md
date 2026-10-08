# Consultas de leitura que o usuário pode rodar para melhorar este projeto
Caminho: Guias > Consultas para extrair do banco

O usuário tem `SELECT` em homologação e produção (sem insert/update/delete). Um chat que precisar de
informação do banco que o repositório não tem deve pedir uma destas consultas (copiar o bloco).
Regras: trazer só **estrutura, contagens e valores de código**; nunca linhas com nome, CPF, matrícula
ou e-mail reais. Incluir `owner` quando houver dúvida de qual schema. Salvar o resultado em .txt (TAB).
Depois de receber: `python -X utf8 tools/schema_real.py <arquivo>` para colunas, ou editar `guias/sql.md`
para o resto, e registrar abaixo a data.

## Já feitas (produção, 2026-10-08)
- Colunas de `CP_PESSOA`, `CP_ORDEM_SERVICO`, `CPE_CSC`, `CAD_FUNCIONARIO_V` → `catalogo/schema_real.tsv`.
- Tabelas com mais de 100 mil linhas → `guias/sql.md`.
- Índices de `CP_PESSOA`, `PESSOA`, `OCORRENCIA` → `guias/sql.md`.
- Valores de `OCORRENCIA.SITUACAO` → `guias/sql.md`.

## Pendentes, por prioridade

### 1. Mapa oficial de campos customizados (o mais valioso)
Substitui o que extraímos dos XMLs pelo que está de fato no banco (inclui campos de fluxos que não temos).
Não traz o script de recuperação de opções (CLOB), que pode conter dados internos.
```sql
SELECT P.NAME, P.TEXT, P.TYPE, P.CONTROL, P.TABLE_NAME, P.TABLE_COLUMN, P.LENGTH, P.INVALID,
       C.NAME AS CLASSE
FROM SV_CUSTOM_PROPERTY P INNER JOIN SV_CLASS C ON C.ID_CLASS = P.ID_CLASS
ORDER BY C.NAME, P.TABLE_NAME, P.NAME;
```

### 2. Lista de todas as tabelas e views do schema, com número de colunas
Mostra o que existe fora do modelo oficial (TB_*, Z_*, views do ERP/PeopleSoft).
```sql
SELECT table_name, COUNT(*) AS colunas FROM all_tab_columns WHERE owner = USER GROUP BY table_name ORDER BY table_name;
```

### 3. Colunas de outras tabelas (trocar a lista)
Primeiro as dos fluxos já analisados: `CPE_CONTRATOS`, `CPE_CONTRATOS02`, `CPE_BOOTCAMP` (usadas pelo fluxo
Atualizar Perfil/Especialidade), `CPE_FINANCEIRO`, `CPE_PESSOAS`, `CPE_NEGOCIOS`; depois as nucleares
(para conferir a documentação de 2018): `OCORRENCIA`, `ORDEM_SERVICO`, `CLASSE_SUB_PROCESSO`, `SERVICO`,
`APROVACAO`, `ASSUNTO_APROVACAO`, `PESSOA`, `ORGAO`.
```sql
SELECT table_name, column_name, data_type, data_length, nullable
FROM all_tab_columns WHERE owner = USER AND table_name IN ('CPE_CONTRATOS','CPE_CONTRATOS02','CPE_BOOTCAMP')
ORDER BY table_name, column_id;
```

### 4. Valores de código (uma linha por valor, sem dados pessoais)
Rodar cada uma e juntar as respostas.
```sql
SELECT 'PESSOA.ATIVO' AS col, ativo AS valor, COUNT(*) AS n FROM pessoa GROUP BY ativo
UNION ALL SELECT 'PESSOA.TIPO_COLABORADOR', tipo_colaborador, COUNT(*) FROM pessoa GROUP BY tipo_colaborador
UNION ALL SELECT 'PESSOA.TIPO', tipo, COUNT(*) FROM pessoa GROUP BY tipo
UNION ALL SELECT 'OCORRENCIA.CLASSE_NEGOCIO', classe_negocio, COUNT(*) FROM ocorrencia GROUP BY classe_negocio
UNION ALL SELECT 'APROVACAO.SITUACAO', situacao, COUNT(*) FROM aprovacao GROUP BY situacao
UNION ALL SELECT 'CAD_FUNC.STATUS_MATRICULA', status_matricula, COUNT(*) FROM cad_funcionario_v GROUP BY status_matricula
UNION ALL SELECT 'CAD_FUNC.TIPO_COLABORADOR', tipo_colaborador || ' ' || desc_colaborador, COUNT(*) FROM cad_funcionario_v GROUP BY tipo_colaborador, desc_colaborador;
```

### 5. Índices e chaves das tabelas de campos e da OS
```sql
SELECT table_name, index_name, column_name FROM all_ind_columns
WHERE table_name IN ('CP_ORDEM_SERVICO','CPE_CSC','ORDEM_SERVICO','CLASSE_SUB_PROCESSO','APROVACAO','ASSUNTO_APROVACAO','SERVICO','ORGAO')
ORDER BY table_name, index_name, column_position;
```

### 6. Quantidade de linhas das tabelas pequenas e das views
`num_rows` vem nulo para views; COUNT(*) é seguro nestas.
```sql
SELECT 'CP_PESSOA' AS tabela, COUNT(*) AS n FROM cp_pessoa
UNION ALL SELECT 'PESSOA', COUNT(*) FROM pessoa
UNION ALL SELECT 'ORGAO', COUNT(*) FROM orgao
UNION ALL SELECT 'CAD_FUNCIONARIO_V', COUNT(*) FROM cad_funcionario_v;
```

### 7. Definição da view CAD_FUNCIONARIO_V (fonte dos dados do RH)
Pode exigir permissão; revisar o texto antes de compartilhar (pode citar nomes de schemas e links de banco).
```sql
SELECT text FROM all_views WHERE view_name = 'CAD_FUNCIONARIO_V';
```

### 8. Plano de execução de uma consulta pesada (opcional, se o usuário tiver permissão)
```sql
EXPLAIN PLAN FOR <a consulta>;
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```
