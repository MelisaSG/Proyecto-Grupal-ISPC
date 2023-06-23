import mysql.connector

class Normativa:
    def __init__(self, nro_registro, tipo_normativa, nro_normativa, fecha, descripcion, categoria, jurisdiccion, organo_legislativo, palabras_clave):
        self.nro_registro = nro_registro
        self.tipo_normativa = tipo_normativa
        self.nro_normativa = nro_normativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.categoria = categoria
        self.jurisdiccion = jurisdiccion
        self.organo_legislativo = organo_legislativo
        self.palabras_clave = palabras_clave

    def __str__(self):
        return f"Número de Registro: {self.nro_registro}\n" \
            f"Tipo de Normativa: {self.tipo_normativa}\n" \
            f"Número de Normativa: {self.nro_normativa}\n" \
            f"Fecha: {self.fecha}\n" \
            f"Descripción: {self.descripcion}\n" \
            f"Categoría: {self.categoria}\n" \
            f"Jurisdicción: {self.jurisdiccion}\n" \
            f"Órgano Legislativo: {self.organo_legislativo}\n" \
            f"Palabras Clave: {self.palabras_clave}"

class GestorNormativas:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Normativas ("
            "NroRegistro INT PRIMARY KEY, "
            "TipoNormativa VARCHAR(250), "
            "NroNormativa VARCHAR(250), "
            "Fecha DATE, "
            "Descripcion VARCHAR(250), "
            "Categoria VARCHAR(250), "
            "Jurisdiccion VARCHAR(250), "
            "OrganoLegislativo VARCHAR(250), "
            "PalabrasClave VARCHAR(250)"
            ")"
        )

    def insertar_normativa(self, normativa):
        sql = "INSERT INTO Normativas (NroRegistro, TipoNormativa, NroNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            normativa.nro_registro, normativa.tipo_normativa, normativa.nro_normativa, normativa.fecha,
            normativa.descripcion, normativa.categoria, normativa.jurisdiccion, normativa.organo_legislativo,
            normativa.palabras_clave
        )
        self.cursor.execute(sql, values)
        self.connection.commit()
        print("Normativa insertada con éxito.")

    def seleccionar_normativa_por_numero(self, numero_normativa):
        sql = "SELECT * FROM Normativas WHERE NroNormativa = %s"
        value = (numero_normativa,)
        self.cursor.execute(sql, value)
        normativa = self.cursor.fetchone()
        if normativa:
            print(Normativa(*normativa))
        else:
            print("No se encontró la normativa.")

    def actualizar_descripcion_normativa(self, nro_registro, nueva_descripcion):
        sql = "UPDATE Normativas SET Descripcion = %s WHERE NroRegistro = %s"
        values = (nueva_descripcion, nro_registro)
        self.cursor.execute(sql, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Descripción de la normativa actualizada con éxito.")
        else:
            print("No se encontró la normativa.")

    def eliminar_normativa(self, nro_registro):
        sql = "DELETE FROM Normativas WHERE NroRegistro = %s"
        value = (nro_registro,)
        self.cursor.execute(sql, value)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Normativa eliminada con éxito.")
        else:
            print("No se encontró la normativa.")

    def buscar_normativas_por_palabra_clave(self, palabra_clave):
        sql = "SELECT * FROM Normativas WHERE PalabrasClave LIKE %s"
        value = ('%' + palabra_clave + '%',)
        self.cursor.execute(sql, value)
        normativas = self.cursor.fetchall()
        if normativas:
            for normativa in normativas:
                print(Normativa(*normativa))
        else:
            print("No se encontraron normativas con esa palabra clave.")

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("1. Insertar una nueva normativa")
    print("2. Seleccionar una normativa por número de normativa")
    print("3. Actualizar descripción de una normativa")
    print("4. Eliminar una normativa")
    print("5. Buscar normativas por palabra clave")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Ejemplo de uso del programa
gestor = GestorNormativas("localhost", "root", "Emiliano29782978", "normativasISPC")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        nro_registro = int(input("Ingrese el número de registro: "))
        tipo_normativa = input("Ingrese el tipo de normativa: ")
        nro_normativa = input("Ingrese el número de normativa: ")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        descripcion = input("Ingrese la descripción: ")
        categoria = input("Ingrese la categoría: ")
        jurisdiccion = input("Ingrese la jurisdicción: ")
        organo_legislativo = input("Ingrese el órgano legislativo: ")
        palabras_clave = input("Ingrese las palabras clave: ")
        normativa = Normativa(nro_registro, tipo_normativa, nro_normativa, fecha, descripcion,
        categoria, jurisdiccion, organo_legislativo, palabras_clave)
        gestor.insertar_normativa(normativa)

    elif opcion == "2":
        nro_normativa = input("Ingrese el número de normativa que desea seleccionar: ")
        gestor.seleccionar_normativa_por_numero(nro_normativa)

    elif opcion == "3":
        nro_registro = int(input("Ingrese el número de registro de la normativa que desea actualizar: "))
        nueva_descripcion = input("Ingrese la nueva descripción de la normativa: ")
        gestor.actualizar_descripcion_normativa(nro_registro, nueva_descripcion)

    elif opcion == "4":
        nro_registro = int(input("Ingrese el número de registro de la normativa que desea eliminar: "))
        gestor.eliminar_normativa(nro_registro)

    elif opcion == "5":
        palabra_clave = input("Ingrese la palabra clave: ")
        gestor.buscar_normativas_por_palabra_clave(palabra_clave)

    elif opcion == "6":
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

gestor.connection.close()
