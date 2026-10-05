# CustomEventArgs

Caminho: Customização > Modelo de objetos > Utilitários > CustomEventArgs

Argumentos disponibilizados pelo mecanismo invocador de Eventos Customizados. Estes argumentos, somente leitura, podem ser utilizados na implementação de regras de negócio contida no evento.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CustomEventId** | Identificador do Evento proprietário do argumento. | Inteiro |
| **Description** | Descrição detalhada sobre o conteúdo e utilização do argumento. | String |
| **Name** | Na implementação do script este argumento pode ser acessado por uma variável declarada com este Nome. | String |
| **Type** | Tipo de dados do argumento. No caso de classes de negócio o tipo se refere aquele disponível para o mecanismo de customização (proxies de customização). | String |
