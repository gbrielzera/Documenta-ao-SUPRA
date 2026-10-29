# Plano de incrementos do projeto

Lista do que o usuário pode levantar e mandar para o chat incorporar ao projeto. Cada item explica **por que importa**,
**como fazer**, **como enviar** e **o que o chat faz depois**. Marque `[x]` ao entregar; o chat registra a data e o que
foi incorporado na tabela do fim.

Atualizado em 2026-10-25, depois de incorporar o material do Felipe. Para um chat novo: ao receber um arquivo, consulta,
print ou texto do usuário, ache aqui a que item corresponde, incorpore (ferramentas em `CLAUDE.md`) e registre a entrega.

## Ordem sugerida
Comece por 11, 1 e 2 (menos de 15 minutos no total e o maior ganho). Depois 3 e 4. O resto, quando der.

| Ordem | Item | Tempo | O que é |
|---|---|---|---|
| 1 | 11 | 1 min | versão do sistema (texto) |
| 2 | 1 | 5 min | schema completo do banco (1 consulta) |
| 3 | 2 | 5 min | mapa dos fluxos com volume (1 consulta) |
| 4 | 3 | 15 min + testes | testes em Qualidade (texto) |
| 5 | 4 | 20 min | prints do Editor de Scripts (imagens) |
| 6 | 5, 13, 14 | 10 min | cadastros de apoio (7 consultas curtas) |
| 7 | 6 e 12 | depende | XMLs de produção e do Felipe |
| 8 | 7, 8, 15, 9, 10 | quando der | diário, prints de propriedades, comportamentos das aulas, pendências |

## Como obter e enviar: guia geral

### O que NUNCA enviar
Nome, CPF, matrícula ou e-mail de pessoas reais; senha, token ou string de conexão; conteúdo de e-mails; dados pessoais do RH.
Os pedidos abaixo foram escritos para trazer só **estrutura, nomes de objetos, contagens e códigos**. Se um resultado vier com
dado de pessoa, apague essas linhas ou troque por "(nome)" antes de enviar. Nos prints, borre nomes e e-mails.

### Consulta de banco (itens 1, 2, 5, 9, 13, 14)
1. **Abra o programa de banco** que você usa (SQL Developer, DBeaver, PL/SQL Developer, Toad ou outro). Use o ambiente de
   **produção**, a não ser que o item diga outro. Você só tem permissão de leitura, e as consultas deste plano são todas
   `SELECT`.
2. **Cole a consulta** na janela de comandos e execute uma por vez. Para executar uma consulta só, use **Ctrl+Enter** (no
   SQL Developer; "Executar Script", F5, roda várias de uma vez mas mostra tudo em outro painel, mais difícil de salvar).
3. **Carregue todas as linhas.** Muitos programas mostram só as primeiras 50 ou 200 linhas e carregam o resto aos poucos.
   No SQL Developer, clique na grade de resultado e use **Ctrl+End**; no DBeaver, confira o contador de linhas no rodapé.
   Se você exportar pelo comando de exportar (passo 4, opção A), isso é tratado por ele e não precisa fazer nada.
4. **Salve o resultado em um arquivo de texto**, de uma destas duas formas:
   - **A. Exportar** (mais seguro). Clique com o botão direito na grade de resultado e escolha **Exportar** (ou *Export data*).
     Formato: **texto delimitado** ou **CSV**, **com cabeçalho**. O separador pode ser TAB, `;` ou `,`: o chat reconhece os três.
     Codificação: **UTF-8**. Salve em uma pasta de fácil acesso, como `D:\Downloads`.
   - **B. Copiar e colar** (mais rápido). Clique na grade, **Ctrl+A** (seleciona tudo), **Ctrl+C** (copia; se o programa tiver
     "copiar com cabeçalho", use). Abra o Bloco de Notas, **Ctrl+V** (cola), **Arquivo > Salvar como**, nome com `.txt` e
     codificação **UTF-8** (no campo "Codificação" da janela de salvar).
5. **Dê um nome claro** ao arquivo (ex.: `schema_completo.txt`, `mapa_fluxos.txt`). Uma consulta por arquivo.
6. **Anexe aqui.** Na caixa de mensagem do chat, arraste o arquivo ou digite `@` e o caminho completo
   (ex.: `@"D:\Downloads\schema_completo.txt"`). Escreva em uma linha de qual item é.
