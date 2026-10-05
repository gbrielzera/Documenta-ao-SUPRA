# ResponsavelId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ResponsavelId

Identificador do Responsável pela ocorrência. A mudança de responsabilidade pode ocorrer em virtude de encaminhamentos ou automatismo de processo (segundo papéis definidos em atividades).

**Exemplo 1: modificação da propriedade ResponsavelId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade ResponsavelId
ocorrencia.ResponsavelId = 1;
# salva modificação da propriedade ResponsavelId
Ocorrencia.Salva(ocorrencia)
```
