# GrupoTrabalhoId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorOrdemServico > GrupoTrabalhoId

Identificador do GrupoTrabalho associado

**Exemplo 1: modificação da propriedade GrupoTrabalhoId**

```
# carrega objeto ApuracaoIndicadorOrdemServico de identificador 1
apuracaoIndicadorOrdemServico = ApuracaoIndicadorOrdemServico.Carrega(1)
# modifica a propriedade GrupoTrabalhoId
apuracaoIndicadorOrdemServico.GrupoTrabalhoId = 1;
# salva modificação da propriedade GrupoTrabalhoId
ApuracaoIndicadorOrdemServico.Salva(apuracaoIndicadorOrdemServico)
```
