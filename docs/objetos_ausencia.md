# Ausencia

Caminho: Customização > Modelo de objetos > Recurso > Ausencia

Registra a Ausência Temporária de um Solucionador. Com este registro o sistema impoem restrições em algumas operações como o Encaminhamento.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **DataHoraInicio** | Data e hora de início de validade para a regra de Ausência Temporária | Data/hora |
| **DataHoraPrevisaoRetorno** | Data e hora para Previsão de retorno do Solucionador | Data/hora |
| **DataHoraRegistro** | Data e hora de registro da Ausência Temporária | Data/hora |
| **EncaminharSubstituto** | Redirecionar encaminhamentos para o Substituto | Booleano |
| **Id** | Identificador da Ausência | Inteiro |
| **Motivo** | Motivo para a ausência | String |
| **PermiteSubstitutoModificar** | Permitir que o Substituto modifique todas as Ordens de Serviço no período de ausência | Booleano |
| **Pessoa** | Pessoa que ficará ausente | [Pessoa](objetos_pessoa) |
| **PessoaId** | Identificador da Pessoa para qual foi registrado o período de Ausencia | Inteiro |
| **Substituto** | Pessoa substituto para durante período de duração da ausencia. | [Pessoa](objetos_pessoa) |
| **SubstitutoId** | Identificador da Pessoa associada | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ObtemSubstituidos** | Recupera os substituídos pela pessoa fornecida como parâmetro no instante da chamada. | Venki.Supravizio.Recurso.AusenciaList ObtemSubstituidos(Venki.Supravizio.Recurso.Pessoa substituto); |
| **ObtemSubstituidos** | Recupera os substituídos pela pessoa fornecida como parâmetro no instante da chamada. | Venki.Supravizio.Recurso.AusenciaList ObtemSubstituidos(Venki.Supravizio.Recurso.Pessoa substituto,bool somenteAbertos); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Ausencia Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Ausencia | Ausencia Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Ausencia Carrega(string nomePropriedade, object valorPropriedade); |
