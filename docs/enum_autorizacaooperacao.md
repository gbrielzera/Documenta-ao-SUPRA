# AutorizacaoOperacao

Caminho: Customização > Modelo de objetos > Recurso > Enumerações > AutorizacaoOperacao

Define regras de autorização para execução de operações em Ordens de Serviço

| **Valor** | **Descrição** |
|---|---|
| **ResponsavelCoordenadores** | A operação pode ser executada pelo responsável corrente pela Ordem de Serviço ou um de seus coordenadores. Para recuperar todos os coordenadores são considerados todos os níveis de grupos até o solucionador responsável. |
| **CoordenadoresResponsaveis** | Somente coordenadores de Grupos de Trablalho responsáveis podem executar a operação. Estes coordenadores são determinados pelo Grupo responsável e todos os seus grupos pai. |
| **TodosCoordenadores** | Todos os coordenadores de Grupos de Trabalho envolvidos no Macroprocesso podem realizar a operação, independente da relação de responsabilidade. |
| **TodosSolucionadores** | Todos os solucionadores envolvidos no Macroprocesso podem realizar a operação. |
| **SolucionadoresGrupoResponsavel** | Todos os solucionadores do Grupo de Trabalho responsável podem executar a operação. |
