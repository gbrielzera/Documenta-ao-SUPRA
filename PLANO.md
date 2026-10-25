# Plano de incrementos do projeto

Lista do que o usuário pode levantar e mandar para o chat incorporar. Cada item diz **o que fazer**, **como mandar** e
**o que melhora**. Marque `[x]` quando entregar; o chat registra a data e o que foi incorporado.

Regras para mandar: aceito TAB, `;` ou `,` como separador, com ou sem cabeçalho. Só **estrutura, nomes, contagens e códigos**, nunca linhas com nome, CPF, matrícula ou e-mail de
pessoas. Resultado de consulta: salvar em `.txt` (separado por TAB) e anexar com `@caminho`. Prints: anexar as imagens.
XMLs: copiar para `XMLs para teste/` e avisar. Depois de cada entrega, o chat atualiza os guias e remonta a skill
(`tools/montar_skill.py`).

## Prioridade alta (pouco esforço, ganho grande)

- [ ] **1. Schema completo do banco (1 consulta).** Hoje só temos as colunas reais de 4 tabelas; o resto vem da doc de 2018.
  Melhora todas as respostas de SQL e mostra as tabelas do cliente (TB_*, VW_*, SV_*).
  ```sql
  SELECT table_name, column_name, data_type, data_length, nullable
  FROM all_tab_columns WHERE owner = USER ORDER BY table_name, column_id;
  ```

- [ ] **2. Mapa dos fluxos em produção, com volume (1 consulta).** Diz quais fluxos existem, quais estão ativos e quais
  são usados de verdade; orienta quais XMLs vale a pena exportar.
  ```sql
  SELECT CS.SIGLA, CS.DESCRICAO, CS.ATIVO, COUNT(O.ID_OCORRENCIA) AS OS_12_MESES
  FROM CLASSE_SUB_PROCESSO CS
  LEFT JOIN OCORRENCIA O ON O.ID_CLASSE_SUB_PROC = CS.ID_CLASSE_SUB_PROCESSO
                        AND O.DATA_HORA_CRIACAO >= ADD_MONTHS(SYSDATE, -12)
  WHERE CS.ID_DOMAIN = 1
  GROUP BY CS.SIGLA, CS.DESCRICAO, CS.ATIVO
  ORDER BY OS_12_MESES DESC;
  ```

- [ ] **3. Testes em Qualidade dos pontos ainda não comprovados** (roteiro e scripts prontos em `guias/testes_qualidade.md`). Rode cada um num fluxo de teste e mande só
  "funcionou" ou "erro: <mensagem>". O chat marca a receita como `[testado]`.
  - Consulta parametrizada: `DB.ExecuteScalar("SELECT NOME FROM PESSOA WHERE ID_PESSOA = :ID", ["ID"], [123])`
    (descobre a sintaxe do marcador; se falhar, tentar `@ID` e `?`).
  - `Mensagem.Cancelar = True` no Script Evento de um evento de mensagem (o e-mail deixa de sair?).
  - `OrdemServico.ModificaCampoFormularioVisivel("CAMPO", False)` no Script Início (o campo some ao abrir a tarefa?).
  - `PossuiAprovacao("COD")` com a aprovação ainda **pendente** (deve dar `False`).
  - Chamada assíncrona de Subprocesso `True` x `False`: qual deixa a OS chamadora avançar sem esperar a filha?
  - Script de papel com `Pessoa.Carrega(...)` **sem** o `from ... import Pessoa`: funciona ou dá erro? (e no Script Início?)
  - Receitas 7 (papel por nome com "A"), 9 (UOR e matrícula ao escolher a pessoa), 10 (vários destinatários) e 14 (API).
  - `Utils.NewSequenceValue("NOME_DA_SEQUENCE")`, se existir alguma sequence própria.

