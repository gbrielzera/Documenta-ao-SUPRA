# Assunto

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Assunto

Texto resumido que descreve o assunto da ocorrência.

**Exemplo 1: modificação da propriedade Assunto**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade Assunto
ocorrencia.Assunto = "Assunto";
# salva modificação da propriedade Assunto
Ocorrencia.Salva(ocorrencia)
```
