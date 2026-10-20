# Códigos de erro do Supravizio
Caminho: Catálogo > Erros do sistema

Importado de `SV_EXCEPTION_CLASS` (producao, 2026-10-19) por tools/importar_metadados.py: 49 códigos. Texto em colchetes (`[NomePapel]`, `[NomeAtividade]`) é parâmetro preenchido pelo sistema. O prefixo do código indica o módulo: SV Utilitários, CF Configuração (Ativos), RH Recurso, PR Processo, PT Portal. A coluna `Identificador Classe` da planilha liga o erro à classe de exceção em `catalogo/classes_supravizio.tsv`. As colunas 'originais' da planilha são idênticas às traduzidas.

## Utilitários (SV)
### SV0001 — Usuário ou senha inválidos
- Causa: O usuário informado não existe no cadastro de usuários do Supravizio ou existe mas sua senha não é válida.
- Efeito: Não foi possível conectar
- Ação: [UserDatasourceMessage]

### SV0002 — Nenhum controle configurado para exibição da Propriedade Customizada [PropertyName]
- Causa: Não foi definido um controle para edição da Propriedade Customizada [PropertyName]
- Efeito: Não é possível exibir o controle de edição da Propriedade [PropertyName]
- Ação: Entre em contato com o responsável pela customização do sistema

### SV0003 — [PythonMessage]
- Causa: Erro na execução do script do Evento Customizado '[EventName]'
- Efeito: Não foi possível concluir a operação
- Ação: Entre em contato com usuário administrador do sistema e informe que o erro ocorreu no evento '[EventName]' do tipo de dado '[ClassName]'.

### SV0004 — Job não pode ser removido
- Causa: Para o processo implementado pelo Job deve existir necessariamente uma instancia ativa.
- Efeito: Não foi possível remover o Job
- Ação: O Job não pode ser removido

### SV0005 — Valor inválido para Período de Job Singleton
- Causa: O valor de período de repetição não é válido para um Job do tipo Singleton
- Efeito: Não é possível gravar dados do Job
- Ação: Para o período informe um valor maior que zero.

### SV0006 — Usuário [Username] não possui autorização para acessar a transação [TransactionName]
- Causa: O Usuário [Username] não possui permissão de acesso a transação [TransactionName]
- Efeito: Este usuário não pode acessar a transação [TransactionName]
- Ação: Solicite um perfil de acesso que disponibiliza acesso a transação [TransactionName]

### SV0007 — Sessão de usuário finalizada. [Reason]
- Causa: A sessão do usuário [Username] foi finalizada
- Efeito: Não é possível acessar transações ou utilizar recursos do sistema com o Login atual
- Ação: Este erro ocorre quando o mesmo usuário faz logon mais de uma vez ou quando o usuário Administrador encerra manualmente a sessão de um usuário conectado. Para contornar feche todas as janelas e execute novamente a conexão informando seu usuário e senha.

### SV0009 — O objeto '[ObjectName]' não tem nome único no Serviço de Diretório
- Causa: Foram encontrada(s) [Count] ocorrência(s) do objeto '[ObjectName]' no Serviço de Diretório.
- Efeito: Não é possível consultar ou modificar o objeto '[ObjectName]'
- Ação: Verifique o cadastro do objeto '[ObjectName]' no Serviço de Diretório. Verifique também informações de conexão ao Serviço de Diretório na transação de configurações do sistema.

### SV0010 — Não foi encontrado nenhum objeto '[ObjectName]' do tipo '[CategoryName]' no Serviço de Diretório
- Causa: O objeto '[ObjectName]' não existe como '[CategoryName]'
- Efeito: Não é possível encontrar o objeto '[ObjectName]'
- Ação: Verifique a existencia do objeto no Serviço de Diretório

### SV0011 — O Endereço de Domínio do Serviço de Diretório não foi configurado na tela de configurações.
- Causa: O endereço do Domínio não foi configurado
- Efeito: Não é possível conectar ao Serviço de diretório
- Ação: Configure o endereço do Domínio na tela de configurações do sistema.

### SV0012 — Erro detectado pelo Serviço de Diretório: [MensagemErro]
- Causa: Ocorreu um erro ao executar operação no Serviço de Diretório. Mensagem de erro: '[MensagemErro]'
- Efeito: Não foi possível processar solicitação no Serviço de Diretório
- Ação: Entre em contato com o suporte informando a mensagem de erro '[MensagemErro]'

