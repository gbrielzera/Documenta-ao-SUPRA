# Id

Caminho: Customização > Modelo de objetos > Processo > GrupoIndicador > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Grupo Indicador. Este Identificador não pode ser modificado pelo usuário.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto GrupoIndicador de identificador 1
grupoIndicador = GrupoIndicador.Carrega(1)
# modifica a propriedade Id
grupoIndicador.Id = 1;
# salva modificação da propriedade Id
GrupoIndicador.Salva(grupoIndicador)
```
