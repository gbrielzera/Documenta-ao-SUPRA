# AtoresItem

Caminho: Customização > Modelo de objetos > Ativos > AtoresItem

Atores

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um AtoresItem | Inteiro |
| **ItemConfiguracaoId** | Item de Configuração proprietário da redefinição de Papel | Inteiro |
| **PapelClasseNegocio** | Papel de Processo que é alvo de redefinição no Item de Configuração. Para um Serviço é possível criar diversas redefinições de Papel. | [PapelClasseNegocio](objetos_papelclassenegocio) |
| **PapelClasseNegocioId** | Identificador do PapelClasseNegocio associado | Inteiro |
| **PapelRedirecionado** | Papel de Processo utilizado como redirecionamento no instante de cálculo de Atores. Se este campo for preenchido o sistema automaticamente limpa o conteúdo do campo 'Pessoa'. Somente um destes campos pode ser preenchido. IMPORTANTE: Este recurso demanda cuidado especial com a criação de redefinições recursivas de Papeis. | [PapelClasseNegocio](objetos_papelclassenegocio) |
| **PapelRedirecionamentoId** | Identificador do Papel utilizado para redirecionamento. | Inteiro |
| **Pessoa** | Pessoa | [Pessoa](objetos_pessoa) |
| **PessoaId** | Identificador da Pessoa atribuída como Ator para o Papel | Inteiro |
