# Program do pracy z listą liczb

# Pobranie ilości liczb i samych liczb od użytkownika
n = int(input("Podaj liczbę elementów, które chcesz dodać do listy: "))
lista = []

for i in range(n):
    liczba = float(input(f"Podaj liczbę {i+1}: "))
    lista.append(liczba)

# Wydruk elementów listy i ich indeksów
print("\nElementy listy i ich indeksy:")
for idx, elem in enumerate(lista):
    print(f"Indeks {idx}: {elem}")

# Wydruk elementów w odwrotnej kolejności
print("\nElementy listy w odwrotnej kolejności:")
print(lista[::-1])

# Wydruk posortowanych elementów
print("\nPosortowane elementy listy:")
print(sorted(lista))

# Usunięcie pierwszego wystąpienia elementu podanego przez użytkownika
for i in range(5000):
    element_do_usuniecia = float(input("\nPodaj element do usunięcia (pierwsze wystąpienie): "))
    if element_do_usuniecia in lista:
        lista.remove(element_do_usuniecia)
        print("Lista po usunięciu elementu:", lista)
        break;
    else:
        print("Element nie znajduje się na liście.")
        continue;

# Usunięcie elementu na podstawie podanego indeksu
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

# Ilość wystąpień i indeks pierwszego wystąpienia podanego elementu
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

# Wybór elementów od indeksu i do j
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