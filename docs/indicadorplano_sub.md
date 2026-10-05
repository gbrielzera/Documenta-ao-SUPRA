# Indicador de Plano de Gestão

Caminho: Janelas > Processo > Plano Gestão > Indicador de Plano de Gestão

Indicador de Plano de Gestão

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Indicador** | Um Indicador de Desempenho, também conhecido como KPI (Key Performance Indicator), define uma medição realizada sobre a execução de Processos ou base de Ativos. Indicadores representam uma importante ferramenta para monitoramento e gerenciamento dos Serviços. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
|---|---|
| **Meta** | Meta estabelecida para o Indicador dentro do plano. Indicadores podem ter metas variadas entre Planos de Gestão distintos ou no mesmo Plano em Períodos distintos. Quando modificado são atualizados os Períodos cuja Meta é igual a valor antigo da Meta de Indicador. No painel de Indicadores do Executive Dashboard valores apurados acima da meta são exibidos na cor verde, enquanto valores abaixo da meta e acima da tolerância são exibidos em amarelo. Para valores apurados abaixo da meta e tolerância a exibição é feita na cor vermelha. Para valores acima da meta ainda existe a possibilidade de exibição na cor azul caso o valor seja também superior ao desafio estabelecido para o Indicador. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna META da tabela [INDICADOR_PLANO](dados_indicador_plano). |
| **Tolerância** | Indica a tolerância para atingir a meta. Valores apurados abaixo da meta e acima da tolerância (dependo do sentido do melhor resultado) são exibidos com farol Amarelo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - O campo 'Tolerância' deve ser maior ou igual a 0 - O campo 'Tolerância' deve ser menor ou igual a 100 Este campo é mantido na coluna TOLERANCIA da tabela [INDICADOR_PLANO](dados_indicador_plano). |
| **Desafio** | Valor acima da meta definido desafio no plano de metas da gestão. No painel de Indicadores do Executive Dashboard períodos que atingirem este valor são exibidos na cor azul. Assim como no campo Metas o Desafio pode ser redefinido nos diversos períodos do Plano de Gestão. |
| **Responsável** | Responsável pela gestão do Indicador. Para usuários responsável pelo Indicador é possível edição de campos na tela de Workspace. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Visibilidade restrita ao responsável pelo indicador** | Define que o indicador só será visivel ao Responsável ou seus Coordenadores de Grupo de Trabalho. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna RESTRITO_RESPONSAVEL da tabela [INDICADOR_PLANO](dados_indicador_plano). |

| **Períodos** | Períodos definidos para o Plano de Gestão. Os períodos são definidos pela 'Data início' e 'Data fim' do Plano de Gestão. Todos os registros desta coleção de dados são mantidos na tabela [PERIODO_PLANO](dados_periodo_plano). |
|---|---|
