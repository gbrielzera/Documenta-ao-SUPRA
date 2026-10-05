# Gap

Caminho: Customização > Modelo de objetos > Processo > Gap

Gaps encontrado durante testes de Controles.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Acoes** | Plano de Ação | [Lista de AcaoGap](objetos_acaogap) |
| **ClasseGAP** | Classificação | [ClasseGap](objetos_classegap) |
| **ClasseGAPId** | Identificador do(a) ClasseGAP associado(a) | Inteiro |
| **DeficienciaDesign** | O Controle não pode ser executado conforme descrito na documentação ou não foi possível alcançar seu objetivo. | Booleano |
| **DeficienciaFaltaEvidencia** | Inexistência de documentação suporte que comprove a execução do Controle. | Booleano |
| **DeficienciaOperacional** | O Controle não opera da forma que foi desenhado ou a mesma pessoa que realiza o controle não tem autoridade ou qualificações necessárias. | Booleano |
| **MotivoCancelamento** | Motivo de cancelamento | String |
| **OcorrenciaId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência | Inteiro |
| **Recomendacao** | Recomendação para resolução do Gap. | String |
| **Resumo** | Resumo do Gap | String |
| **RiscosAdicionais** | Riscos adicionais relação ao conjunto definido no cadastro do Controle | [Lista de RiscoGap](objetos_riscogap) |
| **Sequencial** | Sequencial | Inteiro |
| **Situacao** | Situação do Gap | [SituacaoGap](enum_situacaogap) |
| **Titulo** | Descrição sucinta sobre o Gap. É utilizado em cabeçalho de relatórios. | String |
