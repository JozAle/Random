from Kartezjan import WspolrzedneKartezjanskie
from Biegun import WspolrzedneBiegunowe
from Nukleotyd import Nukleotyd
import matplotlib.pyplot as plot
import numpy

Punkty = []
PunktyKartezjanskie = []
PunktyBiegunowe = []
IloscPunktow = 500
k = int(input("Prosze podac ilosc wymiarow: "))  # Pobieranie ilosci wymiarow
for i in range(0, IloscPunktow):  # Petla dzialajaca od 0 do ilosci punktow
    Punkty.append(WspolrzedneKartezjanskie(k))  # Dodanie do listy punktow wyloswanych przez funkcje

if k == 2:  # W przypadku gdy mamy 2 wymiary
    xw, yw, xp, yp = [], [], [], []
    for Punkt in Punkty:  # Dla kazdego punktu
        if float(Punkt[0]) * float(Punkt[0]) + float(Punkt[1]) * float(Punkt[1]) <= 1:  # Sprawdza czy punkt znajduje
            # sie 1 jednostke od punktu 0,0
            xw.append(Punkt[0])
            yw.append(Punkt[1])  # jesli tak dodaje wspolrzedne do listy punktow wewnetrznych
        else:
            xp.append(Punkt[0])
            yp.append(Punkt[1])  # jesli nie dodaje do listy punkto zewnetrznych
    plot.plot(xw, yw, 'bo')  # rysuje punkty wewnetrzne jako niebieskie kropki
    plot.plot(xp, yp, 'ro')  # rysuje punkty wewnetrzne jako czerwone kropki
    plot.savefig('WykresKartezjanski.pdf')  # Zapisuje wynik do pliku
    plot.close()

for i in range(0, IloscPunktow):  # Petla dzialajaca od 0 do ilosci punktow
    PunktyBiegunowe.append(WspolrzedneBiegunowe())  # Dodanie do listy punktow wyloswanych przez funkcje

for PunktBiegunowy in PunktyBiegunowe:  # Dla kazdego punktu
    Punkt = [PunktBiegunowy[0] * numpy.cos(PunktBiegunowy[1]), PunktBiegunowy[0] * numpy.sin(PunktBiegunowy[1])]
    # Zmiana wspolrzednych biegunowych na kartezjanskie
    PunktyKartezjanskie.append(Punkt)  # Dodanie zmienionych punktow do listy

xw, yw, xp, yp = [], [], [], []
for Punkt in PunktyKartezjanskie:
    if float(Punkt[0]) * float(Punkt[0]) + float(Punkt[1]) * float(Punkt[1]) <= 1:  # Sprawdza czy punkt znajduje
        # sie 1 jednostke od punktu 0,0
        xw.append(Punkt[0])
        yw.append(Punkt[1])  # jesli tak dodaje wspolrzedne do listy punktow wewnetrznych
    else:
        xp.append(Punkt[0])
        yp.append(Punkt[1])  # jesli nie dodaje do listy punkto zewnetrznych
plot.plot(xw, yw, 'bo')  # rysuje punkty wewnetrzne jako niebieskie kropki
plot.plot(xp, yp, 'ro')  # rysuje punkty wewnetrzne jako czerwone kropki
plot.savefig('WykresBiegunowy.pdf')  # Zapisuje wynik do pliku
plot.close()

MacierzPrawdopodobienstwa =[
    [0.2, 0.4, 0.3, 0.1],
    [0.1, 0.6, 0.3, 0],
    [0.5, 0.3, 0.1, 0.1],
    [0.1, 0.3, 0.5, 0.1],
    [0.1, 0.1, 0.6, 0.2],
    [0.4, 0.4, 0.1, 0.1],
    [0.2, 0, 0.2, 0.6],
    [0.7, 0.2, 0.1, 0]]
Ilosc = 1000

Nukleotydy = Nukleotyd(MacierzPrawdopodobienstwa, Ilosc)
Nukleotydy.sort()
with open('Nukleotydy.txt', 'w') as plik:
    for Nukleotyd in Nukleotydy:
        print(Nukleotyd, file=plik)
