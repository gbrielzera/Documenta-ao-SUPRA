# Recurso Aplicado

Caminho: Janelas > Recurso > Contrato > Recurso Aplicado

Recurso a ser Aplicado no cumprimento do Contrato

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Descrição Recurso** | Descrição completa do Recurso. Utilize descritivos de Função, Cargo ou Nome da Pessoa de forma a facilitar a referência na associação com Grupos de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [RECURSO_APLICADO](dados_recurso_aplicado). |
|---|---|
| **Valor mensal** | Valor mensal |
| **Valor hora** | Valor hora padrão para o recurso. O valor final pode variar em função do fator atribuído ao tipo de apontamento realizado. |
| **Quantidade de horas por mês** | Quantidade de horas contratadas por mês. |
| **Validade do saldo restante do mês (em meses)** | Quantidade de meses para validade das horas que não forem utilizadas no mês apurado. Se não for preenchido ou for preenchido com o valor 0 significará que as horas devem ser consumidas no mesmo mês. Se for uma quantidade de meses igual ou superior ao restante de meses do contrato significará que as horas formarão um banco. |

| **Solucionadores** | Grupos de trabalho onde estão lotados os Solucionadores correspondentes ao tipo de recurso do contrato. Todos os registros desta coleção de dados são mantidos na tabela [CONTRATO_TECNICO](dados_contrato_tecnico). |
|---|---|
