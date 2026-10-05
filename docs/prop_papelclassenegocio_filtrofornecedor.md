# FiltroFornecedor

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > FiltroFornecedor

Relação de empresas fornecedoras para recuperação de pessoas do tipo terceiros

**Exemplo 1: modificação da propriedade FiltroFornecedor**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade FiltroFornecedor
papelClasseNegocio.FiltroFornecedor = "Fornecedores";
# salva modificação da propriedade FiltroFornecedor
PapelClasseNegocio.Salva(papelClasseNegocio)
```
