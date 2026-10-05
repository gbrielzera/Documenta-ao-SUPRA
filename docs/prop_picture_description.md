# Description

Caminho: Customização > Modelo de objetos > Utilitários > Picture > Description

Descrição detalhada sobre o conteúdo da imagem.

**Exemplo 1: modificação da propriedade Description**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade Description
picture.Description = "Descrição";
# salva modificação da propriedade Description
Picture.Salva(picture)
```
