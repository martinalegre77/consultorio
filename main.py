
import tkinter as tk
from tkinter import CENTER, ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from turtle import bgcolor
import conecciones
from estilos import Estilos
from perfil import Perfil


class WinMain(Estilos):
    def __init__(self, master):
        super().__init__()
        self.master = master
        # self.master.state('zoomed')
        self.master.geometry('1280x720')
        self.master.title('Mi Consultorio')
        self.master.iconbitmap('./iconos/icono.ico')
        self.query = conecciones.Conexion()
        self.anillado = ImageTk.PhotoImage(Image.open('./imagenes/anillado.png').resize((50,615)))
        self.imagen_psico = ImageTk.PhotoImage(Image.open('./imagenes/logo.png').resize((320, 270)))
  
        # Frames
        frame_principal = tk.Frame(master, bg = self.color_principal)
        frame_principal.place(relwidth=0.82, relheight=1, relx=0.18)
        barra_menu = tk.Frame(master, bg = self.color_secundario)
        barra_menu.place(relwidth=0.18, relheight=1)
        label_anillado = tk.Label(master, image=self.anillado, background=self.color_secundario, relief = 'flat')
        label_anillado.place_configure(x=0, y=15)

    def win_login(self):
        label_imagen = tk.Label(root, image=self.imagen_psico, background=self.color_principal, relief = 'flat')
        label_imagen.place(relx=0.57, rely=0.5, anchor=CENTER)

        etiqueta_titulo = ttk.Label(text="Mi Consultorio", 
                    background = self.color_principal, 
                    font = self.letra_extra,
                    relief = 'flat'  
                    )
        etiqueta_titulo.place(x=600, y=140, anchor = CENTER, 
                    width=198, height=50)

        boton_salir = ttk.Button(text='Salir', command=self.salir)
        boton_salir.place(relx=0.85, y=660, width=85, height=25)

        etiqueta_pass = ttk.Label(text=" Contraseña:", font= 'Arial 10', 
                            background = self.color_principal,
                            relief = 'flat',
                            padding = 2)
        etiqueta_pass.place(x=590, y=620,  width=89, height=25)

        caja_pass = ttk.Entry()
        caja_pass.place(x=680, y=620, width=85, height=25)
        caja_pass.config(background='white')

        boton_ingresar = ttk.Button(text='Ingresar')
        boton_ingresar.place(x=780, y=620, width=85, height=25)

    def cargar_widgets(self):
        etiqueta_principal = ttk.Label(text="Lic. Mariana Barrionuevo", 
                    background = self.color_principal, 
                    font = self.letra_extra, 
                    justify = 'center',
                    relief = 'flat'
                    )
        etiqueta_principal.place_configure(relx=0.6, y=50, anchor = CENTER, 
                                width=333, height=50)

        

    def salir(self):
        if messagebox.askokcancel(
                        title='Advertencia',
                        message='¿Confirma que desea cerrar la aplicación?'
                        ):
            root.destroy()
        else:
            pass   


if __name__=="__main__":
    root = tk.Tk()
    app = WinMain(root)
    
query = conecciones.Conexion()
login = app.win_login()
password = query.consultar_pass()
respuesta = password.fetchall()
clave = respuesta[0][0]

if clave < 1000:
    first_login = Perfil('win_perfil', 'Configuración del Perfil')
else:
    pass






root.mainloop()

# root.destroy

# root.quit