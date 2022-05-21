# %% Uyga vazifa 1
from random import randint
sanoq = 3
while True:
    a = randint(100,999)
    if(a % 5 == 0):
        sanoq -= 1
        print(a)
    if(sanoq == 0):
        break

# %% 2
b = input("So'z: ")
print(b[1::2])


# %% 3

def tubniTop(son):
    if(son == 1 or son == 2 or son == 3):
        return True
    for i in range(2,son-1):
        if(son % i == 0):
            return False
    return True


s1 = int(input("Son 1: "))
s2 = int(input("Son 2: "))

for s in range(s1,s2):
    if(tubniTop(s)):
        print(s,"Tub son!!!")
    else:
        print(s,"Tub Emas !!!")
# %% 5

def faktoriyalniTop(son):
    jami = 1
    for d in range(1,son+1):
        jami *= d
    print(f"{son} ning faktoriyali {jami}")


faktoriyalniTop(6)

# %% 6
son = input("Sonni kiriting: ")
print(son[-1::-1])

# %% 7
lst = [12,3,345,567,2,435,76,4,675]
lst.sort(reverse=True)
print(lst[0])
