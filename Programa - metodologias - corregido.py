import csv
import datetime
import time
import os
import pandas as pd
import sqlite3
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
app = QtWidgets.QApplication([])

#pantallas
confirmacion = uic.loadUi("pantallas_pia/confirmacion.ui")
consulta_clientes = uic.loadUi("pantallas_pia/consulta clientes.ui")
consulta = uic.loadUi("pantallas_pia/consulta.ui")
disponibles = uic.loadUi("pantallas_pia/disponibles.ui")
eliminacion = uic.loadUi("pantallas_pia/Eliminacion.ui") #PANTALLA PENDIENDE DE MODIFICAR
exito_e = uic.loadUi("pantallas_pia/exito_e.ui")
exito_r = uic.loadUi("pantallas_pia/exito_r.ui")
inicio = uic.loadUi("pantallas_pia/Inicio.ui")
registro_clientes = uic.loadUi("pantallas_pia/Registro clientes.ui")
reservacion = uic.loadUi("pantallas_pia/reservacion.ui")
#reporte (PANTALLA PENDIENTE)


fecha_actual = datetime.datetime.now()
rounded_actual = fecha_actual.replace(hour=0, minute=0, second=0, microsecond=0)

dict_por_fecha = dict() #para el csv que se usará para exportar el reporte a excel :(

# set_combs_posibles = set()
# set_combs_ocupadas = set()

# VARIABLES DEL CODIGO ORIGINAL
# claves_salas_disp = list()
# claves_turnos_disp = list()
# salas_disponibles = list()

# VARIABLES PARA PROGRAMA METODOLOGIAS
# claves_habitaciones_disp = list()
# habitaciones_disponibles = list()

# SETS PARA HACER LA RESTA Y OBTENER LAS DIFERENCIAS
set_nums_clientes = set()
set_claves_habitaciones = set()    # originalmente era set_claves_salas
# set_descrip_evento = set()

if os.path.exists("reservaciones.db"):
    inicio.label_19.setText("Se ha encontrado la base de datos en el directorio.")
else:
    inicio.label_19.setText("No se ha encontrado una base de datos previa, se procede a crearla.")
    try:
        with sqlite3.connect("reservaciones.db") as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS clientes (idClientes INTEGER PRIMARY KEY autoincrement, nombre TEXT NOT NULL, telefono INTEGER NOT NULL);")
            print('Tabla "clientes" creada')
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS habitacion (idHabitacion INTEGER PRIMARY KEY autoincrement, tipo_habitacion TEXT NOT NULL, piso INTEGER NOT NULL, precio INTEGER NOT NULL, estado TEXT NOT NULL);")
            print('Tabla "habitación" creada')
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS reservacion (idreservacion INTEGER PRIMARY KEY autoincrement, fecha_inicio DATE NOT NULL, fecha_fin DATE NOT NULL, Clientes_idClientes INT NOT NULL, Habitacion_idHabitacion INT NOT NULL, FOREIGN KEY(Clientes_idClientes) REFERENCES clientes(idClientes), FOREIGN KEY(Habitacion_idHabitacion) REFERENCES habitacion(idHabitacion));")
            print('Tabla "reservacion" creada')
            # 20 habitaciones "estandar"
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 1, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 1, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 1, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 1, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 1, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 1, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 2, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 2, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 2, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 2, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 2, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 2, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 3, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 3, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 3, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 3, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 3, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 3, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 4, 1500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('estandar', 4, 1500, 'D');")

            # 15 habitaciones "doble"
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 4, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 4, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 4, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 5, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 5, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 5, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 5, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 6, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 6, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 6, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 6, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 7, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 7, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 7, 2700, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('doble', 7, 2700, 'D');")

            # # 10 habitaciones "VIP"
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 8, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 8, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 8, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 8, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 9, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 9, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 9, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 9, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 10, 3500, 'D');")
            mi_cursor.execute("INSERT INTO habitacion(tipo_habitacion, piso, precio, estado) VALUES ('VIP', 10, 3500,'D' );")

            inicio.label_20.setText("Registros de habitaciones existentes ingresados.")
    except sqlite3.Error as e:
        print(e)
    except:
        inicio.label_20.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

