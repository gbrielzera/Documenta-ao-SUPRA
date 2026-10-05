# Criar Tipos de Solicitação

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 10: Macroprocessos e Tipos de solicitação > Criar Tipos de Solicitação

Nesta etapa vamos criar Tipos de Solicitação que são disponibilizados no Portal de acordo com seus Macros-Processos.

1. Crie o cadastro de Tipo de Solicitação disponível no menu Processo | Processos | Tipo de solicitação:

Novo tipo de solicitação

2. Selecione no diagrama do subprocesso Liberação de Notas criado anteriormente, seu Iniciador e vincule o Tipo de Solicitação que será apresentado no Portal:

Associação do iniciador com o Tipo de Solicitação

Neste exemplo vinculamos também ao iniciador do subprocesso Incidente do Macro-Processo Tecnologia da Informação, o **Tipo de Serviço** Infra-estrutura Informática.

3. Para visualizar este subprocesso no Portal selecione a opção Visibilidade do iniciador e escolha a opção Todas as aplicações ou Somente Portal de Processos:

Definição da visibilidade

Ao selecionar em Visibilidade do iniciador, a opção **Somente Portal de Processos**, somente poderão ser abertas Ordens de Serviço através deste iniciador pelo Portal. Selecionando a opção **Somente Workspace**, somente poderão ser abertas Ordens de Serviço através deste iniciador pelo Workspace. Já a opção **Todas as aplicações **deixa o iniciador disponível para aberturas de Ordens de Serviço, tanto no Workspace quanto no Portal.

4. Após escolher a opção de visualização no Portal de Processos podemos identificar no passo 2 da abertura de uma Ordem de Serviço no Portal, as opções de Tipos de Solicitações vinculadas aos iniciadores disponíveis de acordo com cada macroprocesso:

Resultado do filtro por Tipo de Solicitação no Portal

Podemos observar que no **Passo 2 **é apresentado a descrição de cada Macroprocesso e a seleção de Tipos de Solicitação.

É apresentado também a opção **Selecionar uma solicitação de '' no próximo passo**. Esta opção somente aparecerá caso existam iniciadores sem Tipos de Solicitação. No exemplo acima podemos identificar esta opção no Macro-Processo Tecnologia da Informação, pois neste Macroprocesso existem outros subprocessos com iniciadores sem Tipo de Solicitação associados.

Caso exista apenas um Macroprocesso cadastrado e não existirem Tipos de Solicitações, o Portal pulará o **Passo 2** e irá direto para o **Passo 3 **onde será selecionado um Subprocesso.

4. Selecione um Tipo de Solicitação e avance o passo 2 no Portal:

## Passo 3 com filtro de tipo de solicitação

Após selecionar o tipo de solicitação e seguir para o passo 3 será filtrado os subprocessos referentes ao tipo de solicitação selecionado.

**Os Tipos de Solicitação são visíveis apenas para iniciadores manuais disponíveis no Portal.**
