import math

print("=== KALKULATOR FIGUR I BRYL ===")
print()

# ---------- POZIOM 1: figury plaskie, bryly czy inne wzory ----------
print("Co chcesz policzyc?")
print("1 - figury plaskie")
print("2 - bryly")
print("3 - inne wzory")
kategoria = input("Twoj wybor: ").strip()
print()

if kategoria == "1":
    # ===================== FIGURY PLASKIE =====================
    print("Co obliczyc?")
    print("1 - obwod")
    print("2 - pole")
    dzialanie = input("Twoj wybor: ").strip()
    print()

    if dzialanie == "1":
        # ---------- OBWODY ----------
        print("Jaka figura?")
        print("1 - kwadrat")
        print("2 - prostokat")
        print("3 - rownoleglobok")
        print("4 - romb")
        print("5 - trojkat")
        print("6 - trojkat rownoboczny")
        print("7 - trapez")
        print("8 - kolo")
        figura = input("Twoj wybor: ").strip()
        print()

        if figura == "1":
            a = float(input("Podaj bok a: "))
            obwod = 4 * a
            print(f"Obwod kwadratu o boku {a} wynosi {obwod:.2f}")
        elif figura == "2":
            a = float(input("Podaj bok a: "))
            b = float(input("Podaj bok b: "))
            obwod = 2 * a + 2 * b
            print(f"Obwod prostokata o bokach {a} i {b} wynosi {obwod:.2f}")
        elif figura == "3":
            a = float(input("Podaj bok a: "))
            b = float(input("Podaj bok b: "))
            obwod = 2 * a + 2 * b
            print(f"Obwod rownolegloboku o bokach {a} i {b} wynosi {obwod:.2f}")
        elif figura == "4":
            a = float(input("Podaj bok a: "))
            obwod = 4 * a
            print(f"Obwod rombu o boku {a} wynosi {obwod:.2f}")
        elif figura == "5":
            a = float(input("Podaj bok a: "))
            b = float(input("Podaj bok b: "))
            c = float(input("Podaj bok c: "))
            obwod = a + b + c
            print(f"Obwod trojkata o bokach {a}, {b}, {c} wynosi {obwod:.2f}")
        elif figura == "6":
            a = float(input("Podaj bok a: "))
            obwod = 3 * a
            print(f"Obwod trojkata rownobocznego o boku {a} wynosi {obwod:.2f}")
        elif figura == "7":
            a = float(input("Podaj bok a: "))
            b = float(input("Podaj bok b: "))
            c = float(input("Podaj bok c: "))
            d = float(input("Podaj bok d: "))
            obwod = a + b + c + d
            print(f"Obwod trapezu o bokach {a}, {b}, {c}, {d} wynosi {obwod:.2f}")
        elif figura == "8":
            r = float(input("Podaj promien r: "))
            obwod = 2 * math.pi * r
            print(f"Obwod kola o promieniu {r} wynosi {obwod:.2f}")
        else:
            print("Nie ma takiej figury.")

    elif dzialanie == "2":
        # ---------- POLA ----------
        print("Jaka figura?")
        print("1 - kwadrat")
        print("2 - prostokat")
        print("3 - rownoleglobok")
        print("4 - romb")
        print("5 - trojkat")
        print("6 - trojkat rownoboczny")
        print("7 - trapez")
        print("8 - kolo")
        figura = input("Twoj wybor: ").strip()
        print()

        if figura == "1":
            a = float(input("Podaj bok a: "))
            pole = a ** 2
            print(f"Pole kwadratu o boku {a} wynosi {pole:.2f}")
        elif figura == "2":
            a = float(input("Podaj bok a: "))
            b = float(input("Podaj bok b: "))
            pole = a * b
            print(f"Pole prostokata o bokach {a} i {b} wynosi {pole:.2f}")
        elif figura == "3":
            a = float(input("Podaj bok a: "))
            h = float(input("Podaj wysokosc h: "))
            pole = a * h
            print(f"Pole rownolegloboku o boku {a} i wysokosci {h} wynosi {pole:.2f}")
        elif figura == "4":
            a = float(input("Podaj bok a: "))
            h = float(input("Podaj wysokosc h: "))
            pole = a * h
            print(f"Pole rombu o boku {a} i wysokosci {h} wynosi {pole:.2f}")
        elif figura == "5":
            a = float(input("Podaj podstawe a: "))
            h = float(input("Podaj wysokosc h: "))
            pole = 0.5 * a * h
            print(f"Pole trojkata o podstawie {a} i wysokosci {h} wynosi {pole:.2f}")
        elif figura == "6":
            a = float(input("Podaj bok a: "))
            pole = (a ** 2 * math.sqrt(3)) / 4
            print(f"Pole trojkata rownobocznego o boku {a} wynosi {pole:.2f}")
        elif figura == "7":
            a = float(input("Podaj dluzsza podstawe a: "))
            b = float(input("Podaj krotsza podstawe b: "))
            h = float(input("Podaj wysokosc h: "))
            pole = ((a + b) * h) / 2
            print(f"Pole trapezu o podstawach {a} i {b} oraz wysokosci {h} wynosi {pole:.2f}")
        elif figura == "8":
            r = float(input("Podaj promien r: "))
            pole = math.pi * r ** 2
            print(f"Pole kola o promieniu {r} wynosi {pole:.2f}")
        else:
            print("Nie ma takiej figury.")

    else:
        print("Nie ma takiej opcji.")

