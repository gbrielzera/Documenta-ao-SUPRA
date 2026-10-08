# Desenho de fluxos — regras para propor e montar um fluxo
Caminho: Guias > Desenho de fluxos

Usar quando o pedido for "como eu desenho/monto este fluxo", "sugira o fluxo para X" ou uma demanda inteira.
Cada regra traz a fonte: `docs/...` (documentação oficial), `[fluxo]` (observado nos fluxos do cliente) ou
`[banco]`/`[api]`. Parte do checklist foi levantada nas anotações de estudo de um colega e **conferida contra
a documentação desta base** antes de entrar aqui; o que não foi conferido está marcado `[não conferido]`.

## Como entregar uma proposta de desenho
Não basta descrever caixas e setas. Entregar, nesta ordem:
1. **Diagrama em texto**: elementos e ligações (modelo: `## Grafo do fluxo` de qualquer `fluxos/*.md`).
2. **Tabela por elemento**: tipo, descrição, **Código** (se algo vai consultá-lo em script), **papel responsável**,
   campos de Entrada de Dados (nome técnico, rótulo, obrigatório), anexos, aprovação, scripts, comunicado.
3. **Gateways**: tipo, fórmula, alternativas com o valor de comparação.
4. **Iniciadores**: manual, link inicial, timer, regra, mensagem, e quem pode abrir (clientes autorizados).
5. **O que depende da instalação** (campos novos, papéis, modelos de comunicado, serviços) e **o que testar** em Qualidade.
6. Fluxo parecido que serve de modelo: `fluxos/_INDICE.md` (marca grid, aprovação, lote, API, planilha).

## Passo a passo no Editor (resumo de docs/criando_fluxos_de_processos.md, docs/tutorial_01.md)
1. Macroprocesso > Processo > **versão Em Edição** > Subprocesso. O Subprocesso é o fluxo desenhado; o **Tipo de
   Subprocesso** guarda o que não muda entre versões (sigla, dono, serviços) — docs/criando_um_sub-processo.md.
2. Inserir elementos pela Toolbox (clique no elemento, depois no desenho); **ligar** com o item Fluxo, arrastando de um
   conector até o do destino. Data Objects se inserem clicando sobre a atividade a que pertencem.
3. Responsável de cada atividade = **Papel**; conferir quem o papel recupera numa OS real (docs/cadastrar_usuario_2_2.md).
4. Data Objects: Entrada de Dados, Itens de Configuração (anexos), Aprovação, Genérico.
5. Scripts, comunicados, ANS/ANO conforme o requisito.
6. **Validar Versão** e **Ativar** (a ativação valida de novo e recusa configuração inválida). Validar não substitui testar
   abertura, avanço, aprovação, reprovação, devolução, cancelamento e encerramento (recomendação das anotações do colega, não da doc).

## Desenhar com os objetos reais da Toolbox
Um desenho tem de mostrar os Data Objects verdadeiros e suas ligações, não só caixas BPMN: Entrada de Dados (laranja) ligada ao iniciador, tarefa ou finalizador; Aprovação (verde) ligada a uma tarefa; Itens de Configuração para anexos; o responsável de cada atividade (papel); as alternativas de cada desvio; mensagens e finalização. Campos propostos precisam ser validados pela área antes do cadastro. Tarefas automáticas usam Script Início com `AvancaProximaAtividade = True` (`guias/scripts.md`).

## Tarefas e responsabilidade
- Responsável é um **Papel** (docs/tarefas.md). Papel de pessoa fixa, fila, grupo, área, campo da OS, composição ou script
  (docs/tipos_papeis.md); critério final: menos OS abertas, fila (FIFO) ou todos; prioridade numérica menor vence.
- `Permissão restrita Papel responsável` (`PermissaoRestritaPapel`): só quem tem o papel pode assumir a tarefa
  (docs/prop_atividade_permissaorestritapapel.md). Sem ela, outra pessoa consegue executar.
- `Permite voltar` habilita o comando Voltar do assistente (docs/tarefas.md). Um caminho de devolução **desenhado** é outra coisa.
- **Código** da atividade e do gateway é **único dentro da versão do subprocesso** e é o que scripts usam
  (`PossuiAprovacao("COD")`, `ObtemMotivoGateway("COD")`) — docs/prop_atividade_codigo.md, docs/prop_gateway_codigo.md.
- Cliente, favorecido, responsável e quem abriu são pessoas diferentes. Nos fluxos do cliente o favorecido costuma ser um
  campo próprio (`FAVORECIDO_COBRA`, ID_PESSOA) e os papéis de gestor partem dele [fluxo]. Não os trate como iguais.

