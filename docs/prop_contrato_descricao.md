# Descricao

Caminho: Customização > Modelo de objetos > Recurso > Contrato > Descricao

Descrição detalhada do Contrato

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade Descricao
contrato.Descricao = "Service Desk 2009";
# salva modificação da propriedade Descricao
Contrato.Salva(contrato)
```
