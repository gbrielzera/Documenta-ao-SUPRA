# PermiteRetormarResponsabilidade

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > PermiteRetormarResponsabilidade

Indica que é permitido ao último responsável retormar responsabilidade de uma ocorrência encaminhada para outro solucionador, seja o encaminhamento manual ou automático por configuração de processos.

**Exemplo 1: modificação da propriedade PermiteRetormarResponsabilidade**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade PermiteRetormarResponsabilidade
ocorrencia.PermiteRetormarResponsabilidade = true;
# salva modificação da propriedade PermiteRetormarResponsabilidade
Ocorrencia.Salva(ocorrencia)
```
