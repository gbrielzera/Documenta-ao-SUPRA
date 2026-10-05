# HistoricoOrgao

Caminho: Customização > Modelo de objetos > Recurso > HistoricoOrgao

Histórico de estrutura organizacional na ocasião do processamento do Charge-back.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ChargeBackId** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | Inteiro |
| **Gestor** | Gestor do Órgão na ocasião da apuração do Charge-back | [Pessoa](objetos_pessoa) |
| **GestorId** | Identificador do Gestor da Área na ocasição da apuração do Charge-back | Inteiro |
| **Orgao** | Órgão na ocasição da apuração do Charge-back | [Orgao](objetos_orgao) |
| **OrgaoId** | Identificador do Orgao associado | Inteiro |
| **OrgaoPai** | Órgão pai da área na ocasição da apuração do Charge-back | [Orgao](objetos_orgao) |
| **OrgaoPaiId** | Identificador do Órgão pai na ocasião da apuração do Charge-back. | Inteiro |
| **Pessoas** | Pessoas lotadas no Órgão na ocasião da apuração do Charge-back. | [Lista de HistoricoPessoa](objetos_historicopessoa) |
