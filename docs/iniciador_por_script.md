# Iniciador por Script

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Iniciadores > Iniciador por Script

Também é possível realizar a abertura de Ordens de Serviço a partir de um script, podendo ser inserido por exemplo, no início ou fim de uma tarefa, em um script de modificação de um campo etc.

Para isso, é utilizada a função OrdemServico.Nova, a qual iremos explicar sua estrutura básica.

```
OrdemServico.Nova(siglaClasseSubProcesso, codigoIniciador, assunto, servico, cliente, responsavel)
```

## Atributos

siglaClasseSubProcesso – Sigla do Subprocesso

codigoIniciador – Código da tarefa a ser iniciada

assunto – Assunto da Ordem de Serviço

servico – Servico.Carrega(Identificador do Serviço)

cliente – Pessoa.Carrega(Identificador da Pessoa)

responsavel - Pessoa.Carrega(Identificador da Pessoa)

## Exemplo

Para melhor entendermos a utilização, iremos citar um exemplo no qual esta função é utilizada.

Adicionamos um campo com nome "Houveram Problemas?" ao fluxo do Subprocesso "Restauração de Backup".

Fluxo utilizado no Processo

Após, adicionamos o seguinte script em Script Fim.

```
if OrdemServico.GetCustom("HOUVE_PROBLEMA") == "Sim":
    novaOS = OrdemServico.Nova("Incidente","INICIO01","Problema durante Restauração de Backup",Servico.Carrega(5),Pessoa.Carrega(5),Pessoa.Carrega(5))
```

Ao abrir uma Ordem de Serviço e avançar até a respectiva tarefa, preenchemos o campo com "Sim".

Abertura da Ordem de Serviço

Após avançar a tarefa, será aberta uma nova Ordem de Serviço referente ao Problema e esta não terá associação com a Ordem de Serviço que a gerou.

Ordem de Serviço gerada
