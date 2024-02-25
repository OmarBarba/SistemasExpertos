import pyodbc

# Parámetros de conexión, reemplázalos con los tuyos
db_path = r'F:\Sistemas_expertos\obtener_conocimiento.accdb'
connection_str = f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path}"


try:
    # Intentar establecer la conexión
    connection = pyodbc.connect(connection_str)
    
    # Si la conexión tiene éxito, imprimir un mensaje de éxito
    print("¡Conexión exitosa a la base de datos!")
    
    # Cerrar la conexión
    connection.close()

except pyodbc.Error as e:
    # Si hay un error, imprimir el mensaje de error
    print(f"Error al conectar a la base de datos: {e}")