# Exportação e importação

Caminho: Guia para Administradores > Editor de Relatórios > Exportação e importação

O Supravizio permite realizar a exportação e importação de um relatório.

**Exportando um Relatório**

Através do Menu Principal, acesse o Editor de Relatórios** (Relatórios | Editor de Relatórios)** e abra o registro do relatório que deseja exportar. Nas opções do relatório, clique no botão "Exporta layout, consultas e configuração de parâmetros":

Exportando um relatório

Selecione o local onde deverá ser salvo o relatório exportado e clique em Salvar. Então será gerado um arquivo com a extensão .rel e o nome do arquivo terá a descrição do relatório.

**Importando um Relatório**

Através do Menu Principal, acesse o Editor de Relatórios** (Relatórios | Editor de Relatórios)** e abra o registro do relatório que deseja importar. Nas opções do relatório, clique no botão "Importar layout, consultas e configuração de parâmetros":

Importando um Relatório

Procure pelo arquivo já exportado (com a extensão .rel), selecione-o e clique em Abrir. Veremos que, na aba Parâmetros, os registros de parâmetro foram importados. O layout, na aba Layout, também será importado, e juntamente, a query responsável pela pesquisa na base de dados.

Parâmetros Importados

Layout e Query importados

No caso de um parâmetro com conexão a um banco externo, ao realizar a exportação, juntamente é exportado o registro da conexão. Assim, ao importar o relatório, não é necessário a criação da conexão de banco de dados, porém, a String de Conexão não é salva, por motivos de segurança dos dados, então é necessário acessar o registro da conexão, em** (Utilitários | Conexões de banco de dados)**, e editar a String de conexão da conexão importada. Veja nas imagens que foi importado o parâmetro com a conexão "Conexao Externa", e na outra imagem, o registro da conexão também foi importado:

Importando parâmetro com conexão externa

Conexão importada

### Exportar e anexar arquivos em ocorrências de processos por script

Também é possível anexar relatórios em Ordens de Serviço com informações de parâmetros passados da própria Ordem de Serviço. Para isso, podemos realizar esta operação por um script em uma tarefa no processo:

Script inserido em tarefa

**Evento: Script Fim**

```
 

OrdemServico.AnexaExportacaoRelatorio("Fornecimento de voucher de taxi nos últimos 30 dias", "DESPESASTAXI", [ "pOcorrencia" ], [ OrdemServico.Id ], "pdf")
```

Assim, quando este script for executado em uma Ordem de Serviço, o relatório será anexado como um arquivo no tipo especificado no script:

### Relatório anexado na Ordem de Serviço

Assim, ao abrirmos o arquivo, ele irá conter o relatório com os parâmetros passados.

### Arquivo anexado
