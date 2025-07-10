import random
import time
kullanicilar=list()

def kullanici_ekle(x):
    print("-"*30)
    print("Kullanıcı ekleme ekranına hoş geldiniz:")
    
    ekle=input("lütfen eklenecek kullanıcıyı yazınız:")

    kullanicilar.append(ekle)
    input("devam etmek için enter tuşuna basınız...")

def kullanici_gor(x):
    say=1
    print("-"*30)
    for i in x:
        print(str(say)+"Kullanıcı Adı:",i)
        say+=1
    print("-"*30)
    input("devam etmek için enter tuşuna basınız...")


def sec(x):
    print("-"*30) 
    say=1
    kisi_sec=int(input("kaç kişi seçilsin?:"))
    rastgele_sec=random.sample(x,kisi_sec)

    for i in rastgele_sec:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
        print("diğer kişi sistemden çekiliyor...")
        time.sleep(3)
    print("-"*30)
    input("devam etmek için enter tuşuna basınız...")

def salla(x):
    print("-"*30)
    say=1
    random.shuffle(x)
    for i in x:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
    print("-"*30)
    input("devam etmek için enter tuşuna basınız...")



        
while True:
    print("****ÇEKİLİŞ UYGULAMASINA HOŞ GELDİNİZ****")
    secim=int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3-Kullanıcıları Karıştır\n4-Rastgele Seç\n"))

    if secim==1:
        kullanici_ekle(kullanicilar)
        
    elif secim==2:
        kullanici_gor(kullanicilar)
    elif secim==3:
        salla(kullanicilar)
    elif secim==4:
        
        sec(kullanicilar)
    else:
        print("Lütfen uygun bir tercih yapınız.")
    