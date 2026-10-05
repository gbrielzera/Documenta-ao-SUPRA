# DescricaoCliente

Caminho: Customização > Modelo de objetos > Processo > Servico > DescricaoCliente

Descritivo apresentado para Cliente no Catálogo de Serviços. Se não for preenchido é utilizado a Descrição padrão do Serviço

**Exemplo 1: modificação da propriedade DescricaoCliente**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade DescricaoCliente
servico.DescricaoCliente = "Conta de rede";
# salva modificação da propriedade DescricaoCliente
Servico.Salva(servico)
```
