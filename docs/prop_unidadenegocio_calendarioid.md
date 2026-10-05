# CalendarioId

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > CalendarioId

Identificador do Calendário associado

**Exemplo 1: modificação da propriedade CalendarioId**

```
# carrega objeto UnidadeNegocio de identificador 1
unidadeNegocio = UnidadeNegocio.Carrega(1)
# modifica a propriedade CalendarioId
unidadeNegocio.CalendarioId = 1;
# salva modificação da propriedade CalendarioId
UnidadeNegocio.Salva(unidadeNegocio)
```