elif kategoria == "2":
    # ===================== BRYLY =====================
    print("Co obliczyc?")
    print("1 - pole powierzchni calkowitej")
    print("2 - objetosc")
    dzialanie = input("Twoj wybor: ").strip()
    print()

    if dzialanie == "1":
        # ---------- POLA POWIERZCHNI ----------
        print("Jaka bryla?")
        print("1 - szescian")
        print("2 - prostopadloscian")
        print("3 - graniastoslup")
        print("4 - ostroslup")
        print("5 - walec")
        print("6 - stozek")
        print("7 - kula")
        bryla = input("Twoj wybor: ").strip()
        print()

        if bryla == "1":
            a = float(input("Podaj krawedz a: "))
            pc = 6 * a ** 2
            print(f"Pole powierzchni szescianu o krawedzi {a} wynosi {pc:.2f}")
        elif bryla == "2":
            a = float(input("Podaj krawedz a: "))
            b = float(input("Podaj krawedz b: "))
            c = float(input("Podaj krawedz c: "))
            pc = 2 * a * b + 2 * a * c + 2 * b * c
            print(f"Pole powierzchni prostopadloscianu o krawedziach {a}, {b}, {c} wynosi {pc:.2f}")
        elif bryla == "3":
            pp = float(input("Podaj pole podstawy Pp: "))
            pb = float(input("Podaj pole powierzchni bocznej Pb: "))
            pc = 2 * pp + pb
            print(f"Pole powierzchni graniastoslupa wynosi {pc:.2f}")
        elif bryla == "4":
            pp = float(input("Podaj pole podstawy Pp: "))
            pb = float(input("Podaj pole powierzchni bocznej Pb: "))
            pc = pp + pb
            print(f"Pole powierzchni ostroslupa wynosi {pc:.2f}")
        elif bryla == "5":
            r = float(input("Podaj promien podstawy r: "))
            wys = float(input("Podaj wysokosc H: "))
            pc = 2 * math.pi * r ** 2 + 2 * math.pi * r * wys
            print(f"Pole powierzchni walca o promieniu {r} i wysokosci {wys} wynosi {pc:.2f}")
        elif bryla == "6":
            r = float(input("Podaj promien podstawy r: "))
            l = float(input("Podaj dlugosc tworzacej l: "))
            pc = math.pi * r ** 2 + math.pi * r * l
            print(f"Pole powierzchni stozka o promieniu {r} i tworzacej {l} wynosi {pc:.2f}")
        elif bryla == "7":
            r = float(input("Podaj promien r: "))
            pc = 4 * math.pi * r ** 2
            print(f"Pole powierzchni kuli o promieniu {r} wynosi {pc:.2f}")
        else:
            print("Nie ma takiej bryly.")

    elif dzialanie == "2":
        # ---------- OBJETOSCI ----------
        print("Jaka bryla?")
        print("1 - szescian")
        print("2 - prostopadloscian")
        print("3 - graniastoslup")
        print("4 - ostroslup")
        print("5 - walec")
        print("6 - stozek")
        print("7 - kula")
        bryla = input("Twoj wybor: ").strip()
        print()

        if bryla == "1":
            a = float(input("Podaj krawedz a: "))
            v = a ** 3
            print(f"Objetosc szescianu o krawedzi {a} wynosi {v:.2f}")
        elif bryla == "2":
            a = float(input("Podaj krawedz a: "))
            b = float(input("Podaj krawedz b: "))
            c = float(input("Podaj krawedz c: "))
            v = a * b * c
            print(f"Objetosc prostopadloscianu o krawedziach {a}, {b}, {c} wynosi {v:.2f}")
        elif bryla == "3":
            pp = float(input("Podaj pole podstawy Pp: "))
            wys = float(input("Podaj wysokosc H: "))
            v = pp * wys
            print(f"Objetosc graniastoslupa wynosi {v:.2f}")
        elif bryla == "4":
            pp = float(input("Podaj pole podstawy Pp: "))
            wys = float(input("Podaj wysokosc H: "))
            v = (1 / 3) * pp * wys
            print(f"Objetosc ostroslupa wynosi {v:.2f}")
        elif bryla == "5":
            r = float(input("Podaj promien podstawy r: "))
            wys = float(input("Podaj wysokosc H: "))
            v = math.pi * r ** 2 * wys
            print(f"Objetosc walca o promieniu {r} i wysokosci {wys} wynosi {v:.2f}")
        elif bryla == "6":
            r = float(input("Podaj promien podstawy r: "))
            wys = float(input("Podaj wysokosc H: "))
            v = (1 / 3) * math.pi * r ** 2 * wys
            print(f"Objetosc stozka o promieniu {r} i wysokosci {wys} wynosi {v:.2f}")
        elif bryla == "7":
            r = float(input("Podaj promien r: "))
            v = (4 / 3) * math.pi * r ** 3
            print(f"Objetosc kuli o promieniu {r} wynosi {v:.2f}")
        else:
            print("Nie ma takiej bryly.")

    else:
        print("Nie ma takiej opcji.")

