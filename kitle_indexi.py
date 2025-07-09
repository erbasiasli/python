def kitle_indexi(boy,kilo):
    hesapla=kilo/(boy**2)

    print(f"\n vücut kitle indeksiniz{hesapla:.2f}")


    if hesapla < 18.5:
        print("Zayıfsınız.")
    elif 18.5 <= hesapla <= 24.9:
        print("Normal kilolusunuz.")
    elif 25 <= hesapla <= 29.9:
        print("Fazla kilolusunuz.")
    elif 30 <= hesapla <= 34.9:
        print("1. derece obezsiniz.")
    elif 35 <= hesapla <= 39.9:
        print("2. derece obezsiniz.")
    else:
        print("3. derece (morbid) obezsiniz.")


boy=float(input("Lütfen boyunuzu giriniz metre cinsinden:"))
kilo=int(input("lütfen kilonuzu giriniz:"))

kitle_indexi(boy,kilo)