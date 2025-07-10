sözlük={"Apple":"Elma","İsim":"Aslı","Telefon":"Iphone"}

#print(sözlük["Apple"])
#print(len(sözlük))
for i in sözlük:
    print(i)

for isim,deger in sözlük.items():
    print(isim,",",deger)
