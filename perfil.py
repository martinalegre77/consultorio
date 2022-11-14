import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from estilos import Estilos
from win_secundaria import WinSecundaria
from conecciones import Conexion

# Configuracion del Perfil

class Perfil(WinSecundaria, Estilos):
    def __init__(self, master, titulo):
        super().__init__(master, titulo)
        # Labels
        label_titulo = ttk.Label(self.master, 
                text='Debe completar todos los campos para configurar su perfil', 
                background=self.color_principal, 
                width=50, 
                font='Arial 12 bold', 
                relief = 'flat')
        label_titulo.place(x=120, y=50)

        x_label = 180
        x_entry = 370
    
        label_apellido = ttk.Label(self.master, text='Apellido:')
        label_apellido.place(x=x_label, y=100)
        caja_apellido = ttk.Entry(self.master)
        caja_apellido.place(x=x_entry, y=100, width=150, height=25)
        apellido = caja_apellido.get()

        label_nombre = ttk.Label(self.master, text='Nombre/s:')
        label_nombre.place(x=x_label, y=150)
        caja_nombre = ttk.Entry(self.master)
        caja_nombre.place(x=x_entry, y=150, width=150, height=25)
        nombre = caja_nombre.get()

        label_dni = ttk.Label(self.master, text='DNI:')
        label_dni.place(x=x_label, y=200)
        caja_dni = ttk.Entry(self.master)
        caja_dni.place(x=x_entry, y=200, width=150, height=25)
        dni = caja_dni.get()

        label_titulo = ttk.Label(self.master, text='Título:')
        label_titulo.place(x=x_label, y=250)
        caja_titulo = ttk.Entry(self.master)
        caja_titulo.place(x=x_entry, y=250, width=150, height=25)
        titulo = caja_titulo.get()

        label_abreviatura = ttk.Label(self.master, text='Abreviatura título:')
        label_abreviatura.place(x=x_label, y=300)
        caja_abreviatura = ttk.Entry(self.master)
        caja_abreviatura.place(x=x_entry, y=300, width=150, height=25)
        abreviatura = caja_abreviatura.get()

        label_nacional = ttk.Label(self.master, text='Matrícula Nacional:')
        label_nacional.place(x=x_label, y=350)
        caja_nacional = ttk.Entry(self.master)
        caja_nacional.place(x=x_entry, y=350, width=150, height=25)
        ma_nacional = caja_nacional.get()

        label_provincial = ttk.Label(self.master, text='Matrícula Provincial:')
        label_provincial.place(x=x_label, y=400)
        caja_provincial = ttk.Entry(self.master)
        caja_provincial.place(x=x_entry, y=400, width=150, height=25)
        ma_provincial = caja_provincial.get()

        label_telefono = ttk.Label(self.master, text='Nro Teléfono:')
        label_telefono.place(x=x_label, y=450)
        caja_telefono = ttk.Entry(self.master)
        caja_telefono.place(x=x_entry, y=450, width=150, height=25)
        telefono = caja_telefono.get()

        label_email = ttk.Label(self.master, text='Email:')
        label_email.place(x=x_label, y=500)
        caja_email = ttk.Entry(self.master)
        caja_email.place(x=x_entry, y=500, width=150, height=25)
        mail = caja_email.get()

        boton_guardar = ttk.Button(self.master, text='Guardar', command = self.guardar(apellido, 
                                                                        nombre, dni, titulo, abreviatura, 
                                                                        ma_nacional, ma_provincial, 
                                                                        telefono, mail))
        boton_guardar.place(x=x_label+40, y=550)

        boton_cerrar = ttk.Button(self.master, text='Cerrar', command = self.cerrar)
        boton_cerrar.place(x=x_entry+35, y=550)

        self.master.focus()
        self.master.grab_set()



    def cerrar(self):
        self.master.destroy()


    def guardar(self, apellido, nombre, dni, titulo, abreviatura, 
                ma_nacional, ma_provincial, telefono, mail):
            print('Click en Guardar')
            if apellido == "" or nombre =="" or dni == "" \
                    or ma_nacional == "" or ma_provincial == "" or telefono == "":
                messagebox.showerror(
                        title='Advertencia',
                        message='Todos los campos deben estar completos'
                        )
                    
            else:
                sql = 'INSERT INTO perfil VALUE (?,?,?,?,?,?,?,?,?)'
                parametros = (apellido, nombre, dni, titulo, abreviatura, 
                                ma_nacional, ma_provincial, telefono, mail)
                Conexion.consultar(sql, parametros)
                    # conn = sqlite3.connect('consultorio.db') 
                    # cursor = conn.cursor()
                    # try:
                    #     cursor.execute('INSERT INTO perfil VALUE (?,?,?,?,?,?,?,?,?)',
                    #              (apellido, nombre, dni, titulo, abreviatura, ma_nacional, ma_provincial, telefono, mail))
                    #     conn.commit()
                    #     conn.close()
                messagebox.showinfo(
                            title="Datos Guardados",
                            message="Los datos se guardaron correctamente."
                            )
                    # except sqlite3.OperationalError:
                    #     pass
                self.cerrar()

    # def cerrar(self):
    #     self.master.destroy()

