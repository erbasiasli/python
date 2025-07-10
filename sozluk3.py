super_lig={"Galatasaray":"63Puan","Fenerbahçe":"62Puan","Beşiktaş":"50Puan"}

while True:
    takim_ekle=input("lütfen takım ismi giriniz:")
    puan_ekle=input("lütfen puan giriniz:")
    super_lig.setdefault(takim_ekle,puan_ekle)

    for i,j in super_lig.items():
        print(i,j)

    secim=input("Çıkmak ister misiniz:E\H").capitalize()
    if secim=="E":
        print("çıkış yapıldı...")
        break
    else:
        pass



