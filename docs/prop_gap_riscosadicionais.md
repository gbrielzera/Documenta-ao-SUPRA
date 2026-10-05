# RiscosAdicionais

Caminho: Customização > Modelo de objetos > Processo > Gap > RiscosAdicionais

Riscos adicionais relação ao conjunto definido no cadastro do Controle

**Exemplo 1: percorrer objetos da propriedade RiscosAdicionais**

```
# carrega objeto Gap de identificador 78
gap = Gap.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if gap != None:
    # percorre objetos da propriedade RiscosAdicionais e para cada uma escreve conteúdo no log de mensagens
    for riscoGap in gap.RiscosAdicionais:
        Utils.LogInformation(riscoGap.ToString())
```