### SV0013 — Valor '[InvalidValue]' inválido para restrição de registros
- Causa: Foi configurada uma fórmula para restrição de acesso a registros que retorna um valor que não é um tipo primitivo (inteiro, string, booleano etc) ou enumeração. Somente tipos primitivos podem ser utilizados em expressões de restrição de registros.
- Efeito: Não é possível acessar registros da transação
- Ação: Entre em contato com o responsável pela manutenção do perfil de acesso '[RoleName]' e correção do filtro da propriedade '[PropertyName]'

### SV0014 — Número máximo de usuários licenciados excedido
- Causa: O número máximo de usuários licenciados foi atingido
- Efeito: Não é possível a conexão no sistema
- Ação: Entre em contato com o administrador do sistema para monitoramento de usuários conectados

### SV0015 — Usuário de rede está travado
- Causa: Usuário de rede está travado
- Efeito: Não é possível conectar no sistema
- Ação: Entre em contato com o suporte para destravamento de senha de rede

### SV0016 — Licença não encontrada
- Causa: Não foi encontrada informação de licenciamento na instalação do produto.
- Efeito: Não é possível a conexão no sistema
- Ação: Entre em contato com o fabricante para regularização de licenciamento

### SV0017 — Licença vencida
- Causa: A Licença excedeu o limite de dias de uso
- Efeito: Não é possível a conexão no sistema
- Ação: Entre em contato com o fabricante para regularização de licenciamento

## Configuração/Ativos (CF)
### CF0001 — Situação Inicial não definida paro Tipo de Item de Configuração '[DescricaoClasseConfiguracao]'
- Causa: o Tipo de Item de Configuração '[DescricaoClasseConfiguracao]'  não possui uma Situação definida como Inicial
- Efeito: Não foi possível concluir operação
- Ação: Solicite ao responsável pelo cadastro de Tipos de Itens de Configuração que defina uma Situação Inicial para o Tipo de Item de Configuração '[DescricaoClasseConfiguracao]'   [DescricaoClasseConfiguracao]

### CF0002 — Digite palavras mais significativas
- Causa: Quando uma pesquisa é realizada utilizando como critério palavras pouco significativas
- Efeito: Não foi possível realizar a pesquisa
- Ação: O usuário deve realizar uma busca por palavras mais significativas

## Recurso (RH)
### RH0002 — Fornecedor não informado
- Causa: Para Pessoas do tipo Terceiro é obrigatório o preenchimento do campo Fornecedor.
- Efeito: Não foi possível gravar os dados da Pessoa
- Ação: Informe o Fornecedor

### RH0003 — Solucionador já está ativo em '[NomeGrupoAtivo]'
- Causa: O Solucionador já se encontra ativado no Grupo de Trabalho '[NomeGrupoAtivo]'
- Efeito: Não é possível ativar o Solucionador
- Ação: Desative esta Pessoa no Grupo de Trabalho '[NomeGrupoAtivo]' e repita esta operação.

### RH0004 — Referência circular em hierarquia de Áreas
- Causa: Um ou mais áreas formam referência circular por meio do campo 'Área pai'.
- Efeito: Não é possível definir hierarquia entre Áreas
- Ação: Analise o cadastro das seguintes Áreas: [ListaOrgaos]

### RH0005 — Usuário AD não pode recuperar senha
- Causa: Quando usuário que tenta recuperar Senha é do AD
- Efeito: Este usuário não possui senha cadastrada, logo não é possível recuperar senha
- Ação: Não existe uma senha cadastrada. Solicite ao administrador do sistema que cadastre uma nova senha para acesso ao Portal de Processos

### RH0006 — Remoção de Charge-back limitada ao último período
- Causa: Houve uma tentativa de remover um período de Charge-back que não é o último período apurado.
- Efeito: Não é possível remover o período [Mes]/[Ano]
- Ação: Se for realmente necessário remover o período [Mes]/[Ano] avalie a possibilidade de remover todos os perídos de [UltimoMes]/[UltimoAno] até o período desejado.

### RH0007 — Substituto não está lotado em um Grupo de Trabalho
- Causa: O Substituto informado na Ausência não é um Solucionador lotado em um Grupo de Trabalho
- Efeito: Não é possível registrar a Ausência
- Ação: Informe um Solucionador lotado em um Grupo de Trabalho.

