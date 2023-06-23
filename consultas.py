

"""creacion de base de datos comanndos a traves de archivo pyton en visual + conexion"""

"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Emiliano29782978",
  database="normativasispc"
)

cursor = mydb.cursor()

# DROP DATABASE
cursor.execute("DROP DATABASE IF EXISTS normativasispc")

# CREATE DATABASE
cursor.execute("CREATE DATABASE normativasispc")
cursor.execute("USE normativasispc")

# CREATE TABLE tipos
cursor.execute("DROP TABLE IF EXISTS tipos")
cursor.execute("CREATE TABLE tipos (id_tipo INT NOT NULL, nombre VARCHAR(20) NOT NULL, PRIMARY KEY(id_tipo))")

# INSERT INTO tipos
tipos_data = [
    (1, "LEY"),
    (2, "DECRETO"),
    (3, "RESOLUCIÓN")
]
cursor.executemany("INSERT INTO tipos (id_tipo, nombre) VALUES (%s, %s)", tipos_data)

# SELECT FROM tipos
cursor.execute("SELECT * FROM tipos")
tipos_result = cursor.fetchall()
for row in tipos_result:
    print(row)

# CREATE TABLE categorias
cursor.execute("DROP TABLE IF EXISTS categorias")
cursor.execute("CREATE TABLE categorias (id_categoria INT NOT NULL, nombre VARCHAR(20) NOT NULL, PRIMARY KEY(id_categoria))")

# INSERT INTO categorias
categorias_data = [
    (1, "LABORAL"),
    (2, "PENAL"),
    (3, "CIVIL"),
    (4, "COMERCIAL"),
    (5, "FAMILIA Y SUCESIONES"),
    (6, "AGRARIO Y AMBIENTAL"),
    (7, "MINERO"),
    (8, "DERECHO INFORMATICO")
]
cursor.executemany("INSERT INTO categorias (id_categoria, nombre) VALUES (%s, %s)", categorias_data)

# SELECT FROM categorias
cursor.execute("SELECT * FROM categorias")
categorias_result = cursor.fetchall()
for row in categorias_result:
    print(row)

# CREATE TABLE jurisdicciones
cursor.execute("DROP TABLE IF EXISTS jurisdicciones")
cursor.execute("CREATE TABLE jurisdicciones (id_jurisdiccion INT NOT NULL, nombre VARCHAR(20) NOT NULL, organo_legislativo VARCHAR(50) NOT NULL, PRIMARY KEY(id_jurisdiccion))")

# INSERT INTO jurisdicciones
jurisdicciones_data = [
    (1, "NACIONAL", "CONGRESO NACIONAL"),
    (2, "PROVINCIAL", "LEGISLATURA PROVINCIAL")
]
cursor.executemany("INSERT INTO jurisdicciones (id_jurisdiccion, nombre, organo_legislativo) VALUES (%s, %s, %s)", jurisdicciones_data)

# SELECT FROM jurisdicciones
cursor.execute("SELECT * FROM jurisdicciones")
jurisdicciones_result = cursor.fetchall()
for row in jurisdicciones_result:
    print(row)

# CREATE TABLE leyes
cursor.execute("DROP TABLE IF EXISTS leyes")
cursor.execute("CREATE TABLE leyes (id_leyes INT NOT NULL, numero_registro VARCHAR(20) NOT NULL, nombre VARCHAR(50) NOT NULL, categoria INT, numero_normativa VARCHAR(50), fecha DATE, jurisdiccion INT, tipo_normativa INT, descripcion VARCHAR(200), palabra_clave VARCHAR(100), PRIMARY KEY(id_leyes))")

# INSERT INTO leyes
leyes_data = [
    (1, "1", "Ley de Contrato de Trabajo", 1, "20.744", "2021-01-01", 1, 1, "Contrato, Trabajo", "Contrato, Trabajo"),
    (2, "2", "Ley de Teletrabajo", 1, "27.555", "2022-02-01", 1, 1, "Teletrabajo", "Teletrabajo"),
    (3, "3", "Ley de Ejercicio Prof.de la Informática en Cba.", 8, "7642", "2023-03-01", 2, 1, "Informática, Ejercicio Profesional", "Informática, Ejercicio Profesional")
]
cursor.executemany("INSERT INTO leyes (id_leyes, numero_registro, nombre, categoria, numero_normativa, fecha, jurisdiccion, tipo_normativa, descripcion, palabra_clave) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", leyes_data)

