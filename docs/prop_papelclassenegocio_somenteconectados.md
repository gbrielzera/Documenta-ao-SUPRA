# SomenteConectados

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > SomenteConectados

Seleciona entre as pessoas recuperadas pela configuração aqueles que são usuários solucionadores conectados na aplicação Supravizio.

**Exemplo 1: modificação da propriedade SomenteConectados**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade SomenteConectados
papelClasseNegocio.SomenteConectados = true;
# salva modificação da propriedade SomenteConectados
PapelClasseNegocio.Salva(papelClasseNegocio)
```
