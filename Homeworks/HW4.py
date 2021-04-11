 
  
 #question 4

n=int(input("Kaç tane öğrenci gireceğinizi giriniz"))
tumliste=[[] for i in range(0,n)]

for i in range(0,n):
    passingGrade=0
    adiSoyadi=input("Ogrencinin adini ve soyadini giriniz")
    vize=int(input("Vize notunuzu giriniz"))
    proje=int(input("Proje notunuzu giriniz"))
    final=int(input("Final notunuzu giriniz"))
    passingGrade=(((vize*30)/100)+((proje*30)/100)+((final*40)/100))
    tumliste[i].append(adiSoyadi)
    tumliste[i].append(vize)
    tumliste[i].append(proje)
    tumliste[i].append(final)
    tumliste[i].append(passingGrade)

ogrenciAdi=[]
ogrenciOrtalamasi=[]

for i in range(0,n):
    ogrenciAdi.append(tumliste[i][0])
for i in range(0,n):
    ogrenciOrtalamasi.append(tumliste[i][4])

print(ogrenciAdi)
print("-----------------")
print(ogrenciOrtalamasi)
ogrenci=dict(zip(ogrenciAdi,ogrenciOrtalamasi))
print(ogrenci)

sorted_ogrenci=sorted(ogrenci.items(),key=lambda x:x[1],reverse=True)
print(sorted_ogrenci)
