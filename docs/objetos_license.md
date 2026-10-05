# License

Caminho: Customização > Modelo de objetos > Utilitários > License

Mantém dados de licenciamento do produto instalador.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Data** | Informações criptografadas sobre o licenciamento | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um License | Inteiro |
| **Owner** | Proprietário da licença de uso. | String |
| **RegisterDate** | Data em que foi realizada a importação do arquivo de licenciamento do produto. | Data/hora |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | License Carrega(int i); |
| **Novo** | Cria um novo registro do tipo License | License Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | License Carrega(string nomePropriedade, object valorPropriedade); |
