# CustomEventImplementation

Caminho: Customização > Modelo de objetos > Utilitários > CustomEventImplementation

Implementação de Eventos

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CustomEventId** | Identificador do Evento | Inteiro |
| **Domain** | Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias | [Domain](objetos_domain) |
| **Source** | Código fonte do script Python. Neste código é possível acessar propriedades da Classe de Negócio customizada. Também é possível interromper modificações utilizando o comando raise (este comando emite uma Exception). | String |
