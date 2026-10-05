# RelacaoPessoas

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > RelacaoPessoas

Relação de pessoas e filas que serão incluídas na recuperação.

**Exemplo 1: percorrer objetos da propriedade RelacaoPessoas**

```
# carrega objeto PapelClasseNegocio de identificador 78
papelClasseNegocio = PapelClasseNegocio.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if papelClasseNegocio != None:
    # percorre objetos da propriedade RelacaoPessoas e para cada uma escreve conteúdo no log de mensagens
    for pessoaPapel in papelClasseNegocio.RelacaoPessoas:
        Utils.LogInformation(pessoaPapel.ToString())
```