- [ ] **4. Prints do Editor de Scripts.** É a maior lacuna: as variáveis disponíveis em cada tipo de script estão no
  código ofuscado das DLLs e não dá para extrair. No editor, a árvore à direita e o autocompletar mostram isso.
  Um print por tipo: Script Início, Validação, Fim, Formulário carregado, Modificado (campo e coluna de grid),
  Seleção de Atores, Evento de mensagem, Fórmula do desvio, Script de recuperação de opções.

## Prioridade média

- [ ] **5. Cadastros de apoio ao desenho (consultas rápidas, sem dados pessoais).** Ajuda a sugerir papéis, serviços,
  filas e modelos que já existem, em vez de inventar novos.
  ```sql
  SELECT NOME, TIPO, ATIVO FROM PAPEL_CLASSE_NEGOCIO WHERE ID_DOMAIN = 1 ORDER BY NOME;
  SELECT SIGLA, DESCRICAO, ATIVO, DISP_AA FROM SERVICO WHERE ID_DOMAIN = 1 ORDER BY SIGLA;
  SELECT SIGLA, DESCRICAO, ATIVO, ID_GRUPO_TRABALHO, ID_GRUPO_TRABALHO_PAI FROM GRUPO_TRABALHO WHERE ID_DOMAIN = 1 ORDER BY DESCRICAO;
  SELECT ID_MODELO_COMUNICA, DESCRICAO FROM MODELO_COMUNICA ORDER BY DESCRICAO;
  SELECT DESCRIPTION, TYPE, ENABLED, STATUS, LAST_TIME, NEXT_TIME FROM SV_JOB ORDER BY DESCRIPTION;
  ```

- [ ] **6. XMLs exportados de produção.** Os 76 XMLs atuais parecem vir de Qualidade (trazem 868 campos que a produção
  não tem). Exportar da produção os fluxos que você mais mexe (use a lista do item 2) deixa os resumos fiéis ao que roda.

- [ ] **7. Diário de perguntas reais.** Anote as perguntas que fizer no estágio e se a resposta da skill estava certa
  (pergunta, resposta certa em uma linha, onde conferiu). Com 10 a 20 delas o chat monta testes automáticos da skill
  e corrige o que ela erra.

- [ ] **8. Prints das telas de propriedades do Editor de Processos.** Tarefa, Data Object de Aprovação, Entrada de Dados
  (diálogo de campos), Desvio Exclusivo, atividade Subprocesso, Link Inicial, Evento de mensagem, Timer. Confirma os
  nomes das propriedades na versão 19.1.1 (a doc é de 2018).

## Quando der

- [ ] **9. Pendências do banco já listadas** em `guias/consultas_banco.md`: valores de `PESSOA.ATIVO/TIPO_COLABORADOR/TIPO`,
  dono de `CAD_FUNCIONARIO_V` e `SV_PARAM` (sinônimos), chaves estrangeiras, matrícula repetida no RH.
- [ ] **10. Padrões internos da equipe**, se existirem por escrito: nomes de campos e papéis, checklist de subida de
  Qualidade para Produção, quem aprova, modelos de comunicado padrão.
- [ ] **11. Versão confirmada.** No cliente, Ajuda > Sobre: versão do cliente e do servidor (os XMLs dizem 19.1.1, as DLLs 18.1.1).
- [ ] **12. Combinar com o Felipe.** Pedir autorização para os 28 XMLs a mais e para a revisão dos scripts dele, e dividir
  o trabalho (ex.: ele revisa scripts, você levanta banco e prints) para não repetir esforço.

## O que o chat faz sozinho (sem depender de entrega)

- Testes automáticos da skill com perguntas reais (item 7) e ajuste da descrição para ela ser acionada nos momentos certos.
- Um comando único de atualização (reindexar, mascarar, remontar a skill) para cada entrega.
- Novas receitas sempre que uma pergunta real se repetir.

## Registro de entregas
| Data | Item | O que foi incorporado |
|---|---|---|
