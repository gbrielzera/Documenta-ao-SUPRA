# Nome

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > Nome

Descritivo utilizado para nomear um Papel.

**Exemplo 1: modificação da propriedade Nome**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade Nome
papelClasseNegocio.Nome = "Nome";
# salva modificação da propriedade Nome
PapelClasseNegocio.Salva(papelClasseNegocio)
```
