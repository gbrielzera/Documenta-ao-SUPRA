# ClassesSubProcesso

Caminho: Customização > Modelo de objetos > Processo > Indicador > ClassesSubProcesso

Tipos de Subprocesso utilizados como filtro na recuperação de Ocorrências. Esta relação de Tipos de Subprocesso só faz sentido para Indicadores apurados a partir da base de dados de Ocorrências de Processos.

**Exemplo 1: percorrer objetos da propriedade ClassesSubProcesso**

```
# carrega objeto Indicador de identificador 78
indicador = Indicador.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if indicador != None:
    # percorre objetos da propriedade ClassesSubProcesso e para cada uma escreve conteúdo no log de mensagens
    for classeSubProcessoIndicador in indicador.ClassesSubProcesso:
        Utils.LogInformation(classeSubProcessoIndicador.ToString())
```
