import time 

try:
    sayı=int(input("sayı1"))
    sayı2=int(input("sayı2"))

    toplam=sayı+sayı2
    print(toplam)

except ValueError:
    print("lütfen sayı giriniz:")

finally:
    sayac=5

    for i in range(5):
        time.sleep(1)
        print("Geri sayım:",sayac)
        sayac-=1
        if sayac==0:
            print("işlem tamamlandı.")

