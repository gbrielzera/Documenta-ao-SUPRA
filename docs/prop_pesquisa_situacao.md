# Situacao

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > Situacao

Indica a Situação da Pesquisa de Satisfação.

**Exemplo 1: modificação da propriedade Situacao**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade Situacao
pesquisa.Situacao = "Andamento";
# salva modificação da propriedade Situacao
Pesquisa.Salva(pesquisa)
```
