# RelacaoOrgaos

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > RelacaoOrgaos

Relação de órgãos que define a regra de recuperação de pessoas.

**Exemplo 1: percorrer objetos da propriedade RelacaoOrgaos**

```
# carrega objeto PapelClasseNegocio de identificador 78
papelClasseNegocio = PapelClasseNegocio.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if papelClasseNegocio != None:
    # percorre objetos da propriedade RelacaoOrgaos e para cada uma escreve conteúdo no log de mensagens
    for orgaoPapel in papelClasseNegocio.RelacaoOrgaos:
        Utils.LogInformation(orgaoPapel.ToString())
```
