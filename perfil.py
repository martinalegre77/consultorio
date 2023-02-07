from tkinter import ttk
from tkinter import messagebox
from estilos import Estilos
from win_secundaria import WinSecundaria
from conecciones import Conexion

class Perfil(WinSecundaria, Estilos):
    def __init__(self, root, titulo, master):
        super().__init__(root, titulo)
        self.query=Conexion()
        self.master = master
        # Labels
        self.root.resizable(0,0) 
        label_titulo = ttk.Label(self.root, 
                text='Debe completar todos los campos para configurar su perfil', 
                background=self.color_principal, 
                width=50, 
                font='Arial 12 bold', 
                relief = 'flat')
        label_titulo.place(x=120, y=50)
        x_label = 180
        x_entry = 370
        label_apellido = ttk.Label(self.root, text='Apellido:')
        label_apellido.place(x=x_label, y=100)
        self.caja_apellido = ttk.Entry(self.root)
        self.caja_apellido.place(x=x_entry, y=100, width=150, height=25)
        
        label_nombre = ttk.Label(self.root, text='Nombre/s:')
        label_nombre.place(x=x_label, y=150)
        self.caja_nombre = ttk.Entry(self.root)
        self.caja_nombre.place(x=x_entry, y=150, width=150, height=25)

        label_dni = ttk.Label(self.root, text='DNI:')
        label_dni.place(x=x_label, y=200)
        self.caja_dni = ttk.Entry(self.root)
        self.caja_dni.place(x=x_entry, y=200, width=150, height=25)
        
        label_titulo = ttk.Label(self.root, text='Título:')
        label_titulo.place(x=x_label, y=250)
        self.caja_titulo = ttk.Entry(self.root)
        self.caja_titulo.place(x=x_entry, y=250, width=150, height=25)

        label_abreviatura = ttk.Label(self.root, text='Abreviatura título:')
        label_abreviatura.place(x=x_label, y=300)
        self.caja_abreviatura = ttk.Entry(self.root)
        self.caja_abreviatura.place(x=x_entry, y=300, width=150, height=25)

        label_nacional = ttk.Label(self.root, text='Matrícula Nacional:')
        label_nacional.place(x=x_label, y=350)
        self.caja_nacional = ttk.Entry(self.root)
        self.caja_nacional.place(x=x_entry, y=350, width=150, height=25)

        label_provincial = ttk.Label(self.root, text='Matrícula Provincial:')
        label_provincial.place(x=x_label, y=400)
        self.caja_provincial = ttk.Entry(self.root)
        self.caja_provincial.place(x=x_entry, y=400, width=150, height=25)

        label_telefono = ttk.Label(self.root, text='Nro Teléfono:')
        label_telefono.place(x=x_label, y=450)
        self.caja_telefono = ttk.Entry(self.root)
        self.caja_telefono.place(x=x_entry, y=450, width=150, height=25)

        label_email = ttk.Label(self.root, text='Email:')
        label_email.place(x=x_label, y=500)
        self.caja_email = ttk.Entry(self.root)
        self.caja_email.place(x=x_entry, y=500, width=150, height=25)

        boton_guardar = ttk.Button(self.root, text='Guardar', command = self.guardar)
        boton_guardar.place(x=x_label+40, y=550)
        boton_cerrar = ttk.Button(self.root, text='Cerrar', command = self.cerrar)
        boton_cerrar.place(x=x_entry+35, y=550)

        self.root.focus()
        self.root.grab_set()

    def cerrar(self):
        if messagebox.askokcancel(
                        title='Advertencia',
                        message='¿Confirma que desea abandonar la ventana?'
                        ):
            try:
                self.master.destroy()
            except:
                pass
        else:
            pass

    def guardar(self):
        apellido = self.caja_apellido.get()
        nombre = self.caja_nombre.get()
        try:
            dni = int(self.caja_dni.get())
        except ValueError:
            dni = 0
        titulo = self.caja_titulo.get()
        abreviatura = self.caja_abreviatura.get()
        try:
            matricula_nac = int(self.caja_nacional.get())
        except ValueError:
            matricula_nac = 0
        try:
            matricula_prov = int(self.caja_provincial.get())
        except ValueError:
            matricula_prov = 0
        try:
            telefono = int(self.caja_telefono.get())
        except ValueError:
            telefono = 0
        mail = self.caja_email.get()
        if len(apellido) == 0 or len(nombre) == 0 or dni == 0\
        or matricula_nac == 0 or matricula_prov == 0 or telefono == 0:
            messagebox.showwarning(
                        title='Advertencia',
                        message='Hay campos obligatorios que están vacíos'
                        )       
        else:
            self.query.guardar_perfil(dni, apellido, nombre, titulo, abreviatura,
                                    matricula_nac, matricula_prov, telefono, mail)
            messagebox.showinfo(
                                title="Datos Guardados",
                                message="Los datos se guardaron correctamente."
                                )
            self.root.destroy()
