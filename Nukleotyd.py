import random

def Nukleotyd(Macierz, Ilosc):
    Nukleotydy = []
    for i in range(0, Ilosc):
        Nukleotyd = ''
        for Linia in Macierz:
            Maks = Linia[0] + Linia[1] + Linia[2]
            Srednia = Linia[0] + Linia[1]
            Min = Linia[0]
            Los = random.randint(0, 100)/100
            if Los > (Maks) and Los < 1:
                Nukleotyd+='T'
            elif Los > Srednia and Los < Maks:
                Nukleotyd+='G'
            elif Los > Min and Los < Srednia:
                Nukleotyd+='C'
            else:
                Nukleotyd+='A'
        Nukleotydy.append(Nukleotyd)
    return Nukleotydy


if __name__ == '__main__':
    MacierzPrawdopodobienstwa =[
        [0.2, 0.4, 0.3, 0.1],
        [0.1, 0.6, 0.3, 0],
        [0.5, 0.3, 0.1, 0.1]
    ]
    Ilosc = 10

    Nukleotydy = Nukleotyd(MacierzPrawdopodobienstwa, Ilosc)
    Nukleotydy.sort()
    with open('Nukleotydy.txt', 'w') as plik:
        for Nukleotyd in Nukleotydy:
            print(Nukleotyd, file=plik)