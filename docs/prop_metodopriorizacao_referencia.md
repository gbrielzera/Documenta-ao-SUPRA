# Referencia

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao > Referencia

Texto de referência sobre o Método de Priorização. Procure especificar neste campo qual o propósito e a aplicação deste Método de Priorização.

**Exemplo 1: modificação da propriedade Referencia**

```
# carrega objeto MetodoPriorizacao de identificador 1
metodoPriorizacao = MetodoPriorizacao.Carrega(1)
# modifica a propriedade Referencia
metodoPriorizacao.Referencia = "Priorização segundo framework ITIL";
# salva modificação da propriedade Referencia
MetodoPriorizacao.Salva(metodoPriorizacao)
```
