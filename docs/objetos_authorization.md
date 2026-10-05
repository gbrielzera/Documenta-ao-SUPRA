# Authorization

Caminho: Customização > Modelo de objetos > Utilitários > Authorization

Autorização para um Perfil de acesso

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **DataRestrictions** | Uma 'Restrição de registro' permite filtrar os registros que são exibidos em uma transação de Cadastro. Todas as restrições formam uma única expressão montada com o operador lógico AND, ou seja, são recuperados e disponibilizados para edição os registros que atendam TODAS as restrições de registro. Se o usuário possui vários perfis vale sempre o princípio da restritividade, ou seja, todas as restrições são acumuladas entre todos os perfis atribuídos. | [Lista de DataRestriction](objetos_datarestriction) |
| **FieldRestrictions** | Uma 'Restrição de campo' permite ocultar ou desabilitar um campo de uma tela de listagem ou edição de registros (Cadastros). IMPORTANTE: Uma ação do tipo Ocultar prevalece sobre uma do tipo Desabilitar. Se o usuário possui vários perfis então vale o princípio da restritividade, ou seja, são aplicadas todas as restrições acumuladas entre os diversos perfis atribuídos. | [Lista de FieldRestriction](objetos_fieldrestriction) |
| **RoleId** | Identificador do Perfil de acesso associado | Inteiro |
| **Transaction** | Tela do sistema autorizada para o usuário | [Transaction](objetos_transaction) |
| **TransactionId** | Identificador da Transação associada | Inteiro |
