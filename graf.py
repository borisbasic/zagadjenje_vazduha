import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
lista_rezultata=[68,162,256,30,350,97,128,233,20,163]
lista_gradova=['Beograd', 'Banja Luka', 'Sarajevo', 'Novi Sad', 'Zagreb', 'Ljubljana', 'Podgorica', 'Split', 'Kragujevac', 'Zenica']
fig, ax = plt.subplots(figsize=(15,10))
for i in range(len(lista_rezultata)):
    if lista_rezultata[i]<50:
        color='#009966'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color, style='oblique', backgroundcolor='white')
    elif lista_rezultata[i]>=50 and lista_rezultata[i]<100:
        color='#FFD700'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    elif lista_rezultata[i]>=100 and lista_rezultata[i]<150:
        color='orange'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    elif lista_rezultata[i]>=150 and lista_rezultata[i]<200:
        color='red'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    elif lista_rezultata[i]>=200 and lista_rezultata[i]<300:
        color='#660099'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    else:
        color='#7e0023'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    ax.add_patch(Rectangle((-0.4+i, lista_rezultata[i]), 0.9, -lista_rezultata[i], facecolor=color, alpha=0.6, edgecolor='grey'))

ax.plot(lista_gradova, lista_rezultata,'black', linewidth=1)
ax.axis([-1,10,0,500])
ax.axhline(50,color='#009966',label='Dobar', alpha=0.6)
ax.axhline(100,color='#FFD700',label='Prihvatljiv', alpha=0.6)
ax.axhline(150,color='orange',label='Nezdrav za osjetljive osobe', alpha=0.6)
ax.axhline(200,color='red',label='Nezdrav', alpha=0.6)
ax.axhline(250,color='#660099',label='Vrlo nezdrav', alpha=0.6)
ax.axhline(300,color='#7e0023',label='Opasan po zdravlje', alpha=0.6)
ax.legend()
plt.title('Zagadjenje vazduha u regionu', fontsize=15)

plt.yticks([0,50,100,150,200,250,300,350,400,450,500])
plt.xlabel('Gradovi regiona', fontsize=15)
plt.ylabel('Zagadjenost vazduha', fontsize=15)
ax.set_facecolor('#e5e6e3')
ax.text(-0.9,490, 'zagadjenje_vazduha_region', color='gray', alpha=0.3)
plt.savefig('zagadjenje_vazduha.png')
plt.show()