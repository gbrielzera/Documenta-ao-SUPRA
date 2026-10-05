# PlanoGestao

Caminho: Customização > Modelo de objetos > Processo > PlanoGestao

O Plano de Gestão é utilizado para gerenciar Indicadores de Desempenho. Este plano pode ser utilizado para gestão de Indicadores de Desempenho Chave da área ou indicadores associados a Acordos de Nível de Serviço.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **DataFim** | Data fim do plano. Quando modificado é atualizada a coleção de períodos de todos os Indicadores associados ao plano. | Data/hora |
| **DataInicio** | Data de início do plano. Quando modificado é atualizada a coleção de períodos de todos os Indicadores associados ao plano. | Data/hora |
| **Descricao** | Descrição detalhada do Plano de Gestão. Esta descrição é utilizada para seleção do Plao de Gestão na aplicação Executive Dashboard. | String |
| **GruposTrabalhoAutorizados** | Grupos de Trabalho que estão autorizados a visualizar o resultado da apuração de indicadores. | [Lista de GrupoTrabalhoAutorizado](objetos_grupotrabalhoautorizado) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um PlanoGestao | Inteiro |
| **Indicadores** | Indicadores associados ao Plano de Gestão. Para cada indicador existe um desdobramento de vários Períodos. Possui também uma Meta geral e redefinições por período. | [Lista de IndicadorPlano](objetos_indicadorplano) |
| **InformacoesRestritas** | O solucionador logado só visualiza suas informações ou informações de subordinados. | Booleano |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | PlanoGestao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo PlanoGestao | PlanoGestao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | PlanoGestao Carrega(string nomePropriedade, object valorPropriedade); |
