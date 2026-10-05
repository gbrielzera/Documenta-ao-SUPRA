# Modelo

Caminho: Customização > Modelo de objetos > Ativos > Modelo

Modelo de Item de Configuração segundo especificação de um Fabricante.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Modelo está ativo no sistema | Booleano |
| **Descricao** | Descrição detalhada sobre o Modelo | String |
| **Fabricante** | Fabricante do Modelo | [Fabricante](objetos_fabricante) |
| **FabricanteId** | Identificador do Fabricante associado ao Modelo | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Modelo | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Modelo Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Modelo | Modelo Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Modelo Carrega(string nomePropriedade, object valorPropriedade); |
