import math

print("Liczymy pole kwadratu.")
a = float(input("Podaj dlugosc boku a: "))
pole = a * a
print(f"Dla kwadratu o boku {a} pole to {pole:.2f}")
print()

print("Liczymy pole prostokata.")
a = float(input("Podaj dlugosc boku a: "))
b = float(input("Podaj dlugosc boku b: "))
pole = a * b
print(f"Dla prostokata o bokach {a} i {b} pole to {pole:.2f}")
print()

print("Liczymy pole trojkata.")
a = float(input("Podaj dlugosc podstawy a: "))
h = float(input("Podaj wysokosc h opuszczona na te podstawe: "))
pole = (a * h) / 2
print(f"Dla trojkata o podstawie {a} i wysokosci {h} pole to {pole:.2f}")
print()

print("Liczymy pole kola.")
r = float(input("Podaj dlugosc promienia r: "))
pole = math.pi * r ** 2
print(f"Dla kola o promieniu {r} pole to {pole:.2f}")
print()

print("Liczymy pole trapezu.")
a = float(input("Podaj dlugosc dluzszej podstawy a: "))
b = float(input("Podaj dlugosc krotszej podstawy b: "))
h = float(input("Podaj wysokosc h: "))
pole = ((a + b) * h) / 2
print(f"Dla trapezu o podstawach {a} i {b} oraz wysokosci {h} pole to {pole:.2f}")
print()

print("To wszystkie 5 figur. Koniec programu.")
