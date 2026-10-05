# Tipos de Papéis

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Papéis e responsabilidades > Tipos de Papéis

Um papel pode indicar os atores utilizando diversos critérios. Esses critérios podem ser:

- [Relação de Grupos de Trabalho](relacao_de_grupos_de_trabalho)
- [Relação de Pessoas e filas](relacao_de_pessoas_e_filas)
- [Filtro no cadastro de pessoas](filtro_no_cadastro_de_pessoas)
- [Relação de Áreas](relacao_de_areas)
- [Pessoa relacionada na ocorrência](pessoa_relacionada_na_ocorrenc)
- [Item de configuração anexado na ocorrência](item_de_configuracao_anexado_n)
- [Composto por outros Papéis](composto_por_outros_papeis)
- [Customizado por script](customizado_por_script)
- [Execução de Tarefa do Processo ](execucao_de_tarefa_do_processo)

Tipos de Papéis

### Critério de Seleção Final

Em diversos casos de definição de papéis citados acima existe a possibilidade de configuração de um filtro para seleção que permite selecionar o solucionador responsável. Estes critérios são:

**1. Solucionador com menor quantidade de Ocorrências abertas** - O solucionador designado como responsável é o que, dentre os solucionadores selecionados durante a recuperação pelo papel, possui menos ocorrências abertas, sendo que podem ser consideradas ocorrências abertas as aprovações pendentes ou podem não ser conforme a configuração:

### Solucionador com menor quantidade de Ocorrências abertas

Veja que nesse caso existe também a propriedade Excluir aprovações. Esta propriedade, se for marcada como verdadeira (True), não serão relacionará ocorrências com aprovação como abertas.

### 2. Solucionador em Fila - Esta organização obedece o conceito da Fila (FIFO - First In, First Out). O solucionador designado como responsável está entre os solucionadores selecionados pela recuperação pelo Tipo de Papel o que é considerado próximo na fila do sistema, por exemplo, se existem três solucionadores o 1, o 2 e o 3. Inicialmente a fila seria 1 , 2, 3 então uma Ordem de Serviço chega para o papel e vai para o 1. Em seguida há outra OS, que respeita o critério sendo que a fila atualmente é 2,3,1 então ela fica sob responsabilidade do 2. Por fim quando receber outra OS será encaminhada para o 3 pois a fila está 3,1,2 e assim ocorre sucessivamente, quem recebe uma OS vai para o fim da fila:

### Solucionador em fila

### 3. Todas as pessoas recuperadas pela regra - Todos os solucionadores selecionados pela recuperação pelo Tipo de Papel são possíveis atores:

### Todas as pessoas recuperadas pela regra

## Determinando Prioridades

### Além das regras descritas acima, podemos também determinar um grau de prioridade para seleção de atores em alguns dos tipos descritos. Observe, por exemplo, que no cadastro de um papel que leva em consideração uma composição de papéis, podemos determinar uma prioridade para cada um dos papéis inseridos:

Papel Composto com Prioridade

### Repare que, para o papel "Analista Responsável", definimos a prioridade igual a 0 (zero) e para o papel Service Desk definimos a prioridade com valor 1. Neste caso, o critério de prioridade leva em consideração a ordem ascendente numérica, ou seja, no nosso exemplo, os atores do papel "Analista de Sistema" terão prioridade maior na seleção. Portanto o papel tentará recuperar atores através do papel Analista Responsável primeiro, e apenas caso não consiga recuperar nenhum ator, tentará recuperar do papel de prioridade menor (no caso do papel Service Desk de Prioridade 1). Caso dois ou mais itens da lista de composição do papel possuam a mesma prioridade, então serão levados em consideração todos os atores destes itens.

### O mesmo critério também está disponível em tipos de papéis baseados em [Relação de Pessoas e filas](tipos_papeis) e em [Relação de Grupos de Trabalho](relacao_de_grupos_de_trabalho)
