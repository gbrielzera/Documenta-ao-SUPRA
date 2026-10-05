# PapelProcesso

Caminho: Customização > Modelo de objetos > Processo > PapelProcesso

Papel de uma Pessoa dentro da execução do Processo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AtorGrupoTrabalho** | Critério para seleção de Atores em Grupos de Trabalho | [AtorGrupoTrabalho](enum_atorgrupotrabalho) |
| **DesenhoProcessoId** | Número sequencial gerado automaticamente pelo sistema para Identificar um DesenhoProcesso | Inteiro |
| **ExcluiAprovacoes** | Exclui da contagem de Ocorrências aquelas que estiveram Pendentes de Aprovação. | Booleano |
| **GrupoTrabalho** | Grupo Trabalho | [GrupoTrabalho](objetos_grupotrabalho) |
| **GrupoTrabalhoId** | Identificador do GrupoTrabalho associado | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um PapelProcesso | Inteiro |
| **IncluiCoordenador** | Inclui seleção do Coordenador do Grupo de Trabalho. Se o critério de seleção de solucionadores do grupo for Coordenador então este campo é desconsiderado. | Booleano |
| **Nome** | Nome do Papel | String |
| **PapelClasseNegocio** | Definição global do Papel | [PapelClasseNegocio](objetos_papelclassenegocio) |
| **PapelClasseNegocioId** | Identificador do PapelClasseNegocio associado | Inteiro |
| **Pessoa** | Solucionador responsável | [Pessoa](objetos_pessoa) |
| **PessoaId** | Identificador da Pessoa associada | Inteiro |
| **Referencia** | Descritivo completo sobre o Papel de Processo. Se não preenchido e estabelecida uma relação com um Papel global então é utilizada a referência deste último. | String |
| **ScriptSelecaoAtores** | Script para seleção de Atores de um Papel de Processo | String |