### RH0008 — Não é possível recuperar senha pois esta sendo utilizada autentidação pelo Serviço de diretório.
- Causa: Quando usuário que tenta recuperar Senha é do Serviço de diretório
- Efeito: Logo não é possível recuperar senha do Serviço de diretório.
- Ação: Solicite ao administrador do sistema que recupere a senha do Serviço de diretório.

## Recurso? (RE, prefixo fora do padrão)
### RE0001 — Nenhum Solucionador cadastrado
- Causa: A Pessoa ou Usuário corrente não foi associado a nenhum Grupo de Trabalho.
- Efeito: Não é possível gerar Ordens de Serviço para o usuário '[NomeUsuario]'
- Ação: Cadastrar a pessoa/usuário  '[NomeUsuario]' em algum Grupo de Trabalho.

## Processo (PR)
### PR0004 — Subprocesso de Link Final não definido
- Causa: Durante a definição de processo não foi definido o Subprocesso associado ao LinkFinal
- Efeito: Não foi possível configurar tela de Edição
- Ação: Entre em contato com o Gestor de Processos

### PR0006 — Não é possível Iniciar ou Cancelar uma Versão para Aprovação de uma Ordem de Serviço Finalizada
- Causa: A Ordem de Serviço associada está Finalizada
- Efeito: Não é possível Iniciar ou Cancelar uma Versão para Aprovação de uma Ordem de Serviço Finalizada
- Ação: Reabra a Ordem de Serviço e tente novamente.

### PR0008 — Existe uma ou mais Versões com Situação diferente de Cancelada
- Causa: Uma ou mais Versões dentro do mesmo Assunto/Fase encontra-se em Elaboração, Pendente, Aprovada ou Reprovada.
- Efeito: Não foi possível criar uma nova Versão para o Assunto '[NomeAssunto]'
- Ação: Cancele todas as versões existentes antes de criar uma nova. Se necessário atualize a exibição da Ordem de Serviço para identificar versões em questão.

### PR0009 — Versão já foi Iniciada
- Causa: A Versão já foi Iniciada e por isto não pode ser modificada.
- Efeito: Não é possível modificar uma Versão que tenha sido iniciada.
- Ação: Se for realmente necessário modificar a Versão então Cancele a corrente e crie uma Nova.

### PR0011 — A Fórmula do desvio não retorna um valor encontrado entre as alternativas da decisão.
- Causa: A Fórmula do desvio não retorna um valor encontrado entre as alternativas.
- Efeito: Não foi possível determinar a próxima Atividade
- Ação: Entre em contato com responsável por configuração de Processo para que providencie ajustes na configuração do desvio de processo.

### PR0012 — '[NomePessoa]' não é Aprovadora da Ordem de Serviço para o assunto '[DescricaoAssunto]'
- Causa: '[NomePessoa]' Não é um Aprovador configurado para a Versão [NumeroVersao] do Assunto '[DescricaoAssunto]'
- Efeito: Não foi possível concluir a Aprovação/Reprovação
- Ação: Solicite ajuda ao Solucionador responsável do atendimento

### PR0013 — A Versão [NumeroVersao] já se encontra Aprovada ou Reprovada por '[NomePessoa]'
- Causa: O aprovador '[NomePessoa]' já realizou a Aprovação/Reprovação
- Efeito: Não é possível Aprovar ou Reprovar novamente
- Ação: Solicite ajuda ao Solucionador responsável

### PR0014 — Subprocesso '[DescricaoSubProcesso]' não possui uma atividade do tipo LinkInicial para criação de Derivadas
- Causa: Não foi configurado no Subprocesso '[DescricaoSubProcesso]' uma Atividade do tipo LinkInicial
- Efeito: Não foi possível iniciar Subprocesso [DescricaoSubProcesso]
- Ação: Entre em contato com o responsável pela manutenção de Processos

### PR0015 — Nenhuma versão ativa para o Processo '[NomeProcesso]'
- Causa: O Processo '[NomeProcesso]' não possui nenhuma Versão ativada.
- Efeito: Não é possível iniciar serviços do Processo '[NomeProcesso]'
- Ação: Para realizar a ativação é necessário acesso a tela de manutenção de Processos. Nesta transação selecione uma Versão e clique em Modificar. Em seguida será exibido um diálogo onde estará visível o botão 'Ativar'

