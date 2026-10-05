# VisivelPainelWorkspace

Caminho: Customização > Modelo de objetos > Processo > NivelSLA > VisivelPainelWorkspace

Indica que Ordens de Serviço neste nível serão exibidas no Painel de Alertas da transação Workspace. Esta configuração ainda está condicionada a regra de visualização do Grupo de Trabalho (veja as configurações do Grupo de Trabalho do solucionador).

**Exemplo 1: modificação da propriedade VisivelPainelWorkspace**

```
# carrega objeto NivelSLA de identificador 1
nivelSLA = NivelSLA.Carrega(1)
# modifica a propriedade VisivelPainelWorkspace
nivelSLA.VisivelPainelWorkspace = true;
# salva modificação da propriedade VisivelPainelWorkspace
NivelSLA.Salva(nivelSLA)
```
