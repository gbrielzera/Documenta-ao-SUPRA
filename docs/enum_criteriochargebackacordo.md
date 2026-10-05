# CriterioChargeBackAcordo

Caminho: Customização > Modelo de objetos > Recurso > Enumerações > CriterioChargeBackAcordo

Critério de cobrança do Acordo de Nível de Serviço pela rotina de Charge-back

| **Valor** | **Descrição** |
|---|---|
| **Nenhum** | O Acordo de Nìvel de Serviço não está sujeito a cobrança do Cliente por rotina de Charge-back. |
| **Ocorrencia** | A Área cliente é cobrada por quantidade de Ordens de Serviço atendidas pelo Acordo de Nível de Serviço. Para obter o valor total o sistema multiplica a quantidade de Ordens de Serviço pelo Valor de Charge-back configurado no acordo. |
| **Hora** | A Área cliente é cobrada por horas apontadas em Ordens de Serviço atendidas pelo Acordo de Nível de Serviço (inclui derivadas da Ordem de Serviço). Para obter o valor total o sistema multiplica a quantidade de horas apontadas pelo Valor de Charge-back configurado no acordo. |
| **ValorFixo** | A Área cliente é cobrada em um valor Fixo enquanto válido o Acordo de Nível de Serviço. |
| **Formula** | O valor de Charge-back é obtivo por fórmula. A fórmula deve obrigatoriamente retornar um valor numérico caso contrário ocorrerá um erro durante a apuração de Charge-back. |