### PR0016 — Não é possível Classificar um Subprocesso Derivado
- Causa: Ocorreu uma tentativa de Classificação de Subprocesso derivado.
- Efeito: Não é possível concluir Classificação
- Ação: Cancela o Subprocesso existente e inicie um novo com o tipo desejado.

### PR0017 — Existem Derivadas não Canceladas
- Causa: Existem Derivadas não Canceladas
- Efeito: Não é possível realizar Classficação
- Ação: Cancele as Derivadas existentes ou inicie uma outra Principal com nova Classificação

### PR0020 — Ator [NomePapel] não definido
- Causa: Não foi definida a pessoa que realizará o papel de '[NomePapel]'
- Efeito: Não é possível realizar operações que envolvam um '[NomePapel]'
- Ação: Informe o '[NomePapel]' ou entre em contato com a pessoa responsável pela manutenção do Processo

### PR0021 — Não foi possível concluir a operação de [NomeOperacao] devido a pendências de Processo.
- Causa: Existem pendências relativas ao Processo
- Efeito: Não foi possível concluir a operação [NomeOperacao]
- Ação: Execute a função de Validação para verificar pendências existentes

### PR0022 — Data/hora de Execução de Mudança inválida
- Causa: A Data/hora de Execução da Mudança informada não é válida
- Efeito: Não é possível registrar a entrega do Serviço.
- Ação: Informe uma Data/hora de Execução de Mudança que seja maior que a Data/hora de Solicitação e menor ou igual a Data/hora corrente.

### PR0023 — Associação não configurada em chamada de Subprocesso
- Causa: Não existe uma Associação configurada na Atividade '[NomeAtividade]'.
- Efeito: Não é possível iniciar Subprocesso previsto na atividade '[NomeAtividade]'
- Ação: Configure uma Associação na Atividade '[NomeAtividade]'

### PR0024 — Ocorrência pendente de gravação
- Causa: Ocorrência pendente de gravação
- Efeito: Não é possível executar a operação '[NomeOperacao]'
- Ação: Salve a Ocorrência antes de executar a operação '[NomeOperacao]'

### PR0025 — Não é possível finalizar uma Principal com Derivadas Abertas
- Causa: Existem Derivadas com a situação Aberta
- Efeito: Não foi concluir com sucesso a Finalização
- Ação: Finalize todas as Derivadas antes de Finalizar a Principal

### PR0026 — Expressão para cálculo de prioridade não definida
- Causa: Não foi configurado no Método de Priorização '[DescricaoMetodoPriorizacao]' a Expressão para Cálculo de Prioridade. Esta expressão é obrigatória se existirem variáveis para cálculo e se for configurado o atributo Cálculo Automático.
- Efeito: Não foi possível Priorizar Ordem de Serviço
- Ação: Entre em contato com o usuário responsável pela manutenção do Processo para definição da Expressão de Cálculo para o Método de Priorização '[DescricaoMetodoPriorizacao]'.

### PR0027 — Pendência de configuração de processo
- Causa: Existe a seguinte pendência de configuração de processo: [DescricaoPendencia]
- Efeito: Não é possível continuidade na execução da ocorrência.
- Ação: Entre em contato com a pessoa responsável pela manutenção do processo e informe sobre esta pendência.

### PR0028 — Existe uma interrupção não-finalizada
- Causa: A interrupção iniciada em '[DataHoraInterrupcao]' foi aceita mas ainda não foi finalizada.
- Efeito: Não é possível adicionar uma nova solicitação de interrupção.
- Ação: Finalize a interrupção em aberto antes de criar uma nova.

### PR0029 — Ocorreu um erro no script '[DescricaoScript]': [MensagemErro]
- Causa: Ocorreu um erro no script [DescricaoScript]
- Efeito: O processo não
- Ação: Solicite ao administrador do sistema que providencie a correção para o script em questão.

### PR0030 — Não é possível Classificar uma Ordem de Serviço que teve a pesquisa de satisfação enviada
- Causa: Ocorreu uma tentativa de Classificar um Subprocesso com pesquisa de satisfação enviada.
- Efeito: Não é possível concluir Classificação
- Ação: Crie um novo Subprocesso com o tipo desejado.

## Portal (PT)
### PT0001 — Acesso Negado
- Causa: Usuário logado não possui permissão de acesso para a página
- Efeito: Acesso Negado
- Ação: Fazer logon com usuário com permissão de acesso.
