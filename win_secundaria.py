from tkinter import ttk
import tkinter
from estilos import Estilos

# Ventanas Secundarias

class WinSecundaria(Estilos):
    def __init__(self, root, titulo):
        super().__init__()
        self.root = root
        self.root = tkinter.Toplevel()
        self.root.iconbitmap('./iconos/ico2.ico')
        self.root.title(titulo)
        self.root.config(width=700, height=600, background=self.color_principal)
        self.root.style = ttk.Style()
        self.root.style.configure("TLabel", foreground="gray15", 
                                        background = 'lightblue', 
                                        font = "Arial 11",
                                        relief = 'ridge',   
                                        bordercolor = 'black', 
                                        anchor = 5, 
                                        padding = 2, 
                                        width=20, 
                                        height=25)      
        self.root.geometry("+300+30")