# FiltroPerfilCliente

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > FiltroPerfilCliente

Relação de perfis de clientes utilizados para recuperação de pessoas

**Exemplo 1: modificação da propriedade FiltroPerfilCliente**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade FiltroPerfilCliente
papelClasseNegocio.FiltroPerfilCliente = "Perfis de clientes";
# salva modificação da propriedade FiltroPerfilCliente
PapelClasseNegocio.Salva(papelClasseNegocio)
```
