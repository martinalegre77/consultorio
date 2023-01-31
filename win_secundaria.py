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
        self.root.config(background=self.color_principal)
        self.root.style = ttk.Style()
        self.root.style.configure("TLabel", foreground="gray15", 
                                        font = "Arial 11",
                                        relief = 'ridge',   
                                        bordercolor = 'black', 
                                        anchor = 5, 
                                        padding = 2, 
                                        width=20, 
                                        height=25)      
        wventana = 700
        hventana = 600
        vx, vy = self.valoresxy(self.root, wventana, hventana)
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(vx+50)+"+"+str(vy-20))