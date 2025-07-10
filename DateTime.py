from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"turkish")


a=datetime.now()
tam_tarih=datetime.strftime(a,"%B")
print(tam_tarih) 

#a=a.year
#a=a.hour
#print(a)


#%a hafta gününün kısaltılmış adı
#%A hafta gününün tam adı
#%b ayın kısaltılmış hali
#%B ayın tam adı
#%c tam tarih,saat ve zaman bilgisi
#%d sayı değerli bir karakter dizisi olarak gün
#%j belli bir tarihin yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
#%m sayı değerli bir karakter dizisi olarak ay
