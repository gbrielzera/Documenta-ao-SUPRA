# Avaliador

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > Avaliador

Avaliador da Pesquisa de Satisfação

**Exemplo 1: modificação da propriedade Avaliador**

```
# carrega objeto Pesquisa de identificador 78
pesquisa = Pesquisa.Carrega(78)
# modifica a propriedade Avaliador
pesquisa.Avaliador = Pessoa.Carrega(23);
# salva modificação da propriedade Avaliador
Pesquisa.Salva(pesquisa)
```
