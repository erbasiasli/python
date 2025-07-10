try:
    sayi1=int(input("sayı1"))
    sayi2=int(input("sayi2"))

    toplam=sayi1/sayi2

    print(toplam)

#except ZeroDivisionError:
  #  print("Bir sayı sıfıra bölünmez.")

#except ValueError:
 #   print("lütfen sayısal veri giriniz:")

except(ZeroDivisionError,ValueError):
    print("Hata var.. ")




