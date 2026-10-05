# RespondidaAutoAtendimento

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > RespondidaAutoAtendimento

Indica que a Pesquisa de Satisfação foi respondida pelo Cliente utilizando a aplicação de Autoatendimento.

**Exemplo 1: modificação da propriedade RespondidaAutoAtendimento**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade RespondidaAutoAtendimento
pesquisa.RespondidaAutoAtendimento = true;
# salva modificação da propriedade RespondidaAutoAtendimento
Pesquisa.Salva(pesquisa)
```
