# Diagrama

Caminho: Customização > Modelo de objetos > Processo > Diagrama

Diagrama

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Figuras** | Figuras que compoem o diagrama | [Lista de Figura](objetos_figura) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Diagrama | Inteiro |
| **SubProcesso** | Subprocesso | [SubProcesso](objetos_subprocesso) |
| **SubProcessoId** | Identificador do SubProcesso associado | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Diagrama Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Diagrama | Diagrama Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Diagrama Carrega(string nomePropriedade, object valorPropriedade); |
