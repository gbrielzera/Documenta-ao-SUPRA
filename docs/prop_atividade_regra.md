# Regra

Caminho: Customização > Modelo de objetos > Processo > Atividade > Regra

Em iniciadores por regra ou temporizador esta fórmula é retornada para identificar o momento de geração de novas ocorrências. Neste caso ele pode retornar um valor lógico indicando que é necessário gerar ocorrências ou uma tabela via comando SQL e, neste último caso, é gerada uma ocorrência para cada linha retornada. Em eventos intermediários utilizamos esta fórmula para retornar um valor lógico indicando que é necessário executar uma transição entre tarefas.
