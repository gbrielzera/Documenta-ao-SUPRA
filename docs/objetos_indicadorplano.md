# IndicadorPlano

Caminho: Customização > Modelo de objetos > Processo > IndicadorPlano

Indicador de Plano de Gestão

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Desafio** | Valor acima da meta definido desafio no plano de metas da gestão. No painel de Indicadores do Executive Dashboard períodos que atingirem este valor são exibidos na cor azul. Assim como no campo Metas o Desafio pode ser redefinido nos diversos períodos do Plano de Gestão. | Decimal |
| **Indicador** | Um Indicador de Desempenho, também conhecido como KPI (Key Performance Indicator), define uma medição realizada sobre a execução de Processos ou base de Ativos. Indicadores representam uma importante ferramenta para monitoramento e gerenciamento dos Serviços. | [Indicador](objetos_indicador) |
| **IndicadorId** | Identificador do(a) Indicador associado(a) | Inteiro |
| **Meta** | Meta estabelecida para o Indicador dentro do plano. Indicadores podem ter metas variadas entre Planos de Gestão distintos ou no mesmo Plano em Períodos distintos. Quando modificado são atualizados os Períodos cuja Meta é igual a valor antigo da Meta de Indicador. No painel de Indicadores do Executive Dashboard valores apurados acima da meta são exibidos na cor verde, enquanto valores abaixo da meta e acima da tolerância são exibidos em amarelo. Para valores apurados abaixo da meta e tolerância a exibição é feita na cor vermelha. Para valores acima da meta ainda existe a possibilidade de exibição na cor azul caso o valor seja também superior ao desafio estabelecido para o Indicador. | Decimal |
| **Periodos** | Períodos definidos para o Plano de Gestão. Os períodos são definidos pela 'Data início' e 'Data fim' do Plano de Gestão. | [Lista de PeriodoPlano](objetos_periodoplano) |
| **PlanoGestaoId** | Identificador do Plano de Gestão | Inteiro |
| **Responsavel** | Responsável pela gestão do Indicador. Para usuários responsável pelo Indicador é possível edição de campos na tela de Workspace. | [Pessoa](objetos_pessoa) |
| **ResponsavelId** | Identificador da Pessoa associada | Inteiro |
| **RestritoResponsavel** | Define que o indicador só será visivel ao Responsável ou seus Coordenadores de Grupo de Trabalho. | Booleano |
| **Tolerancia** | Indica a tolerância para atingir a meta. Valores apurados abaixo da meta e acima da tolerância (dependo do sentido do melhor resultado) são exibidos com farol Amarelo. | Decimal |
