# Descricao

Caminho: Customização > Modelo de objetos > Processo > GrupoIndicador > Descricao

Texto que descreve com clareza a classificação de Indicadores.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto GrupoIndicador de identificador 1
grupoIndicador = GrupoIndicador.Carrega(1)
# modifica a propriedade Descricao
grupoIndicador.Descricao = "Descrição";
# salva modificação da propriedade Descricao
GrupoIndicador.Salva(grupoIndicador)
```
