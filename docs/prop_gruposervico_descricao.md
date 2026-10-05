# Descricao

Caminho: Customização > Modelo de objetos > Processo > GrupoServico > Descricao

Descrição detalhada do GrupoServico

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto GrupoServico de identificador 1
grupoServico = GrupoServico.Carrega(1)
# modifica a propriedade Descricao
grupoServico.Descricao = "Descrição";
# salva modificação da propriedade Descricao
GrupoServico.Salva(grupoServico)
```
