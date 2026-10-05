# Referencia

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > Referencia

Descritivo completo do Papel. Este descritivo é utilizado na geração de documentação de Processos.

**Exemplo 1: modificação da propriedade Referencia**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade Referencia
papelClasseNegocio.Referencia = "Referência";
# salva modificação da propriedade Referencia
PapelClasseNegocio.Salva(papelClasseNegocio)
```
