super_lig={"Galatasaray":"63Puan","Fenerbahçe":"62Puan","Beşiktaş":"50Puan"}

#super_lig.setdefault("Trabzonspor","100 Puan")

takim_ekle=input("lütfen takım ismi giriniz:")
puan_ekle=input("lütfen puan giriniz:")

super_lig.setdefault(takim_ekle,puan_ekle)


for isim,deger in super_lig.items():
    print(isim,deger)


#super_lig.pop("Galatasaray")
#print(super_lig)