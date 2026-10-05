# GrupoIndicadorId

Caminho: Customização > Modelo de objetos > Processo > Indicador > GrupoIndicadorId

Identificador do(a) GrupoIndicador associado(a)

**Exemplo 1: modificação da propriedade GrupoIndicadorId**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade GrupoIndicadorId
indicador.GrupoIndicadorId = 1;
# salva modificação da propriedade GrupoIndicadorId
Indicador.Salva(indicador)
```
