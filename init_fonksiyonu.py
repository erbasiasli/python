class okul:
    def __init__(self,sube,ogretmen,bolum,mevcut):
        self.sube=sube
        self.ogretmen=ogretmen
        self.bolum=bolum
        self.mevcut=mevcut
    

    

    def bilgileri_goster(self):
        print("-"*45)
        print("Sınıf Bilgileri")
        print("Şube:{}Öğretmen:{}Bölüm:{}Mevcut:{}".format(self.sube,self.ogretmen,self.bolum,self.mevcut))
        print("-"*45)

    def ogretmen_adi(self):
        print("Öğretmen adı:",self.ogretmen)

birini_sınıf=okul("11C","Aslı Erbaşı","Matematik","23")

birini_sınıf.bilgileri_goster()

ikinci_sınıf=okul("9A","EMOŞ","Türkçe","22")
ikinci_sınıf.bilgileri_goster()

ikinci_sınıf.ogretmen_adi()