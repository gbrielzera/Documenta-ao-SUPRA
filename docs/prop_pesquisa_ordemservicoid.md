# OrdemServicoId

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > OrdemServicoId

Identificador do OrdemServico associado

**Exemplo 1: modificação da propriedade OrdemServicoId**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade OrdemServicoId
pesquisa.OrdemServicoId = 1;
# salva modificação da propriedade OrdemServicoId
Pesquisa.Salva(pesquisa)
```
