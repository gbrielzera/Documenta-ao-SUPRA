# Utilizando Iniciador por Regra

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 15: Iniciar Ordens de Serviço por Arquivos > Utilizando Iniciador por Regra

Utilizando o subprocesso criado anteriormente, vamos colocar na pasta "D:\Temp" alguns arquivos que devem ser anexados nas Ordens de Serviço (deve ser criada uma Ordem de Serviço por arquivo):

Arquivos de retorno na pasta D:\temp

No Supravizio, todos os iniciadores baseados em Regra são executadas todas vezes que a Máquina de Processos, visível através do Gerenciamento de Ambiente (Utilitários | Gerenciamento de Ambiente), é executada. Para visualizar o intervalo entre execuções do Job de Máquina de processos utilize o botão de Propriedades, na aba de opções):

Gerenciamento do ambiente

Após a máquina ser executada novamente (pode ser feita manualmente utilizando o comando "Repetir"), observe o Relatório de execução:

Relatório de Execução

Observe que foram geradas 3 ocorrências em relação ao Evento inicial por regra. Veja que os arquivos que originaram as ocorrências indicadas foram anexados nas Ordens de Serviço:

Ocorrência 19 - Anexado "Retorno BB.txt"

Veja também que na pasta "D:\Temp" os arquivos foram removidos:

Pasta "D:\Temp" após remoção dos arquivos
