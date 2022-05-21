print("-- Problem 1 --")

vazn = int(input("Vazningizni kiriting: "))
boy = int(input("Boyingizni kiriting: "))

vazn /= 100
bmi = vazn / (boy * boy)

if(bmi < 18.5 and bmi > 10):
    print("Zayif")
elif(bmi < 25):
    print("Normal")
elif(bmi < 30):
    print("Ortiqcha")
elif(bmi > 30 and bmi < 50):
    print("Semiz")
else:
    print("Xatolik bor !!!")


# %%
print("-- Problem 2 --")

s1 = int(input("S1 -> "))
s2 = int(input("S2 -> "))
s3 = int(input("S3 -> "))
s4 = int(input("S4 -> "))
s5 = int(input("S5 -> "))

sonList = [s1,s2,s3,s4,s5]

engKatta = 0
engKichik = 0

engKatta = s1
for i in range(5):
    if(sonList[i] > engKatta):
        engKatta = sonList[i]

engKichik = s1
for j in range(5):
    if(sonList[j] < engKichik):
        engKichik = sonList[j]
        
print("Eng Katta son: ",engKatta)
print("Eng Kichik son: ",engKichik)


# %%
print("-- Problem 3 -- ")

exam1 = int(input("1 - Imtihon bali: "))
exam2 = int(input("2 - Imtihon bali: "))
final = int(input("Final Imtihon bali: "))

ortalama = (exam1 + exam2 + final) / 3
print("Umumiy ball: ",ortalama)
if(ortalama >= 85):
    print("Sizning bahoyingiz: 5")
elif(ortalama >= 80):
    print("Sizning bahoyingiz: 4.5")
elif(ortalama >= 75):
    print("Sizning bahoyingiz: 4")
elif(ortalama >= 70):
    print("Sizning bahoyingiz: 3.5")
elif(ortalama >= 65):
    print("Sizning bahoyingiz: 3")
elif(ortalama >= 60):
    print("Sizning bahoyingiz: 2.5")
elif(ortalama >= 55):
    print("Sizning bahoyingiz: 2")
elif(ortalama < 55):
    print("Yiqildingiz !!!")
else:
    print("Xatolik bor !!!")

# %%
print("-- Problem 4 --")

shakl = input("Uchburchak / To'rtburchak: [t/u]: ")
if(shakl == 't'):
    t1 = int(input("Tomon1: "))
    t2 = int(input("Tomon2: "))
    t3 = int(input("Tomon3: "))
    t4 = int(input("Tomon4: "))
    if(t1 == t2 and t3 == t4 and t1 == t4):
        print("Bu Kvadrad !!!")
    else:
        print("Bu oddiy To'rtburchak !!!")
elif(shakl == 'u'):
    s1 = int(input("Yon tomon: "))
    s2 = int(input("Yon tomon: "))
    asos = int(input("Asos: "))
    if(s1 == s2 and s1 == asos):
        print("Teng tomonli Uchburchak !!!")
    elif((s1**2 + asos**2) == s2**2 or (s1**2 + asos**2) == s2**2):
        print("Tog'ri burchakli Uchburchak !!!")
    elif(s1 == s2):
        print("Teng yonli Uchburchak !!!")
else:
    print("Noto'g'ri amal !!!")

# %%
"""

H - o - m - e - w - o - r - k   3

"""
#%%
print("-- problem 1 --")

while(True):
    num = int(input("Sonni kiriting: "))
    if(num == 0):
        break
    summa = 0
    son = 1
    for i in range(num):
        if(son == num):
            break
        else:
            if(num % son == 0):
                summa += son
            son += 1
    
    if(num == summa):
        print("Mukammal son !!!")
    else:
        print("Mukammal son emas !!!\a")
            
# %%
print("-- Problem 2 --")
while(True):
    number = input("Enter the number: ")
    if(number == '0'):
        break
    uzunlik = len(number)
    index = 0
    jami = 0
    while(index < uzunlik):
        jami += int(number[index]) ** uzunlik
        index += 1
    if(jami == int(number)):
        print("Armstrong !!!")
    else:
        print("Armstrong emas !!!")
print("")



#%%
print("-- Problem 3 --")
for i in range(1,10):
    print(f"\n-- {i} --\n")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")

# %%
print("-- Problem 4 --")
yigindi = 0
while(True):
    a = input("Son: ")
    if(str(a) == 'q'):
        break
    yigindi += int(a)
print("Jami: ",yigindi)
    
# %%
print("-- Problem 5 -- ")
for b in range(1,100):
    if(b % 3 == 0):
        print('-',b,'-')

# %%
print("-- Problem 6 --")

lst = list(range(101))
lst1 = [i for i in lst if i % 2 == 0]
print(*lst1)
    

