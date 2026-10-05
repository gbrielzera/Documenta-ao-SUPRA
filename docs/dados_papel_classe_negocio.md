# PAPEL_CLASSE_NEGOCIO

Caminho: Customização > Modelo de dados > Processo > PAPEL_CLASSE_NEGOCIO

Um Papel representa uma importante ferramenta para configuração de responsabilidades em um Processo. Com este recurso é possível definir no Processo quem será, por exemplo, o responsável por uma determinada tarefa, quem realizará uma determinada aprovação e assim por diante. O Papel pode ser definido por referências de equipes, solucionadores, por scripts (recuperando registros do banco de dados) e também por composição de Papéis. Também é possível a redefinição de Atores de um Papel por Serviço.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PAPEL_CLASSE_NEGOCIO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Papel. | int | number(6,0) | Não |
| **NOME** | Descritivo utilizado para nomear um Papel. | varchar(100) | varchar(100) | Não |
| **ATIVO** | Indica que o Papel está ativo no Sistema. Quando inativo o Papel é ignorado pela rotina de cálculo de Atores. | char(3) | char(3) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **CLASSE_NEGOCIO** | Classe de Negócio dos Processos onde será publicado o Papel. | varchar(250) | varchar(250) | Não |
| **ATOR_GRUPO_TRABALHO** | Critério final de seleção de uma ou mais pessoas aplicado após regras de recuperação. | varchar(250) | varchar(250) | Não |
| **SCRIPT_ATORES** | Script para seleção de Atores de um Papel de Processo | text | clob | Sim |
| **REFERENCIA** | Descritivo completo do Papel. Este descritivo é utilizado na geração de documentação de Processos. | text | clob | Sim |
| **EXC_APROVACAO** | Exclui da contagem de Ocorrências aquelas que estiveram Pendentes de Aprovação. | char(3) | char(3) | Não |
| **USU_CONECTADO** | Seleciona entre as pessoas recuperadas pela configuração aqueles que são usuários solucionadores conectados na aplicação Supravizio. | char(3) | char(3) | Não |
| **TIPO** | Forma de recuperação de pessoas utilizada no cálculo do papel de processo | varchar(250) | varchar(250) | Não |
| **NOME_CAMPO** | Campo da ocorrência ou cadastro associado utilizado para obter um objeto do tipo Pessoa. | varchar(500) | varchar(500) | Sim |
| **OPCAO_NOME_CAMPO** | Opção de seleção por hierarquia a partir do campo indicado para recuperação. | varchar(250) | varchar(250) | Não |
| **FILTRO_TIPO_COLAB** | Permite a recuperação de pessoas pelo tipo empregado ou terceiro | varchar(500) | varchar(500) | Sim |
| **FILTRO_ORGAO** | Relação de órgãos onde estão lotadas as pessoas para recuperação | varchar(500) | varchar(500) | Sim |
| **FILTRO_EMPRESA** | Relação de empresas onde estão lotadas as pessoas que serão recuperadas | varchar(500) | varchar(500) | Sim |
| **FILTRO_ATIVO** | Recupera pessoas pela situação cadastral (ativo e/ou inativo) | char(3) | char(3) | Não |
| **FILTRO_CARGO** | Permite a recuperação pelo preenchimento do campo Cargo. | varchar(500) | varchar(500) | Sim |
| **FILTRO_FORNECEDOR** | Relação de empresas fornecedoras para recuperação de pessoas do tipo terceiros | varchar(500) | varchar(500) | Sim |
| **FILTRO_PERFIL_CLIENTE** | Relação de perfis de clientes utilizados para recuperação de pessoas | varchar(500) | varchar(500) | Sim |
| **FILTRO_UNIDADE** | Relação de Unidades de negócio onde estão localizadas as pessoas que serão recuperadas | varchar(500) | varchar(500) | Sim |
| **FILTRO_CUSTOM** | Relação de campos customizados do cadastro de Pessoas utilizados como filtro para recuperação | varchar(500) | varchar(500) | Sim |
| **ID_TIPO_ANEXO** | Identificador do Tipo de Item de Configuração | int | number(6,0) | Sim |
| **PAPEL_ITEM** | Define qual campo do Item de Configuração deve ser utilizado para identificação da pessoa. | varchar(500) | varchar(500) | Não |
| **ENV_ATIV_EXEC** | Recupera solucionadores pelo tipo de envolvimento na execução da atividade. | varchar(500) | varchar(500) | Não |
| **CODIGO_ATIVIDADE** | Código da atividade para recuperação de solucionadores envolvidos. | varchar(500) | varchar(500) | Sim |
| **SOMENTE_ULT_EXEC** | São considerados apenas os solucionadores envolvidos na última execução da atividade. | char(3) | char(3) | Não |

Tabelas referenciadas por PAPEL_CLASSE_NEGOCIO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_TIPO_ANEXO \| |

Tabelas que dependem de PAPEL_CLASSE_NEGOCIO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_PROCESSO](dados_papel_processo) | \| **PAPEL_PROCESSO** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [ATOR_SERVICO](dados_ator_servico) | \| **ATOR_SERVICO** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [ATOR_SERVICO](dados_ator_servico) | \| **ATOR_SERVICO** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_REDIR \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [PAPEL_COMP](dados_papel_comp) | \| **PAPEL_COMP** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_COMPOSICAO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [MENSAGEM_EVENTO](dados_mensagem_evento) | \| **MENSAGEM_EVENTO** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_DESTINATARIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [PAPEL_COMP](dados_papel_comp) | \| **PAPEL_COMP** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [ORGAO_PAPEL](dados_orgao_papel) | \| **ORGAO_PAPEL** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [GRUPO_PAPEL](dados_grupo_papel) | \| **GRUPO_PAPEL** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [PESSOA_PAPEL](dados_pessoa_papel) | \| **PESSOA_PAPEL** \| **PAPEL_CLASSE_NEGOCIO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
