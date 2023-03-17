f = open('mifichero.txt', 'w', encoding='utf-8')
list = [
    'Fichero de prueba del Ejercicio 8, Curso basico Python.\n'
    'Linea añadida de escritura utilizando el modo "w". \n'
    'Otra linea del fichero.\n'
]

f.writelines(list)

f.close()