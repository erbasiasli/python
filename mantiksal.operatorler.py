#deneme= 8<10 and 11<12
#print(deneme)

#print("and ifadesinde her değer doğru çıkarsa sonuç doğru olur biri yanlışsa çıktı yanlış olur")

db_ps=1234
db_ka="asli"

kullanici_adi=input("lütfen kullanıcı adınızı  giriniz:")
kullanici_sifre=int(input("lütfen şifrenizi giriniz:"))

#kontrol= db_ps==kullanici_sifre and db_ka==kullanici_adi
kontrol= db_ps==kullanici_sifre or db_ka==kullanici_adi

print(kontrol)
