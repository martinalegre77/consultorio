
import tkinter as tk
from tkinter import ttk
from conecciones import Conexion

class Contenedor(tk.Frame):
    def __init__(self, root):
        self.query=Conexion()
        self.frame_cont = tk.Frame(root)
        self.frame_cont.place(x=240, y=50)
        self.frame_cont.config(width=600, height=530, bg='lightcyan2', relief='sunken', borderwidth=3)
        # self.frame_cont.grid(row=0, column=0, columnspan=7)
        
class Agenda(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        tabla = ttk.Treeview(self.frame_cont, 
            columns=('orden', 'fecha', 'hora', 'apellido', 'nombre', 'telefono', 'osocial'), 
            show='headings'
            )
        tabla.heading('orden', text='Orden')
        tabla.heading('fecha', text='Fecha')
        tabla.heading('hora', text='Hora')
        tabla.heading('apellido', text='Apellido')
        tabla.heading('nombre', text='Nombre')
        tabla.heading('telefono', text='Teléfono')
        tabla.heading('osocial', text='O.Social')

        tabla.column('orden', width=50)
        tabla.column('fecha', width=85)
        tabla.column('hora', width=85)
        tabla.column('apellido', width=100)
        tabla.column('nombre', width=100)
        tabla.column('telefono', width=90)
        tabla.column('osocial', width=90)

        tabla.pack()

        sql = 'SELECT fecha_turno, horario_turno, apellido_pac, nombre_pac, telefono_pac, \
                obra_social_pac FROM turnos, paciente WHERE turnos.dni_pac = paciente.dni_pac'
        consulta = self.query.consultar(sql)
        lineas = consulta.fetchall()
        print(lineas)
        # consulta.close()

        # for linea in lineas:
        #     datos_turnos = linea.split(',')
        #     tabla.insert('', tk.END, values=datos_turnos)

class Pacientes(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        pass

class Osociales(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        pass

class Consultorios(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        pass

class Pagos(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        pass

class Turnos(Contenedor):
    def __init__(self, root):
        super().__init__(root)
        pass

