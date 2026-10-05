# ClasseApontamento

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento

Classe de Apontamento

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Codigo** | Código | String |
| **Descricao** | Descrição detalhada do ClasseApontamento | String |
| **DescricaoCampoBooleano1** | Descrição para entrada de dados no Campo Booleano 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoBooleano2** | Descrição para entrada de dados no Campo Booleano 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoDataHora1** | Descrição para entrada de dados no Campo Data/hora 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoDataHora2** | Descrição para entrada de dados no Campo Data/hora 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoDecimal1** | Descrição para entrada de dados no Campo Decimal 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoDecimal2** | Descrição para entrada de dados no Campo Decimal 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoInteiro1** | Descrição para entrada de dados no Campo Inteiro 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoInteiro2** | Descrição para entrada de dados no Campo Inteiro 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoString1** | Descrição para entrada de dados no Campo String 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **DescricaoCampoString2** | Descrição para entrada de dados no Campo String 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseApontamento | Inteiro |
| **MotivoObrigatorio** | A informação de um Motivo é obrigatória no instante em que é realizado o Apontamento. | Booleano |
| **Motivos** | Motivos | [Lista de MotivoClasseApontamento](objetos_motivoclasseapontamento) |
| **PermiteMotivoDigitado** | Permite a informação do Motivo do Apontamento por digitação e não por seleção de Item mantido na propriedade Motivos. | Booleano |
| **PermiteMultiplosApontamentos** | Permite vários apontamentos para uma ocorrência de Processo. | Booleano |
| **PermiteMultiplosMotivos** | Permite a informação de vários motivos no Apontamento | Booleano |
| **SequencialCampoBooleano1** | Define a sequencia de apresentação do controle utilizado para edição do Campo Booleano 1 | Inteiro |
| **SequencialCampoBooleano2** | Define a sequencia de apresentação do controle utilizado para edição do Campo Booleano 2 | Inteiro |
| **SequencialCampoDataHora1** | Define a sequencia de apresentação do controle utilizado para edição do Campo Data/hora 1 | Inteiro |
| **SequencialCampoDataHora2** | Define a sequencia de apresentação do controle utilizado para edição do Campo Data/hora 2 | Inteiro |
| **SequencialCampoDecimal1** | Define a sequencia de apresentação do controle utilizado para edição do Campo Decimal 1 | Inteiro |
| **SequencialCampoDecimal2** | Define a sequencia de apresentação do controle utilizado para edição do Campo Decimal 2 | Inteiro |
| **SequencialCampoInteiro1** | Define a sequencia de apresentação do controle utilizado para edição do Campo Inteiro 1 | Inteiro |
| **SequencialCampoInteiro2** | Define a sequencia de apresentação do controle utilizado para edição do Campo Inteiro 2 | Inteiro |
| **SequencialCampoString1** | Define a sequencia de apresentação do controle utilizado para edição do Campo String 1 | Inteiro |
| **SequencialCampoString2** | Define a sequencia de apresentação do controle utilizado para edição do Campo String 2 | Inteiro |
| **TipoEventoGerado** | Tipo de Evento gerado na ocorrência de um Apontamento | [TipoEvento](objetos_tipoevento) |
| **TipoEventoId** | Identificador do TipoEvento associado | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ClasseApontamento Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ClasseApontamento | ClasseApontamento Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ClasseApontamento Carrega(string nomePropriedade, object valorPropriedade); |
