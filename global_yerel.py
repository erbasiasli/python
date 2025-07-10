#def fonksiyon ():
 #   a=10 #genel değişkendir

    #a=5 #yerel değişkendir bu yüzden çıktı budur.
#    print(a)

#fonksiyon()

a=10

def fonksiyon():
    global a
    a=25

    print(a)

fonksiyon()