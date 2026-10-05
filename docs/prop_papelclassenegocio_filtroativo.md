# FiltroAtivo

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > FiltroAtivo

Recupera pessoas pela situação cadastral (ativo e/ou inativo)

**Exemplo 1: modificação da propriedade FiltroAtivo**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade FiltroAtivo
papelClasseNegocio.FiltroAtivo = true;
# salva modificação da propriedade FiltroAtivo
PapelClasseNegocio.Salva(papelClasseNegocio)
```
