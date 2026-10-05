# Periodos

Caminho: Customização > Modelo de objetos > Processo > IndicadorPlano > Periodos

Períodos definidos para o Plano de Gestão. Os períodos são definidos pela 'Data início' e 'Data fim' do Plano de Gestão.

**Exemplo 1: percorrer objetos da propriedade Periodos**

```
# carrega objeto IndicadorPlano de identificador 78
indicadorPlano = IndicadorPlano.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if indicadorPlano != None:
    # percorre objetos da propriedade Periodos e para cada uma escreve conteúdo no log de mensagens
    for periodoPlano in indicadorPlano.Periodos:
        Utils.LogInformation(periodoPlano.ToString())
```
