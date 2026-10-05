# ResponsavelAtendePapel

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel > ResponsavelAtendePapel

Indica que o usuário responsável atendeu aos requisitos de papeis definidos em processo.

**Exemplo 1: modificação da propriedade ResponsavelAtendePapel**

```
# carrega objeto ApontamentoResponsavel de identificador 1
apontamentoResponsavel = ApontamentoResponsavel.Carrega(1)
# modifica a propriedade ResponsavelAtendePapel
apontamentoResponsavel.ResponsavelAtendePapel = true;
# salva modificação da propriedade ResponsavelAtendePapel
ApontamentoResponsavel.Salva(apontamentoResponsavel)
```
