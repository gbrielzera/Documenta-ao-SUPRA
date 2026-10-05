# PessoaItemConfiguracao

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > PessoaItemConfiguracao

Define qual campo do Item de Configuração deve ser utilizado para identificação da pessoa.

**Exemplo 1: modificação da propriedade PessoaItemConfiguracao**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade PessoaItemConfiguracao
papelClasseNegocio.PessoaItemConfiguracao = "Usuario";
# salva modificação da propriedade PessoaItemConfiguracao
PapelClasseNegocio.Salva(papelClasseNegocio)
```
