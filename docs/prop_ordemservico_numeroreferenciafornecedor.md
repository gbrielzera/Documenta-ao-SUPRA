# NumeroReferenciaFornecedor

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > NumeroReferenciaFornecedor

Número de referência para Chamado registrado no Fornecedor do Serviço

**Exemplo 1: modificação da propriedade NumeroReferenciaFornecedor**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade NumeroReferenciaFornecedor
ordemServico.NumeroReferenciaFornecedor = "Número referência Fornecedor";
# salva modificação da propriedade NumeroReferenciaFornecedor
OrdemServico.Salva(ordemServico)
```
