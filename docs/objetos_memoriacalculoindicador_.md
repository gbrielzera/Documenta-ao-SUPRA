# MemoriaCalculoIndicador

Caminho: MemoriaCalculoIndicador

Uma Memória de cálculo define um texto utilizado para determinar a origem de um valor apurado para um Indicador. O sistema permite a criação de uma série de esquemas de Memória de Cálculo e para um destes esquemas grande flexibilidade na elaboração dos dados utilizados na apuração do Indicador.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ExpressaoCondicao** | Fórmula que deve ter um retorno do tipo Booleano para indicar que deve ou não ser gerada Memória de Cálculo para o registro apurado. Se retornar verdadeiro então é avaliada a 'Expressão Texto' para determinar o conteúdo texto da Memória de Cálculo. Todas as duas Expressões podem acessar o registro apurado da mesma forma que as expressões do Indicador. Se não for fornecida uma Expressão então todos os registros são gravados na memória de cálculo. | String |
| **ExpressaoTexto** | Fórmula utilizada para determinar o Texto da memória de cálculo. Assim como expressões do Indicador pode acessar o registro que está sendo apurado pela rotina de Apuração. Se não for fornecida uma Expressão Texto então o sistema utiliza a representação textual do registro apurado. | String |
| **IndicadorId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Indicador | Inteiro |
| **Rotulo** | Rótulo de Identificação para a Configuração de Memória de Cálculo | String |
