# GrupoPapel

Caminho: Customização > Modelo de objetos > Processo > GrupoPapel

Grupos de Trabalho relacionados em um papel para recuperação de atores do tipo solucionador.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ConsiderarPeriodosUteis** | Na recuperação das pessoas deve ser levando em consideração o cadastro de períodos úteis do calendário da pessoa versus a data/hora corrente do sistema. Se um solucionador recuperado não possuir um calendário ou se possui um calendário sem definição de períodos úteis, então esta regra será ignorada e será considerado que a pessoa possui disponibilidade 24x7. | Booleano |
| **GrupoTrabalho** | Grupo de Trabalho que contem os solucionadores e coordenadores que serão recuperados pelo papel | [GrupoTrabalho](objetos_grupotrabalho) |
| **GrupoTrabalhoId** | Identificador do Grupo Trabalho associado | Inteiro |
| **IncluirSubniveis** | Indica que grupos filhos devem ser incluídos na recuperação. | Booleano |
| **PapelClasseNegocioId** | Papel de processo proprietário da regra por Grupo de Trabalho | Inteiro |
| **Prioridade** | As regras por Grupo de Trabalho serão ordenadas por Prioridade no sentido ascendente e o processamento será interrompido assim que o primeiro agrupamento da Prioridade retornar no mínimo uma pessoa. | Inteiro |
| **RegraRecuperacao** | Define quais colaboradores do grupo devem ser recuperados | [RecuperacaoPapelGrupo](enum_recuperacaopapelgrupo) |
| **SomenteMesmaUnidade** | São incluídas na recuperação apenas pessoas que estão localizadas na mesma Unidade de Negócio do Cliente da ocorrência. Se o Cliente não possuir uma localidade definida então esta regra será ignorada. | Booleano |
