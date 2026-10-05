# Ativo

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > Ativo

Indica que o Papel está ativo no Sistema. Quando inativo o Papel é ignorado pela rotina de cálculo de Atores.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade Ativo
papelClasseNegocio.Ativo = true;
# salva modificação da propriedade Ativo
PapelClasseNegocio.Salva(papelClasseNegocio)
```
