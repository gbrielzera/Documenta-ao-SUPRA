# PropertyLayout

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout

Layout de Classes e Propriedades

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClassId** | Identificador da Classe de uso apenas para otimização de carga | Inteiro |
| **ControlCapabilities** | Recursos disponíveis para o Controle. Exemplos: UpperCase para controles TextBox. O recurso é variável de acordo com o Controle. | String |
| **ControlUrl** | Caminho para carga do Controle em caso de Controles do tipo CustomControl | String |
| **Enabled** | Indica que o Controle está ativo | Booleano |
| **FormId** | Identificador do tipo de Formulário | Inteiro |
| **Group** | Nome do Agrupamento. Se não for preenchido considerar como Grupo Principal | String |
| **GroupParent** | Nome do agrupamento Pai | String |
| **GroupSequence** | Sequencial do Grupo no formulário. Se Group não for preenchido considerar o valor default -1 | Inteiro |
| **Height** | Altura em pixels do Controle | Inteiro |
| **Id** | Identificador do Layout | Inteiro |
| **Property** | Propriedades nativas de uma Classe de Negócio. | [Property](objetos_property) |
| **PropertyId** | Identificador da Propriedade | Inteiro |
| **Sequence** | Sequencial do Controle dentro do seu agrupamento | Inteiro |
| **Visible** | Indica que o Controle está visível | Booleano |
| **Width** | Largura em pixels do Controle | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | PropertyLayout Carrega(int i); |
| **Novo** | Cria um novo registro do tipo PropertyLayout | PropertyLayout Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | PropertyLayout Carrega(string nomePropriedade, object valorPropriedade); |
