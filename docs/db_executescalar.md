# ExecuteScalar

Caminho: Recursos Avançados > Objeto DB > ExecuteScalar

Retorna a primeira coluna da primeira linha contendo o resultado da consulta fornecida como parâmetro. Se ocorrer algum erro durante a gravação da mensagem é levantada uma Exceção. Possui o mesmo comportamento do método ExecuteScalar de um Command do ADO.NET.

## Assinaturas

public object ExecuteScalar(string commandText)

public object ExecuteScalar(string commandText, string database)

### commandText

Comando SQL Select utilizado para recuperação de registros.

### database

Identificador da conexão com banco de dados configurado na camada servidora. Se não for informado o comando será executado no banco de dados do Supravizio.

### Retorno

Valor da primeira coluna do primeiro registro

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
# Retorna a primeira coluna da primeira linha da tabela PESSOA
idPessoa = DB.ExecuteScalar("select ID_PESSOA from PESSOA where upper(USUARIO_REDE) = '" + OrdemServico.Favorecido("Usuario de Rede").ToString().ToUpper() + "'"
```
