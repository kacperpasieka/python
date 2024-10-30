lista = [] #array
def opcje ():
    opcja = int(input("Wybierz opcje: \n[1] Dodaj Liczy [2] Wyswietl Liste [3] Lista od tylu [4] Posortowana lista [5] Usun pierwsza wystepujaca liczbe [6] Usun wpis o podanym indeksie [7] Ilość wystąpien plus indeks [8] Wybierz z listy element od indeksu i do j [9] Zakończ\n"))
                
    match opcja:
        case 1:
            # Wprowadzanie liczby
            for i in range(5000):
                try:
                    liczba = input("Wprowadz liczbe, ktora chcesz dodać, wpisz 'x', żeby przerwać\n")
                    if liczba == "x":
                        print("Zakończono wprowadzanie liczb")
                        break;
                    fliczba = float(liczba)
                    lista.append(fliczba)

                    continue;
                except ValueError:
                    print("Nie podałeś cyfry")
                    return 0;
            opcje()
        case 2: 
            # Wyświetlanie listy
            print("Wyświetlanie listy z indeksami")
            for i, elem in enumerate(lista):
                print(f"{i+1}: {elem}")
            opcje()

        case 3:
            # Lista od tyłu
            print("Lista od tyłu:")
            print(lista[::-1])
            opcje()

        case 4:
            # Sortowanie listy
            print(sorted(lista))
            opcje()
        case 5:
            for i in range(5000):
                element_do_usuniecia = float(input("Podaj liczbe, której chcesz usunąć pierwszy występujący rekord\n"))
                if element_do_usuniecia in lista:
                    lista.remove(element_do_usuniecia)
                    print(f"Usunięto {element_do_usuniecia} z listy")
                    opcje()
                else:
                    print("Nie ma takiej wartośći w liczbie")
                    opcje()
        case 6:
            for i in range(5000):
                try:
                    indeks_do_usuniecia = int(input("\nPodaj indeks elementu do usunięcia: "))
                    usuniety_element = lista.pop(indeks_do_usuniecia)
                    print(f"Usunięto element '{usuniety_element}' z indeksu {indeks_do_usuniecia}.")
                    print("Lista po usunięciu elementu:", lista)
                    break;
                except ValueError:
                    print("Podano nieprawidłową wartość indeksu.")
                    continue;
                except IndexError:
                    print("Podany indeks jest poza zakresem listy.")
                    continue;
            opcje()
        case 7:
            for i in range(5000):
                element_do_znalezienia = float(input("\nPodaj element, aby sprawdzić ilość wystąpień i pierwszy indeks: ")) 
                ilosc_wystapien = lista.count(element_do_znalezienia)
                if ilosc_wystapien > 0:
                    pierwszy_indeks = lista.index(element_do_znalezienia)
                    print(f"Element {element_do_znalezienia} występuje {ilosc_wystapien} razy, pierwszy indeks: {pierwszy_indeks}")
                    break;
                else:
                    print(f"Element {element_do_znalezienia} nie występuje na liście.")
                    continue;
            opcje()
        case 8:
            for i in range(5000):
                try:
                    i = int(input("\nPodaj indeks początkowy (i): ")) 
                    j = int(input("Podaj indeks końcowy (j): ")) 
                    wycinek = lista[i:j]
                    print("Wybrane elementy między indeksami i oraz j:", wycinek)
                    break;
                except ValueError:
                    print("Podano nieprawidłową wartość indeksów.")
                    continue;
                except IndexError:
                    print("Podane indeksy są poza zakresem listy.")
                    continue;
            opcje()
        case 9:
            return 0;


opcje()
