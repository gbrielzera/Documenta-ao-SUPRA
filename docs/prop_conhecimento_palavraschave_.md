# PalavrasChave

Caminho: Customização > Modelo de objetos > Ativos > Conhecimento > PalavrasChave

Palavras Chave para pesquisa

**Exemplo 1: modificação da propriedade PalavrasChave**

```
# carrega objeto Conhecimento de identificador 1
conhecimento = Conhecimento.Carrega(1)
# modifica a propriedade PalavrasChave
conhecimento.PalavrasChave = "Palavras chave";
# salva modificação da propriedade PalavrasChave
Conhecimento.Salva(conhecimento)
```
