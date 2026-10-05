# DataHoraCriacao

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > DataHoraCriacao

Data e hora que a Pesquisa de Satisfação foi gerada.

**Exemplo 1: modificação da propriedade DataHoraCriacao**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade DataHoraCriacao
pesquisa.DataHoraCriacao = DateTime;
# salva modificação da propriedade DataHoraCriacao
Pesquisa.Salva(pesquisa)
```
