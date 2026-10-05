# Corpo

Caminho: Customização > Modelo de objetos > Processo > ModeloComunicado > Corpo

Template utilizado para produção do corpo do email. Neste template é possível introduzir campos que são utilizados para construção de conteúdo dinâmico.

**Exemplo 1: modificação da propriedade Corpo**

```
# carrega objeto ModeloComunicado de identificador 1
modeloComunicado = ModeloComunicado.Carrega(1)
# modifica a propriedade Corpo
# salva modificação da propriedade Corpo
ModeloComunicado.Salva(modeloComunicado)
```
