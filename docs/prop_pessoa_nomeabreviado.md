# NomeAbreviado

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > NomeAbreviado

Nome abreviado da Pessoa

**Exemplo 1: modificação da propriedade NomeAbreviado**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade NomeAbreviado
pessoa.NomeAbreviado = "José Aparecido";
# salva modificação da propriedade NomeAbreviado
Pessoa.Salva(pessoa)
```
