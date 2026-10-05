# DataHoraResposta

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > DataHoraResposta

Data e hora em que foi respondida a Pesquisa

**Exemplo 1: modificação da propriedade DataHoraResposta**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade DataHoraResposta
pesquisa.DataHoraResposta = DateTime;
# salva modificação da propriedade DataHoraResposta
Pesquisa.Salva(pesquisa)
```
