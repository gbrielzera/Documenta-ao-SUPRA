# CelularCliente

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > CelularCliente

Telefone celular para contato com o Cliente

**Exemplo 1: modificação da propriedade CelularCliente**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade CelularCliente
ordemServico.CelularCliente = "Celular";
# salva modificação da propriedade CelularCliente
OrdemServico.Salva(ordemServico)
```
