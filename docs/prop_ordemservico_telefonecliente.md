# TelefoneCliente

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > TelefoneCliente

Telefone de contato do Cliente

**Exemplo 1: modificação da propriedade TelefoneCliente**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade TelefoneCliente
ordemServico.TelefoneCliente = "Telefone";
# salva modificação da propriedade TelefoneCliente
OrdemServico.Salva(ordemServico)
```