7. **Confira acentos.** Se o arquivo abrir com caracteres estranhos (`Ã§`, `Ã£`), salve de novo como UTF-8.

Se a consulta demorar mais de uns 2 minutos, cancele e avise qual era. Se o arquivo passar de uns 5 MB, divida em dois ou
compacte em `.zip`.

### Texto (itens 3, 10, 11, 15)
Escreva direto no chat, uma linha por ponto. Nos testes, copie a mensagem de erro inteira e troque nomes reais por "(nome)".

### Imagens (itens 4 e 8)
1. Abra a tela que o item pede.
2. Tecle **Win+Shift+S**, arraste sobre a área e solte: o recorte vai para a área de transferência.
3. Abra o Paint, **Ctrl+V**, **Arquivo > Salvar como > PNG**, com nome que diga o conteúdo (`script_inicio_arvore.png`).
4. Borre nomes e e-mails (no Paint, selecione a área e use um retângulo preenchido).
5. Anexe as imagens aqui, todas de uma vez, pelo mesmo `@` ou arrastando.

### XMLs (itens 6 e 12)
No Editor de Processos, clique com o botão direito no subprocesso (ou no processo) e escolha **Exportar**; salve o `.xml`.
Copie para a pasta `XMLs para teste` do projeto e avise o nome. O chat gera o resumo e mascara senhas e tokens. O XML cru **não**
vai para o GitHub nem para a skill; só o resumo, depois de mascarado.

### O que o chat faz depois de cada entrega
Carrega os dados com as ferramentas do projeto, atualiza os guias, registra a entrega na tabela do fim, remonta a skill
(`tools/montar_skill.py`) e avisa se há um pacote novo para você subir. Em seguida, pede o commit e o push (o chat não consegue
enviar ao GitHub sozinho).

### Se algo der errado
Mensagem de erro do banco: envie o texto da mensagem e qual item era. Consulta lenta: cancele. Resultado vazio: envie assim
mesmo, avisando "vazio". Programa travou ao carregar tudo: use a exportação (passo 4A). Não conseguiu: diga onde parou e o chat
ajusta o passo a passo.

---

## Prioridade alta

### 11. Versão do sistema (1 minuto)
- [ ] **Por que:** as aulas que o projeto usa são da versão 11.1.2 (2020), os XMLs dizem 19.1.1 e as DLLs 18.1.1. Saber a versão
  real diz quanto do que aprendemos vale e o que deve ser conferido.
- **Como fazer:** no cliente do Supravizio, menu **Ajuda > Sobre**. Anote a versão do cliente. Se houver tela com a versão do
  servidor ou da base (em Utilitários ou no Gerenciamento de Ambiente), anote também. Se não achar o menu, tire um print da
  barra de título e da tela de login.
- **Como enviar:** texto no chat, algo como "cliente 19.1.x, servidor 19.1.y, instalado em mês/ano".
- **O chat faz:** atualiza `guias/contexto.md` e marca quais regras das aulas precisam de teste.

### 1. Schema completo do banco
- [ ] **Por que:** hoje só temos as colunas reais de 4 tabelas; o resto vem da documentação de 2018. Com o schema completo,
  as respostas de SQL deixam de depender de suposição e aparecem as tabelas do cliente (`TB_*`, `VW_*`, `SV_*`).
- **Como fazer:** execute no ambiente de **produção** (guia geral, "Consulta de banco"). Dá cerca de 30 mil linhas, então carregue
  todas ou use a exportação:
  ```sql
  SELECT table_name, column_name, data_type, data_length, nullable
  FROM all_tab_columns WHERE owner = USER ORDER BY table_name, column_id;
  ```
- **Como enviar:** um arquivo (`schema_completo.txt` ou `.csv`) com 5 colunas: tabela, coluna, tipo, tamanho, anulável.
- **O chat faz:** carrega tudo em `catalogo/schema_real.tsv` (`tools/schema_real.py`), atualiza `guias/sql.md` e `guias/banco.md`.
- **Cuidado:** só estrutura; esta consulta não traz dados de pessoas.

### 2. Mapa dos fluxos em produção, com volume
- [ ] **Por que:** mostra quais fluxos existem, quais estão ativos e quais são usados de verdade (OS nos últimos 12 meses).
  Orienta em quais fluxos o conhecimento do projeto deve ser mais fiel e quais XMLs vale a pena exportar.
