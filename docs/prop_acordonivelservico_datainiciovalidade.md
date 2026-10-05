# DataInicioValidade

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > DataInicioValidade

Data de início de validade do Acordo de Nível de Serviço. Uma Ordem de Serviço só pode ser associada a um acordo cuja data de validade seja maior ou igual a data de abertura da ocorrência.

**Exemplo 1: modificação da propriedade DataInicioValidade**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade DataInicioValidade
acordoNivelServico.DataInicioValidade = DateTime;
# salva modificação da propriedade DataInicioValidade
AcordoNivelServico.Salva(acordoNivelServico)
```
