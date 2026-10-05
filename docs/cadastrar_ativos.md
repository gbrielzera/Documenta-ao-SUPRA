# Cadastrar Ativos

Caminho: Guia para Administradores > Roteiro de implantação > Realizando cadastros > Cadastros Adicionais > Cadastrar Ativos

Um ativo é um item de configuração que compõe o cenário de atendimento. Um ativo pode ser um [Equipamento](hardware_sub), um [Software](software_sub), um [Dispositivo Telefônico](dispositivotelefonico_sub), um item de [Base de Conhecimento](conhecimento_sub) ou um [Artefato](artefato_sub) qualquer (documento, comunicado, arquivos em geral, etc). Um ativo também é conhecido como Item de Configuração.

Para realizar o cadastro de ativos você deve seguir os seguintes passos:

1. [Cadastrar Tipos de Item de Configuração](classeconfiguracao_sub).

Neste exemplo estamos cadastrando o **Ativo Tipo de Configuração**:

Ativos Tipos de Itens Configuração

Na tela abaixo, apresentamos os dados principais para cadastrar este **Ativo**:

Dados Principais para Cadastro de Tipos de Itens Configuração

2. [Cadastrar Ativos](supravizio_configuracao)

No campo Super Tipo é possível visualizar os tipos de Ativos disponíveis.

Os tipos de ativos admitidos no Supravizio são:

- [Equipamento](hardware_sub)
- [Software](software_sub)
- [Dispositivo Telefônico](dispositivotelefonico_sub)
- [Conhecimento](conhecimento_sub)
- [Artefato](artefato_sub)

### Situação de um Ativo

Clicando na aba **Situações** no cadastro de alguma **tipo de configuração**, como no exemplo anterior, Notebook para Empréstimo, são exibidas as situações possíveis de um item que seja deste tipo (tipo de configuração). Além disso, dependendo da situação indicada, pode ou não ser exibido um ativo deste tipo:

Aba Situações

Selecionando uma Nova Situação

Como no exemplo acima, um Notebook para Empréstimo pode estar em três situações possíveis: Disponível, Emprestado e Inativo. Observe que, dada a situação, o ativo pode ou não ser exibido em listagens do Portal. Seguindo o exemplo, se um ativo do tipo Notebook para Empréstimo estiver disponível, fica visível nas listagens:

Suponhamos agora que o **Ativo** foi emprestado de acordo com algum processo cadastrado no Supravizio:

Fluxo do Processo - Ativo emprestada

Inicialmente o Ativo abaixo se encontra disponível:

Situação do Ativo

Disponibilidade do Ativo no Portal de Processos

Agora, um cliente realiza a abertura de uma Ordem de Serviço solicitando o Empréstimo de Notebook:

**Ativo disponível no Portal**

Ao ser emprestado, o solucionador deverá modificar a situação do ativo em seu cadastro ou o processo poderá realizar essa mudança automaticamente via automação com scripts:

Mudança de Situação

Disponibilidade no Portal

Atualizando a situação do Ativo para emprestado, este Ativo não será mais exibido nas listagens de busca de Ativos no Portal pois se encontra na situação Emprestado:

**Ativo emprestado no Portal**

Existem outras situações possíveis, como por exemplo, um Certificado Digital que pode estar na situação Válido, Expirado, Em Regularização, e outras. Um Artigo que pode estar Publicado, Em Edição, e outras. Estes exemplos acima são somente algumas situações do que pode ser feito em relação a Situações de uma Tipo de Configuração.

### Componentes de um Ativo

A aba de componentes está disponível para que fique visível sua composição (ou parcialmente) de um Ativo (como um Equipamento, Software, Dispositivo Telefônico etc).

Componentes de um Ativo

Como no exemplo acima, podemos notar que o cadastro indica que a estação de trabalho possui uma licença do software AutoCAD.

**Importante**: Existem muitos casos em que não necessitamos criar ativos para cada periférico que compõe um ativo. Casos típicos como memórias, processadores e teclados. Para facilitar o cadastro, é possível realizar apenas o registro do **Tipo de Item de Configuração**.

Vamos citar um exemplo, cadastrando um processador:

Tipo de Item de Configuração

Ao associar este componente a um Equipamento, basta inserirmos este Tipo de Item de Configuração para realizar a associação de cadastro.

Associação com equipamento