- **Como fazer:** execute em **produção**:
  ```sql
  SELECT CS.SIGLA, CS.DESCRICAO, CS.ATIVO, COUNT(O.ID_OCORRENCIA) AS OS_12_MESES
  FROM CLASSE_SUB_PROCESSO CS
  LEFT JOIN OCORRENCIA O ON O.ID_CLASSE_SUB_PROC = CS.ID_CLASSE_SUB_PROCESSO
                        AND O.DATA_HORA_CRIACAO >= ADD_MONTHS(SYSDATE, -12)
  WHERE CS.ID_DOMAIN = 1
  GROUP BY CS.SIGLA, CS.DESCRICAO, CS.ATIVO
  ORDER BY OS_12_MESES DESC;
  ```
- **Como enviar:** um arquivo pequeno (`mapa_fluxos.txt`), 4 colunas: sigla, descrição, ativo, quantidade.
- **O chat faz:** cruza com os 76 fluxos que temos, aponta os que faltam e os mais usados, e marca no `fluxos/_INDICE.md`.
- **Cuidado:** a consulta lê um mês de OS; se passar de 2 minutos, cancele.

### 3. Testes em Qualidade (comportamentos ainda não comprovados)
- [ ] **Por que:** vários métodos só têm "assinatura confirmada nas DLLs" ou "observado em fluxos"; ninguém comprovou o
  comportamento na 19.1.1. Os testes viram "testado" nas receitas.
- **Como fazer:** o roteiro completo, com os scripts prontos e a montagem do fluxo de teste, está em
  `guias/testes_qualidade.md`. Resumo:
  1. Em **Qualidade** (nunca produção), crie um fluxo "TESTE_SKILL" com Início, Tarefa A, Tarefa B, uma tarefa de aprovação com
     Código `APROV`, um evento de mensagem para você mesmo e um Final (cerca de 15 minutos).
  2. Cole nos lugares indicados os scripts T1 a T4 (consulta parametrizada, `Pessoa` sem import, esconder campo,
     `PossuiAprovacao` pendente). Os scripts só escrevem um comentário na OS; não alteram nada.
  3. Abra uma OS, ande pelas tarefas e aprove a tarefa de aprovação.
  4. Na aba de comentários da OS, copie as linhas que começam por `T`.
- **Como enviar:** texto no chat, uma linha por teste (modelo no guia): `T1: OK com ["ID"]`, `T2: ERRO: ...`,
  `T3: Início = visível; Formulário carregado = sumiu`, `T4: Início = False; Fim = True`.
- **O chat faz:** marca as receitas como `[testado]` ou corrige as erradas e registra em `guias/testes_qualidade.md`.
- **Mais enxuto agora:** T5 (`Mensagem.Cancelar`) e T6 (assíncrono) já têm evidência de aula; entram só se sobrar tempo.

### 4. Prints do Editor de Scripts
- [ ] **Por que:** é a maior lacuna: as variáveis disponíveis em cada tipo de script estão no código ofuscado das DLLs e não
  dá para extrair. O editor mostra isso na árvore à direita e no autocompletar.
- **Como fazer:** para cada tipo de script, abra a tarefa (ou o campo) e o Editor de Scripts:
  1. Expanda a **árvore à direita** (objetos e variáveis) e tire um print.
  2. No texto do script, digite `Formulario.` (ou `OrdemServico.`) e, com a lista do autocompletar aberta, tire outro print.
  Tipos: Script Início, Validação, Fim, Formulário carregado, Modificado de campo, Modificado de coluna de grid, Seleção de Atores,
  Script Evento de mensagem, Fórmula do desvio, Script de recuperação de opções.
- **Como enviar:** PNGs (guia geral, "Imagens"), nomeados `tipo_arvore.png` e `tipo_autocompletar.png`. Anexe todos juntos.
- **O chat faz:** transcreve as variáveis de cada tipo para `guias/scripts.md` e confere com `catalogo/api/`.
- **Cuidado:** borre nomes, e-mails e dados do cliente que apareçam.

---

## Prioridade média

### 5. Cadastros de apoio ao desenho (5 consultas curtas)
- [ ] **Por que:** com os papéis, serviços, grupos, modelos de comunicado e jobs que já existem, o chat sugere o que reaproveitar
  em vez de inventar novos.
