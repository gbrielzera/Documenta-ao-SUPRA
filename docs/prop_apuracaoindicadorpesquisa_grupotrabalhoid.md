# GrupoTrabalhoId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicadorPesquisa > GrupoTrabalhoId

Identificador do GrupoTrabalho associado

**Exemplo 1: modificação da propriedade GrupoTrabalhoId**

```
# carrega objeto ApuracaoIndicadorPesquisa de identificador 1
apuracaoIndicadorPesquisa = ApuracaoIndicadorPesquisa.Carrega(1)
# modifica a propriedade GrupoTrabalhoId
apuracaoIndicadorPesquisa.GrupoTrabalhoId = 1;
# salva modificação da propriedade GrupoTrabalhoId
ApuracaoIndicadorPesquisa.Salva(apuracaoIndicadorPesquisa)
```
