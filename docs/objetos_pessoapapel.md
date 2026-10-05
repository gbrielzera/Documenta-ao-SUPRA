# PessoaPapel

Caminho: Customização > Modelo de objetos > Processo > PessoaPapel

Pessoas relacionadas para recuperação. A seleção destas pessoas ainda está condicionada a configuração de parâmetros complementadores no papel.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ConsiderarPeriodosUteis** | A pessoa ou fila só será recuperada se o seu cadastro de períodos úteis possuir um período que contém a data/hora corrente do sistema. Se a pessoa ou fila não possuir um calendário ou este não possuir ainda definição de períodos úteis, então esta regra será ignorada considerando então que a mesma possui disponibilidade 24x7. | Booleano |
| **PapelClasseNegocioId** | Identificador do Papel proprietário da regra | Inteiro |
| **Pessoa** | Pessoa ou fila relacionada pela regra | [Pessoa](objetos_pessoa) |
| **PessoaId** | Identificador da pessoa relacionada | Inteiro |
| **Prioridade** | As regras por Pessoas/filas serão ordenadas por Prioridade no sentido ascendente e o processamento será interrompido assim que o primeiro agrupamento da Prioridade retornar no mínimo uma pessoa ou fila. Durante o processamento de cada agrupamento serão levados em consideração os parâmetros de períodos úteis e Unidade de negócio. | Inteiro |
| **SomenteMesmaUnidade** | A pessoa só será incluída na recuperação se estiver localizada na mesma Unidade de Negócio do Cliente da ocorrência. Se o Cliente não possuir uma localidade definida então esta regra será ignorada. | Booleano |
