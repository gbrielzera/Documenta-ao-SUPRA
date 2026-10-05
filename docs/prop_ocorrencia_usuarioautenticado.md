# UsuarioAutenticado

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > UsuarioAutenticado

Usuário que foi autenticado pela aplicação de Autoatendimento durante a abertura. Esta autenticação só é possível se não for selecionada a opção de troca de Cliente no Autoatendimento.

**Exemplo 1: modificação da propriedade UsuarioAutenticado**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade UsuarioAutenticado
ocorrencia.UsuarioAutenticado = Pessoa.Carrega(23);
# salva modificação da propriedade UsuarioAutenticado
Ocorrencia.Salva(ocorrencia)
```
