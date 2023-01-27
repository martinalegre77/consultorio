
from calendar import Calendar
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from conecciones import Conexion
from estilos import Estilos
from tkcalendar import DateEntry


class Botones(Estilos):
    def __init__(self, root, titulo):
        super().__init__()
        self.root = root
        self.root = tk.Toplevel()
        self.root.resizable(0,0)
        self.root.focus()
        self.root.style = ttk.Style()
        self.root.geometry("660x570+410+60")
        self.root.grab_set()
        self.root.iconbitmap('./iconos/favicon.ico')
        self.root.title(titulo)
        self.root.config(background=self.color_principal)
        self.root.style.configure("TLabel", foreground="gray15", 
                                        font = "Arial 11",
                                        relief = 'flat',   
                                        bordercolor = 'black', 
                                        anchor = 5, 
                                        padding = 2, 
                                        width=20, 
                                        height=25)
        self.query=Conexion()      

    def mostrar_tabla(self, titulo2, columnas, texto_columnas, ancho_columnas, sql):
        titulo2 = ttk.Label(self.root, text=titulo2, 
                    background = self.color_principal, 
                    font = 'Arial 18 bold', 
                    justify = 'center',
                    relief='flat',
                    width=400)
        titulo2.pack()
        frame_treeview = ttk.Frame(self.root)
        frame_treeview.pack()
        self.scrollbar = ttk.Scrollbar(frame_treeview, orient=tk.VERTICAL)
        self.tabla = ttk.Treeview(frame_treeview,
            yscrollcommand=self.scrollbar.set,
            columns=columnas, 
            show='headings')
        self.scrollbar.config(command=self.tabla.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabla.pack()
        
        for i in range(len(texto_columnas)):
            self.tabla.heading(columnas[i], text=texto_columnas[i])
            self.tabla.column(columnas[i], width=ancho_columnas[i], anchor='center')

        q = self.query.consultar(sql)

        for linea in q.fetchall():
            self.tabla.insert('', tk.END, values=linea)

        self.boton_cerrar = ttk.Button(self.root, text='CERRAR', command = self.root.destroy, )
        self.boton_cerrar.place(x=540, y=520, width=85, height=25)

class Agenda(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'A G E N D A'
        columnas = ['fecha', 'hora', 'apellido', 'nombre', 'telefono', 'osocial']
        texto_columnas = ['Fecha', 'Hora', 'Apellido', 'Nombre', 'Teléfono', 'O. Social']
        ancho_columnas = [95,95,110,110,90,100]

        sql = 'SELECT turnos.fecha_turno, turnos.horario_turno, turnos.apellido_pac, paciente.nombre_pac,\
                paciente.telefono_pac, paciente.obra_social_pac FROM turnos\
                INNER JOIN paciente ON turnos.dni_pac = paciente.dni_pac\
                WHERE turnos.fecha_turno > DATE("now")'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, sql)

class Pacientes(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'P A C I E N T E S'
        columnas = ['dni', 'apellido', 'nombre', 'osocial', 'telefono', 'mail']
        texto_columnas = ['DNI', 'Apellido', 'Nombre', 'Teléfono', 'O. Social', 'Mail']
        ancho_columnas = [75,100,100,85,95,145]
        sql = 'SELECT * FROM paciente ORDER BY apellido_pac'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, sql)

class Osociales(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'O B R A S  S O C I A L E S'
        columnas = ['orden', 'nombre', 'monto', 'descripcion']
        texto_columnas = ['Nro Orden', 'Nombre', 'Monto Cobertura', 'Descripción']
        ancho_columnas = [70,120,100,310]
        sql = 'SELECT * FROM obras_sociales'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, sql)

class Consultorios(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'C O N S U L T O R I O S'
        columnas = ['nombre', 'direccion', 'telefono']
        texto_columnas = ['Nombre', 'Dirección', 'Teléfono']
        ancho_columnas = [300,150,150]
        sql = 'SELECT nombre_cons, direccion_cons, telefono_cons FROM consultorios'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, sql)

class Cobros(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'C O B R O S'
        columnas = ['apellido', 'dni', 'monto', 'fecha', 'tipo']
        texto_columnas = ['Apellido', 'DNI', 'Importe', 'Fecha del cobro', 'Forma de pago']
        ancho_columnas = [150,100,100,100,150]
        sql = 'SELECT paciente.apellido_pac, cobros.dni_pac, cobros.monto, cobros.fecha_cobro, cobros.tipo\
                FROM paciente\
                INNER JOIN cobros\
                ON paciente.dni_pac = cobros.dni_pac'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, sql)

class Turnos(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'T U R N O S'
        columnas = ['fecha', 'hora', 'apellido', 'nombre', 'telefono', 'osocial']
        texto_columnas = ['Fecha', 'Hora', 'Apellido', 'Nombre', 'Teléfono', 'O. Social']
        ancho_columnas = [95,95,110,110,90,100]

        sql = 'SELECT turnos.fecha_turno, turnos.horario_turno, turnos.apellido_pac, paciente.nombre_pac,\
                paciente.telefono_pac, paciente.obra_social_pac FROM turnos\
                INNER JOIN paciente ON turnos.dni_pac = paciente.dni_pac\
                WHERE turnos.fecha_turno < DATE("now")'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, sql)

# ------Interacción Usuario-------------------------------------------------------

        frame_inf = tk.Frame(self.root, bg=self.color_principal, relief='raise')
        frame_inf.pack(pady=20)
        anio = int(datetime.now().year)
        # mes = int(datetime.now().month)
        # dia = int(datetime.now().day)
        lab_cal = ttk.Label(frame_inf)
        lab_cal.config(background='light cyan', relief='flat', padding=5)
        lab_cal.grid(row=0, column=0, columnspan=2)
        self.calendario = DateEntry(lab_cal, background='darkblue',
                                    foreground='white', borderwidth=2, year=anio)
        self.calendario.pack()

        label_apellido = ttk.Label(frame_inf, text='Apellido:', background=self.color_principal, relief='flat')
        label_apellido.grid(row=0, column=2, padx=20, pady=10)
        self.entry_apellido = ttk.Entry(frame_inf, state='disable')
        self.entry_apellido.grid(row=0, column=3, padx=10, pady=10)
        
        label_nombre = ttk.Label(frame_inf, text='Nombre/s:', background=self.color_principal, relief='flat')
        label_nombre.grid(row=1, column=2,padx=20, pady=10)
        self.entry_nombre = ttk.Entry(frame_inf, state='disable')
        self.entry_nombre.grid(row=1, column=3, padx=10, pady=10)

        label_dni = ttk.Label(frame_inf, text='Teléfono:', background=self.color_principal, relief='flat')
        label_dni.grid(row=2, column=2, padx=20, pady=10)
        self.entry_tel = ttk.Entry(frame_inf, state='disable')
        self.entry_tel.grid(row=2, column=3, padx=10, pady=10)
        
        label_titulo = ttk.Label(frame_inf, text='Horario:', background=self.color_principal, relief='flat')
        label_titulo.grid(row=3, column=2, padx=20, pady=10)
        self.entry_horario = ttk.Entry(frame_inf, state='disable')
        self.entry_horario.grid(row=3, column=3, padx=10, pady=10)

        boton_turno = ttk.Button(frame_inf, text='Ingresar turno', 
                                padding=3, command=self.habilitar, cursor='hand2')
        boton_turno.grid(row=0, column=4, padx=20, pady=10)
        boton_guardar_turno = ttk.Button(frame_inf, text='Guardar turno', 
                                        padding=3, command=self.guardar_turno, cursor='hand2')
        boton_guardar_turno.grid(row=2, column=4, padx=20, pady=10)

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