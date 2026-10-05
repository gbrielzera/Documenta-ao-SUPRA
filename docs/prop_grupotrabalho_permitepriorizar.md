# PermitePriorizar

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > PermitePriorizar

Regra de autorização para execução da operação de Priorização de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho.

**Exemplo 1: modificação da propriedade PermitePriorizar**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade PermitePriorizar
grupoTrabalho.PermitePriorizar = "ResponsavelCoordenadores";
# salva modificação da propriedade PermitePriorizar
GrupoTrabalho.Salva(grupoTrabalho)
```
