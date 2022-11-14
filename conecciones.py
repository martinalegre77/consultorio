# Base de Datos

import sqlite3

class Conexion():
    def __init__(self):
        self.db = 'consultorio.db'
        self.cursor = ''

    def consultar(self, sql,parametros=()):
        conn = sqlite3.connect(self.db) # Si la DB no existe la crea
        cursor = conn.cursor()
        try:
            resultado = cursor.execute(sql, parametros) # 'SELECT dni FROM perfil'
            conn.commit()
            return resultado
        except sqlite3.OperationalError:
            self.crear_db(cursor)
            resultado = cursor.execute(sql, parametros) 
            conn.commit()
            return resultado

    def crear_db(self, cursor):
        cursor.execute('CREATE TABLE perfil (dni INT PRIMARY KEY,\
                                                apellido TEXT NOT NULL,\
                                                nombre TEXT NOT NULL,\
                                                titulo TEXT,\
                                                abrev_titulo TEXT,\
                                                mat_nac INT,\
                                                mat_prov INT NOT NULL,\
                                                telefono INT,\
                                                mail TEXT)'\
                                                )
        cursor.execute('CREATE TABLE paciente (dni_pac INT PRIMARY KEY,\
                                                apellido_pac TEXT NOT NULL,\
                                                nombre_pac TEXT NOT NULL,\
                                                obra_social_pac TEXT,\
                                                telefono_pac INT,\
                                                mail_pac TEXT)'\
                                                )
        cursor.execute('CREATE TABLE obras_sociales (id_os INT PRIMARY KEY,\
                                                nombre_os TEXT NOT NULL,\
                                                nom_completo TEXT)'\
                                                )
        cursor.execute('CREATE TABLE consultorios (id_cons INT PRIMARY KEY,\
                                                nombre_cons TEXT,\
                                                direccion_cons TEXT,\
                                                telefono_cons INT)'\
                                                )
        cursor.execute('CREATE TABLE cobros (id_cobro INT PRIMARY KEY,\
                                                dni_pac INT NOT NULL,\
                                                nro_sesion INT,\
                                                monto INT,\
                                                fecha_cobro TEXT,\
                                                tipo TEXT)'\
                                                )
        cursor.execute('CREATE TABLE turnos (nro_turno INT PRIMARY KEY,\
                                                fecha_turno TEXT NOT NULL,\
                                                horario_turno TEXT NOT NULL,\
                                                apellido_pac TEXT NOT NULL,\
                                                telefono_pac INT NOT NULL,\
                                                mail_pac TEXT)'\
                                                )
        cursor.execute('CREATE TABLE sesiones (nro_sesion INT PRIMARY KEY,\
                                                dni_pac INT NOT NULL,\
                                                horario_sesion TEXT NOT NULL,\
                                                motivo TEXT,\
                                                tema_sesion TEXT,\
                                                evaluacion TEXT,\
                                                tratamiento TEXT,\
                                                otras_anot TEXT)'\
                                                )
               



         


    
# def conec():
#     try:
#         cursor = main.conexion()
#         cursor.execute('CREATE TABLE perfiles (id TEXT, dni INT, apellido TEXT,nombre TEXT, \
#             titulo TEXT, abrev_titulo TEXT, mat_nac INT, mat_prov INT, telefono INT, mail TEXT') 
#         # info_perfil = cursor.fetchall()
#         # if info_perfil[0] == '':
#             # pass
#         # else:
#             # pass
#     except sqlite3.OperationalError:
#         pass
#     #     messagebox.showerror(
#     #         title='ERROR INESPERADO',
#     #         message='Error al iniciar, intente nuevamente.'
#     #   )


