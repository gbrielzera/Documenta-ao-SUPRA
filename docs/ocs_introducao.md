# Inventário de Hardware e Software

Caminho: Guia para Administradores > Inventário de Hardware e Software

O inventariado de Hardware e Software é um recurso muito importante para a visibilidade da estrutura de TI de uma empresa e dinamiza os atendimentos técnicos, principalmente os locais. Com ele é possível sabermos de antemão a configuração de um ativo (desktops, notebooks, licenças de software, componentes de um equipamento) para um atendimento mais efetivo. Além disso ele também provê, por exemplo, o conteúdo instalado em um determinado equipamento e suas mudanças de configuração.

O Supravizio possui um cadastro completo de ativos de TI através do módulo Ativos:

Vejamos por exemplo, detalhes sobre o cadastro de um Equipamento:

Podemos indicar, por exemplo, sua classificação em tipo de item, sua situação atual, identificações, responsabilidades, localidades, etc. Repare que é possível também visualizar os componentes deste equipamento:

Com o auxílio do OCS é possível realizarmos a atualização automática tanto do cadastro destes ativos quanto de seus componentes.

**O que é o OCS?**

O **OCS** (**Open Computers and Software Inventory Next Generation**) é uma ferramenta para "descoberta" de hardware e software em uma rede. É um projeto **open source** baseado em ferramentas de grande aceitação pelo mercado: Apache, MySQL, PHP e PERL. A solução possui uma arquitetura que permite grande desempenho. é capaz de inventariar 1.000.000 de computadores por dia utilizando um servidor Xeon 3GHz com 4 GB de memória RAM, por exemplo. No mercado brasileiro possui um case de sucesso no Banco do Brasil onde foram inventariadas mais de 140.000 estações de trabalho.

Para mais informações sobre o OCS acesse: [http://www.ocsinventory-ng.org/en/](http://www.ocsinventory-ng.org/en/)

**Como se dá esta integração?**

O OCS é uma solução composta por um servidor armazenador de dados e diversos coletores de dados instalados nas estações de trabalho ou notebooks. De tempos em tempos estes coletores coletam dados sobre a configuração física de seu contedor e a lista de softwares instalados e enviam para o servidor OCS:

Periodicamente o Supravizio faz consultas à base de dados do servidor OCS coletando as informações necessárias para uma manutenção dos cadastros de Ativos atualizando dados das estações já cadastradas, atualizando listas de componentes e inserindo novos equipamentos ou softwares "descobertos" pelo OCS.

A partir daí é possível realizar uma gestão mais dos itens de configuração. Além de obter informações sobre os cadastros dos ativos, é possível realizar a gestão baseada em relatórios e indicadores. Além disso, configurar processos para tratamento de determinados eventos, dentre eles:

- Novo hardware
- Novo software
- Novo componente
- Novo componente impressora
- Novo componente placa de rede
- Novo componente controladora
- Nova instalação de software
- Nova instalação de software em Blacklist
- Nova memória
- Retirada de memória
- Retirada de componente
- Retirada de monitor
- Retirada de controladora
- Retirada de placa de som
- Desinstalação de software
- Dentre outros

Este capítulo contem mais informações sobre a preparação de ambiente, configuração desta integração, criação de processos e gestão baseada em relatórios. Para isso leia os tópicos abaixo:

- [Pré-requisitos e configurações](ocs_prerequisitos_e_configuracoes)
- [Configurando a rotina de importação](ocs_configurando_a_rotina_de_impor)
- [Criando processos](ocs_criando_processos)
- [Gestão por relatórios](ocs_gestao_por_relatorios)
