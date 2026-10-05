# VisivelPainelWorkspace

Caminho: Customização > Modelo de objetos > Processo > Categoria > VisivelPainelWorkspace

Indica que Ordens de Serviço desta categoria serão visíveis na barra de rolagem localizada na parte inferior da tela Workspace (Painel de Alertas). Esta configuração ainda está condicionada a regra de visualização do Grupo de Trabalho (veja as configurações do Grupo de Trabalho do solucionador).

**Exemplo 1: modificação da propriedade VisivelPainelWorkspace**

```
# carrega objeto Categoria de identificador 1
categoria = Categoria.Carrega(1)
# modifica a propriedade VisivelPainelWorkspace
categoria.VisivelPainelWorkspace = true;
# salva modificação da propriedade VisivelPainelWorkspace
Categoria.Salva(categoria)
```
