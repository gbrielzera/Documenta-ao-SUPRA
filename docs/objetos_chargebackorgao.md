# ChargeBackOrgao

Caminho: Customização > Modelo de objetos > Recurso > ChargeBackOrgao

Conta de charge-back destinada a uma área.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ChargeBackId** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | Inteiro |
| **Itens** | Itens apurados para o Órgão | [Lista de ItemChargeBack](objetos_itemchargeback) |
| **Orgao** | Diretoria, Gerência, Departamento ou Área que compõe a estrutura organizacional. Em um Órgão, também denominado Área, podemos associar empregados ou terceiros (lotação). Um Órgão pode possuir uma associação com outro Órgão denominado "Pai". Esta associação "pai-filho" define a hierarquia de órgãos de uma Empresa. | [Orgao](objetos_orgao) |
| **OrgaoId** | Identificador do Orgao associado | Inteiro |
| **ValorTotal** | Valor total apurado para uma área de negócio. | Decimal |
