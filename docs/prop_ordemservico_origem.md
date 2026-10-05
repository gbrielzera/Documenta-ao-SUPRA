# Origem

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Origem

Origem da Ordem de Serviço: Workspace, Autoatendimento ou Eventos do Processo

**Exemplo 1: modificação da propriedade Origem**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade Origem
ordemServico.Origem = "AutoAtendimento";
# salva modificação da propriedade Origem
OrdemServico.Salva(ordemServico)
```
