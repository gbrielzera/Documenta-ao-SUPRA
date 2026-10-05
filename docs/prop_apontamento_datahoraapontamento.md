# DataHoraApontamento

Caminho: Customização > Modelo de objetos > Processo > Apontamento > DataHoraApontamento

Data e hora do Apontamento

**Exemplo 1: modificação da propriedade DataHoraApontamento**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade DataHoraApontamento
apontamento.DataHoraApontamento = DateTime;
# salva modificação da propriedade DataHoraApontamento
Apontamento.Salva(apontamento)
```
