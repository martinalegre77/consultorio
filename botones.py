
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
        wventana = 660
        hventana = 570
        vx, vy = self.valoresxy(self.root, wventana, hventana)
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(vx+100)+"+"+str(vy-20))
        # self.root.geometry("660x570+410+60")
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
        frame_treeview = tk.Frame(self.root)
        frame_treeview.pack()
        self.scroll = ttk.Scrollbar(frame_treeview, orient=tk.VERTICAL)
        self.tabla = ttk.Treeview(frame_treeview,
            yscrollcommand=self.scroll.set,
            columns=columnas, 
            show='headings')
        self.scroll.config(command=self.tabla.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabla.pack()
        for i in range(len(texto_columnas)):
            self.tabla.heading(columnas[i], text=texto_columnas[i])
            self.tabla.column(columnas[i], width=ancho_columnas[i], anchor='center')
        self.llenar_tabla(sql)
        self.frame_inf = tk.Frame(self.root, bg=self.color_principal, relief='raise')
        self.frame_inf.pack(pady=20)
        self.boton_cerrar = ttk.Button(self.root, text='Cerrar', command = self.root.destroy, )
        self.boton_cerrar.place(x=540, y=520, width=85, height=25)

    def llenar_tabla(self,sql):
        q = self.query.consultar(sql)
        for linea in q.fetchall():
            self.tabla.insert('',0, values=linea) # cambie tk.END por el 0

class Agenda(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'A G E N D A'
        columnas = ['fecha', 'hora', 'apellido', 'nombre', 'telefono', 'osocial']
        texto_columnas = ['Fecha', 'Hora', 'Apellido', 'Nombre', 'Teléfono', 'O. Social']
        ancho_columnas = [95,95,110,110,90,100]
        self.sql = 'SELECT turnos.fecha_turno, turnos.horario_turno, turnos.apellido_pac, paciente.nombre_pac,\
                paciente.telefono_pac, paciente.obra_social_pac FROM turnos\
                INNER JOIN paciente ON turnos.dni_pac = paciente.dni_pac\
                WHERE turnos.fecha_turno > DATE("now")'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, self.sql)
        # ------Interacción Ventana PACIENTE---
        label_paciente = ttk.Label(self.frame_inf, text='Lista de Pacientes', background = self.color_principal, 
                    font = 'Arial 12', justify = 'center')
        label_paciente.grid(row=0, column=0, padx=10, pady=5)
        frame_lista = ttk.Frame(self.frame_inf)
        scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        sql = 'SELECT apellido_pac, nombre_pac FROM paciente'
        lista_pacientes = self.query.consultar(sql)
        self.listbox.insert(0, *lista_pacientes)
        self.listbox.pack()
        frame_lista.grid(row=1, column=0, padx=10, pady=5, rowspan=3)
        boton_buscar = ttk.Button(self.frame_inf, text='Buscar Turnos', 
                                padding=3, command=self.buscar_turnos, cursor='hand2')
        boton_buscar.grid(row=1, column=1, padx=10, pady=5, sticky='S')
        boton_agenda = ttk.Button(self.frame_inf, text='Ver Agenda', 
                                padding=3, command=self.mostrar_agenda, cursor='hand2')
        boton_agenda.grid(row=3, column=1, padx=10, pady=5, sticky='N')

    def buscar_turnos(self):
        try:
            indice = self.listbox.curselection()
            paciente = self.listbox.get(indice)
            apellido, nombre = paciente
            sql = f"""SELECT turnos.fecha_turno, turnos.horario_turno, turnos.apellido_pac, paciente.nombre_pac,
                    paciente.telefono_pac, paciente.obra_social_pac FROM turnos INNER JOIN paciente 
                    ON turnos.dni_pac = paciente.dni_pac WHERE turnos.dni_pac IN (SELECT dni_pac FROM paciente
                    WHERE apellido_pac='{apellido}' AND nombre_pac='{nombre}')"""
            if self.query.consultar(sql).fetchall()==[]:
                messagebox.showinfo(
                        title='Resultado de la consulta',
                        message='El paciente no tiene turnos'
                        )
            else:
                self.tabla.delete(*self.tabla.get_children())
                self.llenar_tabla(sql)
        except:
            messagebox.showwarning(
                        title='Advertencia',
                        message='Debe seleccionar un paciente'
                        )

    def mostrar_agenda(self):
        self.tabla.delete(*self.tabla.get_children())
        self.llenar_tabla(self.sql)

class Pacientes(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'P A C I E N T E S'
        columnas = ['dni', 'apellido', 'nombre', 'osocial', 'telefono', 'mail']
        texto_columnas = ['DNI', 'Apellido', 'Nombre', 'O. Social', 'Teléfono', 'Mail']
        ancho_columnas = [75,100,100,85,95,145]
        self.sql = 'SELECT * FROM paciente ORDER BY apellido_pac DESC'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, self.sql)
        # ------Interacción Ventana PACIENTE---
        label_apellido = ttk.Label(self.frame_inf, text='Apellido:', background=self.color_principal, relief='flat')
        label_apellido.grid(row=0, column=0, padx=5, pady=10)
        self.entry_apellido = ttk.Entry(self.frame_inf, state='disable')
        self.entry_apellido.grid(row=0, column=1, padx=3, pady=10)
        label_nombre = ttk.Label(self.frame_inf, text='Nombre/s:', background=self.color_principal, relief='flat')
        label_nombre.grid(row=1, column=0,padx=5, pady=10)
        self.entry_nombre = ttk.Entry(self.frame_inf, state='disable')
        self.entry_nombre.grid(row=1, column=1, padx=3, pady=10)
        label_dni = ttk.Label(self.frame_inf, text='Nro Documento:', background=self.color_principal, relief='flat')
        label_dni.grid(row=2, column=0,padx=5, pady=10)
        self.entry_dni = ttk.Entry(self.frame_inf, state='disable')
        self.entry_dni.grid(row=2, column=1, padx=3, pady=10)
        label_tel = ttk.Label(self.frame_inf, text='Teléfono:', background=self.color_principal, relief='flat')
        label_tel.grid(row=0, column=2, padx=5, pady=10)
        self.entry_tel = ttk.Entry(self.frame_inf, state='disable')
        self.entry_tel.grid(row=0, column=3, padx=3, pady=10)
        label_osocial = ttk.Label(self.frame_inf, text='Obra Social:', background=self.color_principal, relief='flat')
        label_osocial.grid(row=1, column=2, padx=5, pady=10)
        self.entry_osocial = ttk.Entry(self.frame_inf, state='disable')
        self.entry_osocial.grid(row=1, column=3, padx=3, pady=10)
        label_mail = ttk.Label(self.frame_inf, text='E-mail:', background=self.color_principal, relief='flat')
        label_mail.grid(row=2, column=2, padx=5, pady=10)
        self.entry_mail = ttk.Entry(self.frame_inf, state='disable')
        self.entry_mail.grid(row=2, column=3, padx=3, pady=10)
        self.modificacion = False
        boton_modificar = ttk.Button(self.frame_inf, text='Modificar Paciente', 
                                padding=3, command=self.modificar, cursor='hand2')
        boton_modificar.grid(row=4, column=0, padx=3, pady=40)
        boton_habilitar = ttk.Button(self.frame_inf, text='Ingresar Paciente', 
                                padding=3, command=self.habilitar, cursor='hand2')
        boton_habilitar.grid(row=4, column=1, padx=3, pady=40)

    def modificar(self):
        try:
            self.dni_viejo = self.tabla.item(self.tabla.selection())['values'][0]
            apellido = self.tabla.item(self.tabla.selection())['values'][1]
            nombre = self.tabla.item(self.tabla.selection())['values'][2]
            telefono = self.tabla.item(self.tabla.selection())['values'][4]
            osocial = self.tabla.item(self.tabla.selection())['values'][3]
            mail = self.tabla.item(self.tabla.selection())['values'][5]
            self.habilitar()
            self.entry_apellido.insert(0, apellido)
            self.entry_apellido.focus()
            self.entry_nombre.insert(0, nombre)
            self.entry_dni.insert(0, self.dni_viejo)
            self.entry_tel.insert(0, telefono)
            self.entry_osocial.insert(0, osocial)
            self.entry_mail.insert(0, mail)
            self.modificacion = True
        except:
            messagebox.showwarning(
                        title='Advertencia',
                        message='Debe seleccionar el paciente a modificar'
                        )

    def habilitar(self):
        self.entry_apellido.config(state='normal')
        self.entry_apellido.focus()
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_tel.config(state='normal')
        self.entry_osocial.config(state='normal')
        self.entry_mail.config(state='normal')
        self.boton_guardar = ttk.Button(self.frame_inf, text='Guardar datos', 
                                        padding=3, command=self.guardar_datos, cursor='hand2')
        self.boton_guardar.grid(row=4, column=2, padx=3, pady=40)

    def guardar_datos(self):
        if len(self.entry_apellido.get()) < 3 or len(self.entry_nombre.get()) < 3 or len(self.entry_dni.get()) < 8:
            messagebox.showwarning(
                        title='Advertencia',
                        message='Apellido, Nombre y DNI son campos obligatorios'
                        )
            self.entry_apellido.focus()  
        else:
            apellido = self.entry_apellido.get()
            nombre = self.entry_nombre.get()
            dni = self.entry_dni.get()
            telefono = self.entry_tel.get()
            osocial = self.entry_osocial.get()
            mail = self.entry_mail.get()
            if self.modificacion:
                sql = f"""UPDATE paciente SET dni_pac='{dni}', apellido_pac='{apellido}', nombre_pac='{nombre}',\
                                obra_social_pac='{osocial}', telefono_pac='{telefono}', mail_pac='{mail}'\
                                    WHERE dni_pac = '{self.dni_viejo}'"""
                self.query.consultar(sql)
            else:
                sql = 'INSERT INTO paciente VALUES(?,?,?,?,?,?)'
                parametros = (dni, apellido, nombre, osocial, telefono, mail)
                self.query.consultar(sql, parametros)
            messagebox.showinfo(
                                title="Datos Paciente",
                                message="Los datos se guardaron correctamente."
                                )
            self.borrar_entrys()
            self.tabla.delete(*self.tabla.get_children())
            self.llenar_tabla(self.sql)
            self.modificacion = False   

    def borrar_entrys(self):
        self.entry_apellido.delete(0, tk.END) 
        self.entry_nombre.delete(0, tk.END)
        self.entry_dni.delete(0, tk.END)
        self.entry_tel.delete(0, tk.END)
        self.entry_osocial.delete(0, tk.END)
        self.entry_mail.delete(0, tk.END)
        self.entry_apellido.config(state='disable')
        self.entry_nombre.config(state='disable')
        self.entry_dni.config(state='disable')
        self.entry_tel.config(state='disable')
        self.entry_osocial.config(state='disable')
        self.entry_mail.config(state='disable')
        self.boton_guardar.destroy()

class Osociales(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'O B R A S  S O C I A L E S'
        columnas = ['orden', 'nombre', 'monto', 'descripcion']
        texto_columnas = ['Nro Orden', 'Nombre', 'Monto Cobertura', 'Descripción']
        ancho_columnas = [70,120,100,310]
        self.sql = 'SELECT * FROM obras_sociales'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, self.sql)

class Consultorios(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'C O N S U L T O R I O S'
        columnas = ['nombre', 'direccion', 'telefono']
        texto_columnas = ['Nombre', 'Dirección', 'Teléfono']
        ancho_columnas = [300,150,150]
        self.sql = 'SELECT nombre_cons, direccion_cons, telefono_cons FROM consultorios'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, self.sql)

class Cobros(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'C O B R O S'
        columnas = ['apellido', 'dni', 'monto', 'fecha', 'tipo']
        texto_columnas = ['Apellido', 'DNI', 'Importe', 'Fecha del cobro', 'Forma de pago']
        ancho_columnas = [150,100,100,100,150]
        self.sql = 'SELECT paciente.apellido_pac, cobros.dni_pac, cobros.monto, cobros.fecha_cobro, cobros.tipo\
                FROM paciente\
                INNER JOIN cobros\
                ON paciente.dni_pac = cobros.dni_pac'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, self.sql)

class Turnos(Botones):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        titulo2 = 'T U R N O S'
        columnas = ['fecha', 'hora', 'apellido', 'nombre', 'telefono', 'osocial']
        texto_columnas = ['Fecha', 'Hora', 'Apellido', 'Nombre', 'Teléfono', 'O. Social']
        ancho_columnas = [95,95,110,110,90,100]
        self.sql = 'SELECT turnos.fecha_turno, turnos.horario_turno, turnos.apellido_pac, paciente.nombre_pac,\
                paciente.telefono_pac, paciente.obra_social_pac FROM turnos\
                INNER JOIN paciente ON turnos.dni_pac = paciente.dni_pac\
                WHERE turnos.fecha_turno < DATE("now")'
        self.mostrar_tabla(titulo2, columnas, texto_columnas, ancho_columnas, self.sql)
        # ------Interacción Usuario TURNOS---
        anio = int(datetime.now().year)
        mes = int(datetime.now().month)
        dia = int(datetime.now().day)

        # boton_fecha = ttk.Button(frame_inf, text='Elegir fecha', command=self.elegir_fecha)
        # boton_fecha.grid(row=0, column=0)

        # frame_cal = ttk.Frame(frame_inf, width=20, padding=10)
        # # frame_cal.config(relief='flat', padding=5, width=15)
        # frame_cal.grid(row=0, column=0, columnspan=2)
        calendario = DateEntry(self.frame_inf, width=10, background='darkblue',
                            foreground='white', borderwidth=2, year=anio)
        calendario.grid(row=0, column=0)
        # cal = Calendar(frame_cal, font="Arial 10", selectmode='day', locale='es', year=anio, month=mes, day=dia)
        # cal.pack(expand=0)
        label_apellido = ttk.Label(self.frame_inf, text='Apellido:', background=self.color_principal, relief='flat')
        label_apellido.grid(row=0, column=2, padx=20, pady=10)
        self.entry_apellido = ttk.Entry(self.frame_inf, state='disable')
        self.entry_apellido.grid(row=0, column=3, padx=10, pady=10)
        label_nombre = ttk.Label(self.frame_inf, text='Nombre/s:', background=self.color_principal, relief='flat')
        label_nombre.grid(row=1, column=2,padx=20, pady=10)
        self.entry_nombre = ttk.Entry(self.frame_inf, state='disable')
        self.entry_nombre.grid(row=1, column=3, padx=10, pady=10)
        label_tel = ttk.Label(self.frame_inf, text='Teléfono:', background=self.color_principal, relief='flat')
        label_tel.grid(row=2, column=2, padx=20, pady=10)
        self.entry_tel = ttk.Entry(self.frame_inf, state='disable')
        self.entry_tel.grid(row=2, column=3, padx=10, pady=10)
        label_horario = ttk.Label(self.frame_inf, text='Horario:', background=self.color_principal, relief='flat')
        label_horario.grid(row=3, column=2, padx=20, pady=10)
        self.entry_horario = ttk.Entry(self.frame_inf, state='disable')
        self.entry_horario.grid(row=3, column=3, padx=10, pady=10)

        boton_habilitar = ttk.Button(self.frame_inf, text='Ingresar turno', 
                                padding=3, command=self.habilitar, cursor='hand2')
        boton_habilitar.grid(row=0, column=4, padx=20, pady=10)
        boton_guardar = ttk.Button(self.frame_inf, text='Guardar turno', 
                                        padding=3, command=self.guardar_datos, cursor='hand2')
        boton_guardar.grid(row=2, column=4, padx=20, pady=10)

    def habilitar(self):
        self.entry_apellido.config(state='normal')
        self.entry_apellido.focus()
        self.entry_nombre.config(state='normal')
        self.entry_tel.config(state='normal')
        self.entry_horario.config(state='normal')

    def guardar_datos(self):
        apellido = self.entry_apellido.get()
        nombre = self.entry_nombre.get()
        telefono = self.entry_tel.get()
        horario = self.entry_horario.get()
        self.borrar_entrys()

    def borrar_entrys(self):    
        self.entry_apellido.delete(0, tk.END) 
        self.entry_nombre.delete(0, tk.END)
        self.entry_tel.delete(0, tk.END)
        self.entry_horario.delete(0, tk.END)