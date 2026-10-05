# Responsavel

Caminho: Customização > Modelo de objetos > Recurso > Contrato > Responsavel

Pessoa que é responsável pela manutenção de dados do Contrato.

**Exemplo 1: modificação da propriedade Responsavel**

```
# carrega objeto Contrato de identificador 51
contrato = Contrato.Carrega(51)
# modifica a propriedade Responsavel
contrato.Responsavel = Pessoa.Carrega(94);
# salva modificação da propriedade Responsavel
Contrato.Salva(contrato)
```
