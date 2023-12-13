import pandas as pd

import schedule


import datetime
def nes():
    lista_rezultata=[68,102,46,55,61,97,8,3,20,163]
    lista_gradova=['Beograd', 'Banja Luka', 'Sarajevo', 'Novi Sad', 'Zagreb', 'Ljubljana', 'Podgorica', 'Split', 'Kragujevac', 'Zenica']
    l=[]
    rjecnik={}
    for i in range(len(lista_gradova)):
        rjecnik[lista_gradova[i]]=[]
        l=[]
    dejta_frejm = pd.DataFrame.from_dict(rjecnik)
    dejta_frejm2 = pd.DataFrame.from_dict(rjecnik)
    dejta_frejm3 = pd.concat([dejta_frejm2,dejta_frejm])
    dejta_frejm.to_csv('zagadjenje_vazduha.csv', index=None)
    print("Boris")

#schedule.every().day.at('21:44').do(nes)
#while True:
   # schedule.run_pending()