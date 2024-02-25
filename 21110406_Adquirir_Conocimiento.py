import pyodbc

# Parámetros de conexión, reemplázalos con los tuyos
db_path = r'F:\Sistemas_expertos\obtener_conocimiento.accdb'
connection_str = f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path}"

def conexion():

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


def chat():
    print("Hola soy un chatbot que se dedica a obtener informacion y de igual forma a corroborar si ya tengo esa informacion")
    print("Preguntame lo que sea con confianza: ")
    
    #Se asifgna la forma en la que se accede y se manda la pregunta a la base de datos
    while True:
        input_usuario = input("Usuario: ")
        #se crea la forma para poder salir del chatbot
        if input_usuario.lower() == 'salir':
            print("Hasta luego. ¡Vuelve pronto!")
            break
        #se manda la pregunta a la clase que se dedica a eso.
        respuesta = obtener_respuesta(input_usuario)

if __name__ == "__main__":
   chat()