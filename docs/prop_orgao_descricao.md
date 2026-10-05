# Descricao

Caminho: Customização > Modelo de objetos > Recurso > Orgao > Descricao

Texto que descreve claramente a função do Órgão. Este texto é utilizado por profissionais e clientes para busca por itens da estrutura organizacional.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Orgao de identificador 1
orgao = Orgao.Carrega(1)
# modifica a propriedade Descricao
orgao.Descricao = "Presidência";
# salva modificação da propriedade Descricao
Orgao.Salva(orgao)
```
