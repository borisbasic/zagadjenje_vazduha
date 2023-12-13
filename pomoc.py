import pandas as pd

lista_gradova = ['Beograd','Subotica','Čačak','Kraljevo','Zaječar']
l=[]
rjecnik={}
for i in range(len(lista_gradova)):
    rjecnik[lista_gradova[i]]=[]
    l=[]
dejta_frejm = pd.DataFrame.from_dict(rjecnik)
dejta_frejm.to_csv('zagadjenje_vazduha_srbija.csv', index=None)
print("Boris")

