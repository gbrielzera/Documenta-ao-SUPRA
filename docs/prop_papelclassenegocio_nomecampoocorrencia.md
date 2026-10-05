# NomeCampoOcorrencia

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > NomeCampoOcorrencia

Campo da ocorrência ou cadastro associado utilizado para obter um objeto do tipo Pessoa.

**Exemplo 1: modificação da propriedade NomeCampoOcorrencia**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade NomeCampoOcorrencia
papelClasseNegocio.NomeCampoOcorrencia = "Campo para recuperação";
# salva modificação da propriedade NomeCampoOcorrencia
PapelClasseNegocio.Salva(papelClasseNegocio)
```
