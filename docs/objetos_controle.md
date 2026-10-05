# Controle

Caminho: Customização > Modelo de objetos > Processo > Controle

Controles

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Afirmacoes** | Afirmações relacionadas ao Controle. Esta coleção é preenchida inicialmente com os mesmos itens de afirmações da associação Risco x Subprocesso e pode ser redefinido pelo usuário neste nível. | [Lista de ControleAfirmacao](objetos_controleafirmacao) |
| **AmostragemTeste** | Orientação para amostragem de teste | String |
| **Automacao** | Tipo de operacionalização do Controle. | [AutomacaoControle](enum_automacaocontrole) |
| **ClasseControle** | Item da Biblioteca de Controles | [ClasseControle](objetos_classecontrole) |
| **ClasseControleId** | Identificador do(a) ClasseControle associado(a) | Inteiro |
| **ControleAdequado** | O Controle está adequado | Booleano |
| **ControleChave** | Controle chave | Booleano |
| **COSOAtividadeControle** | Atividade de Controle | Booleano |
| **COSOAvaliacaoRisco** | Avaliação de Risco | Booleano |
| **COSOControlEnviroment** | Control Enviroment | Booleano |
| **COSOInformacaoComunicacao** | Informação e Comunicação | Booleano |
| **COSOMonitoramento** | Monitoramento | Booleano |
| **Descricao** | Descrição do Controle | String |
| **EfetividadeDesenho** | Possui | Booleano |
| **EfetividadeOperacional** | Possui efetividade operacional | Booleano |
| **FrequenciaControle** | Frequência de execução do Controle | [FrequenciaControle](objetos_frequenciacontrole) |
| **FrequenciaControleId** | Identificador do(a) FrequenciaControle associado(a) | Inteiro |
| **FrequenciaTeste** | Frequência de teste do Controle | [FrequenciaControle](objetos_frequenciacontrole) |
| **FrequenciaTesteId** | Frequência de teste do Controle | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Controle | Inteiro |
| **ObjetivoAcessoRestrito** | Acesso restrito | Booleano |
| **ObjetivoExatidao** | Exatidão | Booleano |
| **ObjetivoTotalidade** | Totalidade | Booleano |
| **ObjetivoValidade** | Validade | Booleano |
| **RiscoProcesso** | Risco existente no Subprocesso que é mitigado pelo Controle. | [RiscoProcesso](objetos_riscoprocesso) |
| **RiscoProcessoRiscoId** | Identificador do RiscoProcesso associado | Inteiro |
| **RiscoProcessoSubProcessoId** | Identificador do RiscoProcesso associado | Inteiro |
| **RoteiroTeste** | Roteiro de teste do Controle | String |
| **SubProcessoId** | Identificador do Tipo de Subprocesso | Inteiro |
| **TesteHabilitado** | Controle deve ser testado | Booleano |
| **Tipo** | Tipo de Controle | [TipoControle](enum_tipocontrole) |
