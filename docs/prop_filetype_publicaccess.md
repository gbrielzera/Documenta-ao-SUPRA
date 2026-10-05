# PublicAccess

Caminho: Customização > Modelo de objetos > Utilitários > FileType > PublicAccess

Indica que arquivos deste tipo são público e portanto podem ser acessados por qualquer usuário autenticado na aplicação. Arquivos que não são públicos podem ser acessados somente por usuários que possuem autorização na respectiva transação.

**Exemplo 1: modificação da propriedade PublicAccess**

```
# carrega objeto FileType de identificador 1
fileType = FileType.Carrega(1)
# modifica a propriedade PublicAccess
fileType.PublicAccess = true;
# salva modificação da propriedade PublicAccess
FileType.Salva(fileType)
```