# SELECT FROM leyes
cursor.execute("SELECT * FROM leyes")
leyes_result = cursor.fetchall()
for row in leyes_result:
    print(row)

mydb.commit()
cursor.close()
mydb.close()

"""
"""AQUI TERMINA LA CREACION DE LA BASE DE DATOS"""

import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Emiliano29782978",
            database="normativasispc"
        )
        self.cursor = self.mydb.cursor()

    def __del__(self):
        self.cursor.close()
        self.mydb.close()

    def insert_tipo(self, id_tipo, nombre):
        query = "INSERT INTO tipos (id_tipo, nombre) VALUES (%s, %s)"
        values = (id_tipo, nombre)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def select_tipos(self):
        query = "SELECT * FROM tipos"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_tipo_nombre(self, id_tipo, nuevo_nombre):
        query = "UPDATE tipos SET nombre = %s WHERE id_tipo = %s"
        values = (nuevo_nombre, id_tipo)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_tipo(self, id_tipo):
        query = "DELETE FROM tipos WHERE id_tipo = %s"
        values = (id_tipo,)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def insert_categoria(self, id_categoria, nombre):
        query = "INSERT INTO categorias (id_categoria, nombre) VALUES (%s, %s)"
        values = (id_categoria, nombre)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def select_categorias(self):
        query = "SELECT * FROM categorias"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_categoria_nombre(self, id_categoria, nuevo_nombre):
        query = "UPDATE categorias SET nombre = %s WHERE id_categoria = %s"
        values = (nuevo_nombre, id_categoria)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_categoria(self, id_categoria):
        query = "DELETE FROM categorias WHERE id_categoria = %s"
        values = (id_categoria,)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def insert_jurisdiccion(self, id_jurisdiccion, nombre, organo_legislativo):
        query = "INSERT INTO jurisdicciones (id_jurisdiccion, nombre, organo_legislativo) VALUES (%s, %s, %s)"
        values = (id_jurisdiccion, nombre, organo_legislativo)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def select_jurisdicciones(self):
        query = "SELECT * FROM jurisdicciones"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_jurisdiccion_nombre(self, id_jurisdiccion, nuevo_nombre):
        query = "UPDATE jurisdicciones SET nombre = %s WHERE id_jurisdiccion = %s"
        values = (nuevo_nombre, id_jurisdiccion)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_jurisdiccion_organo_legislativo(self, id_jurisdiccion, nuevo_organo_legislativo):
        query = "UPDATE jurisdicciones SET organo_legislativo = %s WHERE id_jurisdiccion = %s"
        values = (nuevo_organo_legislativo, id_jurisdiccion)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_jurisdiccion(self, id_jurisdiccion):
        query = "DELETE FROM jurisdicciones WHERE id_jurisdiccion = %s"
        values = (id_jurisdiccion,)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def insert_ley(self, numero_registro, nombre, categoria, numero_normativa, fecha, jurisdiccion, tipo_normativa, descripcion, palabra_clave):
        query = """
            INSERT INTO leyes (numero_registro, nombre, categoria, numero_normativa, fecha, jurisdiccion, tipo_normativa, descripcion, palabra_clave)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (numero_registro, nombre, categoria, numero_normativa, fecha, jurisdiccion, tipo_normativa, descripcion, palabra_clave)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def select_ley(self, id_ley):
        query = """
            SELECT l.id_leyes, l.numero_registro, l.nombre, c.nombre, l.numero_normativa,
                l.fecha, j.nombre, t.nombre, l.descripcion, l.palabra_clave
            FROM leyes l
            JOIN categorias c ON l.categoria = c.id_categoria
            JOIN jurisdicciones j ON l.jurisdiccion = j.id_jurisdiccion
            JOIN tipos t ON l.tipo_normativa = t.id_tipo
            WHERE l.id_leyes = %s
        """
        values = (id_ley,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def update_ley_numero_registro(self, id_ley, nuevo_numero_registro):
        query = "UPDATE leyes SET numero_registro = %s WHERE id_leyes = %s"
        values = (nuevo_numero_registro, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_ley_nombre(self, id_ley, nuevo_nombre):
        query = "UPDATE leyes SET nombre = %s WHERE id_leyes = %s"
        values = (nuevo_nombre, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_ley_categoria(self, id_ley, nueva_categoria):
        query = "UPDATE leyes SET categoria = %s WHERE id_leyes = %s"
        values = (nueva_categoria, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_ley_numero_normativa(self, id_ley, nuevo_numero_normativa):
        query = "UPDATE leyes SET numero_normativa = %s WHERE id_leyes = %s"
        values = (nuevo_numero_normativa, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_ley_fecha(self, id_ley, nueva_fecha):
        query = "UPDATE leyes SET fecha = %s WHERE id_leyes = %s"
        values = (nueva_fecha, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_ley_jurisdiccion(self, id_ley, nueva_jurisdiccion):
        query = "UPDATE leyes SET jurisdiccion = %s WHERE id_leyes = %s"
        values = (nueva_jurisdiccion, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_ley_tipo_normativa(self, id_ley, nuevo_tipo_normativa):
        query = "UPDATE leyes SET tipo_normativa = %s WHERE id_leyes = %s"
        values = (nuevo_tipo_normativa, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_ley_descripcion(self, id_ley, nueva_descripcion):
        query = "UPDATE leyes SET descripcion = %s WHERE id_leyes = %s"
        values = (nueva_descripcion, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def update_ley_palabra_clave(self, id_ley, nueva_palabra_clave):
        query = "UPDATE leyes SET palabra_clave = %s WHERE id_leyes = %s"
        values = (nueva_palabra_clave, id_ley)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_ley(self, id_ley):
        query = "DELETE FROM leyes WHERE id_leyes = %s"
        values = (id_ley,)
        self.cursor.execute(query, values)
        self.mydb.commit()

class Impresora:

    @staticmethod
    def print_tipos(tipos):
        print("---- Tipos ----")
        for tipo in tipos:
            print(f"ID: {tipo[0]}, Nombre: {tipo[1]}")
        print()

    @staticmethod
    def print_categorias(categorias):
        print("---- Categorias ----")
        for categoria in categorias:
            print(f"ID: {categoria[0]}, Nombre: {categoria[1]}")
        print()

    @staticmethod
    def print_jurisdicciones(jurisdicciones):
        print("---- Jurisdicciones ----")
        for jurisdiccion in jurisdicciones:
            print(f"ID: {jurisdiccion[0]}, Nombre: {jurisdiccion[1]}, Organo Legislativo: {jurisdiccion[2]}")
        print()

    @staticmethod
    def print_ley(ley):
        if ley:
            print("---- Ley ----")
            print(f"ID: {ley[0]}")
            print(f"Número de Registro: {ley[1]}")
            print(f"Nombre: {ley[2]}")
            print(f"Categoría: {ley[3]}")
            print(f"Número de Normativa: {ley[4]}")
            print(f"Fecha: {ley[5]}")
            print(f"Jurisdicción: {ley[6]}")
            print(f"Tipo de Normativa: {ley[7]}")
            print(f"Descripción: {ley[8]}")
            print(f"Palabra Clave: {ley[9]}")
            print()
        else:
            print("No se encontró la ley.")
            print()


def main_menu():
    print("=== Gestión de Normativas ===")
    print("1. Tipos")
    print("2. Categorías")
    print("3. Jurisdicciones")
    print("4. Leyes")
    print("5. Salir")

def tipos_menu():
    print("=== Tipos ===")
    print("1. Ver Tipos")
    print("2. Agregar Tipo")
    print("3. Actualizar Nombre de Tipo")
    print("4. Eliminar Tipo")
    print("5. Volver al Menú Principal")

def categorias_menu():
    print("=== Categorías ===")
    print("1. Ver Categorías")
    print("2. Agregar Categoría")
    print("3. Actualizar Nombre de Categoría")
    print("4. Eliminar Categoría")
    print("5. Volver al Menú Principal")

def jurisdicciones_menu():
    print("=== Jurisdicciones ===")
    print("1. Ver Jurisdicciones")
    print("2. Agregar Jurisdicción")
    print("3. Actualizar Nombre de Jurisdicción")
    print("4. Actualizar Órgano Legislativo de Jurisdicción")
    print("5. Eliminar Jurisdicción")
    print("6. Volver al Menú Principal")

def leyes_menu():
    print("=== Leyes ===")
    print("1. Ver Ley")
    print("2. Agregar Ley")
    print("3. Actualizar Número de Registro de Ley")
    print("4. Actualizar Nombre de Ley")
    print("5. Actualizar Categoría de Ley")
    print("6. Actualizar Número de Normativa de Ley")
    print("7. Actualizar Fecha de Ley")
    print("8. Actualizar Jurisdicción de Ley")
    print("9. Actualizar Tipo de Normativa de Ley")
    print("10. Actualizar Descripción de Ley")
    print("11. Actualizar Palabra Clave de Ley")
    print("12. Eliminar Ley")
    print("13. Volver al Menú Principal")

db = DatabaseManager()

while True:
    main_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            tipos_menu()
            opcion_tipos = input("Seleccione una opción: ")

            if opcion_tipos == "1":
                tipos = db.select_tipos()
                Impresora.print_tipos(tipos)
            elif opcion_tipos == "2":
                id_tipo = input("Ingrese el ID del Tipo: ")
                nombre_tipo = input("Ingrese el nombre del Tipo: ")
                db.insert_tipo(id_tipo, nombre_tipo)
                print("Tipo agregado exitosamente.")
            elif opcion_tipos == "3":
                id_tipo = input("Ingrese el ID del Tipo a actualizar: ")
                nuevo_nombre_tipo = input("Ingrese el nuevo nombre del Tipo: ")
                db.update_tipo_nombre(id_tipo, nuevo_nombre_tipo)
                print("Tipo actualizado exitosamente.")
            elif opcion_tipos == "4":
                id_tipo = input("Ingrese el ID del Tipo a eliminar: ")
                db.delete_tipo(id_tipo)
                print("Tipo eliminado exitosamente.")
            elif opcion_tipos == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    elif opcion == "2":
        while True:
            categorias_menu()
            opcion_categorias = input("Seleccione una opción: ")

            if opcion_categorias == "1":
                categorias = db.select_categorias()
                Impresora.print_categorias(categorias)
            elif opcion_categorias == "2":
                id_categoria = input("Ingrese el ID de la Categoría: ")
                nombre_categoria = input("Ingrese el nombre de la Categoría: ")
                db.insert_categoria(id_categoria, nombre_categoria)
                print("Categoría agregada exitosamente.")
            elif opcion_categorias == "3":
                id_categoria = input("Ingrese el ID de la Categoría a actualizar: ")
                nuevo_nombre_categoria = input("Ingrese el nuevo nombre de la Categoría: ")
                db.update_categoria_nombre(id_categoria, nuevo_nombre_categoria)
                print("Categoría actualizada exitosamente.")
            elif opcion_categorias == "4":
                id_categoria = input("Ingrese el ID de la Categoría a eliminar: ")
                db.delete_categoria(id_categoria)
                print("Categoría eliminada exitosamente.")
            elif opcion_categorias == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    elif opcion == "3":
        while True:
            jurisdicciones_menu()
            opcion_jurisdicciones = input("Seleccione una opción: ")

            if opcion_jurisdicciones == "1":
                jurisdicciones = db.select_jurisdicciones()
                Impresora.print_jurisdicciones(jurisdicciones)
            elif opcion_jurisdicciones == "2":
                id_jurisdiccion = input("Ingrese el ID de la Jurisdicción: ")
                nombre_jurisdiccion = input("Ingrese el nombre de la Jurisdicción: ")
                organo_legislativo_jurisdiccion = input("Ingrese el órgano legislativo de la Jurisdicción: ")
                db.insert_jurisdiccion(id_jurisdiccion, nombre_jurisdiccion, organo_legislativo_jurisdiccion)
                print("Jurisdicción agregada exitosamente.")
            elif opcion_jurisdicciones == "3":
                id_jurisdiccion = input("Ingrese el ID de la Jurisdicción a actualizar: ")
                nuevo_nombre_jurisdiccion = input("Ingrese el nuevo nombre de la Jurisdicción: ")
                db.update_jurisdiccion_nombre(id_jurisdiccion, nuevo_nombre_jurisdiccion)
                print("Jurisdicción actualizada exitosamente.")
            elif opcion_jurisdicciones == "4":
                id_jurisdiccion = input("Ingrese el ID de la Jurisdicción a actualizar: ")
                nuevo_organo_legislativo_jurisdiccion = input("Ingrese el nuevo órgano legislativo de la Jurisdicción: ")
                db.update_jurisdiccion_organo_legislativo(id_jurisdiccion, nuevo_organo_legislativo_jurisdiccion)
                print("Órgano legislativo de Jurisdicción actualizado exitosamente.")
            elif opcion_jurisdicciones == "5":
                id_jurisdiccion = input("Ingrese el ID de la Jurisdicción a eliminar: ")
                db.delete_jurisdiccion(id_jurisdiccion)
                print("Jurisdicción eliminada exitosamente.")
            elif opcion_jurisdicciones == "6":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    elif opcion == "4":
        while True:
            leyes_menu()
            opcion_leyes = input("Seleccione una opción: ")

            if opcion_leyes == "1":
                id_ley = input("Ingrese el ID de la Ley: ")
                ley = db.select_ley(id_ley)
                Impresora.print_ley(ley)
            elif opcion_leyes == "2":
                numero_registro = input("Ingrese el número de registro de la Ley: ")
                nombre_ley = input("Ingrese el nombre de la Ley: ")
                categoria_ley = input("Ingrese el ID de la Categoría de la Ley: ")
                numero_normativa = input("Ingrese el número de normativa de la Ley: ")
                fecha_ley = input("Ingrese la fecha de la Ley (YYYY-MM-DD): ")
                jurisdiccion_ley = input("Ingrese el ID de la Jurisdicción de la Ley: ")
                tipo_normativa = input("Ingrese el ID del Tipo de Normativa de la Ley: ")
                descripcion_ley = input("Ingrese la descripción de la Ley: ")
                palabra_clave = input("Ingrese la palabra clave de la Ley: ")
                db.insert_ley(numero_registro, nombre_ley, categoria_ley, numero_normativa, fecha_ley, jurisdiccion_ley, tipo_normativa, descripcion_ley, palabra_clave)
                print("Ley agregada exitosamente.")
            elif opcion_leyes == "3":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nuevo_numero_registro = input("Ingrese el nuevo número de registro de la Ley: ")
                db.update_ley_numero_registro(id_ley, nuevo_numero_registro)
                print("Número de registro de Ley actualizado exitosamente.")
            elif opcion_leyes == "4":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nuevo_nombre_ley = input("Ingrese el nuevo nombre de la Ley: ")
                db.update_ley_nombre(id_ley, nuevo_nombre_ley)
                print("Nombre de Ley actualizado exitosamente.")
            elif opcion_leyes == "5":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nueva_categoria_ley = input("Ingrese el nuevo ID de la Categoría de la Ley: ")
                db.update_ley_categoria(id_ley, nueva_categoria_ley)
                print("Categoría de Ley actualizada exitosamente.")
            elif opcion_leyes == "6":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nuevo_numero_normativa = input("Ingrese el nuevo número de normativa de la Ley: ")
                db.update_ley_numero_normativa(id_ley, nuevo_numero_normativa)
                print("Número de normativa de Ley actualizado exitosamente.")
            elif opcion_leyes == "7":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nueva_fecha_ley = input("Ingrese la nueva fecha de la Ley (YYYY-MM-DD): ")
                db.update_ley_fecha(id_ley, nueva_fecha_ley)
                print("Fecha de Ley actualizada exitosamente.")
            elif opcion_leyes == "8":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nueva_jurisdiccion_ley = input("Ingrese el nuevo ID de la Jurisdicción de la Ley: ")
                db.update_ley_jurisdiccion(id_ley, nueva_jurisdiccion_ley)
                print("Jurisdicción de Ley actualizada exitosamente.")
            elif opcion_leyes == "9":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nuevo_tipo_normativa = input("Ingrese el nuevo ID del Tipo de Normativa de la Ley: ")
                db.update_ley_tipo_normativa(id_ley, nuevo_tipo_normativa)
                print("Tipo de Normativa de Ley actualizado exitosamente.")
            elif opcion_leyes == "10":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nueva_descripcion_ley = input("Ingrese la nueva descripción de la Ley: ")
                db.update_ley_descripcion(id_ley, nueva_descripcion_ley)
                print("Descripción de Ley actualizada exitosamente.")
            elif opcion_leyes == "11":
                id_ley = input("Ingrese el ID de la Ley a actualizar: ")
                nueva_palabra_clave = input("Ingrese la nueva palabra clave de la Ley: ")
                db.update_ley_palabra_clave(id_ley, nueva_palabra_clave)
                print("Palabra clave de Ley actualizada exitosamente.")
            elif opcion_leyes == "12":
                id_ley = input("Ingrese el ID de la Ley a eliminar: ")
                db.delete_ley(id_ley)
                print("Ley eliminada exitosamente.")
            elif opcion_leyes == "13":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
