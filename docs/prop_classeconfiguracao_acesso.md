# Acesso

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > Acesso

Define o mecanismo utilizado para acessar o arquivo, que pode ser por Compartilhamento de rede ou pelo mecanismo de Download/upload. No segundo caso o arquivo é transferido para a máquina local e, após modificações, deve ser enviado para atualização no servidor. O valor default deste campo está condicionado a configuração do tipo de acesso default existente na tela de Configurações (grupo Configuração)

**Exemplo 1: modificação da propriedade Acesso**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade Acesso
classeConfiguracao.Acesso = "Compartilhamento";
# salva modificação da propriedade Acesso
ClasseConfiguracao.Salva(classeConfiguracao)
```
