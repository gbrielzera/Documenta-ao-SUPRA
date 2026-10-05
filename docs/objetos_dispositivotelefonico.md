# DispositivoTelefonico

Caminho: Customização > Modelo de objetos > Ativos > DispositivoTelefonico

Dispositivo Telefônico

Este tipo herda atributos e funcionalidades do ancestral [ItemConfiguracao](objetos_itemconfiguracao)

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **NumeroLinha** | Número de linha | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | DispositivoTelefonico Carrega(int i); |
| **Novo** | Cria um novo registro do tipo DispositivoTelefonico | DispositivoTelefonico Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | DispositivoTelefonico Carrega(string nomePropriedade, object valorPropriedade); |
