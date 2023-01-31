
class Estilos:
    def __init__(self):
        self.color_principal = 'light cyan'
        self.color_secundario = 'lightcyan2'
        self.color_label = 'cyan3'
        self.letra_grande = 'Arial 14'
        self.letra_chica = 'Arial 11'
        self.letra_extra = 'Arial 20 italic'

    def valoresxy(self, root, wventana, hventana):
        wtotal = root.winfo_screenwidth()
        htotal = root.winfo_screenheight()
        vx = round(wtotal/2-wventana/2)
        vy = round(htotal/2-(hventana)/2)
        # return str(vx)+"+"+str(vy-30)
        return vx, vy