# Contrato

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Contrato

Contrato da Ordem de Serviço

**Exemplo 1: modificação da propriedade Contrato**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# modifica a propriedade Contrato
ordemServico.Contrato = Contrato.Carrega(23);
# salva modificação da propriedade Contrato
OrdemServico.Salva(ordemServico)
```