## Campos (Entrada de Dados)
- Obrigatório bloqueia o avanço (pendência); **Opcional recomendado** só gera aviso (docs/data_obj_entrada_de_dados.md).
- Nome técnico ≠ rótulo (Descrição resumida) ≠ controle visual ≠ regra de preenchimento.
- `Coluna` organiza o layout; Listagem de Registros (grid) aceita edição no formulário, na própria linha ou popup (docs/controle_grid.md).
- Anexo = Item de Configuração do tipo Artefato/arquivo; **Requerido inicialização** e **Produzido ao término** indicam
  entrada e saída e são **mutuamente exclusivos** (docs/dados_classe_anexo.md). Desenhar o ícone de documento não torna o anexo obrigatório.
- Criar campo novo: tabela `CPE_*`, nunca `CP_ORDEM_SERVICO` (cheia, 1000 colunas) — `guias/sql.md` [banco].

## Aprovação (docs/data_obj_aprovacao.md)
- É um Data Object associado a uma **Tarefa**; aprovadores por Papel.
- **Campos para Aprovação** = o que o aprovador analisa; **Campos para Preenchimento** = o que ele informa (obrigatório ao
  aprovar, reprovar, ambos ou nenhum).
- Padrão: todos precisam aprovar e **uma reprovação reprova tudo**. Mudam isso `Mínimo aprovadores` e `Reprovar imediatamente`.
- Campos aprovados ficam bloqueados; alternativas: cancelar/nova versão da aprovação ou **Permitir modificação após aprovação**.
- A solicitação inicia ao entrar na tarefa; `Iniciar automaticamente = falso` passa isso ao solucionador.
- Pré-aprovação (reaproveitar aprovação anterior ou a identidade do solicitante) só com condições; não ligar por conveniência.
- Rótulos dos botões (`RotuloBotaoAprovar`/`Reprovar`) **não criam um terceiro estado**: as situações são só
  `Elaboracao`, `Pendente`, `Aprovado`, `Reprovado`, `Cancelado` (docs/enum_situacaoaprovacao.md). Em produção só existem as
  quatro primeiras [banco]. Para "devolver" x "rejeitar" é preciso um campo/rota próprios.
- Depois da aprovação: desvio exclusivo com `OrdemServico.PossuiAprovacao("COD")` ou a **Regra de Desvio** (docs/por_formula.md). O argumento é o **Código da tarefa de aprovação**. `PossuiAprovacao` só é verdadeiro com a aprovação finalizada como Aprovada: `False` também ocorre com aprovação pendente, então o gateway tem de vir depois da conclusão da aprovação. Reprovação não implica cancelar a OS; o caminho da reprovação (nova tentativa, justificativa, cancelamento) é decisão de negócio.

## Desvios
- **Exclusivo** (por fórmula): avalia IronPython e compara com o `Valor comparação`; vale a primeira alternativa satisfeita pela
  sequência de avaliação. **Por Evento**: o solucionador responde uma pergunta (docs/pergunta_e_resposta.md).
- **Paralelo**: cada saída gera uma OS filha, sem condição (docs/paralelo.md). **Inclusivo**: gera as alternativas verdadeiras
  (docs/desvio_inclusivo.md). A enumeração `TipoGateway` só lista os dois exclusivos; isso não prova que os outros não existam.

## Subprocessos e iniciadores
- Chamada de subprocesso exige **Associação** (frase e inversa), parâmetros de entrada/saída e a decisão assíncrono/síncrono
  (docs/subprocessos.md). O destino precisa de um **Link Inicial** com a associação inversa (docs/iniciador_link_inicial.md);
  um fluxo pode ter vários iniciadores de origens diferentes (docs/iniciador_multiplas_formas_subpr.md).
- **Timer**: o campo Responsável é obrigatório; sem ele a máquina de processos ignora o iniciador e não gera OS
  (docs/iniciador_por_temporizador.md). `[não conferido]` fluxo só com timer não abre manualmente no Portal.
- Iniciador por mensagem: e-mail ou WebService (docs/iniciador_por_mensagem.md). Não rodar o exemplo da doc em caixa real
  (ele remove os e-mails processados).
- Finalizadores: sucesso x cancelamento (cancelamento exige motivo); Link Final gera/associa outra OS.

## Comunicados, prazos e scripts
- Evento de mensagem: modelo de comunicado + destinatários por papel e/ou lista fixa; a descrição do evento entra no assunto.
- ANS = compromisso de atendimento (calendário, serviço, interrupções); ANO = prazo de tarefa (minutos, % do ANS ou esforço).
- Onde roda cada script: `guias/scripts.md`. Importar fluxo copia scripts que dependem de IDs e campos do ambiente de origem
  (docs/importacao.md): revisar depois de importar.

## Divergências da documentação a lembrar ao desenhar
Ver `guias/contexto.md` > "Divergências conhecidas da documentação" (chamada assíncrona, tipos de evento inicial, enumeração de gateway).
