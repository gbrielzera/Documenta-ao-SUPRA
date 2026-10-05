# OpcaoCampoOcorrencia

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > OpcaoCampoOcorrencia

Opção de seleção por hierarquia a partir do campo indicado para recuperação.

**Exemplo 1: modificação da propriedade OpcaoCampoOcorrencia**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade OpcaoCampoOcorrencia
papelClasseNegocio.OpcaoCampoOcorrencia = "Pessoa";
# salva modificação da propriedade OpcaoCampoOcorrencia
PapelClasseNegocio.Salva(papelClasseNegocio)
```
