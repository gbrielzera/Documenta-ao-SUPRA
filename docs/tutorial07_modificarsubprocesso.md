# Modificar o sub-processo de acesso a perfis de sistemas

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 7: Inclusão e remoção de usuários em Itens de Configuração > Modificar o sub-processo de acesso a perfis de sistemas

### 1. No Editor de Processos selecione a janela Process Explorer e gere uma nova versão do processo de Atendimento:

Nova versão do processo de Atendimento

### 2. Selecione o fluxo do Subprocesso Acesso a Sistema e Recurso de Rede que está na nova versão

Seleção do fluxo que será modificado

### 3. No diagrama do subprocesso em edição selecione o Data Object de Itens de Configuração associado ao iniciador:

Edição da regra de associação de Itens de Configuração

Como podemos observar na regra configurada acima Pastas de Rede e Perfis de Sistemas foram cadastrados no sistema como Artefatos (veja módulo de Ativos). Vamos então configurar a propriedade **Ação de configuração de usuários** atribuindo o valor **Incluir Favorecido ao finalizar a ocorrência**.

Configuração da regra de associação de usuários

Com esta configuração quando finalizarmos uma Ordem de Serviço deste subprocesso o usuário informado como Favorecido será incluído na listagem de usuários da Pasta de Rede relacionada na Ordem de Serviço.

### 4. Repita a configuração anterior para itens do tipo Perfil de Sistema

Configuração da associação em Itens de Configuração

5. Salve todas as modificações pendentes e ative a versão em edição

Ativação da nova versão do processo de Atendimento
