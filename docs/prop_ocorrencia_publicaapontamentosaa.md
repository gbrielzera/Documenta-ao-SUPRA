# PublicaApontamentosAA

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > PublicaApontamentosAA

Caso o subprocesso permita que sejam publicados os apontamentos (PublicacaoApontamentosAutoAtendimento diferente de Nunca ou Sempre), sendo verdadeira esta propriedade seram exibidos os apontamentos no Autoatendimento.

**Exemplo 1: modificação da propriedade PublicaApontamentosAA**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade PublicaApontamentosAA
ocorrencia.PublicaApontamentosAA = true;
# salva modificação da propriedade PublicaApontamentosAA
Ocorrencia.Salva(ocorrencia)
```
