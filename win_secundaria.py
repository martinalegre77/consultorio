
from tkinter import ttk
import tkinter
from estilos import Estilos

# Ventanas Secundarias

class WinSecundaria(Estilos):
    def __init__(self, master, titulo):
        super().__init__()
        self.master = master
        self.master = tkinter.Toplevel()
        self.master.iconbitmap('./iconos/icono.ico')
        self.master.title(titulo)
        self.master.config(width=700, height=600, background=self.color_principal)
        self.master.style = ttk.Style()
        self.master.style.configure("TLabel", foreground="gray15", 
                                        background = 'lightblue', 
                                        font = "Arial 11",
                                        relief = 'ridge',   
                                        bordercolor = 'black', 
                                        anchor = 5, 
                                        padding = 2, 
                                        width=20, 
                                        height=25)
