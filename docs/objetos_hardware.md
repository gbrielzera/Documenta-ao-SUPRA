# Hardware

Caminho: Customização > Modelo de objetos > Ativos > Hardware

Itens de Configuração do tipo 'Equipamento'

Este tipo herda atributos e funcionalidades do ancestral [ItemConfiguracao](objetos_itemconfiguracao)

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CodigoOCS** | Código do hardware original do banco de dados OCS | String |
| **EtiquetaIdentificacao** | Número da Etiqueta de Identificação do Equipamento pela equipe de suporte. Este número pode ser utilizado pelo Solucionador durante o atendimento de um chamado. | String |
| **Local** | Localização do Equipamento | [Local](objetos_local) |
| **LocalId** | Identificador da localização do Equipamento | Inteiro |
| **MemoriaOCS** | Tamanho da memória detectada pelo OCS NG em megabytes | Inteiro |
| **Patrimonio** | Identificação de Patrimonio | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Hardware Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Hardware | Hardware Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Hardware Carrega(string nomePropriedade, object valorPropriedade); |
