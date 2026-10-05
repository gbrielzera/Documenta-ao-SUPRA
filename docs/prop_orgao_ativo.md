# Ativo

Caminho: Customização > Modelo de objetos > Recurso > Orgao > Ativo

Indica que o Órgão está Ativo

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Orgao de identificador 1
orgao = Orgao.Carrega(1)
# modifica a propriedade Ativo
orgao.Ativo = true;
# salva modificação da propriedade Ativo
Orgao.Salva(orgao)
```
