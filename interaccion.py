
import calendar
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from conecciones import Conexion
from tkcalendar import Calendar, DateEntry

class Contenedor(tk.Frame):
    def __init__(self, root):
        self.query=Conexion()
        self.frame_cont = tk.Frame(root)
        self.frame_cont.place(x=240, y=50)
        # self.frame_cont.config(width=600, height=530, bg ='lightcyan2', relief='ridge', borderwidth=5)
        self.frame_cont.config(bg ='lightcyan2', relief='ridge', borderwidth=5)
        # 2do frame
        self.frame_turnos = tk.Frame(root)
        self.frame_turnos.place(x=260, y=370)
        self.frame_turnos.config(bg ='light cyan', relief='flat')

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
                WHERE turnos.fecha_turno > DATE("now")'
        self.mostrar_tabla(titulo, columnas, texto_columnas, ancho_columnas, sql)

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
        titulo = 'T U R N O S'
        columnas = ['fecha', 'hora', 'apellido', 'nombre', 'telefono', 'osocial']
        texto_columnas = ['Fecha', 'Hora', 'Apellido', 'Nombre', 'Teléfono', 'O. Social']
        ancho_columnas = [95,95,110,110,90,100]

        sql = 'SELECT turnos.fecha_turno, turnos.horario_turno, turnos.apellido_pac, paciente.nombre_pac,\
                paciente.telefono_pac, paciente.obra_social_pac FROM turnos\
                INNER JOIN paciente ON turnos.dni_pac = paciente.dni_pac\
                WHERE turnos.fecha_turno < DATE("now")'
        self.mostrar_tabla(titulo, columnas, texto_columnas, ancho_columnas, sql)

        self.anio = int(datetime.now().year)
        self.mes = int(datetime.now().month)
        self.dia = int(datetime.now().day)
        
        # --------- FRAME TURNOS -----------------
        self.label_calendar = ttk.Label(self.frame_turnos, width=50)
        self.label_calendar.grid(row=1, column=0, rowspan=4)
        self.label_calendar.config(background='light cyan', relief='flat')
        self.calendario = DateEntry(self.label_calendar, width=12, background='darkblue',
                                foreground='white', borderwidth=2, year=self.anio)
        # self.calendario = DateEntry(self.frame_calendar, bg='darkblue', fg='white', font=('arial', 9 , 'bold'), year=self.anio)
        # self.calendario = Calendar(self.frame_turnos, selectmode='day', 
        #                                             year=self.anio, month=self.mes, day=self.dia, 
        #                                             date_pattern='dd/mm/y', font=('arial', 9 , 'bold'))
        self.calendario.pack(padx=10, pady=10)

        label_apellido = ttk.Label(self.frame_turnos, text='Apellido:', background='light cyan', relief='flat')
        label_apellido.grid(row=1, column=2, padx=20, pady=10)
        self.entry_apellido = ttk.Entry(self.frame_turnos, state='disable')
        self.entry_apellido.grid(row=1, column=3, padx=10, pady=10)
        
        label_nombre = ttk.Label(self.frame_turnos, text='Nombre/s:', background='light cyan', relief='flat')
        label_nombre.grid(row=2, column=2,padx=20, pady=10)
        self.entry_nombre = ttk.Entry(self.frame_turnos, state='disable')
        self.entry_nombre.grid(row=2, column=3, padx=10, pady=10)

        label_dni = ttk.Label(self.frame_turnos, text='Teléfono:', background='light cyan', relief='flat')
        label_dni.grid(row=3, column=2, padx=20, pady=10)
        self.entry_tel = ttk.Entry(self.frame_turnos, state='disable')
        self.entry_tel.grid(row=3, column=3, padx=10, pady=10)
        
        label_titulo = ttk.Label(self.frame_turnos, text='Horario:', background='light cyan', relief='flat')
        label_titulo.grid(row=4, column=2, padx=20, pady=10)
        self.entry_horario = ttk.Entry(self.frame_turnos, state='disable')
        self.entry_horario.grid(row=4, column=3, padx=10, pady=10)

        boton_turno = ttk.Button(self.frame_turnos, text='Ingresar turno', 
                                padding=3, command=self.habilitar, cursor='hand2')
        boton_turno.grid(row=1, column=4, padx=20, pady=10)
        boton_guardar_turno = ttk.Button(self.frame_turnos, text='Guardar turno', 
                                        padding=3, command=self.guardar_turno, cursor='hand2')
        boton_guardar_turno.grid(row=3, column=4, padx=20, pady=10)

    def habilitar(self):
        self.entry_apellido.config(state='normal')
        self.entry_apellido.focus()
        self.entry_nombre.config(state='normal')
        self.entry_tel.config(state='normal')
        self.entry_horario.config(state='normal')

    def guardar_turno(self):
        apellido_turno = self.entry_apellido.get()
        nombre_turno = self.entry_nombre.get()
        telefono_turno = self.entry_tel.get()
        horario_turno = self.entry_horario.get()

        self.entry_apellido.delete(0, tk.END) 
        self.entry_nombre.delete(0, tk.END)
        self.entry_tel.delete(0, tk.END)
        self.entry_horario.delete(0, tk.END)

        print(apellido_turno, nombre_turno, telefono_turno, horario_turno)