#***********************************************************************************
# ********************* Funciones apertura y clausura de pantallas *****************
##**********************************************************************************

# REGISTRAR UNA RESERVACION *****(CHECK)*****
def registro_reservacion():
    # **** COMPRUEBA CLIENTES REGISTRADOS ****
    #COMPRUEBA CLIENTES REGISTRADOS
    numero_capturado = reservacion.lineEdit.text() #ID Cliente
    if (len(numero_capturado) == 0) :
        reservacion.label_3.setText("Por favor ingrese un ID")
    else:
        try:
            numero_capturado_int = int(numero_capturado)
            try:
                with sqlite3.connect("reservaciones.db") as conexion:  #comprobar que haya clientes registrados
                    mi_cursor = conexion.cursor()
                    mi_cursor.execute("SELECT idClientes FROM clientes;")
                    numeros_clientes = mi_cursor.fetchall()
                for elemento in numeros_clientes:
                    set_nums_clientes.add(elemento[0])  # set con los id's de los clientes
            except sqlite3.Error as e:
                print(e)
            except:
                #print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                reservacion.label_9.setText("Por favor ingrese un usuario valido")
        except:
            reservacion.label_3.setText("Por favor ingrese un dato valido (Dato numerico)")

    try:
        with sqlite3.connect("reservaciones.db") as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute("SELECT * FROM habitacion;")
            habitaciones_registradas = mi_cursor.fetchall() # originalmente era salas_registradas
            if len(habitaciones_registradas) == 0:
                reservacion.label_10.setText("No se encontraron habitaciones registradas, registra una habitación para reservarla")
            else:
                habitacion_deseada = reservacion.lineEdit_5.text()
                if len(habitacion_deseada) == 0:
                    reservacion.label_9.setText("Por favor ingresa una habitacion para continuar")
                else:
                    try:
                        habitacion_deseada_int = int(habitacion_deseada)# originalmente era sala_deseada
                    except:
                        reservacion.label_9.setText("Por favor ingresa dato numerico")
                    for elemento in habitaciones_registradas:
                        set_claves_habitaciones.add(elemento[0])    # set con los id's de cada habitación
                    if habitacion_deseada_int not in set_claves_habitaciones:
                        reservacion.label_9.setText("La clave de habitación no existe, ingresa una clave existente")
                #habitacion_deseada=int(input('\nIngrese la clave de la habitación que desea reservar: '))
    except sqlite3.Error as e:
        print(e)
    except:
        reservacion.label_9.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

    # fecha de inicio de la reservación
    fecha_inicio_capturada = reservacion.lineEdit_3.text()
    if (fecha_inicio_capturada == "" or str.isspace(fecha_inicio_capturada)):
        reservacion.label_8.setText("Se debe escribir una fecha para la reservación")
    else:
        try:
            fecha_inicio_procesada = datetime.datetime.strptime(fecha_inicio_capturada, "%d/%m/%Y").date()
            fecha_inicio_reservacion = datetime.datetime.combine(fecha_inicio_procesada, datetime.time(00, 00, 00)) # originalmente era fecha_evento
            delta = fecha_inicio_reservacion - rounded_actual
            if (delta.days < 2):
                reservacion.label_8.setText("La reservación tiene que ser, por lo menos, dos días antes de la fecha actual")
            else:
                fecha_fin_capturada = reservacion.lineEdit_4.text()
                if (fecha_fin_capturada == "" or str.isspace(fecha_fin_capturada)):
                    reservacion.label_10.setText("Se debe escribir una fecha final para la reservación")
                else:
                    try:
                        fecha_fin_procesada = datetime.datetime.strptime(fecha_fin_capturada, "%d/%m/%Y").date()
                        if fecha_fin_procesada <= fecha_inicio_procesada:
                            reservacion.label_10.setText("La fecha de fin no puede ser antes o el mismo dia a la fecha de inicio")
                        else:
                            with sqlite3.connect("reservaciones.db") as conn:
                                datos_reservacion = (str(fecha_inicio_procesada), habitacion_deseada) #originalmente era condiciones_sala, tupla para los datos a verificar si ya existen en la tabla reservacion
                                mi_cursor = conn.cursor()
                                mi_cursor.execute("SELECT * FROM reservacion WHERE fecha_inicio=:fecha_inicio AND Habitacion_idHabitacion=:habitacion_id", {"fecha_inicio": fecha_inicio_procesada, "habitacion_id": habitacion_deseada})
                                habitaciones_ocupadas = mi_cursor.fetchall()
                                if habitaciones_ocupadas:
                                    reservacion.label_10.setText("Ya existe una reservación para esa habitación, a esa fecha y en ese turno.")
                                else:
                                    if numero_capturado_int in set_nums_clientes:
                                        try:
                                            with sqlite3.connect("reservaciones.db") as conn:
                                                mi_cursor = conn.cursor()
                                                dict_reservacion = {"fecha_inicio": fecha_inicio_procesada, "fin": fecha_fin_procesada,"cliente": numero_capturado_int,"Habitacion": habitacion_deseada}
                                                mi_cursor.execute("INSERT INTO reservacion (fecha_inicio, fecha_fin, Clientes_idClientes, Habitacion_idHabitacion) VALUES(:fecha_inicio, :fin, :cliente, :Habitacion)", dict_reservacion)
                                                reservacion.hide()
                                                reservacion.label_3.setText("")
                                                reservacion.label_8.setText("")
                                                reservacion.label_10.setText("")
                                                reservacion.label_8.setText("")
                                                reservacion.lineEdit.setText("")
                                                reservacion.lineEdit_3.setText("")
                                                reservacion.lineEdit_4.setText("")
                                                reservacion.lineEdit_5.setText("")
                                                inicio.label_19.setText("Registro exitoso")
                                                inicio.label_20.setText(f"Reservación numero: {mi_cursor.lastrowid}, fecha de inicio: {fecha_inicio_procesada.strftime('%d/%m/%Y')}, fecha fin: {fecha_fin_procesada.strftime('%d/%m/%Y')}, cliente: {numero_capturado}, Habitación: {habitacion_deseada}")
                                                inicio.show()
                                        except sqlite3.Error as e:
                                            print (e)
                                        except:
                                            reservacion.label_9.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                                    else:
                                        reservacion.label_3.setText("Cliente no registrado, registrate para hacer una reservación")
                    except:
                        reservacion.label_10.setText("Formato de fecha invalido (DD/MM/AAAA)")
                            # fecha de fin de la reservación:
        except:
            reservacion.label_8.setText("Formato de fecha invalido (DD/MM/YYYY)")