elif kategoria == "3":
    # ===================== INNE WZORY =====================
    print("Ktory wzor?")
    print("1 - wysokosc trojkata rownobocznego")
    print("2 - przekatna kwadratu")
    print("3 - twierdzenie Pitagorasa")
    print("4 - pole rombu z przekatnych")
    wzor = input("Twoj wybor: ").strip()
    print()

    if wzor == "1":
        a = float(input("Podaj bok a: "))
        h = (a * math.sqrt(3)) / 2
        print(f"Wysokosc trojkata rownobocznego o boku {a} wynosi {h:.2f}")
    elif wzor == "2":
        a = float(input("Podaj bok a: "))
        d = a * math.sqrt(2)
        print(f"Przekatna kwadratu o boku {a} wynosi {d:.2f}")
    elif wzor == "3":
        a = float(input("Podaj przyprostokatna a: "))
        b = float(input("Podaj przyprostokatna b: "))
        c = math.sqrt(a ** 2 + b ** 2)
        print(f"Przeciwprostokatna c dla a = {a} i b = {b} wynosi {c:.2f}")
    elif wzor == "4":
        e = float(input("Podaj przekatna e: "))
        f = float(input("Podaj przekatna f: "))
        pole = (e * f) / 2
        print(f"Pole rombu o przekatnych {e} i {f} wynosi {pole:.2f}")
    else:
        print("Nie ma takiego wzoru.")

else:
    print("Nie ma takiej opcji.")

print()
print("Koniec programu.")
