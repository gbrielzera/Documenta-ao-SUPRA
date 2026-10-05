# PermiteEncaminhar

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > PermiteEncaminhar

Regra de autorização para execução da operação de Encaminhamento de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho.

**Exemplo 1: modificação da propriedade PermiteEncaminhar**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade PermiteEncaminhar
grupoTrabalho.PermiteEncaminhar = "ResponsavelCoordenadores";
# salva modificação da propriedade PermiteEncaminhar
GrupoTrabalho.Salva(grupoTrabalho)
```
