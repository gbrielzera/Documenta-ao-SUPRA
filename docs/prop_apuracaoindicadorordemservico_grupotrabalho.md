# GrupoTrabalho

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorOrdemServico > GrupoTrabalho

Grupo Trabalho

**Exemplo 1: modificação da propriedade GrupoTrabalho**

```
# carrega objeto ApuracaoIndicadorOrdemServico de identificador 94
apuracaoIndicadorOrdemServico = ApuracaoIndicadorOrdemServico.Carrega(94)
# modifica a propriedade GrupoTrabalho
apuracaoIndicadorOrdemServico.GrupoTrabalho = GrupoTrabalho.Carrega(82);
# salva modificação da propriedade GrupoTrabalho
ApuracaoIndicadorOrdemServico.Salva(apuracaoIndicadorOrdemServico)
```
