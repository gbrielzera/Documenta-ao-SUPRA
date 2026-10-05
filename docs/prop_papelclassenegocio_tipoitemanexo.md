# TipoItemAnexo

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > TipoItemAnexo

Tipo de Item de Configuração que será utilizado para recuperar o responsável ou usuários que farão parte do papel. Durante o cálculo do papel serão utilizados todos os itens destes tipo que foram anexados na ocorrência.

**Exemplo 1: modificação da propriedade TipoItemAnexo**

```
# carrega objeto PapelClasseNegocio de identificador 78
papelClasseNegocio = PapelClasseNegocio.Carrega(78)
# modifica a propriedade TipoItemAnexo
papelClasseNegocio.TipoItemAnexo = ClasseConfiguracao.Carrega(23);
# salva modificação da propriedade TipoItemAnexo
PapelClasseNegocio.Salva(papelClasseNegocio)
```
