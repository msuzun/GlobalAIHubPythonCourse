
#question 1
def swap(a,b):
    tmp=a
    a=b
    b=tmp
    return a,b

liste1 = list() # Create a List
print(liste1)
n=int(input("Liste 1 kaç elemanli olsun?"))
divide=1
print("-----------------------")
print("Liste için elemanlari giriniz...")
for i in range(0,n):
    liste1.append(input("Elemanı giriniz."))
    print(liste1)

if n%2==0:
    divide=n//2
    for i in range(0,divide):
        a,b=swap(liste1[i],liste1[divide+i])
        liste1[i]=a
        liste1[divide+i]=b
else:
    divide=(n//2)+1
    for i in range(0,divide-1):
        a,b=swap(liste1[i],liste1[divide+i])
        liste1[i]=a
        liste1[divide+i]=b

print(liste1)

