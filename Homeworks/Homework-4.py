print("-- Problem 1 --")


soz = input("So'zni kiriting: ")
lst = list()
index = 0

if(len(soz) % 4 == 0): 
    lst += soz
    while(index < len(soz) / 2):
        print(lst[index],end='')
        index += 1
    index = len(soz) - 1
    while(index >= len(soz) / 2):
        print(lst[index],end='')
        index -= 1

# %%
print()
print("-- Problem 2 --")

string = input("String: ")
sozList = list()
sozList += string

sozList[0] = ord(sozList[0]) - 32
sozList[-1] = ord(sozList[-1]) - 32
sozList[0] = chr(sozList[0])
sozList[-1] = chr(sozList[-1])
print(*sozList)

# %%
print("-- Problem 3 --")
while(True):
    sozlarSoni = 1
    a = input("Gap: ")  
    if(a == "0"):
        print("Yana Kutib Qolamiz !!!")
        break
    for i in a:
        if(ord(i) == 32):
            sozlarSoni += 1
    print("So'zlar Soni : ",sozlarSoni)
            
      

# %%
print("-- problem 4 --")

# =============================================================================
# body mass index
# =============================================================================

# %%
print("-- Problem 5 --")

km = int(input("Necha km yo'l yurdingiz: "))
pul = int(input("Km benzin narxi: "))
jami = km * pul

print("Jami:",jami,"dollar to'lashingiz kerak !!!")

# %%
print("-- Problem 6 --")

import math
b1 = int(input("a = "))
b2 = int(input("b = "))

gipotenuza = b1**2 + b2**2
gipotenuza = math.sqrt(gipotenuza)

print("Uchburchak Gipotenuzasi:",gipotenuza)

# %%
print("-- Problem 7 --")

# =============================================================================
# eng katta son topish
# =============================================================================

# %%
print("-- Problem 8 --")

while(True):
    str1 = input("So'z kiriting: ")
    str2 = input("Chetga qo'shiladigan so'z: ")
    
    index = 0
    if(str1 == '0'):
        break
    lst = list()
    lst += str2
    lenth = len(str2)
    
    while(index < lenth):
        if(index == int(lenth / 2)):
            print(str1,end='')
        print(lst[index],end='')
        index += 1

# %%
print("-- Problem 9 --")

string = input("string kiriting: ")
list1 = list()
list1  += string

list1.append(list1[0])
list1.pop(0)
list1.insert(0,list1[-2])
list1.pop(-2)

sanoq = 0
while(sanoq < len(string)):
    print(list1[sanoq],end='')
    sanoq += 1

