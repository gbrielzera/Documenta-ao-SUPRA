# Agendar o envio de Comunicados

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 11: Envio de Comunicados > Agendar o envio de Comunicados

Também é possível agendar o envio de Comunicados, para que estes sejam enviados apenas quando atendida a regra de determinada fórmula.

Neste primeiro exemplo, criaremos um **Comunicado** que será enviado no dia seguinte da criação da **Ordem de Serviço**.

| **1.** | Crie uma nova versão do Subprocesso |
|---|---|

Utilizando o mesmo fluxo do tópico anterior, insira o seguinte código em **Script Evento** no** Evento Intermediário Mensagem**:

```
Mensagem.DataHoraAgendada = OrdemServico.DataHoraCriacao.AddDays(1)
```

Editor de Processos

### 2. Salve e ative a versão

Ativação da Versão

### 3.Inicie uma nova Ordem de Serviço

Em seguida, avance até a tarefa **Aguardar Resposta e executar solução apresentada**, onde será exibida a seguinte tela:

Ordem de Serviço criada

### 4.Abra a aba Comunicados

### A coluna Envio Agendado deverá estar preenchida com a respectiva data.

Aba Comunicados da Ordem de Serviço

Note que o envio do **Comunicado** permanecerá pendente. Assim que enviado, o ícone será alterado:

Comunicado enviado com sucesso

Também podem ser utilizados outros scripts que resultarão no envio do **Comunicado** na data desejada.

Seguem mais alguns exemplos:

### Próximo Mês

```
Mensagem.DataHoraAgendada = OrdemServico.DataHoraCriacao.AddMonths(1)
```

### Último dia do mês

```
Mensagem.DataHoraAgendada = DateTime(DateTime.Now.Year, DateTime.Now.Month, 1).AddMonths(1).AddDays(-1)
```

### Data Prevista de Fim da Ordem de Serviço

```
Mensagem.DataHoraAgendada = OrdemServico.DataHoraFimPrevisto
```

### Data recuperada de um Campo Customizado

```
Mensagem.DataHoraAgendada = OrdemServico.Cliente.GetCustom("DATA_CUSTOM")
```

### Primeiro Dia do Próximo Mês

```
Mensagem.DataHoraAgendada = DateTime(DateTime.Now.AddMonths(1).Year, DateTime.Now.AddMonths(1).Month, 1)
```
