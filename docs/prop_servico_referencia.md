# Referencia

Caminho: Customização > Modelo de objetos > Processo > Servico > Referencia

Texto de Referência para utilização do Produto

**Exemplo 1: modificação da propriedade Referencia**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade Referencia
servico.Referencia = "Acesso a rede por conta";
# salva modificação da propriedade Referencia
Servico.Salva(servico)
```
