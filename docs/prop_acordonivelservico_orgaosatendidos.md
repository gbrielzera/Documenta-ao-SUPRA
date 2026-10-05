# OrgaosAtendidos

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > OrgaosAtendidos

Relação de Órgãos atendidos pelo ANS

**Exemplo 1: percorrer objetos da propriedade OrgaosAtendidos**

```
# carrega objeto AcordoNivelServico de identificador 51
acordoNivelServico = AcordoNivelServico.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if acordoNivelServico != None:
    # percorre objetos da propriedade OrgaosAtendidos e para cada uma escreve conteúdo no log de mensagens
    for orgaoAtendidoANS in acordoNivelServico.OrgaosAtendidos:
        Utils.LogInformation(orgaoAtendidoANS.ToString())
```
