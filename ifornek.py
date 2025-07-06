sut_miktari=int(input("lütfen süt miktarınızı giriniz:"))
kasar_peyniri_siniri=11

if sut_miktari <kasar_peyniri_siniri:
    print("süt miktarınzın yetersiz.",sut_miktari)
    print("kaşar peyniri üretmek için ihtiyacınız olan süt miktarı",(kasar_peyniri_siniri-sut_miktari))
else:
    toplam_üretim=sut_miktari/kasar_peyniri_siniri
    print(f"toplam üretim:{int(toplam_üretim)}")