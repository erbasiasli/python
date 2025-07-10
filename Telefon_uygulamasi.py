tel_rehberi=dict()

def tel_no_ekle(x):
    print("***NUMARA EKLEME EKRANINA HOŞ GELDİNİZ***")
    numara_isim_al=input("lütfen isim giriniz:")
    numara_no_al=input("lütfen telefon numarasını giriniz:")

    x=tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"{numara_isim_al}adlı kişi telefon listesine ekledi...")


def tel_rehber_göster(x):
    kisi_sayisi=len(x)
    print(f"rehberinizdeki kayıtlı kişi sayısı",{kisi_sayisi})
    print("rehbere hoş geldiniz")

    for i,j in x.items():
        print(i,":",j)
    input("devam edilsin mi?")

tel_no_ekle(tel_rehberi)
tel_rehber_göster(tel_rehberi)

def no_sil(x):
    print("kişi silme ekranına hoş geldiniz:")
    silinicek_kisi=input("silinicek kişiyi yazınız:")
    x=tel_rehberi.pop(silinicek_kisi)
    input("devam edilsin mi?")


while True:
    print("***HOŞ GELDİNİZ***")
    print("***Seçim Yapınız***")
    secim_yap=int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n"))
    
    if secim_yap==1:
        tel_no_ekle(tel_rehberi)

    elif secim_yap==2:
        no_sil(tel_rehberi)

    elif secim_yap==3:
        tel_rehber_göster(tel_rehberi)
    else:
        print("lütfen uygun tuşa basınız:")
