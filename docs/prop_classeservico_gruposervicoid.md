# GrupoServicoId

Caminho: Customização > Modelo de objetos > Processo > ClasseServico > GrupoServicoId

Identificador do Grupo de Servicos associado

**Exemplo 1: modificação da propriedade GrupoServicoId**

```
# carrega objeto ClasseServico de identificador 1
classeServico = ClasseServico.Carrega(1)
# modifica a propriedade GrupoServicoId
classeServico.GrupoServicoId = 1;
# salva modificação da propriedade GrupoServicoId
ClasseServico.Salva(classeServico)
```
