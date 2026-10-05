# CoordenadorId

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > CoordenadorId

Identificador da Pessoa responsável pela Coordenação do Grupo de Trabalho. O coordenador possui atribuições especiais podendo realizar diversas operações e edições nas Ordens de Serviço sob responsabilidade dos seus subordinados.

**Exemplo 1: modificação da propriedade CoordenadorId**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade CoordenadorId
grupoTrabalho.CoordenadorId = 1;
# salva modificação da propriedade CoordenadorId
GrupoTrabalho.Salva(grupoTrabalho)
```
