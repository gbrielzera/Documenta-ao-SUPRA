# Iniciador por Regra

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Eventos Iniciadores > Iniciador por Regra

O iniciador por regra define uma fórmula que é avaliada constantemente e quando esta fórmula retorna valores então é gerada uma nova Ordem de Serviço. Este recurso é utilizado com frequência para leitura em um banco de dados via comando SQL. Neste caso são geradas Ordens de Serviço para cada registro retornado pela consulta SQL.

Evento inicial por regra

A condição configurada no iniciador é avaliada sempre que for executado o job denominado "Máquina de Processos" que está disponível na tela **Gerenciamento de Ambiente** (menu Utilitários). Veja na figura abaixo a configuração deste job:

Configuração do Job que controla a execução de eventos de processos

É importante não confundir a configuração de ciclo do Job que monitora os processos com o ciclo de um iniciador por timer. O ciclo do job é utilizado para verificação constante de todos os eventos iniciais ou intermediários que possuem configuração de termporizador ou regra. Na tela abaixo podemos observar um exemplo de configuração do ciclo do job:

Repetição do job que controla a Máquina de Procesos do Supravizio

A configuração acima indica que a cada 5 minutos será feita a verificação das fórmulas em iniciadores do tipo regra e, se necessário, serão geradas Ordens de Serviço. Também a cada 5 minutos o job verificará a necessidade de criação de Ordens de Serviço do tipo temporizador e, se for o momento configurado no ciclo do elemento, será gerada uma nova Ordem de Serviço.

### Retornos para propriedade de Regra:

É possível obter quatro tipos diferentes de retorno da regra:

- **Valor lógico**: Ativa ou desativa a geração.
- **Objeto DataTable do .Net**: Para cada registro será gerada uma OS.
- **Array do .Net**: Para cada item do array será gerada uma OS.
- **Lista de objetos do .Net que implementam a interface IList**: Para cada item da lista será gerada uma OS.

**Exemplo de Objeto DataTable:**

É possível utilizar um comando powershell que retorna uma lista de processos.

**Exemplo de Array:**

É possível utilizar uma regra que retorna um array de arquivos em um determinado diretório d:\temp: Directory.GetFiles(“d:\temp”)

OBS: Com a função OrdemServico.AnexaArquivo é possível anexar um arquivo da rede em uma Ordem de Serviço. Portanto seria possível recuperar pela regra com o comando Directory.GetFiles("d:\temp") diversos arquivos, abrir automaticamente uma Ordem de Serviço para cada arquivo e anexar o arquivo na Ordem de Serviço.

**Exemplo de IList:**

É possível utilizar um comando que retorna uma lista de objetos do Supravizio:

Orgao.ObtemTodosGestores()
