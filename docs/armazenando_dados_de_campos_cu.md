# Armazenando Campos Customizados em Tabelas Customizadas

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Campos Customizados > Armazenando Campos Customizados em Tabelas Customizadas

Por padrão, quando criamos um Campo Customizado, o Supravizio armazena seus dados em tabelas com prefixo CP_ seguido do nome da tabela do cadastro relacionado. Por exemplo, quando criamos um Campo Customizado no cadastro de Pessoas, o Supravizio armazena a informação na tabela CP_PESSOA, pois a tabela de armazenamento desta entidade chama-se PESSOA. Veja abaixo, criamos um campo de Data de admissão no cadastro de Pessoas:

Observação: Para campos do tipo Lista de Registro e Lista de Objetos, o Supravizio cria tabelas separadas, tendo em vista que estes campos tem a característica de armazenamento de dados tabelados.

O Supravizio trata a entidade Ordem de Serviço de uma maneira especial. É possível configurar o armazenamento de um novo campo em tabelas especiais nomeadas pelo próprio analista. Para isso, criando um campo pelo cadastro de Campos ou através de um Data Object de Preenchimento de Campos, na propriedade Nome Tabela, selecione <Novo>:

Abre-se uma nova janela para o cadastro. Estas tabelas possuem sempre o prefixo **CPE_**:

O sistema cria então uma nova tabela para armazenar este campo:

Por se tratar de uma entidade (Ordem de Serviço) que geralmente onde criamos inúmeros Campos Customizados, esta pode ser uma configuração bem útil. Alguns Sistemas Gerenciadores de Bancos de Dados possuem limitações em quantidades de colunas em tabelas.

Caso necessite elaborar consultas de solicitações envolvendo este campo, é importante utilizar a cláusula LEFT JOIN pois o Supravizio armazena registros em solicitações que utilizaram tal campo:

```
select * from OCORRENCIA O left join CPE_FATURAS CPE on CPE.ID_OCORRENCIA = O.ID_OCORRENCIA
```
