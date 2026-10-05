# RecordColumn

Caminho: Customização > Modelo de objetos > Utilitários > RecordColumn

Campos de registros utilizados em propriedades customizadas do tipo Listagem de registros

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CalculateFormula** | Fórmla utilizada para cálculo de campos. Campos calculado não são persistidos em banco de dados. | String |
| **Control** | Controle utilizado para edição da coluna do registro | [RecordControlType](enum_recordcontroltype) |
| **CustomPropertyId** | Identificador da Propriedade Customizada | Inteiro |
| **Length** | Tamanho de campos string em quantidade de caracteres. Se não for preenchido então é adotado o tamanho padrão de 250 caracteres | Inteiro |
| **ListItems** | Listagem de itens disponíveis para seleção em um controle do tipo combobox. | String |
| **LookupScript** | Script utilizado para recuperação de itens utilizados como opções de preenchimento para o campo. Para o caso específico de recuperação a partir de banco de dados, se for fornecida uma tabela com dois campos então o primeiro será utilizado para preenchimento do campo enquanto o segundo fornecerá as opções exibidas no controle. | String |
| **Name** | Nome da coluna do registro. No caso de campos persistentes este nome é utilizado para criar uma coluna na tabela onde são persistidos os registros. | String |
| **Sequence** | Sequencial para apresentação no controle grid utilizado para visualização e edição | Inteiro |
| **Text** | Descrição resumida que é exibida no rótulo de controles utilizados na edição da coluna. | String |
| **Type** | Tipo de dado da coluna | [RecordType](enum_recordtype) |
| **Width** | Largura do controle utilizado para Edição da coluna. Quando não definido o sistema assume valor default conforme controle selecionado. | Inteiro |
