# ServicoId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ServicoId

Identificador do Serviço associado

**Exemplo 1: modificação da propriedade ServicoId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade ServicoId
ordemServico.ServicoId = 1;
# salva modificação da propriedade ServicoId
OrdemServico.Salva(ordemServico)
```
