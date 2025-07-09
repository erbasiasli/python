db_ka = "admin"
db_ps = "1234"

while True:
    kullanici_adi = input("Lütfen kullanıcı adınızı giriniz: ")
    kullanici_sifre = input("Lütfen şifrenizi giriniz: ")

    if db_ka == kullanici_adi and db_ps == kullanici_sifre:
        print("Hoş geldiniz:", kullanici_adi)
        break

    elif db_ka != kullanici_adi and db_ps == kullanici_sifre:
        print("Kullanıcı adınız hatalı.")

    elif db_ka == kullanici_adi and db_ps != kullanici_sifre:
        print("Şifreniz hatalı...")
        cevap = input("Şifre değiştirilsin mi? (E/H): ")
        if cevap.upper() == "E":
            yeni_sifre = input("Lütfen yeni şifrenizi yazınız: ")
            db_ps = yeni_sifre
            print("Şifreniz başarıyla değiştirildi.")
            print("Lütfen tekrar giriş yapın.\n")
        else:
            print("Tekrar deneyin.\n")

    else:
        print("Kullanıcı adı veya şifre hatalı.")
