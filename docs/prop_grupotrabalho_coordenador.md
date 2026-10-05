# Coordenador

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > Coordenador

Coordenador do Grupo de Trabalho

**Exemplo 1: modificação da propriedade Coordenador**

```
# carrega objeto GrupoTrabalho de identificador 51
grupoTrabalho = GrupoTrabalho.Carrega(51)
# modifica a propriedade Coordenador
grupoTrabalho.Coordenador = Pessoa.Carrega(94);
# salva modificação da propriedade Coordenador
GrupoTrabalho.Salva(grupoTrabalho)
```
