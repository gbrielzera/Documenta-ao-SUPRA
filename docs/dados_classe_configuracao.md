# CLASSE_CONFIGURACAO

Caminho: Customização > Modelo de dados > Ativos > CLASSE_CONFIGURACAO

Um Tipo de Item de Configuração é utilizado para classificar Itens de Configuração, que são ativos sujeitos a alteração (como entrada ou saída) em processos de negócio.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_CONFIGURACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Item de Configuração. Este identificador não pode ser modificado pelo usuário. | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente a classificação de um Item de Configuração. No caso de tipos que representam arquivos este descritivo não pode conter os caracteres \\ / : > ? * " pois este descritivo é utilizado para nomear pastas no repositório de arquivos. | varchar(500) | varchar(500) | Não |
| **SIGLA** | Nome abreviado (código) utilizado para recuperar um Tipo de Item de Configuração em comandos SQL de relatórios ou scripts de customização. Esta sigla deve contar apenas números e letras. | varchar(50) | varchar(50) | Não |
| **ATIVO** | Indica que o Tipo de Item de Configuração está ativo no sistema. | char(3) | char(3) | Não |
| **SUPER_CLASSE** | Nome do Super Tipo associado que pode ser ser um Equipamento, Software, Dispositivo telefônico, Artigo da Base de Conhecimento ou Artefato (tipo genérico). Para cada Super tipo existe uma tela de cadastro no módulo de Ativos. | varchar(250) | varchar(250) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **CUSTO_AQUISICAO** | Valor do Custo de Aquisição Padrão para Itens do tipo. Este valor pode ser redefinido com o campo correspondente no Item. | decimal(15,2) | number(15,2) | Sim |
| **CUSTO_MANUTENCAO** | Valor do Custo de Manutenção Mensal Padrão para Itens da Classe. Este valor pode ser redefinido com o campo correspondente no Item. | decimal(15,2) | number(15,2) | Sim |
| **ID_FATOR_PRIORIDADE** | Identificador do(a) FatorPrioridade associado(a) | int | number(6,0) | Sim |
| **FONTE** | Indica a origem do cadastro do Tipo de Item de Configuração. | varchar(250) | varchar(250) | Não |
| **FONTE_DADOS** | Fonte de dados (válido somente para Artefatos) | varchar(250) | varchar(250) | Não |
| **HAB_REDEF_PAPEIS** | Habilita a redefinição de Papéis por Itens da Classe. Papéis possuem uma definição global de Atores que pode ser sobreposta por um Serviço. Este parâmetro indica que Itens de Configuração desta Classe podem acumular um segundo nível de redefinição de Papéis, que ainda está condicionada a parametrização do Serviço. | char(3) | char(3) | Não |
| **CRIT_CHARGE_BACK** | Critério para destino de custo no cálculo de Charge-back. | varchar(250) | varchar(250) | Não |
| **AGRUP_ITENS** | Define a forma como itens de charge-back apurado são agrupados no relatório apresentado para gestores de áreas clientes. | varchar(250) | varchar(250) | Não |
| **TIPO_ACESSO** | Define o mecanismo utilizado para acessar o arquivo, que pode ser por Compartilhamento de rede ou pelo mecanismo de Download/upload. No segundo caso o arquivo é transferido para a máquina local e, após modificações, deve ser enviado para atualização no servidor. O valor default deste campo está condicionado a configuração do tipo de acesso default existente na tela de Configurações (grupo Configuração) | varchar(250) | varchar(250) | Não |
| **TAMANHO_MAXIMO** | Tamanho máximo (em megabytes) permitido por arquivo deste tipo. | int | number(6,0) | Não |
| **COMENT_OBRIGATORIO** | Determina se o Item pertencente a esta Classe de Configuração terá o campo Comentário como Obrigatório | char(3) | char(3) | Não |
| **FILTRO_SERVICO** | Sempre que um item deste tipo for associado a uma Ordem de Serviço (na tela de edição ou Autoatendimento) existirá um filtro implícito por componentes do Serviço informado na ocorrência de processo. | char(3) | char(3) | Não |
| **INC_BLACK_LIST** | Indica que itens deste tipo fazem parte de um blacklist | char(3) | char(3) | Não |

Tabelas referenciadas por CLASSE_CONFIGURACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |

Tabelas que dependem de CLASSE_CONFIGURACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [CLASSE_COMPONENTE](dados_classe_componente) | \| **CLASSE_COMPONENTE** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_COMPONENTE \| ID_CLASSE_CONFIGURACAO \| |
| [CLASSE_DEPENDENCIA](dados_classe_dependencia) | \| **CLASSE_DEPENDENCIA** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_DEPENDENCIA \| ID_CLASSE_CONFIGURACAO \| |
| [CLASSE_COPIA](dados_classe_copia) | \| **CLASSE_COPIA** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_COPIA \| ID_CLASSE_CONFIGURACAO \| |
| [ITEM_COMPONENTE](dados_item_componente) | \| **ITEM_COMPONENTE** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [SITUACAO_CLASSE](dados_situacao_classe) | \| **SITUACAO_CLASSE** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [CLASSE_COMPONENTE](dados_classe_componente) | \| **CLASSE_COMPONENTE** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [CLASSE_DEPENDENCIA](dados_classe_dependencia) | \| **CLASSE_DEPENDENCIA** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [CLASSE_COPIA](dados_classe_copia) | \| **CLASSE_COPIA** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [TOPICO_CONH](dados_topico_conh) | \| **TOPICO_CONH** \| **CLASSE_CONFIGURACAO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |

**Exemplo 1: join com a tabela FATOR_PRIORIDADE**

```
select CLASSE_CONFIGURACAO.*, FATOR_PRIORIDADE.DESCRICAO
from CLASSE_CONFIGURACAO left outer join FATOR_PRIORIDADE on CLASSE_CONFIGURACAO.ID_FATOR_PRIORIDADE = FATOR_PRIORIDADE.ID_FATOR_PRIORIDADE
```
