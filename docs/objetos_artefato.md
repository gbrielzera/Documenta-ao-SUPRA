# Artefato

Caminho: Customização > Modelo de objetos > Ativos > Artefato

Itens de Configuração do tipo 'Artefato'. Um Artefato é o produto de uma fase qualquer do ciclo de desenvolvimento de um software. Exemplos: código fonte, modelo ER, especificação funcional etc

Este tipo herda atributos e funcionalidades do ancestral [ItemConfiguracao](objetos_itemconfiguracao)

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Artefato Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Artefato | Artefato Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Artefato Carrega(string nomePropriedade, object valorPropriedade); |
