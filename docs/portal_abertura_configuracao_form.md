# Abertura por Formulário Direto

Caminho: Guia para Administradores > Portal de Processos > Módulos > Módulo de Abertura > Configurando o Módulo > Abertura por Formulário Direto

A abertura por Formulário Direto equivale ao preenchimento apenas ao Passo 5 do modo Assistente. Neste formato de abertura, o Cliente e Subprocesso são definidos previamente pelo Administrador, cabendo ao solicitante apenas realizar o preenchimento dos campos presentes na abertura.

Modo Formulário Direto

Configurando o Tipo de Abertura para Formulário Direto, serão exibidas as seguintes opções para preenchimento:

Configurador para o Modo Formulário

## Subprocesso

Define o subprocesso da Ordem de Serviço a ser aberta pelo solicitante. É importante ressaltar que serão listados apenas subprocessos que contenham ao menos um iniciador com Código preenchido.

## Iniciador

Define qual o iniciador vai ser utilizado na abertura.

## Serviço

Define o Serviço da Ordem de Serviço, este campo permite o não preenchimento, dando a possibilidade de o solicitante escolher o Serviço no momento da abertura (caso haja mais de um para o subprocesso).

## Permitir alteração do serviço

Habilita/Desabilita a edição do campo Serviço no preenchimento de campos na abertura.

## Recebendo parâmetros através do link da página

Para o módulo de Abertura, podemos receber parâmetros através do Query String da página. Podemos utilizar estes valores recebidos em scripts, como no exemplo abaixo, onde preenchemos o **Favorecido** da Ordem de Serviço com o valor recebido no link.

Script Formulário carregado

Assim, ao entrarmos no módulo através de um link que contenha o parâmetro, o valor do campo já será preenchido automaticamente.

Campo Favorecido
