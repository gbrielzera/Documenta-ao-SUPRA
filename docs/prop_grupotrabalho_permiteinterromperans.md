# PermiteInterromperANS

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > PermiteInterromperANS

Regra de autorização para execução da operação de adicionar uma Interrupção de ANS de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho.

**Exemplo 1: modificação da propriedade PermiteInterromperANS**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade PermiteInterromperANS
grupoTrabalho.PermiteInterromperANS = "ResponsavelCoordenadores";
# salva modificação da propriedade PermiteInterromperANS
GrupoTrabalho.Salva(grupoTrabalho)
```
