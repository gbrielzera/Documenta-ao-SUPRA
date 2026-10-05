# AcaoAcordo

Caminho: Customização > Modelo de objetos > Processo > AcaoAcordo

Ações disparadas pela atividade (email, encaminhamento etc) mediante a um marca atingida no tempo do Acordo de Nível Operacional.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Acao** | Ação executada quando for atingido o tempo configurado | [OpcaoAcaoAcordo](enum_opcaoacaoacordo) |
| **AtividadeId** | Identificador da Atividade proprietária da Ação. | Inteiro |
| **CodigoGrupoANO** | Código utilizado para sincronizar ações entre atividades contidas no mesmo grupo de Acordo de Nível Operacional | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um AcaoAcordo | Inteiro |
| **ModeloComunicado** | Modelo de comunicado utilizado para compor o email que será enviado | [ModeloComunicado](objetos_modelocomunicado) |
| **ModeloComunicadoId** | Identificador do Modelo de comunicado | Inteiro |
| **PapelProcesso** | Papel utilizado para recuperar pessoas ou filas de destino para encaminhamento ou envio de emal | [PapelProcesso](objetos_papelprocesso) |
| **PapelProcessoId** | Identificador do papel utilizado para obter as pessoas ou filas de destino | Inteiro |
| **Percentual** | Percentual do tempo o Acordo de Nível Operacional que determina o momento de execução da ação. Se for igual a 0 então a ação não será executada. | Decimal |
| **Temporalidade** | Define para a ação do tipo email após quantos dias a mensagem será excluída da base de dados. Se for 0 (zero) ela será excluída assim que o email for enviado. Se estiver sem preenchimento a mensagem não será excluída. | Inteiro |