- **Como fazer:** execute **uma por vez** em produção; salve um arquivo por consulta (`apoio_papeis.txt`, `apoio_servicos.txt`,
  `apoio_grupos.txt`, `apoio_modelos.txt`, `apoio_jobs.txt`):
  ```sql
  SELECT NOME, TIPO, ATIVO FROM PAPEL_CLASSE_NEGOCIO WHERE ID_DOMAIN = 1 ORDER BY NOME;
  SELECT SIGLA, DESCRICAO, ATIVO, DISP_AA FROM SERVICO WHERE ID_DOMAIN = 1 ORDER BY SIGLA;
  SELECT SIGLA, DESCRICAO, ATIVO, ID_GRUPO_TRABALHO, ID_GRUPO_TRABALHO_PAI FROM GRUPO_TRABALHO WHERE ID_DOMAIN = 1 ORDER BY DESCRICAO;
  SELECT ID_MODELO_COMUNICA, DESCRICAO FROM MODELO_COMUNICA ORDER BY DESCRICAO;
  SELECT DESCRIPTION, TYPE, ENABLED, STATUS, LAST_TIME, NEXT_TIME FROM SV_JOB ORDER BY DESCRIPTION;
  ```
- **Como enviar:** os cinco arquivos de uma vez.
- **O chat faz:** cria `catalogo/cadastros_apoio.md` e passa a citar papéis, serviços e grupos reais nas propostas de desenho.
- **Cuidado:** nomes de papéis e grupos (como "Fila CSC - Pagamentos") são aceitáveis; se vier nome de pessoa, apague.

### 13. Conexões externas cadastradas (só os nomes)
- [ ] **Por que:** `DB.ExecuteDataTable(sql, "NOME_CONEXAO")` consulta outras bases pelo nome cadastrado; saber os nomes evita
  script errado.
- **Como fazer:** em produção:
  ```sql
  SELECT SHORT_NAME, TYPE, ENABLED FROM SV_DB_CONNECTION ORDER BY SHORT_NAME;
  ```
- **Como enviar:** arquivo `conexoes.txt`.
- **O chat faz:** documenta em `guias/sql.md` quais bases externas existem.
- **Cuidado:** **não** traga a coluna `CONNECTION_STRING` (tem servidor e senha). A consulta acima já a omite.

### 14. Motivos de interrupção de ANS
- [ ] **Por que:** responde perguntas de prazo e de pausa na aprovação.
- **Como fazer:** em produção:
  ```sql
  SELECT DESCRICAO, COMENTARIO_OBRIGATORIO, TEMPO_MAXIMO FROM MOTIVO_INTER_SLA ORDER BY DESCRICAO;
  ```
- **Como enviar:** arquivo `motivos_ans.txt`.
- **O chat faz:** acrescenta os motivos a `guias/aulas_resumo.md` (seção de ANS e ANO).

### 6. XMLs exportados de produção
- [ ] **Por que:** os 76 XMLs atuais parecem vir de **Qualidade** (trazem 868 campos que a produção não tem). XMLs da produção
  deixam os resumos fiéis ao que roda de verdade.
- **Como fazer:** use a lista do item 2 e exporte da **produção** os fluxos que você mais mexe (guia geral, "XMLs"). Poucos já ajudam.
- **Como enviar:** copie os `.xml` para `XMLs para teste` e avise os nomes.
- **O chat faz:** `tools/fluxo.py resumir`, `guias.py`, `mascarar.py`, reindexa e remonta a skill.
- **Cuidado:** XML contém dados da empresa e credenciais na biblioteca de scripts; só o resumo mascarado vai para o projeto
  publicado.

### 12. Material do Felipe (autorização recebida em 2026-10-25)
- [~] **Já incorporado:** aulas por tema, padrões de erro de script, imports, regras de aprovação e ANS/ANO.
- **Ainda falta:** (a) os XMLs a mais (ele tem 104, nós 76); (b) a leitura literal de 464 scripts que ele ainda não leu;
  (c) dividir o trabalho para não repetir (ex.: ele revisa scripts, você levanta banco e prints).
- **Como fazer:** peça a ele, por conversa, os XMLs que não temos (só com o OK dele e o da empresa) e a lista dos scripts que
  ele considera mais importantes. Combine quem faz o quê.
