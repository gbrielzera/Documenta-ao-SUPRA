# SubProcessoId

Caminho: Customização > Modelo de objetos > Processo > Diagrama > SubProcessoId

Identificador do SubProcesso associado

**Exemplo 1: modificação da propriedade SubProcessoId**

```
# carrega objeto Diagrama de identificador 1
diagrama = Diagrama.Carrega(1)
# modifica a propriedade SubProcessoId
diagrama.SubProcessoId = 1;
# salva modificação da propriedade SubProcessoId
Diagrama.Salva(diagrama)
```
