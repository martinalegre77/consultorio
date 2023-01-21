import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import messagebox
from estilos import Estilos
from PIL import ImageTk, Image
from win_secundaria import WinSecundaria

class Login(WinSecundaria, Estilos):
    def __init__(self, root, titulo):
        super().__init__(root, titulo)
        # self.master = master
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
        caja_pass = ttk.Entry(self.root, show='*')
        caja_pass.place(x=307, y=500, width=85, height=25)
        caja_pass.config(background='white')
        boton_ingresar = ttk.Button(self.root, text='Ingresar', command=self.ingresar)
        boton_ingresar.place(x=307, y=530, width=85, height=25)
        self.root.focus()
        self.root.grab_set()

    def ingresar(self):
        print('Ingresando')   

    def salir(self):
        if messagebox.askokcancel(
                        title='Advertencia',
                        message='¿Confirma que desea salir de la ventana?'
                        ):
            self.root.destroy()
        else:
            pass