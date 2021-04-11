

#Final Project


cevap_Anahtari=dict()
cevap_Anahtari={"Soru1":"1071","Soru2":"Fatih Sultan Mehmet","Soru3":"1923","Soru4":"Yavuz Sultan Selim","Soru5":"Ramazan","Soru6":"1881","Soru7":"Osman Gazi","Soru8":"Mustafa Kemal Atatürk","Soru9":"Mehmet Akif Ersoy","Soru10":"Rusya"}
print("Bilgi yarışmamıza hoş geldiniz")
print("-------------------------------")
puan=0

soru1=("Soru 1: Malazgirt savaşı hangi tarihte yapılmıştır?") 
soru2=("Soru 2: İstanbul'u hangi padişah doneminde fethedilmiştir?")
soru3=("Soru 3: Cumhuriyet ne zaman ilan edilmiştir.?")
soru4=("Soru 4: İlk Türk halife kimdir?")
soru5=("Soru 5: Müslümanlar hicri hangi ay oruç tutarlar?")
soru6=("Soru:6  Atatürk miladi hangi yıl doğmuştur?")
soru7=("Soru:7  Osmanlı devletinin kurucu ismi kimdir?")
soru8=("Soru:8  Türkiye cumhuriyetinin kurucu ismi kimdir?")
soru9=("Soru:9  İstiklal Marşımızın yazarının ismi?")
soru10=("Soru:10 Dünyada yüz ölçümü en yüksek olan ülke?")
basla=input("Hazirsaniz Y veya y tuslarina basiniz")
if (basla=="Y") or (basla=="y"):
    print(soru1)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru1"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
        print("Cevap yanlis. Puan alamadınız")
    print(soru2)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru2"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
         print("Cevap yanlis. Puan alamadınız")
    print(soru3)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru3"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
        print("Cevap yanlis. Puan alamadınız")
    print(soru4)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru4"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
        print("Cevap yanlis. Puan alamadınız")
    print(soru5)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru5"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
        print("Cevap yanlis. Puan alamadınız")
    print(soru6)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru6"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
        print("Cevap yanlis. Puan alamadınız")
    print(soru7)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru7"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
        print("Cevap yanlis. Puan alamadınız")
    print(soru8)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru8"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
        print("Cevap yanlis. Puan alamadınız")
    print(soru9)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru9"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
        print("Cevap yanlis. Puan alamadınız")
    print(soru10)
    cevap=input("Cevabınızı giriniz")
    if cevap==cevap_Anahtari["Soru10"]:
        puan+=10
        print("Cevap dogru. Toplam puan = %d"%puan)
    else:
         print("Cevap yanlis. Puan alamadınız")
else:
    print("Güle Güle")

if puan>50:
    print("Yarışmadan başarılı olarak ayrıldınız tebrikler...")
else:
    print("Malesef başarısız oldunuz.")
