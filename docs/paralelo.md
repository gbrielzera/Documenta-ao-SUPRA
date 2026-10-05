# Paralelo

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Desvios > Paralelo

### O desvio Paralelo permite a divisão de uma ocorrência em uma ou mais ocorrências permitindo que uma solicitação seja atendida por mais de uma tarefa e responsabilidade ao mesmo tempo:

### Todas os os fluxos que saem deste elemento geram uma nova solicitação filha. Não há condição nem fórmula para sua configuração.

### A configuração deste desvio é bem simples. Inicialmente, basta inserir um elemento de desvio Paralelo:

### Em seguida, inclua uma ou mais tarefas que serão executadas no mesmo instante:

### Adicione os fluxos preenchendo a propriedade "Texto" em cada uma das oções:

### Depois, inclua um outro elemento Paralelo e inclua os elementos fluxos cuminando neste:

### Após ativado o seu processo, executando uma solicitação, no instante em que o processo encontra o desvio, geram-se novas solicitações filhas:

### Cada solicitação filha é seguida do número da solicitação pai, mais um símbolo separador e um número incremental:

### Para modificar este símbolo separador, selecione o elemento de paralelismo gerador das ocorrências e modifique a propriedade "Separador para numeração relativa":

### Configurando desta forma, os números das solicitações filhas são incrementais ao número da solicitação pai:
