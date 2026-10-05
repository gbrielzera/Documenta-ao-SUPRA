# Fabricante

Caminho: Customização > Modelo de objetos > Ativos > Fabricante

Fabricante de um Item de Configuração.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Fabricante está ativo no sistema | Booleano |
| **Descricao** | Descrição detalhada do Fabricante | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Fabricante | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Fabricante Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Fabricante | Fabricante Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Fabricante Carrega(string nomePropriedade, object valorPropriedade); |
