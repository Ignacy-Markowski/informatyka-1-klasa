print("=== ZADANIA Z LISTAMI (wersja z while i break) ===")
print()

# ---------- 1. Utworz pusta liste o nazwie numbers ----------
numbers = []
print(f"Zadanie 1: utworzylem pusta liste numbers = {numbers}")
print()

# ---------- 2. Popros uzytkownika o 5 liczb i dodaj je do listy ----------
print("Zadanie 2: podaj 5 liczb calkowitych.")
while True:
    liczba = int(input(f"Podaj liczbe nr {len(numbers) + 1}: "))
    numbers.append(liczba)
    if len(numbers) == 5:
        break
print(f"Lista numbers = {numbers}")
print()

# ---------- 3. Oblicz sume liczb w liscie ----------
suma = 0
i = 0
while i < len(numbers):
    suma = suma + numbers[i]
    i = i + 1
print(f"Zadanie 3: suma liczb = {suma}")
print()

# ---------- 4. Znajdz najwieksza liczbe ----------
najwieksza = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > najwieksza:
        najwieksza = numbers[i]
    i = i + 1
print(f"Zadanie 4: najwieksza liczba = {najwieksza}")
print()

# ---------- 5. Znajdz najmniejsza liczbe ----------
najmniejsza = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] < najmniejsza:
        najmniejsza = numbers[i]
    i = i + 1
print(f"Zadanie 5: najmniejsza liczba = {najmniejsza}")
print()

# ---------- 6. Znajdz srednia arytmetyczna ----------
srednia = suma / len(numbers)
print(f"Zadanie 6: srednia arytmetyczna = {srednia:.2f}")
print()

# ---------- 7. Znajdz ilosc liczb parzystych ----------
ile_parzystych = 0
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        ile_parzystych = ile_parzystych + 1
    i = i + 1
print(f"Zadanie 7: liczb parzystych jest {ile_parzystych}")
print()

# ---------- 8. Stworz liste duplicates z powtarzajacymi sie elementami ----------
duplicates = []
i = 0
while i < len(numbers):
    # policz, ile razy numbers[i] wystepuje w calej liscie
    ile_razy = 0
    j = 0
    while j < len(numbers):
        if numbers[j] == numbers[i]:
            ile_razy = ile_razy + 1
        j = j + 1

    # sprawdz, czy ta liczba juz trafila do duplicates
    juz_jest = False
    k = 0
    while k < len(duplicates):
        if duplicates[k] == numbers[i]:
            juz_jest = True
            break
        k = k + 1

    if ile_razy > 1 and juz_jest == False:
        duplicates.append(numbers[i])
    i = i + 1
print(f"Zadanie 8: duplicates = {duplicates}")
print()

# ---------- 9. Usun wszystkie powtarzajace sie elementy z numbers ----------
bez_powtorzen = []
i = 0
while i < len(numbers):
    # sprawdz, czy ta liczba juz jest w nowej liscie
    juz_jest = False
    k = 0
    while k < len(bez_powtorzen):
        if bez_powtorzen[k] == numbers[i]:
            juz_jest = True
            break
        k = k + 1

    if juz_jest == False:
        bez_powtorzen.append(numbers[i])
    i = i + 1
numbers = bez_powtorzen
print(f"Zadanie 9: numbers bez powtorzen = {numbers}")
print()

# ---------- 10. Stworz liste squares z kwadratami liczb z numbers ----------
squares = []
i = 0
while i < len(numbers):
    squares.append(numbers[i] ** 2)
    i = i + 1
print(f"Zadanie 10: squares = {squares}")
print()

print("Koniec programu.")
