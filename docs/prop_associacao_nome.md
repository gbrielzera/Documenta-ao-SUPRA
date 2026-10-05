# Nome

Caminho: Customização > Modelo de objetos > Processo > Associacao > Nome

Nome para identificação e recuperação da Associação. O nome não pode conter espaços e deve conter apenas caracteres alfanuméricos. Também deve ser único entre todas as Associações e utilizado em scripts para recuperação da Associação.

**Exemplo 1: modificação da propriedade Nome**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade Nome
associacao.Nome = "INCIDENTE_PROBLEMA";
# salva modificação da propriedade Nome
Associacao.Salva(associacao)
```
