import sqlite3

class Conexion():
    def __init__(self):
        self.db = 'consultorio.db'

    def consultar(self, sql, parametros=()):
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(sql, parametros) 
            conn.commit()
            return resultado

    def cerrar_conexion(self):
        Conexion.close()

    def consultar_pass(self):
        sql = 'SELECT dni FROM perfil'
        try:
            resultado = self.consultar(sql)
            return resultado
        except sqlite3.OperationalError:
            self.crear_db()
            resultado = self.consultar(sql)
            return resultado

    def guardar_perfil(self, dni, apellido, nombre, titulo, abreviatura,
                        matricula_nac, matricula_prov, telefono, mail):
        sql = 'INSERT INTO perfil VALUES(?,?,?,?,?,?,?,?,?)'
        parametros = (dni, apellido, nombre, titulo, abreviatura,
                    matricula_nac, matricula_prov, telefono, mail)
        self.consultar(sql, parametros)
        

    def crear_db(self):
        sql = 'CREATE TABLE perfil (dni INT PRIMARY KEY, apellido TEXT NOT NULL,\
                                    nombre TEXT NOT NULL, titulo TEXT,\
                                    abrev_titulo TEXT, mat_nac INT,\
                                    mat_prov INT NOT NULL, telefono INT, mail TEXT)'
        self.consultar(sql)
        sql = 'CREATE TABLE paciente (\
                dni_pac INTEGER NOT NULL,\
                apellido_pac TEXT NOT NULL,\
                nombre_pac	TEXT NOT NULL,\
                obra_social_pac	TEXT,\
                telefono_pac INT NOT NULL,\
                mail_pac TEXT,\
                PRIMARY KEY(dni_pac)\
                )'
        self.consultar(sql)                                         
        sql = 'CREATE TABLE obras_sociales (\
                id_os INTEGER NOT NULL,\
                nombre_os TEXT NOT NULL,\
                monto NUMERIC,\
                descripcion TEXT,\
                PRIMARY KEY(nombre_os)\
                )'
        self.consultar(sql)
        sql = 'CREATE TABLE consultorios (\
                id_cons INTEGER NOT NULL,\
                nombre_cons	TEXT NOT NULL,\
                direccion_cons TEXT NOT NULL,\
                telefono_cons INT,\
                PRIMARY KEY(id_cons AUTOINCREMENT)\
                )'
        self.consultar(sql)
        sql = 'CREATE TABLE cobros (\
                dni_pac TEXT NOT NULL,\
                monto NUMERIC NOT NULL,\
                fecha_cobro TEXT NOT NULL,\
                tipo TEXT,\
                PRIMARY KEY(dni_pac,fecha_cobro)\
                )'
        self.consultar(sql)
        sql = 'CREATE TABLE turnos (\
                nro_turno INTEGER NOT NULL,\
                    fecha_turno TEXT NOT NULL,\
                    horario_turno TEXT NOT NULL,\
                    apellido_pac TEXT NOT NULL,\
                    dni_pac INTEGER,\
                    nom_consultorio TEXT NOT NULL,\
                    PRIMARY KEY(nro_turno AUTOINCREMENT),\
                    FOREIGN KEY(dni_pac) REFERENCES paciente(dni_pac)\
                    )'
        self.consultar(sql)
        sql = 'CREATE TABLE sesiones (nro_sesion INT PRIMARY KEY, dni_pac INT NOT NULL,\
                            horario_sesion TEXT NOT NULL, motivo TEXT,\
                            tema_sesion TEXT, evaluacion TEXT,\
                            tratamiento TEXT, otras_anot TEXT)'
        self.consultar(sql)