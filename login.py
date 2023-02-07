import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import messagebox
from estilos import Estilos
from PIL import ImageTk, Image
from win_secundaria import WinSecundaria

class Login(WinSecundaria, Estilos):
    def __init__(self, root, titulo, clave, master):
        super().__init__(root, titulo)
        self.clave = clave
        self.master = master
        self.root.resizable(0,0)
        self.imagen_psico = ImageTk.PhotoImage(Image.open('./imagenes/logo.png').resize((320, 270)))
        label_imagen = tk.Label(self.root, image=self.imagen_psico, background=self.color_principal, relief = 'flat')
        label_imagen.place(relx=0.5, rely=0.5, anchor=CENTER)
        etiqueta_titulo = ttk.Label(self.root, text='Mi consultorio', 
                    background = self.color_principal, 
                    font = self.letra_extra,
                    relief = 'flat'  
                    )
        etiqueta_titulo.place(x=350, y=140, anchor = CENTER, 
                    width=198, height=40)
        boton_salir = ttk.Button(self.root, text='Salir', command=self.salir)
        boton_salir.place(relx=0.85, y=560, width=85, height=25)
        etiqueta_pass = ttk.Label(self.root, text=" Contraseña:", font= 'Arial 10', 
                            background = self.color_principal,
                            relief = 'flat',
                            padding = 2)
        etiqueta_pass.place(x=220, y=500,  width=90, height=25)
        self.caja_pass = ttk.Entry(self.root, show='*')
        self.caja_pass.place(x=307, y=500, width=85, height=25)
        self.caja_pass.config(background='white')
        boton_ingresar = ttk.Button(self.root, text='Ingresar', command=self.ingresar)
        boton_ingresar.place(x=307, y=530, width=85, height=25)
        self.root.focus()
        self.root.grab_set()
        self.intentos = 0

    def ingresar(self):
        usuario = self.caja_pass.get()
        try:
            self.clave = str(self.clave)
        except:
            pass
        if usuario == self.clave:
            self.root.destroy()
        else:
            messagebox.showwarning(
                        title='Advertencia',
                        message='La contraseña ingresada es incorrecta'
                        )
            self.caja_pass.delete(0, tk.END)
            self.caja_pass.focus()
            self.intentos+=1
            if self.intentos == 3:
                messagebox.showwarning(
                        title='3 intentos fallidos de ingreso',
                        message='La aplicación se cerrará'
                        )
                try:
                    self.master.destroy()
                except:
                    pass
            
    def salir(self):
        if messagebox.askokcancel(
                        title='Advertencia',
                        message='¿Confirma que desea abandonar la aplicación?'
                        ):
            try:
                self.master.destroy()
            except:
                pass
        else:
            pass