# PSExecuteCmdlet

Caminho: Recursos Avançados > Objeto PowerShell > PSExecuteCmdlet

Executa um Cmdlet (simples comando) da tecnologia de scripts Microsoft PowerShell.

## Assinatura

public object PSExecuteCmdlet(string command)

### command

Comando PowerShell que será executado.

Na figura abaixo demonstramos o uso do PowerShell para recuperar a data do sistema, este retorno é um objeto DateTime:

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Finalização**

dat = PowerShell.PSExecuteCmdlet("get-date")

Utils.LogInformation("Data: " + dat.ToString(), "Exemplo")

A função também pode retornar uma coleção de valores. No exemplo abaixo listamos todos os processos existentes em um computador:

**Processo: Acesso a Sistema e Recusrsos de Rede**

**Evento: Implementar acesso**

processos = PowerShell.PSExecuteCmdlet("get-process")

for p in processos:

Utils.LogInformation("Nome do Processo: " + p.ProcessName, "Exemplo")
