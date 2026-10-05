# ResponsavelInicial

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ResponsavelInicial

Primeiro Solucionador responsável pelo atendimento da Ocorrência.

**Exemplo 1: modificação da propriedade ResponsavelInicial**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade ResponsavelInicial
ocorrencia.ResponsavelInicial = Pessoa.Carrega(23);
# salva modificação da propriedade ResponsavelInicial
Ocorrencia.Salva(ocorrencia)
```
