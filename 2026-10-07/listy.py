print("=== ZADANIA Z LISTAMI ===")
print()

# ---------- 1. Utworz pusta liste o nazwie numbers ----------
numbers = []
print(f"Zadanie 1: utworzylem pusta liste numbers = {numbers}")
print()

# ---------- 2. Popros uzytkownika o 5 liczb i dodaj je do listy ----------
print("Zadanie 2: podaj 5 liczb calkowitych.")
for i in range(5):
    liczba = int(input(f"Podaj liczbe nr {i + 1}: "))
    numbers.append(liczba)
print(f"Lista numbers = {numbers}")
print()

# ---------- 3. Oblicz sume liczb w liscie ----------
suma = sum(numbers)
print(f"Zadanie 3: suma liczb = {suma}")
print()

# ---------- 4. Znajdz najwieksza liczbe ----------
najwieksza = max(numbers)
print(f"Zadanie 4: najwieksza liczba = {najwieksza}")
print()

# ---------- 5. Znajdz najmniejsza liczbe ----------
najmniejsza = min(numbers)
print(f"Zadanie 5: najmniejsza liczba = {najmniejsza}")
print()

# ---------- 6. Znajdz srednia arytmetyczna ----------
srednia = suma / len(numbers)
print(f"Zadanie 6: srednia arytmetyczna = {srednia:.2f}")
print()

# ---------- 7. Znajdz ilosc liczb parzystych ----------
ile_parzystych = 0
for liczba in numbers:
    if liczba % 2 == 0:
        ile_parzystych = ile_parzystych + 1
print(f"Zadanie 7: liczb parzystych jest {ile_parzystych}")
print()

# ---------- 8. Stworz liste duplicates z powtarzajacymi sie elementami ----------
duplicates = []
for liczba in numbers:
    if numbers.count(liczba) > 1 and liczba not in duplicates:
        duplicates.append(liczba)
print(f"Zadanie 8: duplicates = {duplicates}")
print()

# ---------- 9. Usun wszystkie powtarzajace sie elementy z numbers ----------
bez_powtorzen = []
for liczba in numbers:
    if liczba not in bez_powtorzen:
        bez_powtorzen.append(liczba)
numbers = bez_powtorzen
print(f"Zadanie 9: numbers bez powtorzen = {numbers}")
print()

# ---------- 10. Stworz liste squares z kwadratami liczb z numbers ----------
squares = []
for liczba in numbers:
    squares.append(liczba ** 2)
print(f"Zadanie 10: squares = {squares}")
print()

print("Koniec programu.")
