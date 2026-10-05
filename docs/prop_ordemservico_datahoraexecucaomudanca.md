# DataHoraExecucaoMudanca

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > DataHoraExecucaoMudanca

Data/hora em que foi Executada a Mudança o ambiente

**Exemplo 1: modificação da propriedade DataHoraExecucaoMudanca**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade DataHoraExecucaoMudanca
ordemServico.DataHoraExecucaoMudanca = DateTime;
# salva modificação da propriedade DataHoraExecucaoMudanca
OrdemServico.Salva(ordemServico)
```
