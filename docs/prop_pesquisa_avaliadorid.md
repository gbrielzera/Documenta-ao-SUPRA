# AvaliadorId

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > AvaliadorId

Identificador do Avaliador da Pesquisa

**Exemplo 1: modificação da propriedade AvaliadorId**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade AvaliadorId
pesquisa.AvaliadorId = 1;
# salva modificação da propriedade AvaliadorId
Pesquisa.Salva(pesquisa)
```
