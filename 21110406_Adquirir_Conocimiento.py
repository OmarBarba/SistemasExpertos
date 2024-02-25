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

def obtener_respuesta(pregunta):
    connection = pyodbc.connect(connection_str)
    cursor = connection.cursor()
    query = "SELECT Respuesta FROM Chat WHERE Pregunta = ?"
    resultado = cursor.execute(query, pregunta).fetchone()
    cursor.close()
    connection.close()
    return resultado[0] if resultado else None

# Función para almacenar nuevas preguntas y respuestas en la base de datos
def almacenar_conocimiento(pregunta, respuesta):
    connection = pyodbc.connect(connection_str)
    cursor = connection.cursor()
    query = "INSERT INTO Chat (Pregunta, Respuesta) VALUES (?, ?)"
    cursor.execute(query, pregunta, respuesta)
    connection.commit()
    cursor.close()
    connection.close()
    
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
        
        if respuesta:
            print(f"Chatbot: {respuesta}")
        else:
            print("Chatbot: No tengo una respuesta para eso. ¿Puedes enseñarme algo nuevo?")
            nuevo_conocimiento = input("Usuario (si/no): ").lower()
            
            if nuevo_conocimiento == 'si':
                respuesta_nueva = input("Usuario: (Ingresa la respuesta que debería tener): ")
                almacenar_conocimiento(input_usuario, respuesta_nueva)
                print("Chatbot: ¡Gracias por enseñarme algo nuevo!")

if __name__ == "__main__":
   chat()