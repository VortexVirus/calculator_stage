from tkinter import *
from tkinter import ttk


def calculatorPlus(chiffre, plus):
    chiffre_float = float(chiffre)
    plus_float = float(plus)
    result = chiffre_float + plus_float
    return(result)

def calculatorMoin(chiffre, moin):
    chiffre_float = float(chiffre)
    moin_float = float(moin)
    resultat = chiffre_float - moin_float
    return(resultat)

def calculatorTimes(chiffre, time):
    chiffre_float = float(chiffre)
    time_float = float(time)
    resultat = chiffre_float - time_float
    return(resultat)

def calculatorDivide(chiffre, divisor):
    chiffre_float = float(chiffre)
    divisor_float = float(divisor)
    result = chiffre_float / divisor_float
    return(result)



window = Tk() #créer le truc
window.title("calculatrice") # donne le nom de la fenetre

mainframe = ttk.Frame(window, padding=(30)) # créer une frame pour placer des choses dedans
mainframe.grid(column=0, row=0)  # gére la geo

ttk.Button(window, text="calculate").grid(column=1, row=1) # créer un button avec marquer calculate dessus


window.mainloop()  # print la fenetre
