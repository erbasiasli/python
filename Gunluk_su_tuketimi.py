def su_hesapla(kilo):
    e_hesapla=kilo*0.04
    k_hesapla=kilo*0.03

    cinsiyet=input("lütfen cinsiyetinizi giriniz:Kadın\Erkek:").lower()
    
    if cinsiyet=="erkek":
        print("-"*30)
        print("Cinsiyetiniz",cinsiyet)
        print(e_hesapla,"Litre su içmelisin")
        print("-"*30)
    elif not cinsiyet:
        print("lütfen cinsiyet belirt.")

    elif cinsiyet=="kadın":
        print("-"*30)
        print("Cinsiyetiniz",cinsiyet)
        print(k_hesapla,"Litre su içmelisiniz..")
        print("-"*30)


Kilo_al=int(input("lütfen kilonuzu giriniz:"))
su_hesapla(Kilo_al)

