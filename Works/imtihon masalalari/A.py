# %% A
db_user = "user"
db_pass = "1111"

imkon = 3
while(True):
    password = input("Parolni kiriting: ")
    user = input("Usernameni kiriting: ")
    if(user == db_user and password != db_pass):
        print("Password noto'g'ri !!!")
        print(db_pass)
        imkon -= 1
    elif(user != db_user and password == db_pass):
        print("Username noto'g'ri !!!")
        imkon -= 1
    elif(user != db_user and password != db_pass):
        imkon -= 1
        print("Username va Password noto'g'ri !!!")
    elif(user == db_user and password == db_pass):
        print("Hush kelibsiz !!!")
        break
    if(imkon == 0):
        javob = input("Parolni tiklashni istaysizmi [ha / yoq]?")
        if(javob == "ha"):
            password = input("Eski password: ")
            if(password == db_pass):
                password = input("Yangi password: ")
                db_pass = password
                print("Parol muvaffaqiyatli Tiklandi. Tizimga kirishingiz mumkin !!!")
                break
            
