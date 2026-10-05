# Format

Caminho: Customização > Modelo de objetos > Utilitários > Picture > Format

Extensão do arquivo informando o formato da figura

**Exemplo 1: modificação da propriedade Format**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade Format
picture.Format = "Formato do arquivo";
# salva modificação da propriedade Format
Picture.Salva(picture)
```
