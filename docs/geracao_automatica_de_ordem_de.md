# Geração automática de Ordens de Serviço associadas

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Iniciadores > Geração automática de Ordens de Serviço associadas

A geração automática de Ordens de Serviço possibilita abertura de Ordens de Serviços a partir de arquivo de texto ou campo customizado.

Pode ser utilizada em um **Link Inicial, Link Final** ou em uma chamada de [Subprocesso](subprocessos).

Para maiores informações, consulte [Eventos Iniciadores](bpmn_iniciadores) e [Ordem de Serviços Associadas](workspace_os_associada).

**Link Final** adicionado no final de Subprocesso para chamar Subprocesso associado, geralmente contém um script, sempre associado a um **Link Inicial **de Subprocesso**.**

Link Final

**Link Inicial **inicia Subprocesso associado a um Link Final.

Link Inicial

Subprocesso permite invocar um outro fluxo de processo.

Subprocesso

Gera uma nova Ordem de Serviço de acordo com:

**Assinatura**

OrdemServico.IniciaSubProcesso(Atividade atividade)

**Atividade**

Atividade corrente na ocorrência

**Return**

Retorna um Subprocesso derivado da OS

Neste tópico, iremos citar alguns exemplos de uso da **Geração automática de Ordens de Serviço associadas**.

## Exemplo 1: Gerar Ordens de Serviço associadas a partir de um arquivo de texto

No Link Final do Subprocesso chamador, é adicionado um Script para tratar arquivo de texto anexado, como no exemplo da figura:

Script que trata arquivos textos

Segue o código em formato de texto:

```
itemProcessar = OrdemServico.ObtemItem("TESTE")
linha = "LinhaInicial"
try:
    tr = File.OpenText("D:\\Supravizio\\" + itemProcessar.Localizacao)
    while linha != None:
            linha = tr.ReadLine()
            derivada = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
            if not String.IsNullOrEmpty (linha):
                    campos = linha.Split(';')
                    derivada.Assunto = campos[0]
                    derivada.DescricaoDetalhada = campos[1]
                    OrdemServico.Salva(derivada)
except Exception, exc:
    OrdemServico.AdicionaComentario(exc.Message, False)
```

O Script obtém um Item de Configuração do tipo fornecido como parâmetro associado a Ocorrência. Se não existir um Item ou existirem vários, então retorna mensagem de erro.

O documento de texto a ser tratado deve ter a seguinte formatação:

- Cada registro deve estar contido em uma linha, pois, os registros, neste exemplo, são separados por linhas.
- Os campos preenchidos foram separados por "**;**" (ponto e vírgula)

Os seguintes dados devem estar contidos no documento de texto:

**ASSUNTO; DESCRICAODETALHADA;**

O documento deve ter o formato como mostra a figura abaixo:

Arquivo de texto

## Exemplo 2: Gerar Ordens de Serviço associadas a partir de um campo customizado tipo lista de objetos

Objetos de uma lista são selecionados em um elemento [Entrada de Dados](data_obj_entrada_de_dados) ou [outro](bpmn_data_objects) e passados ao Subprocesso associado.

No Link Final do Subprocesso chamador, é adicionado um Script para tratar a lista de objetos, como no exemplo da figura:

Script que trata uma lista de objetos

Segue o código em formato de texto:

```
for pessoa in OrdemServico.GetCustom("LISTA_PESSOAS"):
    derivada = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
    derivada.Assunto = pessoa.ToString()
    OrdemServico.Salva(derivada)
```

O Script obtem uma lista de objetos, no exemplos LISTAS_PESSOAS, para que cada objeto da lista seja tratado no Subprocesso associado, como demonstra a figura:

Lista de Pessoas

## Exemplo 3: Gerar Ordens de Serviço associadas a partir de um campo customizado tipo Lista de Registro

Registros de uma lista são selecionados em um elemento [Entrada de Dados](data_obj_entrada_de_dados) ou [outro](bpmn_data_objects) e passados ao Subprocesso associado.

No Link Final do Subprocesso chamador, é adicionado um Script para tratar a lista de registros, como no exemplo da figura:

Segue o código em formato de texto:

```
reg = OrdemServico.GetCustom("REG_PESSOAS")
qtdlinhas = reg.Rows.Count
for dr in reg.Rows:
    derivada = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
    derivada.Assunto = dr["NOME"]+" - " + dr["CARGO"]
    OrdemServico.Salva(derivada)
```

O Script obtem o preenchimento de uma lista de registros, com os campos apontados em REG_PESSOAS, como demonstra a figura:

Lista de Registros

Em seguida, serão apresentadas as Ordens de Serviço que foram geradas:

Ordens de Serviço Geradas
