from pult import *

print("""---- Pult Menu -----
1. Tv power Off/On
2. Tv Malumotlari
3. Kanal Soni
4. Kanal Qosh
5. Random Kanal O't
6. Ovozni O'zgartir

7. exit
""")
p1 = Pult()

while True:
    amal = input("Tugmani Tanlang: ")
    if(amal == "7"):
        print("Pult Dasturi Tugatildi...")
        break
    if(amal == "1"):
        p1.tv_power()
    elif(amal == "2"):
        print(p1)
    elif(amal == "3"):
        print(len(p1),"ta kanal mavjud")
    elif(amal == "4"):
        p1.kanal_qosh(input("Yangi kanal: "))
    elif(amal == "5"):
        p1.random_kanal()
    elif(amal == "6"):
        p1.ovoz_ozgartir()
    else:
        print("Brat Tepage qara !!!")
        

