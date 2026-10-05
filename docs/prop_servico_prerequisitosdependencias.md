# PrerequisitosDependencias

Caminho: Customização > Modelo de objetos > Processo > Servico > PrerequisitosDependencias

Pré-requisitos ou Dependências para o perfeito funcionamento do Serviço.

**Exemplo 1: modificação da propriedade PrerequisitosDependencias**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade PrerequisitosDependencias
servico.PrerequisitosDependencias = "Pré-requisitos/Dependências";
# salva modificação da propriedade PrerequisitosDependencias
Servico.Salva(servico)
```
