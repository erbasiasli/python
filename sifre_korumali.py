import subprocess as sp

psw = "123456"
kullanici_sifre = input("lütfen şifrenizi giriniz:")

# subprocess.call("notepad.exe")

if kullanici_sifre == psw:

    while True:
        print("***UYGULAMA AÇMA EKRANINA HOŞ GELDİNİZ***")
        secim_yap = input("1-Notepad\n2-Hesap Makinesi\n3-Excel\n")
    
        if secim_yap == "1":
            sp.call("notepad.exe")
            input("devam edilsin mi?")
        elif secim_yap == "2":
            sp.call("calc.exe")
            input("devam edilsin mi?")
        elif secim_yap == "3":
            sp.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

else:
    print("hatalı şifre")
