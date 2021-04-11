

#question 3

loginUsernamePassword={"admin":"admin",
                       "root":"1234567",
                       "login":"qwerty"}

print(loginUsernamePassword.keys())

username=input("Kullanıcı adinizi giriniz")
password=input("Parolanızı giriniz")

if username in loginUsernamePassword.keys():
    if loginUsernamePassword[username] == password:
        print("Parolaniz dogru")
    else:
        print("Kullanici adiniz veya parolaniz yanlis")
else:
    print("Kullanici adiniz veya parolaniz yanlis")
