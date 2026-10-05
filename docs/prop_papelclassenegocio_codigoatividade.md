# CodigoAtividade

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > CodigoAtividade

Código da atividade para recuperação de solucionadores envolvidos.

**Exemplo 1: modificação da propriedade CodigoAtividade**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade CodigoAtividade
papelClasseNegocio.CodigoAtividade = "Código da atividade";
# salva modificação da propriedade CodigoAtividade
PapelClasseNegocio.Salva(papelClasseNegocio)
```
