import random
import numpy
import matplotlib.pyplot as plot


def WspolrzedneBiegunowe():
    """Funkcja zwraca wspolrzedne biegunowe wygenerowane funkcja random dla
    jednego punktu w 2-wymiarowej przestrzeni."""
    Punkt = []  # Tworzy pusta liste
    r = random.randint(0, 100)/100  # Losuje dlugosc od 0 do 1 z dokladnoscia do setnych miejsc po przecinku
    k = random.randint(0, 360)  # Losuje kat
    Punkt.append(r)
    Punkt.append(k)
    return Punkt  # Zwraca wspolrzedne


assert max(list(WspolrzedneBiegunowe())) <= 360, "Zbyt duza wartosc kata!"
assert max(list(WspolrzedneBiegunowe())) >= 0, "Zbyt mala wartosc kata!"
assert min(list(WspolrzedneBiegunowe())) >= 0, "Zbyt mala wartosc odleglosci!"
assert min(list(WspolrzedneBiegunowe())) <= 1, "Zbyt duza wartosc odleglosci!"

if __name__ == "__main__":
    PunktyKartezjanskie = []
    PunktyBiegunowe = []
    IloscPunktow = 50
    for i in range(0, IloscPunktow):  # Petla dzialajaca od 0 do ilosci punktow
        PunktyBiegunowe.append(WspolrzedneBiegunowe())  # Dodanie do listy punktow wyloswanych przez funkcje
    print(PunktyBiegunowe)