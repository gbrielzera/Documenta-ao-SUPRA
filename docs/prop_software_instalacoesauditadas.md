# InstalacoesAuditadas

Caminho: Customização > Modelo de objetos > Ativos > Software > InstalacoesAuditadas

Instalações auditadas

**Exemplo 1: modificação da propriedade InstalacoesAuditadas**

```
# carrega objeto Software de identificador 1
software = Software.Carrega(1)
# modifica a propriedade InstalacoesAuditadas
software.InstalacoesAuditadas = 1;
# salva modificação da propriedade InstalacoesAuditadas
Software.Salva(software)
```