- **Como enviar:** os XMLs como no item 6; combinados em texto no chat.

### 7. Diário de perguntas reais
- [ ] **Por que:** com 10 a 20 perguntas reais e a resposta certa, o chat monta testes da skill e corrige o que ela erra.
- **Como fazer:** durante o estágio, anote cada pergunta que fizer à skill ou ao chat, se a resposta estava certa e, se não,
  o que era o certo e onde você conferiu. Pode ser no celular, em qualquer app de notas.
- **Como enviar:** texto no chat, no formato abaixo, quando juntar umas 10:
  ```
  P: <pergunta>
  R: certa / errada / parcial
  Certo seria: <uma linha>
  Onde conferi: <tela, colega, documentação>
  ```
- **O chat faz:** cria casos de teste, ajusta a descrição e o conteúdo da skill e registra em `guias/receitas.md`.

### 8. Prints das telas de propriedades do Editor de Processos
- [ ] **Por que:** a documentação é de 2018; os prints confirmam os nomes e as opções na versão que você usa.
- **Como fazer:** um print de cada janela de propriedades: Tarefa, Data Object de Aprovação, Entrada de Dados (diálogo de campos),
  Desvio Exclusivo, atividade Subprocesso, Link Inicial, Evento de mensagem e Timer.
- **Como enviar:** PNGs (guia geral, "Imagens").
- **O chat faz:** corrige nomes e opções em `guias/desenho_fluxos.md`.

### 15. Quatro comportamentos das aulas, na versão real (opcional)
- [ ] **Por que:** as aulas são de 2020. Estes pontos mudam o desenho de fluxos e não estão confirmados na 19.1.1.
- **Como fazer (em Qualidade):**
  (a) hierarquia **Única** com dois aprovadores exige os dois, e `Mínimo aprovadores = 1` deixa um bastar;
  (b) pausa do ANS na etapa de aprovação, com o motivo permitido no acordo e na atividade;
  (c) `Quantidade máxima de execuções = 1` no evento de mensagem evita repetição quando a OS volta;
  (d) iniciador por Timer: gera OS retroativa no mesmo dia? gera sem responsável?
- **Como enviar:** texto, uma linha por ponto: "funcionou como a aula" ou o que viu de diferente.
- **O chat faz:** corrige `guias/aulas_resumo.md` e `guias/contexto.md`.

---

## Quando der

### 9. Pendências do banco listadas em `guias/consultas_banco.md`
- [ ] Valores de `PESSOA.ATIVO`, `TIPO_COLABORADOR` e `TIPO` (a primeira consulta rodou sem resultado colado), dono de
  `CAD_FUNCIONARIO_V` e `SV_PARAM` (sinônimos), chaves estrangeiras e matrícula repetida no RH.
- **Como fazer e enviar:** as consultas prontas estão naquele arquivo; siga o guia geral desta página.

### 10. Padrões internos da equipe (se existirem por escrito)
- [ ] Nomes de campos e papéis, checklist de subida de Qualidade para Produção, quem aprova, modelos de comunicado padrão.
- **Como enviar:** o documento (sem dados pessoais) ou um resumo em texto.
- **O chat faz:** acrescenta a `guias/contexto.md` e passa a seguir os padrões nas propostas.

---

## O que o chat faz sozinho (sem depender de entrega)
- Testes automáticos da skill com as perguntas do item 7 e ajuste da descrição para ela ser acionada nos momentos certos.
- Um comando único de atualização (reindexar, mascarar, remontar a skill) a cada entrega.
- Novas receitas sempre que uma pergunta real se repetir.

## Registro de entregas
| Data | Item | O que foi incorporado |
|---|---|---|
| 2026-10-25 | 12 (parcial) | Material do Felipe: aulas por tema, padrões de erro de script, imports, regras de aprovação e ANS/ANO |
| 2026-10-28 | 1, 2, 11, 14, 4 (parcial) | Schema completo de produção (776 tabelas); mapa de fluxos por volume (`catalogo/fluxos_producao.*`); versão 19.1.1; motivos de interrupção do ANS; prints do Object Browser (OrdemServico, Utils, QueryString, PowerShell, WebService, Formulario) em `catalogo/api_19_object_browser.md` |
