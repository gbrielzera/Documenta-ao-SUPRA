# Temporality

Caminho: Customização > Modelo de objetos > Utilitários > Picture > Temporality

Prazo em dias para manutenção da figura no banco de dados. Este prazo tem como referência o último acesso a figura.

**Exemplo 1: modificação da propriedade Temporality**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade Temporality
picture.Temporality = 1;
# salva modificação da propriedade Temporality
Picture.Salva(picture)
```
