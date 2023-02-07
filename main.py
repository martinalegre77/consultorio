import tkinter as tk
from tkinter import CENTER
from PIL import ImageTk, Image
from tkinter import messagebox
# from turtle import bgcolor
from botones import * 
import conecciones
from estilos import Estilos
from login import Login
from perfil import Perfil

class WinMain(Estilos):
    def __init__(self, root):
        super().__init__()
        self.root = root
        root.resizable(0,0)
        wventana = 900
        hventana = 630
        vx, vy = self.valoresxy(self.root, wventana, hventana)
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(vx)+"+"+str(vy-30))
        self.root.title('Mi Consultorio')
        self.root.iconbitmap('./iconos/favicon.ico')
        self.query = conecciones.Conexion()
        self.anillado = ImageTk.PhotoImage(Image.open('./imagenes/anillado.png').resize((50,600)))
        # Frames
        frame_principal = tk.Frame(root, bg = self.color_principal)
        frame_principal.place(relwidth=0.82, relheight=1, relx=0.18)
        barra_menu = tk.Frame(root, bg = self.color_secundario)
        barra_menu.place(relwidth=0.22, relheight=1)
        label_anillado = ttk.Label(root, image=self.anillado, background=self.color_secundario, relief = 'flat')
        label_anillado.place_configure(x=0, y=15)
        # Botones
        self.boton_ingresar = ttk.Button(root, text='Ingresar', command=self.ingresar, cursor='hand2')
        self.boton_ingresar.place(relx=.85, y=555, width=85, height=25)
        boton_salir = ttk.Button(root, text='Salir', command=self.salir, cursor='hand2')
        boton_salir.place(relx=.85, y=585, width=85, height=25)

        # LOGUEO
        acceso = self.ver_pass()
        self.clave = 0
        if acceso == []:
            first_login = Perfil('win_perfil', 'Configuración del Perfil', self.root)
        else:
            self.clave = acceso[0][0]
            self.ingresar()

        self.cargar_widgets()

    def ver_pass(self):
        query = conecciones.Conexion()
        password = query.consultar_pass()
        respuesta = password.fetchall()
        return respuesta

    def ingresar(self):
        login = Login('win_login', 'Mi Consultorio', self.clave, self.root)

    def perfil(self):
        edit_perfil = Perfil('win_perfil', 'Modificar Datos del Perfil', self.root)

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
                    relief = 'flat',
                    )
        etiqueta_principal.place_configure(relx=0.6, y=75, anchor = CENTER, 
                                width=333, height=50)
        self.imagen_psico = ImageTk.PhotoImage(Image.open('./imagenes/logo.png').resize((320, 270)))
        label_imagen = ttk.Label(self.root, image=self.imagen_psico, background=self.color_principal, relief = 'flat')
        label_imagen.place(relx=0.6, rely=0.5, anchor=CENTER)
        self.boton_ingresar.destroy()
        #Botones - Menú
        btn_agenda = ttk.Button(root, text='AGENDA', command=self.agenda, cursor='hand2')
        btn_agenda.place(x=75, y=50, width=110, height=30)
        btn_paciente = ttk.Button(root, text='PACIENTES', command=self.pacientes, cursor='hand2')
        btn_paciente.place(x=75, y=120, width=110, height=30)
        btn_obras_soc = ttk.Button(root, text='OBRAS SOCIALES', command=self.osociales, cursor='hand2')
        btn_obras_soc.place(x=75, y=190, width=110, height=30)
        btn_consultorio = ttk.Button(root , text='CONSULTORIOS', command=self.consultorios, cursor='hand2')
        btn_consultorio.place(x=75, y=260, width=110, height=30)
        btn_cobro = ttk.Button(root, text='COBROS', command=self.cobros, cursor='hand2')
        btn_cobro.place(x=75, y=330, width=110, height=30)
        btn_turno = ttk.Button(root, text='TURNOS', command=self.turnos, cursor='hand2')
        btn_turno.place(x=75, y=400, width=110, height=30)
        btn_perfil = ttk.Button(root, text='PERFIL', command=self.perfil, cursor='hand2')
        btn_perfil.place(x=75, y=515, width=110, height=30)
        btn_contrasena = ttk.Button(root, text='MODIFICAR PASS')
        btn_contrasena.place(x=75, y=585, width=110, height=30)

    def agenda(self):
        frame_agenda = Agenda('win_botones', 'Agenda')

    def pacientes(self):
        frame_pacientes = Pacientes('win_botones', 'Pacientes')

    def osociales(self):
        frame_osociales = Osociales('win_botones', 'O. Sociales')

    def consultorios(self):
        frame_consultorios = Consultorios('win_botones', 'Consultorios')

    def cobros(self):
        frame_cobros = Cobros('win_botones', 'Cobros')

    def turnos(self):
        frame_turnos = Turnos('win_botones', 'Turnos')

if __name__=="__main__":
    root = tk.Tk()
    app = WinMain(root)
    
# query = conecciones.Conexion()
# password = query.consultar_pass()

# respuesta = password.fetchall()

# if respuesta == []:
#     first_login = Perfil('win_perfil', 'Configuración del Perfil')
# else:
#     clave = respuesta[0][0]
#     if clave < 100000:
#         first_login = Perfil('win_perfil', 'Configuración del Perfil')
#     else:
#         login = Login('win_login', 'Mi Consultorio', clave)

root.mainloop()