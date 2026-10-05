# CustomEvent

Caminho: Customização > Modelo de objetos > Utilitários > CustomEvent

Evento para disponível para Customização em uma determinada Classe de Negócio. Todos os eventos são implementados pela linguagem de scripts Python e podem acessar propriedades da Classe de Negócio customizada.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClassId** | Idenficador da Classe | Inteiro |
| **CustomEventArgs** | Parâmetros fornecidos pelo mecanismo de invocação de eventos. Estes argumentos, somente leitura, podem ser utilizados para customização de regras de negócio em classes do sistema. | [Lista de CustomEventArgs](objetos_customeventargs) |
| **Description** | Descrição detalhada sobre quando o Evento é disparado pelo sistema. | String |
| **Id** | Identificador do Evento | Inteiro |
| **Implementations** | Implementações do Evento. Cada implementação está associada a um Domínio. | [Lista de CustomEventImplementation](objetos_customeventimplementation) |
| **Name** | Nome do Evento | String |
