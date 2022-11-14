
import tkinter as tk
from tkinter import CENTER, ttk
from turtle import bgcolor
from PIL import ImageTk, Image
import conecciones
from estilos import Estilos
from perfil import Perfil

class WinMain(Estilos):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.geometry('1000x680')
        self.master.title('Mi Consultorio')
        self.master.iconbitmap('./iconos/icono.ico')
        
        # self.query = conecciones.Conexion()
  
        # Frames
        frame_principal = tk.Frame(master, bg = self.color_principal)
        frame_principal.place(relwidth=0.82, relheight=1, relx=0.18)
        barra_menu = tk.Frame(master, bg = self.color_secundario)
        barra_menu.place(relwidth=0.18, relheight=1)
        anillado = ImageTk.PhotoImage(Image.open('./imagenes/anillado.jpg').resize((50,660)))
        label_anillado = tk.Label(image=anillado, background=self.color_secundario, relief = 'flat')
        label_anillado.place_configure(x=1, y=15)

    def agregar_botones(self):
        pass

    def win_login(self):
        imagen_psico = ImageTk.PhotoImage(Image.open('./imagenes/logo.png').resize((300, 250)))
        label_imagen = ttk.Label(image=imagen_psico, background=self.color_principal, relief = 'flat')
        label_imagen.place(relx=0.6, rely=0.5, anchor=CENTER)

        etiqueta_principal = ttk.Label(text="Lic. Mariana Barrionuevo", 
                    background = self.color_principal, 
                    font = self.letra_extra, 
                    justify = 'center',
                    relief = 'flat'
                    )
        etiqueta_principal.place_configure(relx=0.6, y=50, anchor = CENTER, 
                                width=333, height=50)

        etiqueta_titulo = ttk.Label(text="Mi Consultorio", 
                    background = self.color_principal, 
                    font = self.letra_extra,
                    relief = 'flat'  
                    )
        etiqueta_titulo.place(relx=0.6, y=150, anchor = CENTER, 
                    width=198, height=50)

        etiqueta_pass = ttk.Label(text=" Contraseña", font= self.letra_chica, 
                            background = self.color_principal,
                            relief = 'flat',
                            padding = 2)
        etiqueta_pass.place(relx=0.547, y=550,  width=89, height=25)

        caja_pass = ttk.Entry()
        caja_pass.place(relx=0.55, y=580, width=85, height=25)
        caja_pass.config(background='white')

        boton_ingresar = ttk.Button(text='Ingresar')
        boton_ingresar.place(relx=0.55, y=620, width=85, height=25)


if __name__=="__main__":
    root = tk.Tk()
    app = WinMain(root)
    
query = conecciones.Conexion()
password = query.consultar('SELECT dni FROM perfil')
clave = password.fetchall()

if len(clave) == 0:
    first_login = Perfil('win_perfil', 'Configuración del Perfil')

login = app.win_login()


root.mainloop()

# root.destroy

# root.quit