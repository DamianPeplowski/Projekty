definicje = {}
while(True):
    print('1: Dodaj definicję')
    print('2: Znajdz definicję')
    print('3: Usuń definicję')
    print('4: Zakończ')
    wybor = input("co chcesz zrobić?")
    if (wybor == '1'):
        klucz = input('Podaj klucz do zdefiniowania: ')
        definicja = input('Podaj definicję: ')
        definicje[klucz] = definicja
        print('Definicja dodana pomyślnie')
    elif (wybor == '2'):
        klucz = input('Czego szukasz?')
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print('Nie znaleziono definicji o nazwie', klucz)
    elif(wybor == '3'):
        klucz = input('Jaką definicję chcesz usunąć? ')
        if klucz in definicje:
            del definicje[klucz]
            print('Usunięto klucz o nazwie:',klucz)
        else:
            print('Nie znaleziono definicji o nazwie',klucz)
    elif(wybor == '4'):
        print('Żegnam')
        break
    else:
        print('Podałeś coś z poza zakresu')







