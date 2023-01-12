import tkinter as tk
from tkinter import CENTER, ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from turtle import bgcolor
import conecciones
from estilos import Estilos
from login import Login
from perfil import Perfil

class WinMain(Estilos):
    def __init__(self, root):
        super().__init__()
        self.root = root
        root.resizable(0,0)

        wtotal = root.winfo_screenwidth()
        htotal = root.winfo_screenheight()
        wventana = 900
        hventana = 630
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-(hventana)/2)
        
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight-30))
        

        self.root.title('Mi Consultorio')
        self.root.iconbitmap('./iconos/icono.ico')
        self.query = conecciones.Conexion()
        self.anillado = ImageTk.PhotoImage(Image.open('./imagenes/anillado.png').resize((50,600)))
        # self.imagen_psico = ImageTk.PhotoImage(Image.open('./imagenes/logo.png').resize((320, 270)))
        # Frames
        frame_principal = tk.Frame(root, bg = self.color_principal)
        frame_principal.place(relwidth=0.82, relheight=1, relx=0.18)
        barra_menu = tk.Frame(root, bg = self.color_secundario)
        barra_menu.place(relwidth=0.18, relheight=1)
        label_anillado = tk.Label(root, image=self.anillado, background=self.color_secundario, relief = 'flat')
        label_anillado.place_configure(x=0, y=15)
        # Botones
        boton_salir = ttk.Button(root, text='Salir', command=self.salir)
        boton_salir.place(relx=0.85, y=560, width=85, height=25)
        boton_ingresar = ttk.Button(root, text='Ingresar', command=self.ingresar)
        boton_ingresar.place(x=307, y=530, width=85, height=25)

    def ingresar(self):
        login = Login('win_login', 'Mi Consultorio')   

    def salir(self):
        if messagebox.askokcancel(
                        title='Advertencia',
                        message='¿Confirma que desea salir de la aplicación?'
                        ):
            root.destroy()
        else:
            pass

    def cargar_widgets(self):
        etiqueta_principal = ttk.Label(text="Lic. Mariana Barrionuevo", 
                    background = self.color_principal, 
                    font = self.letra_extra, 
                    justify = 'center',
                    relief = 'flat'
                    )
        etiqueta_principal.place_configure(relx=0.6, y=50, anchor = CENTER, 
                                width=333, height=50)

if __name__=="__main__":
    root = tk.Tk()
    app = WinMain(root)
    
query = conecciones.Conexion()
password = query.consultar_pass()
respuesta = password.fetchall()

if respuesta == []:
    first_login = Perfil('win_perfil', 'Configuración del Perfil')
else:
    clave = respuesta[0][0]
    if clave < 1000:
        first_login = Perfil('win_perfil', 'Configuración del Perfil')
    else:
        login = Login('win_login', 'Mi Consultorio')



root.mainloop()

# root.destroy
# root.quit