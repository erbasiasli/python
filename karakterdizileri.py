buyukharfler="NE MUTLU TÜRKÜM DİYENE".lower()
print(buyukharfler)
print("harfleri küçüğe çevirir.")
kucukharfler="ne mutlu türküm diyene".upper()
print(kucukharfler)
print("harfleri büyüğe çevirir")

sadece_basharfi_buyuk="ne mutlu türküm diyene".capitalize()
print(sadece_basharfi_buyuk)

tam_tersi="galatasaray sk".swapcase()
print(tam_tersi)
print("swapcase büyükse küçük küçükse büyük yapar.")

sil="++++asli++++".strip("+")
print(sil)
print("neyi silmek istersen içine yazarsın.")
print("tuncay","erol",sep="+")
print("kişinin adı",end=":")
adi="asli"
soyadi="erbaşı"
yasi="23"
print("kişinin adı {}\n kişinin soyadı{}\n kişininyaşı{}".format(adi,soyadi,yasi))

print(f"kişinin adı{adi}kişinin soyadı{soyadi}kişinin yaşı{yasi}")



