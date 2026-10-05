# GruposEnvolvidos

Caminho: Customização > Modelo de objetos > Processo > MacroProcesso > GruposEnvolvidos

Os Grupos de Trabalho envolvidos (incluindo seus sub-níveis) identificam todas as equipes que atuam Macroprocesso. A definição de Grupos envolvidos pode interferir na autorização para visualização de Ocorrências. A abertura de ocorrências de subprocessos contidos no Macroprocesso também está limitada a solucionadores lotados no grupo informado ou um dos seus sub-níveis.

**Exemplo 1: percorrer objetos da propriedade GruposEnvolvidos**

```
# carrega objeto MacroProcesso de identificador 78
macroProcesso = MacroProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if macroProcesso != None:
    # percorre objetos da propriedade GruposEnvolvidos e para cada uma escreve conteúdo no log de mensagens
    for envolvimentoGrupo in macroProcesso.GruposEnvolvidos:
        Utils.LogInformation(envolvimentoGrupo.ToString())
```
