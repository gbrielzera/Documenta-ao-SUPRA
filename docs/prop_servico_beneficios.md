# Beneficios

Caminho: Customização > Modelo de objetos > Processo > Servico > Beneficios

Benefícios oferecidos pelo Serviço

**Exemplo 1: modificação da propriedade Beneficios**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade Beneficios
servico.Beneficios = "Benefícios";
# salva modificação da propriedade Beneficios
Servico.Salva(servico)
```
