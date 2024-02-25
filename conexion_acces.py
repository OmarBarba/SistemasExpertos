import pyodbc

# Parámetros de conexión, reemplázalos con los tuyos
db_path = r'F:\Sistemas_expertos\obtener_conocimiento.accdb'
connection_str = f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path}"

# Establecer la conexión
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# Ejemplo de inserción de datos
nombre = 'Ejemplo'
edad = 25
email = 'ejemplo@email.com'

# Query para insertar datos en una tabla ficticia, ajusta según tu base de datos
query = f"INSERT INTO Pruebas (Nombre, Edad, Email) VALUES (?, ?, ?)"
cursor.execute(query, nombre, edad, email)

# Confirmar la transacción
connection.commit()

# Cerrar la conexión
cursor.close()
connection.close()
