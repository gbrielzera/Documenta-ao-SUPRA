# Contrato

Caminho: Customização > Modelo de objetos > Recurso > Contrato

Um Contrato relaciona recursos (pessoas), Itens de configuração e regras para apontamento de horas trabalhadas. Além destas informações o contrato possui uma vigência, um fornecedor e um contratante. Um contrato pode ser informado em uma Ordem de Serviço por meio de um campo nativo denominado Contrato. Este campo é editado em um controle do tipo DropDownList contendo os contratos vigentes do Cliente da Ordem de Serviço. O Contrato é visível para seu gestor na aplicação de Autoatendimento, onde é possível acompanhar os apontamentos associados.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CodigoReferencia** | Código do contrato gerado pela área de suprimentos. | String |
| **ContatoFornecedor** | Telefone ou email de contato com Responsável pelo Contrato pelo Fornecedor. | String |
| **Contratante** | Empresa Contratante | [Empresa](objetos_empresa) |
| **ContratanteId** | Identificador do Orgao Contratante do Serviço | Inteiro |
| **DataFimValidade** | Data de fim de Validade do Contrato | Data/hora |
| **DataInicioValidade** | Data início de Validade do Contrato | Data/hora |
| **Descricao** | Descrição detalhada do Contrato | String |
| **FormaApontamento** | Forma de definição de apontamentos, se por total de horas ou por período | [FormaApontamento](enum_formaapontamento) |
| **Fornecedor** | Um Fornecedor é uma tipo especial de Empresa habilitada como prestador de serviços para a área. | [Fornecedor](objetos_fornecedor) |
| **FornecedorId** | Identificador do Fornecedor associado | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | Inteiro |
| **Items** | Itens de Configuração mantidos pelo Contrato | [Lista de ContratoItem](objetos_contratoitem) |
| **PlanoGestao** | Indicadores de Desempenho para Gestão do Contrato | [PlanoGestao](objetos_planogestao) |
| **PlanoGestaoId** | Identificador do Plano de Gestão | Inteiro |
| **PublicaVigenciaAA** | Publicar a vigência do contrato (data de início e fim de validade) na página de contratos do Autoatendimento | Booleano |
| **RecursosAplicados** | Grupos de solucionadores previstos na prestação de Serviço. | [Lista de RecursoAplicado](objetos_recursoaplicado) |
| **Responsavel** | Pessoa que é responsável pela manutenção de dados do Contrato. | [Pessoa](objetos_pessoa) |
| **ResponsavelFornecedor** | Nome da pessoa responsavável pelo Contrato pelo Fornecedor contratado. | String |
| **ResponsavelId** | Identificador da Pessoa associada | Inteiro |
| **TiposApontamento** | Tipos de Apontamentos previstos no Contrato | [Lista de TipoApontamentoContrato](objetos_tipoapontamentocontrato_) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ValidaMudancaForma** | Efetua validação antes de salvar em método da classe cliente Contrato. A principal validação é em relação a mudança de Forma de Apontamento, verificando se existem Ordens de Serviço com apontamentos de forma de apontar igual a forma antes da atualização. | System.Boolean ValidaMudancaForma(Venki.Supravizio.Recurso.Contrato contrato); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Contrato Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Contrato | Contrato Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Contrato Carrega(string nomePropriedade, object valorPropriedade); |
