# Combobox

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Toolbox e elementos do BPMN > Data Objects > Entrada de Dados > Criação de Campos Customizados > Tipos de Controle > Combobox

Exibe um campo que, quando selecionado, exibe lista de opções onde o usuário pode selecionar apenas uma. Para este controle, é possível utilizar valores dos tipos Alfanumérico, Lógico, Listagem de Objetos.

Exemplo de controle Combobox

Neste tipo de controle, é possível configurar três formas de recuperação de opções:

- **Cadastros do sistema**: Recupera cadastros realizados no sistema, como por exemplo, pessoas, áreas ou artefatos;
- **Listagem de itens**: Obtém as opções preenchidas no campo, separados por ponto-e-vírgula (;) sem espaçamentos;
- **Script**: Retorna os resultados de uma consulta para a variável Itens, através do método **DB.ExecuteDataTable. **Caso seja do tipo Inteiro, deverá retornar um DataTable com no mínimo duas colunas, a primeira com o identificador e as colunas seguintes corresponderão à descrição que será exibida ao usuário. Caso haja mais de uma coluna, as próximas serão concatenadas à descrição. Caso seja Alfanumérico, o campo poderá armazenar diretamente o descritivo do valor ou se possuir mais de uma coluna, a primeira será utilizada como identificador. Ao visualizarmos o controle, serão exibidas as descrições para que possamos realizar a seleção. No entanto, o valor a ser armazenado no campo será o Identificador retornado.

Script para recuperação de opções

**Importante**: Caso o campo seja do tipo lógico e a propriedade ainda não tiver sido preenchida, esta retornará False ao ser acessada através de scripts utilizando o método **GetCustom**. Portanto, se for necessário verificar a mesma não tem valor, deve ser passado None como segundo parâmetro (valor default).
