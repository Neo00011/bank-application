import random
import time
from datetime import datetime
import os
kullanıcılar={}
rakamlar=["1","2","3","4","5","6","7","8","9","0"]


def giris():
    
    hak=6
    while True:
        
        ad=input("Adınızı giriniz: ".title())
        key=input("Şifrenizi giriniz: ")
        print("Bekleyiniz...")
        time.sleep(4)

        if ad in kullanıcılar and kullanıcılar[ad]["şifre"]==key:
            print("Giriş yapıldı.")

            print("1-Para çekme ")
            print("2-Para yatırma")                                 #GİRİS MENÜSÜ
            print("3-Bakiye sorgula")
            print("4-Hesap geçmişi görüntüle")
            print("5-Hesap Özeti")
            print("6-Çıkış")
           
            while True:
                islem=input("Hangi işlemi yapmak istersiniz(1,2,3,4,5,6): ")
                if islem=="1":
                    paracekme(ad)

                elif islem=="2":
                    parayatirma(ad)

                elif islem=="3":
                    print("Bakiyeniz: ",kullanıcılar[ad]["bakiye"])

                elif islem=="4":
                    print("Hesap geçmişiniz :",kullanıcılar[ad]["geçmiş"])
                
                elif islem=="5":
                    print("--------------------Hesap Özeti--------------------")

                    for i in kullanıcılar[ad]["geçmiş"]:
                        print("-",i)
                    print("Bakiyeniz: ",kullanıcılar[ad]["bakiye"])
                    print("Hesap kurulma tarihi: ",zaman)
                    print(f"Hesap sahibinin adı: {ad.title()}")
                
                elif islem=="6":
                    print("Hesaptan çıkılıyor...")
                    time.sleep(3)
                    return        
                else:
                    continue        
        
        else:
            print("Giriş yapılamadı.")
            hak-=1
            print(f"{hak} hakkınız kaldı.")
            
            if hak==3:
                pass
                print("Üst üste girdiğiniz hatalı denemeler sonucu 60 saniye bekleyeceksiniz")
                for i in range(60,-1,-1):
                    print(f"Tekrar denemeniz için {i} saniye kaldı.")
                    time.sleep(1)
                    os.system("cls")
            elif hak==0:
                print("Sistemi gereksiz meşgul ettiğiniz tespit edilmiştir.Verilen süreyi bekleyin.")
                for i in range(100000,-1,-1):
                    print(f"Tekrar denemeniz için {i} saniye kaldı.")
                    time.sleep(1)
                    os.system("cls")
                
            while True:
    
                karar=input("Tekrar denemek için 1,menüye dönmek içinse 2'yi tuşlayın: ")
                if karar=="1":
                    break
                elif karar=="2":
                    print("Menüye dönülüyor...")
                    time.sleep(2)
                    return
                else:
                    continue
def kayit():
    print("Kayıt olmanız için adınızı girmeniz gerekiyor.")
    while True:
        name=input("Adınız(rakamsız ve sembolsüz): ".title())
        time.sleep(2)
        if name.isalpha():
            break
        else:
            print("Yalnız harf kullanın.")
    print("Adınız onaylandı.Şifreniz seçiliyor bekleyiniz...")
    time.sleep(2)
    sifre="".join(random.choices(rakamlar,k=4))
    print(f"Şifreniz: {sifre}")
    global zaman
    zaman=datetime.now()
    kullanıcılar[name]={"şifre":sifre,"bakiye":0,"geçmiş":[]}
    (kullanıcılar[name]["geçmiş"]).append(f"{zaman} tarihinde hesap açıldı")
    time.sleep(1.5)
    print("Kaydınız tamamlanmıştır menüye yönlendiliyorsunuz...")        
    

def paracekme(ad):
    print("Bakiyeniz",+ kullanıcılar[ad]["bakiye"])
    tutar=float(input("Çekmek istediğiniz tutarı giriniz: "))
    
    if float(kullanıcılar[ad]["bakiye"])<tutar:
        print("Yetersiz bakiye.")
        
    else:
        print("Paranız çekildi.Kalan bakiyeniz: ",float(kullanıcılar[ad]["bakiye"]-tutar))   
        kullanıcılar[ad]["bakiye"]=float(kullanıcılar[ad]["bakiye"]-tutar)
        (kullanıcılar[ad]["geçmiş"]).append(f"{datetime.now()} {tutar} TL para çekildi.")
def parayatirma(ad):
    para=float(input("Yatırmak istediğiniz tutarı giriniz: "))
    print("Paranız yatırılıyor.bekleyiniz...")
    time.sleep(2)
    print("Paranız yatırıldı.Bakiyeniz: ",float(kullanıcılar[ad]["bakiye"]+para))
    kullanıcılar[ad]["bakiye"]=float(kullanıcılar[ad]["bakiye"]+para)
    (kullanıcılar[ad]["geçmiş"]).append(f"{datetime.now()} tarihinde {para} TL para yatırıldı.")



print("Halkbank dijital banka platformuna hoşgeldiniz.")
time.sleep(2)

while True:
    sayi=input("Giriş yapmak için 1,kayıt olmak için 2,çıkış yapmak içinse 3'ü tuşlayınız: ")           #ANAMENU

    if sayi=="1":   #giris
        giris()


    elif sayi=="2":     #kayıt
        kayit()

    elif sayi=="3":     #cıkıs
        print("Çıkış yapılıyor...")
        time.sleep(4)
        break

    else:
        print("Geçersiz giriş.Yalnızca belirtilen rakamları giriniz.")  #hata






























