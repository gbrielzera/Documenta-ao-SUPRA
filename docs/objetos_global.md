# Global

Caminho: Customização > Modelo de objetos > Utilitários > Global

Informações globais sobre a instalação

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ApplicationVersion** | Versão da aplicação | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Global | Inteiro |
| **Status** | Situação final após atualização de versão | String |
| **StatusMessage** | Mensagem para esclarecimento sobre a situação. Se a situação for Erro, por exemplo, esta mensagem contém a mensage de Exceção. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Global Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Global | Global Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Global Carrega(string nomePropriedade, object valorPropriedade); |
