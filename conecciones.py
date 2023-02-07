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

    # def cerrar_conexion(self):
    #     Conexion.close()

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
        sql = 'CREATE TABLE perfil (dni INTEGER PRIMARY KEY,\
                                    apellido TEXT NOT NULL,\
                                    nombre TEXT NOT NULL,\
                                    titulo TEXT,\
                                    abrev_titulo TEXT,\
                                    mat_nac INTEGER,\
                                    mat_prov INTEGER NOT NULL,\
                                    telefono INTEGER,\
                                    mail TEXT\
                                    )'
        self.consultar(sql)
        sql = 'CREATE TABLE paciente (\
                dni_pac INTEGER NOT NULL,\
                apellido_pac TEXT NOT NULL,\
                nombre_pac	TEXT NOT NULL,\
                obra_social_pac	INTEGER NOT NULL,\
                telefono_pac INTEGER NOT NULL,\
                mail_pac TEXT,\
                PRIMARY KEY(dni_pac),\
                FOREIGN KEY(obra_social_pac) REFERENCES obra_social(id_os)\
                )'
        self.consultar(sql)                                         
        sql = 'CREATE TABLE obra_social (\
                id_os INTEGER NOT NULL,\
                nombre_os TEXT NOT NULL,\
                monto_cob_os INTEGER NOT NULL,\
                descripcion TEXT,\
                PRIMARY KEY(id_os AUTOINCREMENT)\
                )'
        self.consultar(sql)
        sql = 'CREATE TABLE consultorio (\
                id_cons INTEGER NOT NULL,\
                nombre_cons	TEXT NOT NULL,\
                direccion_cons TEXT NOT NULL,\
                telefono_cons INTEGER,\
                PRIMARY KEY(id_cons AUTOINCREMENT)\
                )'
        self.consultar(sql)
        sql = 'CREATE TABLE cobro (\
                fecha_cob TEXT NOT NULL,\
                monto_cob INTEGER NOT NULL,\
                dni_pac_cob INTEGER NOT NULL,\
                descripcion_cob text,\
                FOREIGN KEY(dni_pac_cob) REFERENCES paciente(dni_pac),\
                PRIMARY KEY(dni_pac_cob,fecha_cob)\
                )'
        self.consultar(sql)
        sql = 'CREATE TABLE turno (\
                nro_turno INTEGER NOT NULL,\
                    fecha_turno TEXT NOT NULL,\
                    horario_turno TEXT NOT NULL,\
                    dni_pac_turno INTEGER NOT NULL,\
                    id_cons_turno INTEGER NOT NULL,\
                    PRIMARY KEY(fecha_turno,horario_turno),\
                    FOREIGN KEY(id_cons_turno) REFERENCES consultorio(id_cons),\
                    FOREIGN KEY(dni_pac_turno) REFERENCES paciente(dni_pac)\
                    )'
        self.consultar(sql)
        sql = 'CREATE TABLE sesion (\
                    fecha_ses TEXT NOT NULL,\
                    hora_ses TEXT NOT NULL,\
                    motivo_ses TEXT,\
                    tema_ses TEXT,\
                    evaluacion_ses TEXT,\
                    tratamiento_ses TEXT,\
                    notas_ses TEXT,\
                    dni_pac_ses INTEGER NOT NULL,\
                    FOREIGN KEY(dni_pac_ses) REFERENCES paciente(dni_pac),\
                    PRIMARY KEY(fecha_ses,dni_pac_ses)\
                    )'
        self.consultar(sql)