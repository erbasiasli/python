vize=int(input("lütfen vize notunuzu giriniz:"))
final=int(input("lütfen final notunuzu giriniz:"))

ortalama=(vize+final)/2

if ortalama>=85:
    print("Tebrikler AA aldınız:",ortalama)
elif ortalama >=65:
    print("Tebrikler BB aldınız",ortalama)
elif ortalama>=50:
    print("Tebrikler CC aldınız",ortalama)
else:
    print("Maalesef dersten kaldınız.",ortalama)
    