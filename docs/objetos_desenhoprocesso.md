# DesenhoProcesso

Caminho: Customização > Modelo de objetos > Processo > DesenhoProcesso

Desenho do Processo a ser executado. Permite que uma Etapa do Processo possa armazenar versões do Processo

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o DesenhoProcesso está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | Booleano |
| **Comentarios** | Comentários sobre a Versão. | String |
| **DataAtivacao** | Data em que o Desenho foi ativado no sistema. | Data/hora |
| **DataCriacao** | Data de criação da Modelagem | Data/hora |
| **DataDesativacao** | Data em que o modelo foi desativado. | Data/hora |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um DesenhoProcesso | Inteiro |
| **Papeis** | Papéis de Pessoas na execução do Processo | [Lista de PapelProcesso](objetos_papelprocesso) |
| **ProcessoId** | Identificador do Processo | Inteiro |
| **SubProcessos** | Subprocesso | [Lista de SubProcesso](objetos_subprocesso) |
| **Versao** | Número incremental indicando a versão do Desenho de Processo | Inteiro |
