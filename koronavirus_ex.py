ates_durumu=float(input("lütfen ateş derecenizi yazınız:"))
oksuruk=input("öksürüğünüz var mı? E/H: ").lower()
bas_agrisi=input("baş ağrınız var mı? E/H" ).lower()
gün=int(input("kaç gündür var?"))

if ates_durumu >=39:
    if gün>=3:
        print("***uyarı hastaneye gidiniz.")
    else:
        print("ateş durumunuz sınırda,devam ederse lütfen en yakın sağlık kuruluşuna gidiniz...")



if (ates_durumu >=39) and (oksuruk=="e") and(bas_agrisi=="e")and (gün>=3):
    print("*** ACİL lütfen en yakın sağlık kuruluşuna gidiniz...")
    print("****ACİL durumunuz olumlu değil")


elif (oksuruk=="e") or(bas_agrisi=="e") or (gün>=3):
    print("Durumunuz böyle giderse lütfen sağlık kuruluşuna gidiniz.")


else:
    print("ateşinizin 39 derecenin üstüne çıkarsa sağlık kuruluşuna gidiniz.")

