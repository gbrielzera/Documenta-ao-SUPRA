# Id

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Papel.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade Id
papelClasseNegocio.Id = 1;
# salva modificação da propriedade Id
PapelClasseNegocio.Salva(papelClasseNegocio)
```
