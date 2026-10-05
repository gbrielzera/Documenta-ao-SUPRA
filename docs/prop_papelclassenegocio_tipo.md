# Tipo

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > Tipo

Forma de recuperação de pessoas utilizada no cálculo do papel de processo

**Exemplo 1: modificação da propriedade Tipo**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade Tipo
papelClasseNegocio.Tipo = "RelacaoPessoas";
# salva modificação da propriedade Tipo
PapelClasseNegocio.Salva(papelClasseNegocio)
```
