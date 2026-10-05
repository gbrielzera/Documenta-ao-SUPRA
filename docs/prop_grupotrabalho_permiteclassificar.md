# PermiteClassificar

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > PermiteClassificar

Regra de autorização para execução da operação de Classificação de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho.

**Exemplo 1: modificação da propriedade PermiteClassificar**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade PermiteClassificar
grupoTrabalho.PermiteClassificar = "ResponsavelCoordenadores";
# salva modificação da propriedade PermiteClassificar
GrupoTrabalho.Salva(grupoTrabalho)
```
