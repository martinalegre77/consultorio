# Código para personalizar el calendario:

import calendar
from datetime import datetime

def print_calendario(a,m):
    meses = ("ene", "feb", "mar", "abr", "may", "jun","jul", "ago", "sep", "oct", "nov", "dic")
    semana = ("lun", "mar", "mié", "jue", "vie", "sab", "dom")
    try:
        fecha=datetime(a,m,1)
    except ValueError:
        fecha=datetime.now()
    calendario=calendar.Calendar()
    mes=calendario.monthdays2calendar(fecha.year,fecha.month)
    print("Calendario: ",fecha.year,meses[fecha.month-1])
    for dia in semana:
        print("%3s"%dia,end=" ")
    print()
    for s in mes:
        for d in s:
            if d[0]!=0:
                print("%3d"%d[0],end=" ")
            else:
                print("%3s"%" ",end=" ")
        print()

def main():
 print_calendario(2022,6)
 
if __name__=="__main__":
    main()