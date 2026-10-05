# ComposicaoPapel

Caminho: Customização > Modelo de objetos > Processo > ComposicaoPapel

Permite que um Papel seja definido pela composição de um ou mais Papéis. No primeiro caso ocorre um simples redirecionamento no instante de cálculo de Atores enquanto no segundo são retornados todos os Atores (soma) de todos os Papéis configurados na composição. A rotina de cálculo de Atores possui função de recursividade, ou seja, se o Papel A é composto por B e C, e B por sua vez composto por D e E, então o resultado total de A é igual a soma de C, D e E.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **PapelClasseNegocioId** | Identificador do Papel de Classe de Negócio composto | Inteiro |
| **PapelComposicao** | Papel de Classe de Negócio utilizado na Composição de outro Papel | [PapelClasseNegocio](objetos_papelclassenegocio) |
| **PapelComposicaoId** | Identificador do Papel utilizado na Composição | Inteiro |
| **Prioridade** | Os papéis da composição serão ordenadas por Prioridade no sentido ascendente e o processamento será interrompido assim que o primeiro agrupamento da Prioridade retornar no mínimo uma pessoa. | Inteiro |
