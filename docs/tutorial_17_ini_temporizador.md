# Utilizando Iniciador por Temporizador

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 15: Iniciar Ordens de Serviço por Arquivos > Utilizando Iniciador por Temporizador

No exemplo anterior foi possível construir um subprocesso que detecta a existência de um novo arquivo para processamento. Vimos também que esta verificação é configurada no job "Máquina de Processos" e ocorre sempre que este job é executado. Em algumas circunstâncias é desejado que a verificação ocorra apenas em momentos programados: todos os dias as 22 horas, todos os sábados as 18 horas etc. Para estas situações devemos utilizar um iniciador do tipo timer e nele configurar a mesma regra utilizada no exemplo anterior. Neste tópico veremos como utilizar esta alternativa.

### Configurando o Iniciador no Subprocesso

No Editor de Processos, inclua um evento iniciador por Temporizador no subprocesso de "Processamento de Arquivos de Retorno":

Fluxo com Evento iniciador por Temporizador

No iniciador por temporizador, preencha a propriedade de "Regra" com:

Directory.GetFiles("D:\\temp-programado")

E preencha a propriedade de "Script Evento" com:

OrdemServico.AnexaArquivo(Regra.ToString(), "ANALISEPRECO", True)

E defina o tipo de ciclo que desejar (no exemplo utilizaremos o ciclo diário para ocorrer às 14:00 hrs). Portanto a aba de propriedades contém as seguintes definições (observação: não se esqueça de preencher a propriedade "Responsável"):

Propriedades do Iniciador por Temporizador

### Utilizando o Iniciador

Para utilizar um exemplo, vamos adicionar arquivos na pasta "D:\temp-programado":

Arquivos de Retorno

Agora basta aguardar a chegada do horário programado para observar no Relatório de execução da Máquina de Processo, visível através do Gerenciamento de Ambiente (Utilidades | Gerenciamento de Ambiente), que as ocorrências foram geradas:

Gerenciamento do Ambiente

E então consultar as ocorrências para ver que os arquivos foram anexados:

Ocorrência 22 - Anexado "Retorno BB.txt"

Veja também que na pasta "D:\Temp-Programado" os arquivos foram removidos:

Pasta "D:\Temp-Programado" após remoção dos arquivos
