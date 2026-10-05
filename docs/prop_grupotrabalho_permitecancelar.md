# PermiteCancelar

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > PermiteCancelar

Regra de autorização para execução da operação de Cancelamento de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho.

**Exemplo 1: modificação da propriedade PermiteCancelar**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade PermiteCancelar
grupoTrabalho.PermiteCancelar = "ResponsavelCoordenadores";
# salva modificação da propriedade PermiteCancelar
GrupoTrabalho.Salva(grupoTrabalho)
```
