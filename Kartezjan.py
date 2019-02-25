import random
import matplotlib.pyplot as plot

def WspolrzedneKartezjanskie(k):
    """Funkcja zwraca wspolrzedne kartezjanskie wygenerowane funkcja random dla 
    jednego punktu w k-wymiarowej przestrzeni."""
    x = []  # Tworzenie pustej listy
    for n in range(0, k):  # Petla dzialajaca tyle razy ile zostalo podane wymiarow
        x.append(random.randint(-100, 100)/100)  # Dodanie wspolrzednej dla kazdego wymiaru
    return x  # Zwrot wspolrzednych


assert len(WspolrzedneKartezjanskie(2)) == 2, "Zla ilosc wymiarow!"
assert max(list(WspolrzedneKartezjanskie(2))) <= 1, "Zbyt duza wartosc wspolrzednej!"
assert min(list(WspolrzedneKartezjanskie(2))) >= -1, "Zbyt mala wartosc wspolrzednej!"

if __name__ == "__main__":
    Punkty = []
    IloscPunktow = 10
    k = int(input("Prosze podac ilosc wymiarow: "))  # Pobieranie ilosci wymiarow
    for i in range(0, IloscPunktow):  # Petla dzialajaca od 0 do ilosci punktow
        Punkty.append(WspolrzedneKartezjanskie(k))  # Dodanie do listy punktow wyloswanych przez funkcje
    print(Punkty)