# ModeloComunicado

Caminho: Customização > Modelo de objetos > Processo > ModeloComunicado

Template utilizado para produzir o corpo de um email. Neste template podemos utilizar campos especiais para produção de conteúdo dinâmico.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Corpo** | Template utilizado para produção do corpo do email. Neste template é possível introduzir campos que são utilizados para construção de conteúdo dinâmico. | System.Object |
| **Descricao** | Descrição detalhada do ModeloComunicado | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ModeloComunicado | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ModeloComunicado Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ModeloComunicado | ModeloComunicado Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ModeloComunicado Carrega(string nomePropriedade, object valorPropriedade); |
