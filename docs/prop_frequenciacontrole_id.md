# Id

Caminho: Customização > Modelo de objetos > Processo > FrequenciaControle > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um FrequenciaControle

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto FrequenciaControle de identificador 1
frequenciaControle = FrequenciaControle.Carrega(1)
# modifica a propriedade Id
frequenciaControle.Id = 1;
# salva modificação da propriedade Id
FrequenciaControle.Salva(frequenciaControle)
```
