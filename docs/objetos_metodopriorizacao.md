# MetodoPriorizacao

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao

Define uma Metodologia para Priorização de Ocorrências e cálculo de ANS.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CalculoAutomatico** | Indica que o cálculo é automático sempre que ocorrer modificação no campos Cliente, Serviço ou quando for adicionado ou removido um Item de Configuração. | Booleano |
| **ClasseNegocio** | Classe de negócio da Ocorrência onde será aplicado o Método de Priorização. | [ClasseNegocio](enum_classenegocio) |
| **Descricao** | Descrição detalhada da ClasseSeveridade | String |
| **ExpressaoCalculo** | Expressão utilizada para determinar a base de cálculo utilizada para seleção do Grau de Prioridade a partir. Para seleção do Grau de Prioridade é selecionado aquele com Limite Superior maior que o valor resultante na Expressão. A expressão deve retornar obrigatoriamente um número Inteiro não negativo. | String |
| **Graus** | Graus de Pririodade | [Lista de GrauPrioridade](objetos_grauprioridade) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Método de Priorização de Ocorrências. | Inteiro |
| **Referencia** | Texto de referência sobre o Método de Priorização. Procure especificar neste campo qual o propósito e a aplicação deste Método de Priorização. | String |
| **Variaveis** | Variáveis utilizada para compor a Prioridade da Ocorrência. | [Lista de VariavelPriorizacao](objetos_variavelpriorizacao) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | MetodoPriorizacao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo MetodoPriorizacao | MetodoPriorizacao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | MetodoPriorizacao Carrega(string nomePropriedade, object valorPropriedade); |
