import sqlite3

#conecto a la base de datos
conn = sqlite3.connect('mi_db.db')

#creo la tabla
conn.execute('''CREATE TABLE IF NOT EXISTS estudiantes (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL);''')

#insertar datos
conn.execute("INSERT INTO  estudiantes (nombre, apellido) VALUES(?, ?)", ('Jhonathan', 'Rivera'))
conn.execute("INSERT INTO  estudiantes (nombre, apellido) VALUES(?, ?)", ('Juan', 'Perez'))
conn.execute("INSERT INTO  estudiantes (nombre, apellido) VALUES(?, ?)", ('Ana', 'Aguirre'))
conn.execute("INSERT INTO  estudiantes (nombre, apellido) VALUES(?, ?)", ('Lalo', 'Landa'))
conn.execute("INSERT INTO  estudiantes (nombre, apellido) VALUES(?, ?)", ('Oreo', 'Rivera'))
conn.execute("INSERT INTO  estudiantes (nombre, apellido) VALUES(?, ?)", ('Brenda', 'Valencia'))
conn.execute("INSERT INTO  estudiantes (nombre, apellido) VALUES(?, ?)", ('Alejandro', 'Fernandez'))
conn.execute("INSERT INTO  estudiantes (nombre, apellido) VALUES(?, ?)", ('Diego', 'Messi'))

#guardar cambios
conn.commit

#cursor para la base de datos
cursor = conn.cursor()

#ejecuto consulta
nombre_estudiante = 'Diego'
cursor.execute('SELECT * FROM estudiantes WHERE nombre = ?', (nombre_estudiante,))

#obtener registro
nombre_encontrado = cursor.fetchone()

#imprimir por consola
if nombre_encontrado:
    print(nombre_encontrado)
else:
    print(f"No existe el registro con el nombre '{nombre_estudiante}'.")

#cerrar conexion
conn.close
