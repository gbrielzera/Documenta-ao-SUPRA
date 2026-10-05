# ApuracaoIndicador

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador

Valores apurador para um Indicador de Desempenho

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ano** | Ano | Inteiro |
| **DataHoraApuracao** | Data e hora em que foi apurado o valor do Indicador | Data/hora |
| **Denominador** | Denominador para apuração de indicadores que possuem como função de agregação Percentual | Decimal |
| **Indicador** | Indicador que gerou apuração | [Indicador](objetos_indicador) |
| **IndicadorId** | Identificador do(a) Indicador associado(a) | Inteiro |
| **Memoria** | Memória de cálculo com as chaves e valores. Formato: {IdObjeto}{S=atendeu critério;N=não atendeu critério}, ex: 1028S (Id igual 1028 e atendeu critério) | System.Object |
| **Mes** | Mês | Inteiro |
| **Numerador** | Numerador para apuração de indicadores que possuem como função de agregação Percentual | Decimal |
| **OrgaoCliente** | Órgão solicitante de serviço ou usuário de ativo | [Orgao](objetos_orgao) |
| **OrgaoClienteId** | Identificador do Orgao solicitante | Inteiro |
| **PlanoGestao** | O Plano de Gestão é utilizado para gerenciar Indicadores de Desempenho. Este plano pode ser utilizado para gestão de Indicadores de Desempenho Chave da área ou indicadores associados a Acordos de Nível de Serviço. | [PlanoGestao](objetos_planogestao) |
| **PlanoGestaoId** | Identificador do Plano de Gestão proprietário da apuração | Inteiro |
| **RitmoDenominador** | Valor do denominador da razão utilizada para cálculo de Ritmo. Este valor só é importante em Indicadores que realizem Contagem (Count). | Inteiro |
| **RitmoNumerador** | Valor do Numerador utilizado na razao para cálculo de Ritmo. Este valor só é importante em Indicadores que realizem Contagem (Count). | Inteiro |
| **RitmoValor** | Valor de Ritmo do Indicador estimado até fim do Período associado. Este valor será igual ao Valor apurado se o período estiver finalizado e só é importante em Indicadores que realizem Contagem (Count). | Decimal |
| **Sequencia** | Sequencia | Inteiro |
| **TipoApuracao** | Tipo de dado Apurado. | [TipoApuracao](enum_tipoapuracao) |
| **Valor** | Valor apurado para o Indicador | Decimal |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ApuracaoIndicador Carrega(string nomePropriedade, object valorPropriedade); |
