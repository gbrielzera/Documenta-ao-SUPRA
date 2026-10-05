# DataHoraApropriacao

Caminho: Customização > Modelo de objetos > Processo > Apropriacao > DataHoraApropriacao

Data/Hora da Apropriação

**Exemplo 1: modificação da propriedade DataHoraApropriacao**

```
# carrega objeto Apropriacao de identificador 1
apropriacao = Apropriacao.Carrega(1)
# modifica a propriedade DataHoraApropriacao
apropriacao.DataHoraApropriacao = DateTime;
# salva modificação da propriedade DataHoraApropriacao
Apropriacao.Salva(apropriacao)
```
