print("=== TEST NA RANDKE ===")
print("Odpowiadaj tak albo nie, a tam gdzie trzeba podaj liczbe.")
print()

# ---------- ETAP 1: podstawowe dane ----------
imie = input("Jak masz na imie? ")
wiek = int(input("Ile masz lat? "))
singiel = input("Czy jestes singlem? (tak/nie) ").lower()

if wiek >= 18 and singiel == "tak":
    print(f"Hej {imie}, 1 etap za toba!")
    print()

    # ---------- ETAP 2: wyglad ----------
    print("Teraz kilka pytan o Twoj wyglad.")
    wzrost = float(input("Podaj swoj wzrost w metrach (np. 1.75): "))
    oczy = input("Jaki masz kolor oczu? ").lower()
    wlosy = input("Jaki masz kolor wlosow? ").lower()
    sport = input("Czy uprawiasz jakis sport? (tak/nie) ").lower()
    usmiech = input("Czy czesto sie usmiechasz? (tak/nie) ").lower()

    punkty = 0

    if wzrost >= 1.60 and wzrost <= 1.95:
        punkty = punkty + 1
    if oczy == "niebieskie" or oczy == "zielone" or oczy == "piwne":
        punkty = punkty + 1
    if wlosy == "blond" or wlosy == "brazowe" or wlosy == "czarne":
        punkty = punkty + 1
    if sport == "tak":
        punkty = punkty + 1
    if usmiech == "tak":
        punkty = punkty + 1

    print(f"Za wyglad dostajesz {punkty} punktow na 5.")
    print()

    if punkty >= 3:
        print(f"Masz piekne oczy {imie}, 2 etap za toba!")
        print()

        # ---------- ETAP 3: charakter ----------
        print("Ostatni etap, pytania o charakter.")
        zwierzeta = input("Czy lubisz zwierzeta? (tak/nie) ").lower()
        papierosy = input("Czy palisz papierosy? (tak/nie) ").lower()
        odleglosc = float(input("Ile kilometrow dzieli nas od siebie? "))
        hobby = input("Jakie masz hobby? ")

        if zwierzeta == "tak" and papierosy == "nie" and odleglosc <= 50:
            print(f"{imie}, pasujemy do siebie! Zapraszam na randke w sobote.")
            print(f"Skoro Twoje hobby to {hobby}, to moze zrobimy to razem.")
        elif papierosy == "tak":
            print("Nie znosze dymu papierosowego, wiec jednak nie.")
        elif zwierzeta == "nie":
            print("Mam psa i kota, wiec chyba nam nie po drodze.")
        else:
            print(f"Az {odleglosc} km to dla mnie za daleko. Moze kiedys.")
    else:
        print("Zostanmy przyjaciolmi.")
else:
    if wiek < 18:
        print("Jestes za mlody na randke ze mna, wroc za pare lat.")
    else:
        print("Skoro masz juz kogos, to randka odpada.")

print()
print("Koniec programu.")
