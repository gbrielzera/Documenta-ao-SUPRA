# Desvio Exclusivo

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Desvios > Desvio Exclusivo

Um Desvio Exclusivo é um desvio automático onde o Supravizio computa uma expressão IronPython determinando qual das alternativas satisfaz a expressão (apenas uma). Configuramos a fórmula na propriedade "Fórmula critério":

Quando uma solicitação processa esse elemento, computa esta fórmula e em seguida compara o valor preenchido na alternativa através do campo Valor comparação:

A sintaxe do Valor comparação deve ser exatamente como é sua representação por script. Caso a fórmula retorne um valor alfanumérico, este deve ser delimitado com áspas duplas "".

Configurando desvios em aprovações O Desvio Exclusivo comumente é utilizado após uma aprovação para indicar a "consequência" da aprovação ou reprovação de uma demanda. Para configurar este desvio, basta selecionar a tarefa relacionada a aprovação na propriedade **Regra de Desvio**:
