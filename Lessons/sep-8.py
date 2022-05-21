import math
import pandas


# help(int)
# help(math)
# print(dir(math))
# print(dir(pandas))

print(math.factorial(10))
print(math.tan(10.3))
print(math.log(23))
print(math.gcd(12, 23))
print(math.lcm(12,3))
print(math.floor(23.5))
print(math.fmod(23, 2))
print(math.ceil(23))

#%%
from math import factorial,tan

print(factorial(19))
print(tan(11))

from math import *

print(factorial(int(input("Son: "))))
print(tan(10))
print(gcd(10))
a = 34

# %%
from random import randint
from time import sleep
print("""---- Son Top O'yini ----
Shartlar: 
1. 3ta imkoniyatda aniq sonni topishingiz kerek !!!
2. Agar 1 - imkonni o'zida topsangiz mukofaot
1 va 10 orasida sonlar kiriting: """)

randSon = randint(1,10)
tahmin_haqqi = 3
while True:
    tahmin = int(input("Tahminningiz: "))
    while(tahmin < 0 or tahmin > 10):
        print("Faqat 1-10 orasida NIGGA !!!")
        tahmin = int(input("Tahminningiz: "))
    if(tahmin < randSon):
        print("Loading.....")
        sleep(2)
        print("Ozgina qosh NIGGA")
        tahmin_haqqi -= 1
    elif(tahmin > randSon):
        print("Loading.....")
        sleep(2)
        print("Ozgina tushir NIGGA")
        tahmin_haqqi -= 1
    else:
        if(tahmin_haqqi == 3):
            print("Mashina sizniki NIGGA")
            break
        else:
            print("Loading.....")
            sleep(2)
            print("Tabriklaymiz NIGGA topdingiz !!!")
        break
    if(tahmin_haqqi == 0):
        print("Game over NIGGA !!!")
        break


































































































