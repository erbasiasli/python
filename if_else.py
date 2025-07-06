#müsteri=15
#if müsteri<18:
#    print("maalesef yaşınız 18 den küçük sizin yaşınız",müsteri)

#else:
#    print("tebrikler yaşınız 18den büyük yaşınız:",müsteri)

müsteri_yas=int(input("yaşınızı giriniz:"))
kabul_yas=18

if müsteri_yas<kabul_yas:
    print("maalesef yaşınız uygun değil yaşınız",müsteri_yas)
else:
    print("hoş geldiniz yaşınız:",müsteri_yas)