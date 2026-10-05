# Apontamento

Caminho: Customização > Modelo de objetos > Processo > Apontamento

Apontamento

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CampoBooleano1** | Campo opcional do tipo Booleano de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | Booleano |
| **CampoBooleano2** | Campo opcional do tipo Booleano de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | Booleano |
| **CampoDataHora1** | Campo opcional do tipo Data/Hora de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | Data/hora |
| **CampoDataHora2** | Campo opcional do tipo Data/Hora de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | Data/hora |
| **CampoDecimal1** | Campo opcional do tipo Decimal de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | Decimal |
| **CampoDecimal2** | Campo opcional do tipo Decimal de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | Decimal |
| **CampoInteiro1** | Campo opcional do tipo Inteiro de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | Inteiro |
| **CampoInteiro2** | Campo opcional do tipo Inteiro de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | Inteiro |
| **CampoString1** | Campo opcional do tipo String de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | String |
| **CampoString2** | Campo opcional do tipo String de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | String |
| **ClasseApontamento** | Classe de Apontamento | [ClasseApontamento](objetos_classeapontamento) |
| **ClasseApontamentoId** | Identificador do ClasseApontamento associado | Inteiro |
| **DataHoraApontamento** | Data e hora do Apontamento | Data/hora |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Apontamento | Inteiro |
| **Motivos** | Motivos indicados pelo Solucionador no instante do Apontamento | [Lista de MotivoApontamento](objetos_motivoapontamento) |
| **Responsavel** | Responsável pelo Apontamento | [Pessoa](objetos_pessoa) |
| **ResponsavelId** | Identificador do Responsável pelo Apontamento | Inteiro |
| **Situacao** | Situação do Apontamento | [SituacaoApontamento](enum_situacaoapontamento) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Apontamento Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Apontamento | Apontamento Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Apontamento Carrega(string nomePropriedade, object valorPropriedade); |
