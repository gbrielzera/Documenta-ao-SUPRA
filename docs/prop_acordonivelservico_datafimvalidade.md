# DataFimValidade

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > DataFimValidade

Data de fim de validade do Acordo de Nível de Serviço. Uma Ordem de Serviço só pode ser associada a um acordo cuja data de fim de validade seja menor que a data de abertura da ocorrência.

**Exemplo 1: modificação da propriedade DataFimValidade**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade DataFimValidade
acordoNivelServico.DataFimValidade = DateTime;
# salva modificação da propriedade DataFimValidade
AcordoNivelServico.Salva(acordoNivelServico)
```
