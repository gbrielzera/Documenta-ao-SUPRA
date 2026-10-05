# Versao

Caminho: Customização > Modelo de objetos > Ativos > Software > Versao

Versão do Software

**Exemplo 1: modificação da propriedade Versao**

```
# carrega objeto Software de identificador 1
software = Software.Carrega(1)
# modifica a propriedade Versao
software.Versao = "Versão";
# salva modificação da propriedade Versao
Software.Salva(software)
```
