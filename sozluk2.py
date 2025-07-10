super_lig={"Galatasaray":"63Puan","Fenerbahçe":"62Puan","Beşiktaş":"50Puan"}

#print(super_lig["Galatasaray"])

takım=input("lütfen puan durumunu öğrenmek istediğiniz takımı yazınız").capitalize()

#if takım not in super_lig:
    #print("Seçtiğiniz takım listemizde bulunmuyor..")

#else:
    #print(takım,":",super_lig[takım])


print(takım,":",super_lig.get(takım,"Bu takım listede bulunmuyor."))