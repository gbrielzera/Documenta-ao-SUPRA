# Sigla

Caminho: Customização > Modelo de objetos > Recurso > Orgao > Sigla

Nome resumido (código) utilizado para identificar um Órgão.

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto Orgao de identificador 1
orgao = Orgao.Carrega(1)
# modifica a propriedade Sigla
orgao.Sigla = "PRESIDENCIA";
# salva modificação da propriedade Sigla
Orgao.Salva(orgao)
```
