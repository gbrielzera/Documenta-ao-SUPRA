# Gestor

Caminho: Customização > Modelo de objetos > Recurso > Orgao > Gestor

Gestor responsável pelo Órgão

**Exemplo 1: modificação da propriedade Gestor**

```
# carrega objeto Orgao de identificador 51
orgao = Orgao.Carrega(51)
# modifica a propriedade Gestor
orgao.Gestor = Pessoa.Carrega(94);
# salva modificação da propriedade Gestor
Orgao.Salva(orgao)
```
