# EscoreGeral

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > EscoreGeral

Avaliação geral

**Exemplo 1: modificação da propriedade EscoreGeral**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade EscoreGeral
pesquisa.EscoreGeral = 1;
# salva modificação da propriedade EscoreGeral
Pesquisa.Salva(pesquisa)
```
