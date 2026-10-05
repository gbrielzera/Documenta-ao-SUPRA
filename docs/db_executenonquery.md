# ExecuteNonQuery

Caminho: Recursos Avançados > Objeto DB > ExecuteNonQuery

Executa um comando SQL de modificação (Insert, Update ou Delete) em um banco de dados. Se ocorrer algum erro durante a gravação da mensagem é levantada uma Exceção.

## Assinatura

public int ExecuteNonQuery(string commandText)

public int ExecuteNonQuery(string commandText, string database)

### commandText

Comando SQL DELETE, UPDATE ou INSERT para modificação de banco de dados.

### database

Identificador da conexão com banco de dados configurado na camada servidora. Se não for informado o comando será executado no banco de dados do Supravizio.

### Retorno

Quantidade de registros modificados pela comando.

**Processo: Backup**

**Evento: Inicialização**

```
# Executa Update do telefone da tabela PESSOA
DB.ExecuteNonQuery("Update PESSOA SET TELEFONE = '99999999' WHERE ID_PESSOA = 4")
# indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
