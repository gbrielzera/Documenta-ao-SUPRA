# Pessoa

Caminho: Customização > Modelo de objetos > Recurso > Ausencia > Pessoa

Pessoa que ficará ausente

**Exemplo 1: modificação da propriedade Pessoa**

```
# carrega objeto Ausencia de identificador 51
ausencia = Ausencia.Carrega(51)
# modifica a propriedade Pessoa
ausencia.Pessoa = Pessoa.Carrega(94);
# salva modificação da propriedade Pessoa
Ausencia.Salva(ausencia)
```
