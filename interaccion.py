
import tkinter as tk
from tkinter import ttk
from conecciones import Conexion

class Contenedor(tk.Frame):
    def __init__(self, root):
        self.query=Conexion()
        self.frame_cont = tk.Frame(root)
        self.frame_cont.place(x=240, y=50)
        # self.frame_cont.config(width=600, height=530, bg ='lightcyan2', relief='ridge', borderwidth=5)
        self.frame_cont.config(bg ='lightcyan2', relief='ridge', borderwidth=5)

    def mostrar_tabla(self, titulo, columnas, texto_columnas, ancho_columnas, sql):

        titulo = ttk.Label(self.frame_cont, text=titulo, 
                    background = 'lightcyan2', 
                    font = 'Arial 18', 
                    justify = 'center',
                    relief='flat')
        titulo.pack()
        self.barra = ttk.Scrollbar(self.frame_cont)
        self.barra.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabla = ttk.Treeview(self.frame_cont,
            yscrollcommand=self.barra.set,
            columns=columnas, 
            show='headings')
        
        for i in range(len(texto_columnas)):
            self.tabla.heading(columnas[i], text=texto_columnas[i])
            self.tabla.column(columnas[i], width=ancho_columnas[i], anchor='center')

        self.tabla.pack()

        self.barra.config(command=self.tabla.yview)

        q = self.query.consultar(sql)

        for linea in q.fetchall():
            self.tabla.insert('', tk.END, values=linea)

class Agenda(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        titulo = 'A G E N D A'
        columnas = ['fecha', 'hora', 'apellido', 'nombre', 'telefono', 'osocial']
        texto_columnas = ['Fecha', 'Hora', 'Apellido', 'Nombre', 'Teléfono', 'O. Social']
        ancho_columnas = [95,95,110,110,90,100]

        sql = 'SELECT turnos.fecha_turno, turnos.horario_turno, turnos.apellido_pac, paciente.nombre_pac,\
                paciente.telefono_pac, paciente.obra_social_pac FROM turnos\
                INNER JOIN paciente ON turnos.dni_pac = paciente.dni_pac\
                WHERE turnos.fecha_turno = DATE("now")'
        self.mostrar_tabla(titulo, columnas, texto_columnas, ancho_columnas, sql)

        # self.titulo('A G E N D A')
        # self.barra = ttk.Scrollbar(self.frame_cont)
        # self.barra.pack(side=tk.RIGHT, fill=tk.Y)
        # self.tabla = ttk.Treeview(self.frame_cont,
        #     yscrollcommand=self.barra.set,
        #     columns=('fecha', 'hora', 'apellido', 'nombre', 'telefono', 'osocial'), 
        #     show='headings')
        # self.tabla.heading('fecha', text='Fecha')
        # self.tabla.heading('hora', text='Hora')
        # self.tabla.heading('apellido', text='Apellido')
        # self.tabla.heading('nombre', text='Nombre')
        # self.tabla.heading('telefono', text='Teléfono')
        # self.tabla.heading('osocial', text='O.Social')

        # self.tabla.column('hora', width=95, anchor='center')
        # self.tabla.column('fecha', width=95, anchor='center')
        # self.tabla.column('nombre', width=110, anchor='center')
        # self.tabla.column('apellido', width=110, anchor='center')
        # self.tabla.column('osocial', width=90, anchor='center')
        # self.tabla.column('telefono', width=100, anchor='center')

        # self.tabla.pack()

        # self.barra.config(command=self.tabla.yview)

        # sql = 'SELECT turnos.fecha_turno, turnos.horario_turno, turnos.apellido_pac, paciente.nombre_pac,\
        #         paciente.telefono_pac, paciente.obra_social_pac FROM turnos\
        #         INNER JOIN paciente ON turnos.dni_pac = paciente.dni_pac'
        # q = self.query.consultar(sql)
        # for linea in q.fetchall():
        #     self.tabla.insert('', tk.END, values=linea)

class Pacientes(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        titulo = 'P A C I E N T E S'
        columnas = ['dni', 'apellido', 'nombre', 'osocial', 'telefono', 'mail']
        texto_columnas = ['DNI', 'Apellido', 'Nombre', 'Teléfono', 'O. Social', 'Mail']
        ancho_columnas = [75,100,100,85,95,145]
        sql = 'SELECT * FROM paciente ORDER BY apellido_pac'
        self.mostrar_tabla(titulo, columnas, texto_columnas, ancho_columnas, sql)

class Osociales(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        titulo = 'O B R A S  S O C I A L E S'
        columnas = ['orden', 'nombre', 'monto', 'descripcion']
        texto_columnas = ['Nro Orden', 'Nombre', 'Monto Cobertura', 'Descripción']
        ancho_columnas = [70,120,100,310]
        sql = 'SELECT * FROM obras_sociales'
        self.mostrar_tabla(titulo, columnas, texto_columnas, ancho_columnas, sql)

class Consultorios(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        titulo = 'C O N S U L T O R I O S'
        columnas = ['nombre', 'direccion', 'telefono']
        texto_columnas = ['Nombre', 'Dirección', 'Teléfono']
        ancho_columnas = [300,150,150]
        sql = 'SELECT nombre_cons, direccion_cons, telefono_cons FROM consultorios'
        self.mostrar_tabla(titulo, columnas, texto_columnas, ancho_columnas, sql)

class Cobros(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        titulo = 'C O B R O S'
        columnas = ['apellido', 'dni', 'monto', 'fecha', 'tipo']
        texto_columnas = ['Apellido', 'DNI', 'Importe', 'Fecha del cobro', 'Forma de pago']
        ancho_columnas = [150,100,100,100,150]
        sql = 'SELECT paciente.apellido_pac, cobros.dni_pac, cobros.monto, cobros.fecha_cobro, cobros.tipo\
                FROM paciente\
                INNER JOIN cobros\
                ON paciente.dni_pac = cobros.dni_pac'
        self.mostrar_tabla(titulo, columnas, texto_columnas, ancho_columnas, sql)

class Turnos(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        pass

