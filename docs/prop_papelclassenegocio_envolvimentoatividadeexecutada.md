# EnvolvimentoAtividadeExecutada

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > EnvolvimentoAtividadeExecutada

Recupera solucionadores pelo tipo de envolvimento na execução da atividade.

**Exemplo 1: modificação da propriedade EnvolvimentoAtividadeExecutada**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade EnvolvimentoAtividadeExecutada
papelClasseNegocio.EnvolvimentoAtividadeExecutada = "Inicial";
# salva modificação da propriedade EnvolvimentoAtividadeExecutada
PapelClasseNegocio.Salva(papelClasseNegocio)
```
