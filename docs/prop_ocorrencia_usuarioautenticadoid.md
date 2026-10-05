# UsuarioAutenticadoId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > UsuarioAutenticadoId

Identificador do usuário autenticado

**Exemplo 1: modificação da propriedade UsuarioAutenticadoId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade UsuarioAutenticadoId
ocorrencia.UsuarioAutenticadoId = 1;
# salva modificação da propriedade UsuarioAutenticadoId
Ocorrencia.Salva(ocorrencia)
```
