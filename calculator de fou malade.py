from tkinter import *
from tkinter import ttk
import tkinter as tk

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
mainframe.grid()  # gére la geo


ttk.Button(window, text="1", ).grid(column=1, row=1)
ttk.Button(window, text="2", ).grid(column=2, row=1)
ttk.Button(window, text="3", ).grid(column=3, row=1)
ttk.Button(window, text="4", ).grid(column=1, row=3)
ttk.Button(window, text="5", ).grid(column=2, row=3)
ttk.Button(window, text="6", ).grid(column=3, row=3)
ttk.Button(window, text="7", ).grid(column=1, row=5)
ttk.Button(window, text="8", ).grid(column=2, row=5)
ttk.Button(window, text="9", ).grid(column=3, row=5)
ttk.Button(window, text="0", ).grid(column=2, row=10)
tk.Button(window, text="+").grid(column=4, row=3)
tk.Button(window, text="=").grid(column=4, row=5)


ttk.Button(window, text="calculate").grid(column=3, row=10) # créer un button avec marquer calculate dessus


window.mainloop()  # print la fenetre