# CONSULTAR HABITACIONES DISPONIBLES PARA UNA FECHA *****(CHECK)*****
def consulta_habitaciones():
    fecha_busqueda = disponibles.lineEdit.text()
    if (fecha_busqueda == "" or str.isspace(fecha_busqueda)):
        disponibles.label_7.setText("Por favor escribe una fecha para continuar (DD/MM/AAAA)")
    try:
        fecha_busq_proc = datetime.datetime.strptime(fecha_busqueda, "%d/%m/%Y").date()
        tupla_fecha_disp = (fecha_busq_proc,)
        try:
            with sqlite3.connect("reservaciones.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conexion:
                mi_cursor = conexion.cursor()
                mi_cursor.execute("SELECT * FROM habitacion WHERE idHabitacion NOT IN (SELECT Habitacion_idHabitacion FROM reservacion WHERE ? BETWEEN fecha_inicio AND fecha_fin);", tupla_fecha_disp)
                fetch_habitaciones_disp = mi_cursor.fetchall() #todas las fechas (de inicio y fin) de cada reservación
                if fetch_habitaciones_disp:
                    disponibles.tableWidget.setRowCount(0)
                    fila = 0
                    for fecha in fetch_habitaciones_disp:
                        disponibles.tableWidget.insertRow(fila)
                        columna = 0
                        for elemento in fecha:
                            celda = QTableWidgetItem(str(elemento))
                            disponibles.tableWidget.setItem(fila,columna, celda)
                            columna += 1
                        fila += 1
                else:
                    disponibles.label_8.setText("No se encontraron habitaciones disponibles en esa fecha.")
        except sqlite3.Error as e:
            print(e)
        except:
            disponibles.label_8.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    except:
        disponibles.label_7.setText("Formato de fecha invalido (DD/MM/YYYY)")

# Consulta de reservaciones para una fecha especifica ******** [CHECK] ********

def consulta_reservaciones():
    fecha_consulta = consulta.lineEdit.text()
    if (fecha_consulta == "" or str.isspace(fecha_consulta)):
        consulta.label_5.setText("Por favor ingrese una fecha para continuar")
    else:
        try:
            fecha_proc_consulta = datetime.datetime.strptime(fecha_consulta, "%d/%m/%Y").date() # checar formato de fecha
            try:
                tupla_fecha_consulta = (fecha_proc_consulta,)
                consulta.tableWidget.clearContents()  # Elimina el contenido de las celdas
                while consulta.tableWidget.rowCount() > 0:
                    consulta.tableWidget.removeRow(0)
                with sqlite3.connect("reservaciones.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conexion:
                    mi_cursor = conexion.cursor()
                    mi_cursor.execute("SELECT idreservacion, fecha_inicio, fecha_fin, Clientes_idClientes, Habitacion_idHabitacion FROM reservacion WHERE ? BETWEEN fecha_inicio AND fecha_fin;", tupla_fecha_consulta)  # CAMBIÉ: estaba agregada la tupla pero faltaba el WHERE
                    reservaciones_en_fecha = mi_cursor.fetchall()
                    if reservaciones_en_fecha:
                        consulta.tableWidget.setRowCount(0)
                        fila = 0
                        for reservacion in reservaciones_en_fecha:
                            consulta.tableWidget.insertRow(fila)
                            columna = 0
                            for elemento in reservacion:
                                celda = QTableWidgetItem(str(elemento))
                                consulta.tableWidget.setItem(fila,columna, celda)
                                columna += 1
                            fila += 1
                    else:
                        consulta.label_5.setText("No se encontraron reservaciones registradas para esa fecha.")
            except sqlite3.Error as e:
                consulta.label_5.setText(e)
            except:
                consulta.label_5.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        except:
            consulta.label_5.setText("Formato de fecha incorrecto (DD/MM/AAAA)")

# CREAR REPORTE EN EXCEL ******* [CHECK] *******

def reporte_excel():
    fecha_consultar_reservacion = consulta.lineEdit.text()
    if (fecha_consultar_reservacion == "" or str.isspace(fecha_consultar_reservacion)):
        consulta.label_6.setText("Por favor ingrese una fecha (DD/MM/AAAA)")
    else:
        try:
            fecha_procesada_consul = datetime.datetime.strptime(fecha_consultar_reservacion, "%d/%m/%Y").date()
            tupla_fecha_exportar = (fecha_procesada_consul,)
            try:
                with sqlite3.connect("reservaciones.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conexion:
                    mi_cursor = conexion.cursor()
                    mi_cursor.execute("SELECT idreservacion, fecha_inicio, fecha_fin, Clientes_idClientes, Habitacion_idHabitacion FROM reservacion WHERE ? BETWEEN fecha_inicio AND fecha_fin", tupla_fecha_exportar)  #CAMBIÉ: faltaba el WHERE
                    reservacion_a_exportar = mi_cursor.fetchall()
                    if reservacion_a_exportar:
                        for id, fecha_inicio, fecha_fin, cliente, habitacion in reservacion_a_exportar: # CAMBIÉ: los datos enlistados estaban en un orden distinto al original escrito en el SELECT (los datos se hubieran guardado desordenados)
                            dict_por_fecha[id] = [fecha_inicio, fecha_fin, cliente, habitacion]
                        with open("reservaciones.csv","w", newline="") as archivo_reserv:
                            grabador = csv.writer(archivo_reserv)
                            grabador.writerow(("Clave de reservacion", "Fecha de inicio", "Fecha de fin", "Cliente", "Habitacion"))
                            grabador.writerows([(id_columna, datos[0], datos[1], datos[2], datos[3]) for id_columna, datos in dict_por_fecha.items()])
                        df_reserv_fecha = pd.read_csv('reservaciones.csv')
                        excel_reserv = pd.ExcelWriter('reservaciones.xlsx')
                        df_reserv_fecha.to_excel(excel_reserv, index=False)
                        excel_reserv.save()     # si crea el archivo pero aparece el mensaje "save is not part of the public API, usage can give in unexpected results and will be removed in a future version"
                        consulta.label_6.setText("Se ha creado el archivo excel.")
                    else:
                        consulta.label_6.setText("No se encontraron reservaciones registradas para esa fecha.")
            except sqlite3.Error as e:
                consulta.label_6.setText(e)
            except:
                consulta.label_6.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        except:
            consulta.label_5.setText("Formato de fecha incorrecto (DD/MM/AAAA)")

def eliminar_buscar():
    try:
        clave_eliminar = eliminacion.lineEdit.text()
        clave_eliminar_int = int(clave_eliminar)
        try:
            tupla_numero_reservacion = (clave_eliminar_int,)
            with sqlite3.connect("reservaciones.db") as conexion:
                mi_cursor = conexion.cursor()
                mi_cursor.execute("SELECT * FROM reservacion WHERE idreservacion = ? ",tupla_numero_reservacion)
                reserv_registrados = mi_cursor.fetchall()   # originalmente era eventos_registrados
                if reserv_registrados:
                    eliminacion.tableWidget.setRowCount(0)
                    fila = 0
                    for fecha in reserv_registrados:
                        eliminacion.tableWidget.insertRow(fila)
                        columna = 0
                        for elemento in fecha:
                            celda = QTableWidgetItem(str(elemento))
                            eliminacion.tableWidget.setItem(fila,columna, celda)
                            columna += 1
                        fila += 1
                else:
                    eliminacion.label_4.setText("No se encontraron reservaciones registradas.")
        except sqlite3.Error as e:
            eliminacion.label_4.setText(e)
        except:
            eliminacion.label_4.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    except:
        eliminacion.label_4.setText("ingrese un caracter valido")

# ELIMINAR UNA RESERVACION
def eliminar_reservacion():
    try:
        clave_eliminar = eliminacion.lineEdit.text()
        clave_eliminar_int = int(clave_eliminar)
        try:
            with sqlite3.connect("reservaciones.db") as conexion:
                mi_cursor = conexion.cursor()
                tupla_clave_eliminar = (clave_eliminar_int,)
                mi_cursor.execute("SELECT fecha_inicio FROM reservacion WHERE idreservacion = ?", tupla_clave_eliminar)
                reserv_con_clave = mi_cursor.fetchall()
                if reserv_con_clave:
                    for fecha in reserv_con_clave:
                        for elemento in fecha:
                            elemento_str = str(elemento)
                            fecha_reserv_eliminar = datetime.datetime.strptime(elemento_str, "%Y-%m-%d").date()
                            fecha_proc_eliminar = datetime.datetime.combine(fecha_reserv_eliminar, datetime.time(00, 00, 00))
                            delta_eliminar = fecha_proc_eliminar - rounded_actual
                            if (delta_eliminar.days < 3):
                                eliminacion.label_4.setText("Solo se pueden eliminar reservaciones con, por lo menos, tres días de anticipación.")
                            else:
                                eliminacion.hide()
                                confirmacion.show()
                else:
                    eliminacion.label_4.setText("No se encontró una reservación con esa clave.")
        except sqlite3.Error as e:
            eliminacion.label_4.setText(e)
        except:
            eliminacion.label_4.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    except:
        eliminacion.label_4.setText("ingrese un caracter valido")

def confirmar_eliminacion_si():
    clave_eliminar = eliminacion.lineEdit.text()
    clave_eliminar_int = int(clave_eliminar)
    tupla_clave_eliminar = (clave_eliminar_int,)
    try:
        with sqlite3.connect("reservaciones.db") as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute("DELETE FROM reservacion WHERE idreservacion = ?", tupla_clave_eliminar)
            confirmacion.hide()
            eliminacion.lineEdit.setText("")
            exito_r.show()
    except sqlite3.Error as e:
        eliminacion.label_4.setText(e)
    except:
        eliminacion.label_4.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

def confirmar_eliminacion_no():
    confirmacion.hide()
    eliminacion.label_4.setText("Eliminacion cancelada")
    eliminacion.show()

def exito_regresar_eliminacion():
    exito_r.hide()
    eliminacion.show()
    eliminacion.label_4.setText("")
    try:
        with sqlite3.connect("reservaciones.db") as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute("SELECT * FROM reservacion")
            reserv_registrados = mi_cursor.fetchall()   # originalmente era eventos_registrados
            if reserv_registrados:
                eliminacion.tableWidget.setRowCount(0)
                fila = 0
                for fecha in reserv_registrados:
                    eliminacion.tableWidget.insertRow(fila)
                    columna = 0
                    for elemento in fecha:
                        celda = QTableWidgetItem(str(elemento))
                        eliminacion.tableWidget.setItem(fila,columna, celda)
                        columna += 1
                    fila += 1
            else:
                eliminacion.label_4.setText("No se encontraron reservaciones registradas.")
    except sqlite3.Error as e:
        eliminacion.label_4.setText(e)
    except:
        eliminacion.label_4.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    eliminacion.show()

# REGISTRO DE CLIENTE *****(CHECK)*****

def registro_cliente():
    nombre_cliente = registro_clientes.lineEdit.text()
    try:
        telefono_cliente = registro_clientes.lineEdit_2.text()
        telefono_cliente_int = int(telefono_cliente)
    except:
        registro_clientes.label_7.setText("Numero de telefono no valido")
    if nombre_cliente == "" or nombre_cliente.isspace() == True:
        registro_clientes.label_7.setText("") #Para desaparecer un antiguo mensaje de error
        registro_clientes.label_5.setText("Debe escribirse un nombre de cliente para el registro")
    elif telefono_cliente == "" or telefono_cliente.isspace() == True:
        registro_clientes.label_5.setText("") #Para desaparecer un antiguo mensaje de error
        registro_clientes.label_7.setText("Debe escribir un numero telefonico para su registro")
    else:
        try:
            with sqlite3.connect("reservaciones.db") as conexion:
                mi_cursor = conexion.cursor()
                tupla_datos_cliente =(nombre_cliente, telefono_cliente_int)
                mi_cursor.execute("INSERT INTO clientes (nombre,telefono) VALUES(?, ?);", tupla_datos_cliente)
                registro_clientes.label_5.setText("")
                registro_clientes.label_7.setText("")
                registro_clientes.lineEdit.setText("")
                registro_clientes.lineEdit_2.setText("")
                registro_clientes.hide()
                inicio.show()
                inicio.label_19.setText("Registro de cliente exitoso")
                inicio.label_20.setText(f"El número de cliente para {nombre_cliente} es {mi_cursor.lastrowid}")
        except sqlite3.Error as e:
            registro_clientes.label_8.setText(e)
            print(e)
        except:
            registro_clientes.label_8.setText("Ingrese los datos correctamente")
            #print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

#CONSULTA DE CLIENTES (CON ID) *****(CHECK)*****

def consulta_clientes_id():
    id_cliente = consulta_clientes.lineEdit.text()
    if id_cliente.isspace():
        consulta_clientes.label_4.setText("Porfavor ingrese un ID")
    try:
        id_cliente_int = int(id_cliente)
    except:
        consulta_clientes.label_4.setText("ID no valido")
    tupla_idcliente = (id_cliente_int,)
    try:
        with sqlite3.connect("reservaciones.db") as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute(f"SELECT idClientes, nombre, telefono FROM clientes WHERE idClientes = ?;", tupla_idcliente)
            registros= mi_cursor.fetchall()
            consulta_clientes.tableWidget.setRowCount(0)
            fila = 0
        for registro in registros:
            consulta_clientes.tableWidget.insertRow(fila)
            columna = 0
            for elemento in registro:
                celda = QTableWidgetItem(str(elemento))
                consulta_clientes.tableWidget.setItem(fila,columna, celda)
                columna += 1
            fila += 1
    except:
        consulta_clientes.label_4.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

#Inmediatamente entrando al programa, se muestran todos los clientes
def ver_clientes():
    try:
        with sqlite3.connect("reservaciones.db") as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute("SELECT idClientes, nombre, telefono FROM clientes")
            registros= mi_cursor.fetchall()
            consulta_clientes.tableWidget.setRowCount(0)
            fila = 0
        for registro in registros:
            consulta_clientes.tableWidget.insertRow(fila)
            columna = 0
            for elemento in registro:
                celda = QTableWidgetItem(str(elemento))
                consulta_clientes.tableWidget.setItem(fila,columna, celda)
                columna += 1
            fila += 1
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

#De INICIO a REGISTRO

def inicio_registrar():
    inicio.hide()
    inicio.label_19.setText("")
    inicio.label_20.setText("")
    reservacion.show()

#De REGISTRO a INICIO (AL REVES)
def registrar_inicio():
    reservacion.hide()
    inicio.show()

#De INICIO a Habitaciones disponibles
def inicio_disponibles():
    inicio.hide()
    try:
        with sqlite3.connect("reservaciones.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute("SELECT * FROM habitacion;")
            fetch_habitaciones_disp = mi_cursor.fetchall() #todas las fechas (de inicio y fin) de cada reservación
            if fetch_habitaciones_disp:
                disponibles.tableWidget.setRowCount(0)
                fila = 0
                for fecha in fetch_habitaciones_disp:
                    disponibles.tableWidget.insertRow(fila)
                    columna = 0
                    for elemento in fecha:
                        celda = QTableWidgetItem(str(elemento))
                        disponibles.tableWidget.setItem(fila,columna, celda)
                        columna += 1
                    fila += 1
            else:
                disponibles.label_7.setText("No se encontraron habitaciones disponibles en esa fecha.")
    except sqlite3.Error as e:
        disponibles.label_7.setText(e)
    except:
        disponibles.label_7.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    disponibles.show()

#De Habitaciones disponibles a INICIO (AL REVES)
def disponibles_inicio():
    disponibles.hide()
    inicio.show()

#De INICIO a Consultar reservaciones
def inicio_consulta():
    inicio.hide()
    inicio.label_19.setText("")
    inicio.label_20.setText("")
    try:
        with sqlite3.connect("reservaciones.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute("SELECT * FROM reservacion;")
            fetch_habitaciones_disp = mi_cursor.fetchall() #todas las fechas (de inicio y fin) de cada reservación
            if fetch_habitaciones_disp:
                consulta.tableWidget.setRowCount(0)
                fila = 0
                for fecha in fetch_habitaciones_disp:
                    consulta.tableWidget.insertRow(fila)
                    columna = 0
                    for elemento in fecha:
                        celda = QTableWidgetItem(str(elemento))
                        consulta.tableWidget.setItem(fila,columna, celda)
                        columna += 1
                    fila += 1
            else:
                consulta.label_5.setText("No se encontraron habitaciones disponibles en esa fecha.")
    except sqlite3.Error as e:
        consulta.label_5.setText(e)
    except:
        consulta.label_5.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    consulta.show()

#De Consultar reservaciones a INICIO (AL REVES)
def consulta_inicio():
    consulta.hide()
    consulta.tableWidget.clearContents()  # Elimina el contenido de las celdas
    while consulta.tableWidget.rowCount() > 0:
        consulta.tableWidget.removeRow(0)
    consulta.label_5.setText("")
    consulta.lineEdit.setText("")
    inicio.show()

#De INICIO a ELIMINAR
def inicio_eliminar():
    inicio.hide()
    inicio.label_19.setText("")
    inicio.label_20.setText("")
    try:
        with sqlite3.connect("reservaciones.db") as conexion:
            mi_cursor = conexion.cursor()
            mi_cursor.execute("SELECT * FROM reservacion")
            reserv_registrados = mi_cursor.fetchall()   # originalmente era eventos_registrados
            if reserv_registrados:
                eliminacion.tableWidget.setRowCount(0)
                fila = 0
                for fecha in reserv_registrados:
                    eliminacion.tableWidget.insertRow(fila)
                    columna = 0
                    for elemento in fecha:
                        celda = QTableWidgetItem(str(elemento))
                        eliminacion.tableWidget.setItem(fila,columna, celda)
                        columna += 1
                    fila += 1
            else:
                eliminacion.label_4.setText("No se encontraron reservaciones registradas.")
    except sqlite3.Error as e:
        eliminacion.label_4.setText(e)
    except:
        eliminacion.label_4.setText(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    eliminacion.show()

#De ELIMINAR a INICIO (AL REVES)
def eliminar_inicio():
    eliminacion.hide()
    inicio.show()

#De INICIO a REGISTRAR CLIENTE
def inicio_registro_cliente():
    inicio.hide()
    inicio.label_19.setText("")
    inicio.label_20.setText("")
    ver_clientes()
    registro_clientes.show()

#De REGISTRAR CLIENTE a INICIO (AL REVES)
def registro_cliente_inicio():
    registro_clientes.hide()
    inicio.show()

#De INICIO a CONSULTAR CLIENTE
def inicio_consulta_clientes():
    inicio.hide()
    inicio.label_19.setText("")
    inicio.label_20.setText("")
    ver_clientes()
    consulta_clientes.show()

#De INICIO a CONSULTAR CLIENTE
def consulta_clientes_inicio():
    consulta_clientes.hide()
    inicio.show()

#De REGISTRO DE CLIENTE a CONSULTA DE CLIENTES
def registro_clientes_consulta_clientes():
    registro_clientes.hide()
    consulta_clientes.show()
    ver_clientes()

#De CONSULTA DE CLIENTES a REGISTRO DE CLIENTE
def consulta_clientes_registro_clientes():
    consulta_clientes.hide()
    registro_clientes.show()

#Cerrar app
def salir_app():
    inicio.hide()
    inicio.label_19.setText("")
    inicio.label_20.setText("")
    app.exit()

# ************ Botones pantallas ************
#Inicio
inicio.registrar.clicked.connect(inicio_registrar)
inicio.disponibles.clicked.connect(inicio_disponibles)
inicio.consultar.clicked.connect(inicio_consulta)
inicio.eliminar.clicked.connect(inicio_eliminar)
inicio.registro_cliente.clicked.connect(inicio_registro_cliente)
inicio.consulta_cliente.clicked.connect(inicio_consulta_clientes)
inicio.salir.clicked.connect(salir_app)

# ***** Registrar reservacion *****
#registrar
reservacion.registrar.clicked.connect(registro_reservacion)
#regresar al menu
reservacion.regresar.clicked.connect(registrar_inicio)

# ***** Habitaciones disponibles *****

disponibles.regresar.clicked.connect(disponibles_inicio)

disponibles.consultar.clicked.connect(consulta_habitaciones)

# ***** Consultar reservaciones *****

consulta.volver.clicked.connect(consulta_inicio)

consulta.consultar.clicked.connect(consulta_reservaciones)

consulta.reporte_excel.clicked.connect(reporte_excel)

# ***** Eliminar reservacion *****

eliminacion.regresar.clicked.connect(eliminar_inicio) #MODIFICAR EL NOMBRE DE ESTE BOTON EN LA PANTALLA AL CAMBIARSE

eliminacion.eliminar.clicked.connect(eliminar_reservacion)

eliminacion.buscar.clicked.connect(eliminar_buscar)

# ***** Registrar cliente *****

registro_clientes.volver.clicked.connect(registro_cliente_inicio)
#Ver clientes registrados (CAMBIO DE PANTALLA)
registro_clientes.ver_clientes_registrados.clicked.connect(registro_clientes_consulta_clientes)
#Boton registrar cliente
registro_clientes.registrar.clicked.connect(registro_cliente)

# ***** Consultar cliente *****

#Ir a la pantalla de registro de cliente
consulta_clientes.registrar_cliente.clicked.connect(consulta_clientes_registro_clientes)
#Consultar cliente
consulta_clientes.consultar_cliente.clicked.connect(consulta_clientes_id)
#Mostrar clientes completos de nuevo o actualizar la lista
consulta_clientes.clientes_completos.clicked.connect(ver_clientes)

#Regresar al menu
consulta_clientes.menu_principal.clicked.connect(consulta_clientes_inicio)

# ***** Pantalla confirmacion *****
confirmacion.si.clicked.connect(confirmar_eliminacion_si)
confirmacion.no.clicked.connect(confirmar_eliminacion_no)

# *********** Pantalla exito_r ***********

exito_r.volver.clicked.connect(exito_regresar_eliminacion)

#Ejecutable del inicio de programa
inicio.show()
app.exec()