# Assunto

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > Assunto

Assunto abordado pela Pesquisa de Satisfação

**Exemplo 1: modificação da propriedade Assunto**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade Assunto
pesquisa.Assunto = "Assunto";
# salva modificação da propriedade Assunto
Pesquisa.Salva(pesquisa)
```
