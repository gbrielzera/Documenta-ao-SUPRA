# UserIsDisabled

Caminho: Recursos Avançados > Objeto AD > UserIsDisabled

Verifica no serviço de diretório se o usuário fornecido como parâmetro está desabilitado no serviço de diretório.

## Assinaturas

public bool UserIsDisabled(string username)

### username

Nome da conta de usuário para consulta. Se não for encontrado um usuário cujo campo **Nome de logon do usuário (anterior ao Windows 2000)** corresponda ao parâmetro **username**, então ocorrerá um erro de execução.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### Retorno

Verdadeiro se o usuário estiver desabilitado e Falso caso contrário. O fato do usuário estar bloqueado não influencia no resultado da consulta.

**Processo: Remoção de Acesso**

**Evento: Inicialização**

```
# Verifica se o usuário de rede do favorecido da Ordem de Serviço está desabilitado no Active Directory
if AD.UserIsDisabled(OrdemServico.Favorecido.UsuarioRede):
    AD.DisableUser(OrdemServico.Favorecido.UsuarioRede)
    # preenche o campo Solução da Ordem de Serviço com evidência
    OrdemServico.Solucao = "Usuário" + OrdemServico.Favorecido.UsuarioRede + " desabilitado em" +  DateTime.Now.ToString()
    # indica que o sistema deve avançar automaticamente para a próxima atividade do processo
    AvancaProximaAtividade = True
```
