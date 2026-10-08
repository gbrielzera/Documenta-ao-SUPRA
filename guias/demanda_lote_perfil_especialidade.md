# Demanda em andamento: Atualizar Perfil/Especialidade em LOTE
Caminho: Guias > Demandas > Atualizar Perfil/Especialidade - LOTE

Estado em 2026-10-08: analisada, não implementada. O documento de requisitos ainda não foi lido
(o usuário ficou de enviar); os pontos marcados com (?) dependem dele.

## Pedido
Disponibilizar, no fluxo "Serviços do Programa Valor > Atualizar Perfil/Especialidade", inclusão ou
atualização em lote por planilha: até 3 perfis por técnico e até 1 especialidade por perfil
(até 3 especialidades por matrícula).

## Fluxo original
`fluxos/Programa_Valor_Versão_15_Atualizar_Perfil-Especialidade.md` (sigla ATTPERFILESPEC, serviço
ATUALIZARPERFILESPECIALIDADE). Evento Inicial (Cliente) → aviso → tarefa "Aprovação do Gerente de
Centro" (Código APROV) → gateway `PossuiAprovacao('APROV')` → justificativa → aviso → fim.
Não grava em nenhuma tabela: o resultado é a própria OS aprovada.

Campos: `FAVORECIDO_COBRA` (ID_PESSOA do técnico), `TE_MATRICULA`, `TE_UOR`, `COMBOBOX` (Perfil 1),
`COMBOBOX1` (Especialidade principal), `COMBOBOX_BOX1` (Perfil 2), `COMBOBOX2` (Esp. secundária),
`COMBOBOX_SIM_NAO` (Perfil 3), `COMBOBOX3` (Esp. terciária), `DESCRICAO_DETALHADA` (Comentário).
Papéis 277, 278 e 1349 dependem de `FAVORECIDO_COBRA`.

## Regras de validação (extraídas dos scripts da versão 15)
1. Perfil 1 é um dos 7 perfis; a especialidade 1 pertence a `especialidades_principais[perfil1]`.
2. Perfis 2 e 3 só existem se a especialidade 1 estiver em `especialidades_hibridas`.
3. Perfis 2 e 3 só podem ser "Téc. de Soluções" ou "Téc. de Suporte Administrativo".
4. Especialidade 2 ∈ `especialidades_secundarias[perfil2]`; especialidade 3 ∈ `especialidades_terciarias[perfil3]`.
5. Sem repetir especialidade; perfil 2 pode ser igual ao perfil 1 com especialidade diferente.
6. Não há perfil 3 sem perfil 2, nem especialidade sem o seu perfil.
As listas completas estão no `ScriptFormCarregado` do Evento Inicial do fluxo original.

## Plano proposto (o usuário concorda com a ideia geral)
Padrão dos lotes existentes (receita 16): fluxo novo "Atualizar Perfil/Especialidade - LOTE".
1. Evento Inicial: anexo "Planilha" (classe Arquivo) + checkbox "ler planilha" + GRID com colunas
   `MATRICULA`, as dos campos originais, `NOME`, `UOR`, `VALIDACAO`, `OS_GERADA`.
2. `ScriptModificado` do checkbox: lê o .xlsx, valida linha a linha (matrícula existe e está ativa,
   sem duplicata, regras acima) e preenche o GRID.
3. `ScriptValidacao` do Evento Inicial: `Criticas.AdicionaPendencia` se houver linha com erro.
4. Atividade Subprocesso: para cada linha OK e sem `OS_GERADA`, cria a OS filha, preenche
   `FAVORECIDO_COBRA` (ID_PESSOA pela matrícula), `TE_MATRICULA`, `TE_UOR` e os 6 campos de perfil.
   Cliente da filha = quem enviou o lote.

Duas formas de criar a OS filha (decidir com teste):
- **A. Link Inicial**: nova versão do fluxo original com Link Inicial (ApenasChamador) + Associação;
  no lote, `sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)`, `sub.SetCustom(...)`,
  `sub.Salva()`, `sub.AvancaAtividade()`. É o padrão dos lotes existentes.
- **B. Sem alterar o original**: `OrdemServico.Nova(sigla, codigoIniciador, assunto, servico, cliente,
  responsavel, valoresCustomizados)` com um Hashtable dos campos. Exige Código no Evento Inicial.

## Pendências
- (?) Layout da planilha: uma linha por matrícula (6 colunas de perfil/especialidade) ou uma por perfil.
- (?) "Atualização" exige gravar em alguma tabela, além de gerar a OS?
- (?) Aprovação individual por técnico (um e-mail por OS ao gerente) ou agrupada por gerente.
- Limite de linhas por planilha e teste de tempo de execução (10, 50, 200 linhas).
- Restringir quem abre o lote (clientes autorizados do iniciador).
- Conferir duplicidade com OS aberta para a mesma matrícula: consulta 6 de `guias/sql.md` (`CPE_CSC.TE_MATRICULA` existe em produção; o `FAVORECIDO_COBRA` está em `CP_ORDEM_SERVICO`, NVARCHAR2(500), e guarda o ID_PESSOA como texto).
- Confirmar em produção as colunas das tabelas dos campos de perfil (`CPE_CONTRATOS`, `CPE_CONTRATOS02`, `CPE_BOOTCAMP`): consulta 3 de `guias/consultas_banco.md`. `COMBOBOX` (NVARCHAR2 1800) e `COMBOBOX1` (400) já foram conferidos.
- Escrever os scripts (leitura/validação, trava, criação) seguindo a regra de script mínimo.
