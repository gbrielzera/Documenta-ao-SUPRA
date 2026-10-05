# OrgaoPapel

Caminho: Customização > Modelo de objetos > Processo > OrgaoPapel

Órgãos relacionados em um papel para recuperação de atores.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **IncluirSubniveis** | Indica que órgãos filhos devem ser incluídos na recuperação. | Booleano |
| **Orgao** | Órgão que contém colaboradores e gestor que serão recuperados pelo papel | [Orgao](objetos_orgao) |
| **OrgaoId** | Identificador do Órgão associado | Inteiro |
| **PapelClasseNegocioId** | Identificador do papel proprietário da relação de órgãos. | Inteiro |
| **RegraRecuperacao** | Define quais colaboradores do órgão devem ser recuperados | [RecuperacaoPapelOrgao](enum_recuperacaopapelorgao) |
