# SomenteUltimaExecucao

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > SomenteUltimaExecucao

São considerados apenas os solucionadores envolvidos na última execução da atividade.

**Exemplo 1: modificação da propriedade SomenteUltimaExecucao**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade SomenteUltimaExecucao
papelClasseNegocio.SomenteUltimaExecucao = true;
# salva modificação da propriedade SomenteUltimaExecucao
PapelClasseNegocio.Salva(papelClasseNegocio)
```
