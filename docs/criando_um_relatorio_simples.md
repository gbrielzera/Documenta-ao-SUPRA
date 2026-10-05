# Criando um Relatório Simples

Caminho: Guia para Administradores > Editor de Relatórios > Criando Relatórios > Criando um Relatório Simples

Através deste exemplo demonstraremos a criação e utilização de um relatório simples que listará as Ordens de Serviço contando com o Número e Assunto.

1. Selecione no menu principal o comando **Relatórios | Editor de Relatórios**.

2. Crie um novo relatório.

3. No campo Descrição dê um nome adequado para o relatório. No nosso caso, vamos chamá-lo de "Relatório de Ordens de Serviço Simplificado".

4. Selecione a aba "Layout" e clique no comando "Novo Layout".

5. Clique em seguida no comando "Configurar dados".

6. Será exibida uma janela para criação de consulta baseada em SQL. Na listagem de tabelas exibida no lado direito da janela, dê um duplo clique na tabela [OCORRENCIA](dados_ocorrencia).

7. Observe que, na aba "Principal", foi adicionada a tabela OCORRENCIA exibindo as suas colunas (no formato NOME_DA_COLUNA e tipo). Selecione as colunas ASSUNTO e NUMERO.

Observe que ao selecionarmos as colunas, elas são automaticamente indicadas na consulta SQL no quadro inferior da janela.

Clique em OK. Repare que a consulta elaborada já está disponível no quadro "Lista de Campos".

8. Com a consulta já elaborada, podemos agora incluir os campos para exibição no próprio relatório. Na Lista de Campos, selecione, da consulta "Principal", o campo ASSUNTO. Com o campo selecionado no mouse, arraste até o início da [banda](bandas_de_um_relatorio) [Detail](bandas_de_um_relatorio).

Repita o mesmo procedimento para o campo ASSUNTO.

9. Faça a formatação dos campos utilizando larguras e alturas adequadas. Neste exemplo, vamos aumentar a largura do campo ASSUNTO de forma que fique limitada horizontalmente próxima à margem.

Após aumentarmos horizontalmente o comprimento do campo ASSUNTO, vamos agora reduzir verticalmente o tamanho do campo, visando diminuir os espaçamentos para economia de espaço.

Clique no fim da banda Detail e arraste para cima para delimitarmos a altura das linhas do relatório.

10. Salve o relatório.

11. Para conferir o resultado do relatório impresso, clique no comando "Visualizar".

O resultado retornado foi o seguinte:

Para publicar este relatório no menu principal, leia o tópico [Relatórios no Menu Principal](relatorios_no_menu_principal).
