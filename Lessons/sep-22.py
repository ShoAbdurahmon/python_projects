from os import system
def faylOqi():
    try:
        faylNomi = input("Qaysi Faylni O'qiy: ")
        fayl = open(f"{faylNomi}.txt","r")
        a = fayl.read()
        print(a)
        fayl.close()
    except:
        print("Fayl Topilmadi !!!")
def faylgaYoz():
    faylNomi = input("fayl nomini kiriting: ")
    mode = input("Qayta yozish(a) / Qo'shish(w): ")
    fayl = open(f"{faylNomi}.txt",mode)
    fayl.write(input("Nima Yozdirmoqchisiz: "))
    fayl.close()
print("""-- Faylga Yozdirish Dasturi --
1. Faylni O'qish
2. Faylga Yozish
3. Fayllarni Ko'rish
4. Oynani Tozalash""")

while True:
    tanlov = input("Tanlang: ")
    if tanlov == '1':
        faylOqi()
    elif tanlov == '2':
        faylgaYoz()
    elif(tanlov == '3'):
        system("ls")
    elif(tanlov == "4"):
        system("clear")
    else:
        print("Dastur Tugadi !!!")
        break
    


# %%

fayl = open("info.txt","r")


print(fayl.read())
print(fayl.read(50))
print(fayl.readline())

print(fayl.read)



with open("info.txt","r+") as fayl:
    fayl.seek(20)
    print(fayl.tell())
    print(fayl.read(20))
    print(fayl.tell())
    fayl.seek(0)
    fayl.write("Men yana boshiga Qaytdim")
    print(fayl.tell())
    fayl.seek(0)
    print(fayl.read())

print(dir(fayl))





















