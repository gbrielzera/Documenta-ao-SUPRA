# Empresa

Caminho: Customização > Modelo de objetos > Recurso > Orgao > Empresa

Empresa ao qual pertence o Órgão. Se preenchido é anulado o campo Unidade de Negócio.

**Exemplo 1: modificação da propriedade Empresa**

```
# carrega objeto Orgao de identificador 51
orgao = Orgao.Carrega(51)
# modifica a propriedade Empresa
orgao.Empresa = Empresa.Carrega(94);
# salva modificação da propriedade Empresa
Orgao.Salva(orgao)
```
