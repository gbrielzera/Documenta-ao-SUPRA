# ClasseGap

Caminho: Customização > Modelo de objetos > Processo > ClasseGap

Classificações de Gaps

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do ClasseGAP | String |
| **Explicacao** | Explicação | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseGAP | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ClasseGap Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ClasseGap | ClasseGap Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ClasseGap Carrega(string nomePropriedade, object valorPropriedade); |
