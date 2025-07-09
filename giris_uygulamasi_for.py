

for i in range(3):
    sifre=input("lütfen şifre belirleyiniz:")
    if not sifre:
        print("bu alan boş bırakılamaz.")
    elif len(sifre) in range(3,8):
        print("yeni şifreniz",sifre)
        break
    elif i==2:
        print("şifreyi 3 kere yanlış girdiniz.lütfen 15 dakika bekleyiniz")
    else:
        print("şifreniz 8 karakter uzun ya da 3 karakterden kısa...")
