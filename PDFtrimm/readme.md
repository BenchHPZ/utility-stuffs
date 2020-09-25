# PDF Trimm

Programa que _mágicamente_ 🧙‍♂️ trata de eliminar contenido reduntante de presentaciones pdf.

Este programa trata de trabajar con las presentaciones que se suelen usar en clases con animaciones. Estas animaciones ya no son relevantes cuando se trata de estudiar con estas diapositivas, además de que eliminarlas de una en una es perder tiempo en el se debería estar estudiando. (al igual que cuando programe esto 😅🙂😐😕😞😓)



## Como usarlo

Trate de programar dos maneras para usar este programa, mediante la termial y desde python.

### CLI

Para poder usar esta utilidad desde la terminal se deben seguir las siguientes reglas de uso:
```
Usage:
    PDFtrimm.py <file> [-o <o_file>] [--reverse]

Options:
    -h --help     Mostrar esta ayuda.
    -r --reverse  Orden para ciclar el archivo.
```

Donde `<file>` es el archivo de entrada y `<o_file>`  es el parametro opcional que indica el nombre del archivo de salida. La opción `--reverse` permite alterar el orden en el que se ciclaran las diapositivas; si no se pasa el archivo se ciclara del _final al inicio_.

### Python

Desde _python_ únicamente se necesita importar la función `trim_file` de `PDFtrimm`. Esta necesita dos parametros y tiene uno opcional
 - `i_name` El nombre de archivo de entrada
 - `o_name` El nombre del archivo de salida
 - `reverse` Parametro de orden del ciclo [opcional].
