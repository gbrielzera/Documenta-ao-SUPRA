# Cadastro da Base de Conhecimento

Caminho: Guia para Solucionadores > Base de Conhecimento > Cadastro da Base de Conhecimento

**Cadastro pela Tela de Edição de Registros**

Quando um Problema é Conhecido, ou seja, um problema que foi diagnosticado e identificado como um problema sem solução no momento, o especialista pode gerar um documento que será utilizado pelos solucionadores de suporte. Este documento será um artigo de conhecimento.

Para criar este cadastro acesse o no menu do **Supravizio** a opção **Ativos | Conhecimento** de acordo com a figura abaixo:

**Acesso a base de conhecimento**

Caso existam conhecimentos já registrados será exibida uma lista com estes Conhecimentos existentes.

Para registrar um novo Conhecimento clique em **Novo **e inicie o preenchimento do cadastro:

**Base de conhecimento**

Na imagem abaixo é possível identificar os campos necessários para gerar um novo Conhecimento:

**Tela principal**

Na tabela abaixo apresentamos as descrições dos campos presentes na aba Dados Principais que é exibida ao solicitar um novo cadastro de Conhecimento:

| ## Campo | ## Descrição |
|---|---|
| **Identificador** | Número sequencial gerado automaticamente para identificar o artigo da base de conhecimento. Este identificador é global entre todos os itens de configuração do CMDB. Isto significa que podemos ter um artigo com o identificador 5, um equipamento com o identificador 6 e outro artigo com o identificador 7. |
| **Tipo Item Configuração** | A Tipo de Configuração representa o tipo de artigo. Podemos criar classes como "Tutorial", "Problema Conhecido" etc. No tipo configuramos quais seções o documento deve conter. Em um Problema conhecido, por exemplo, é natural que exista um Sintoma e uma Solução de Contorno. |
| **Situação** | Configura todos os estados possíveis para o artigo. |
| **Título** | Título do Conhecimento que ficará visível na listagem da tela principal do Ativo e que será exibido também na busca. Importante: o título não é um critério de recuperação. |
| **Sumário** | Descrição que possibilite o entendimento do principal objetivo do Conhecimento. Importante: o sumário não é um critério de recuperação. |
| **Comentários para Cliente ** | Comentário sobre o Item de Configuração destinado ao cliente. Para histórico de observações a respeito dos Itens de Configuração utilize na aba "Observações" a relação de Observações existentes. |
| **Data Cadastro** | Data em que o artigo foi gerado. |
| **Usuário Responsável** | Usuário responsável pelo artigo. Este campo tem o seu uso em função da configuração de processos. Poderíamos, por exemplo, escrever um processo de revisão de artigos onde o **Usuário responsável** deve revisar o texto. |
| **Fator Prioridade** | Fator utilizado para calculo de Prioridade em Ocorrência. Possui relação com o conceito de **Método de Priorização** que é responsável por calcular automaticamente a prioridade de uma Ordem de Serviço. |
| **Ocorrência Criação** | Ocorrência de processo que gerou o artigo. Neste caso podemos dizer que o artigo foi uma saída do processo. |
| **Palavras Chaves** | Palavras utilizadas para recuperação de artigos. |

**Sumário** e **Título** são campos obrigatórios sendo recomendado um título que descreva em poucas palavras o Conhecimento e um sumário com uma descrição completa do Conhecimento.

**Importante: o campo Palavras chaves deve ser preenchido com bastante atenção pois ele é utilizado na** [recuperação automática de Ordens de Serviço](pesquisar_publicacoes).

Para que um conhecimento fique mais estruturado é possível organizar em **Tópicos**. Estes tópicos são definidos no **Tipo de Configuração** do artigo, um [Conhecimento](conhecimento_sub). Para incluir, selecione a aba **Dados Principais **e clique em cima do link **Tipo Configuração**. Será exibida a tela da figura abaixo, que permite o gerenciamento da Tipo de Configuração associada ao Conhecimento:

Tela da Tipo de Configuração

Na tela referenciada na figura acima selecione a aba Conhecimento:

Este conhecimento define a **Sequência** que é utilizada para ordenação ascendente dos tópicos de um determinado artigo e o **Subtítulo **que será utilizado no tópico:

Aba conhecimento

A sequência dos tópicos influenciará na visualização do artigo. Veja o exemplo abaixo:

Exemplo de artigo e seus tópicos ordenados

Após criar um Tópico podemos acessar uma das opções clicando em **Visualizar **na barra de ferramentas. Será aberto então um editor de texto que possibilita a edição e de conteúdos:

**Tópicos do conhecimento**

Neste editor de texto podemos desenvolver artigos formatados, inserir imagens, importar e exportar de RTF e imprimir.

### Descontinuando Itens da Base de Conhecimento

Para desativar um Item da base de conhecimento, acesse o cadastro de Tipos de Itens de Configuração (**Ativos | Tipos de Itens de Configuração**) selecione o Tipo de Artigo que poderá ser descontinuado (nesse exemplo utilizaremos o tipo **Tutorial**):

Tipos de Itens de Configuração

Observe na aba de Situações que não há nenhuma situação desativada e então adicione um nova situação em que o tipo de conhecimento será desativado:

Adicionar nova situação

Salve as alterações e então acesse a Base de Conhecimento (Ativos | Base de Conhecimento). Entrando no registro de algum tutorial, foi definida como nova situação "Descontinuado":

Alteração da Situação de um Tutorial

Observe que existe um outro tutorial semelhante porém atualizado para a nova versão com situação "Publicado":

Tutoriais com Situações diferentes

Ao realizar uma busca no Workspace utilizando uma palavra chave (que se aplica tanto ao tutorial publicado quanto ao descontinuado), repare que a busca retorna apenas os itens que não estão descontinuados:

Artigos retornados pela consulta
