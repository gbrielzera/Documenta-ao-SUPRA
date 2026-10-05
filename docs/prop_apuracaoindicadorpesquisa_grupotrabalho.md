# GrupoTrabalho

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorPesquisa > GrupoTrabalho

Grupo Trabalho

**Exemplo 1: modificação da propriedade GrupoTrabalho**

```
# carrega objeto ApuracaoIndicadorPesquisa de identificador 94
apuracaoIndicadorPesquisa = ApuracaoIndicadorPesquisa.Carrega(94)
# modifica a propriedade GrupoTrabalho
apuracaoIndicadorPesquisa.GrupoTrabalho = GrupoTrabalho.Carrega(82);
# salva modificação da propriedade GrupoTrabalho
ApuracaoIndicadorPesquisa.Salva(apuracaoIndicadorPesquisa)
```
