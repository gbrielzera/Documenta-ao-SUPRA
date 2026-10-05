# ContatoResponsavelFornecedor

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ContatoResponsavelFornecedor

Informações de contato no Forncedor incluindo solucionador responsável, email e telefone quando possível.

**Exemplo 1: modificação da propriedade ContatoResponsavelFornecedor**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade ContatoResponsavelFornecedor
ordemServico.ContatoResponsavelFornecedor = "ContatoFornecedor";
# salva modificação da propriedade ContatoResponsavelFornecedor
OrdemServico.Salva(ordemServico)
```
