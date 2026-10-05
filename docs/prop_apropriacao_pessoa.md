# Pessoa

Caminho: Customização > Modelo de objetos > Processo > Apropriacao > Pessoa

Pessoa

**Exemplo 1: modificação da propriedade Pessoa**

```
# carrega objeto Apropriacao de identificador 94
apropriacao = Apropriacao.Carrega(94)
# modifica a propriedade Pessoa
apropriacao.Pessoa = Pessoa.Carrega(82);
# salva modificação da propriedade Pessoa
Apropriacao.Salva(apropriacao)
```
