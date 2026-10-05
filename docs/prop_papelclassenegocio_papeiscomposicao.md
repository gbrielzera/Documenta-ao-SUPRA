# PapeisComposicao

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > PapeisComposicao

Relação de papéis de processo que serão utilizados para compor este papel. O papel resultante é formado pela soma de todas as pessoas sem ocorrência de duplicidades.

**Exemplo 1: percorrer objetos da propriedade PapeisComposicao**

```
# carrega objeto PapelClasseNegocio de identificador 78
papelClasseNegocio = PapelClasseNegocio.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if papelClasseNegocio != None:
    # percorre objetos da propriedade PapeisComposicao e para cada uma escreve conteúdo no log de mensagens
    for composicaoPapel in papelClasseNegocio.PapeisComposicao:
        Utils.LogInformation(composicaoPapel.ToString())
```
