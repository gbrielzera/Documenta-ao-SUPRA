# Sigla

Caminho: Customização > Modelo de objetos > Processo > Servico > Sigla

Nome resumido do Serviço

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade Sigla
servico.Sigla = "REDE";
# salva modificação da propriedade Sigla
Servico.Salva(servico)
```
