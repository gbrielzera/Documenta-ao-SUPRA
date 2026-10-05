# UnidadeDefinicaoANO

Caminho: Customização > Modelo de objetos > Processo > Enumerações > UnidadeDefinicaoANO

Unidade de medida para configuração do Acordo de Nível de Serviço

| **Valor** | **Descrição** |
|---|---|
| **Minutos** | O tempo é configurado em minutos independente da existência de ANS ou serviços. Este método utiliza preferencialmente a configuração de períodos úteis do calendário associado ao solucionador (relação de Solucionadores do cadastro de Grupo de Trabalho). Se não existir o cadastro deste calendário é utilizado então o calendário onde está localizado o Solucionador (cadastro de Unidade de Negócio associada a pessoa). Por fim se não for encontrado um calendário o sistema considera disponibilidade 24x7 para cálculo de tempo disponível. |
| **PercentualANS** | O tempo é definido em função de um percentual sobre o tempo total configurado no Acordo de Nível de Serviço. |
| **HoraApontada** | O tempo é configurado em horas e o período apurado é formado pela soma de todos os apontamentos relacionados com a atividade ou grupo de atividade. |
