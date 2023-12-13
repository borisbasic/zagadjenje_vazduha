import pyautogui
import os

lista_drzava = ['bih','crna_gora','hrvatska','makedonija','slovenija','srbija']
path_ = r'C:\Users\XXXX\OneDrive\zagadjenje_vazduha_slike\zagadjenje_vazduha_'
datum = str(datetime.date.today().strftime("%d.%m.%Y"))
new_path=''
for ld in lista_drzava:
    new_path = new_path + '"'+path_+ld+datum+'" '



