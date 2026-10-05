# Descricao

Caminho: Customização > Modelo de objetos > Processo > FrequenciaControle > Descricao

Descrição detalhada do FrequenciaControle

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto FrequenciaControle de identificador 1
frequenciaControle = FrequenciaControle.Carrega(1)
# modifica a propriedade Descricao
frequenciaControle.Descricao = "Descrição";
# salva modificação da propriedade Descricao
FrequenciaControle.Salva(frequenciaControle)
```
