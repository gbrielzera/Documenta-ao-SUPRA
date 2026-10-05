# GrauPrioridade

Caminho: Customização > Modelo de objetos > Processo > GrauPrioridade

Graus de Prioridade

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CorIndicadorGrafico** | Cor associada ao nível de ANS. Na tela da de Fila de Ordens de Serviço é exibido um ícone nesta cor indicando o Nível atual de ANS. | [CorIndicadorGrafico](enum_corindicadorgrafico) |
| **Descricao** | Descritivo associado ao Grau de Prioridade | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um GrauPrioridade | Inteiro |
| **LimiteSuperiorCalculo** | Limite superior para determinar seleção do Grau de Prioridade a partir do valor retornado pela Expressão de Cálculo do Método de Priorização. Para determinar o Grau de Prioridade é realizado primeiramente a ordenação dos Graus existentes com base no campo sequência. Em seguida os Graus são comparados com o Limite Superior e é selecionado aquele que apresentar o Limite Superior maior ou igual que o cálculo base. | Inteiro |
| **MetodoPriorizacaoId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Método de Priorização. | Inteiro |
| **Sequencial** | Número de Sequencia para o Nível | Inteiro |
