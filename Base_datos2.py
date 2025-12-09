import mysql.connector

# CONEXIÓN A LA BASE DE DATOS
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Turnero_Estrella"
    )


# REGISTRAR USUARIO
def registrar_usuario():
    print("\n--- REGISTRAR USUARIO ---")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    contraseña = input("Contraseña: ")
    telefono = input("Teléfono: ")
    seguro_medico = input("Seguro_medico: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
        INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, contraseña, telefono, email, seguro_medico)
        VALUES ('Carlos', 'Suarez',  '2001-09-05', '351867500', 'Carlos@gimail.com', 'Blue Cross');
    """
    datos = (nombre, apellido, fecha_nacimiento, contraseña, telefono, email, seguro_medico)

    cursor.execute(query, datos)
    conexion.commit()

    print("\nUsuario registrado con éxito.\n")

    cursor.close()
    conexion.close()


# INICIAR SESIÓN
# -------------------------------------
def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    email = input("Email: ")
    contraseña = input("contraseña: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT id, nombre, apellido FROM usuarios WHERE email = (email, ) AND contraseña = (contraseña, )"
    cursor.execute(query, (email, contraseña))
    resultado = cursor.fetchone()

    if resultado:
        print(f"\nBienvenido {resultado[1]} {resultado[2]} (ID: {resultado[0]})\n") #type: ignore
    else:
        print("\nDatos incorrectos.\n")

    cursor.close()
    conexion.close()

# -------------------------------------
# CONSULTAR USUARIO POR ID
# -------------------------------------
def consultar_usuario():
    print("\n--- CONSULTAR USUARIO ---")
    telefono = input("ingrese número de telefono: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, apellido FROM usuarios WHERE telefono = 351867500", (telefono,))
    resultado = cursor.fetchone()

    if resultado:
        print("\nDatos del usuario:")
        print(resultado)
    else:
        print("\nNo existe un usuario con ese número de telefono.")

    cursor.close()
    conexion.close()

# -------------------------------------
# MODIFICAR DATOS DEL USUARIO
# -------------------------------------
def modificar_doctores():
    print("\n--- MODIFICAR DATOS ---")
    especialidad= input("Ingrese su especialidad: ")

    consultorio= input("Nuevo número de consultorio: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
        UPDATE usuarios
        SET consultorio = 8
        WHERE especialidad  = 'Ortodoncia'
    """

    cursor.execute(query, (consultorio, especialidad))
    conexion.commit()

    print("\nDatos modificados correctamente.\n")

    cursor.close()
    conexion.close()

# -------------------------------------
# MODIFICAR FECHA DE NACIMIENTO
# -------------------------------------
def modificar_fecha_nacimiento():
    print("\n--- CAMBIAR FECHA DE NACIMIENTO ---")
    user_id = input("ID del usuario: ")
    nueva_fecha = input("Nueva fecha de nacimiento: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = "UPDATE usuarios SET fecha_nacimiento = %s WHERE id = %s"
    cursor.execute(query, (nueva_fecha, user_id))
    conexion.commit()

    print("\nFecha actualizada correctamente.\n")

    cursor.close()
    conexion.close()

# -------------------------------------
# ELIMINAR USUARIO
# -------------------------------------
def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    apellido = input("Ingrese apellido: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM usuarios WHERE apellido = Suarez", (apellido,))
    conexion.commit()

    print("\nUsuario eliminado correctamente.\n")

    cursor.close()
    conexion.close()

# -------------------------------------
# Menú principal
# -------------------------------------
def menu():
    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Consultar usuario")
        print("4. Modificar datos")
        print("5. Cambiar fecha de nacimiento")
        print("6. Eliminar usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            consultar_usuario()
        elif opcion == "4":
            modificar_usuario()
        elif opcion == "5":
            modificar_fecha_nacimiento()
        elif opcion == "6":
            eliminar_usuario()
        elif opcion == "7":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# -------------------------------------
# EJECUCIÓN
# -------------------------------------
if __name__ == "__main__":
    menu()