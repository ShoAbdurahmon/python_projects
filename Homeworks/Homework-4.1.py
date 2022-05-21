def perfect(son):
    jami = 0
    for i in range(1,son):
        if(son % i == 0):
            jami += i
    if(jami == son):
        return True
    else:
        return False

for a in range(1,100000):
    if(perfect(a) == True):
        print(f"{a} Ferfect son !!!")

# %%
def ekubniTop(son1,son2):
    temp = 1
    while(temp != 0):
        temp = son1 % son2
        if(temp == 0):
            return son2
        son1 = son2
        son2 = temp

print(ekubniTop(20,32))

# %%

def ekukniTop(s1, s2):
    engKatta = s1
    while True:
        if(engKatta % s1 == 0 and engKatta % s2 == 0):
            return engKatta
        engKatta += 1

print(ekukniTop(3, 2))


# %%

def sozgaOgir(number):
    birlik = number % 10
    onlik = number // 10
    string = str()
    
    if(onlik == 1):
        string = "O'n "
    elif(onlik == 2):
        string = "Yigirma "
    elif(onlik == 3):
        string = "O'ttiz "
    elif(onlik == 4):
        string = "Qirq "
    elif(onlik == 5):
        string = "Ellik "
    elif(onlik == 6):
        string = "Oltmish "
    elif(onlik == 7):
        string = "Yetmish "
    elif(onlik == 8):
        string = "Sakson "
    elif(onlik == 9):
        string = "To'qson "
        
    if(birlik == 1):
        string += "Bir"
    elif(birlik == 2):
        string += "Ikki"
    elif(birlik == 3):
        string += "Uch"
    elif(birlik == 4):
        string += "To'rt"
    elif(birlik == 5):
        string += "Besh"
    elif(birlik == 6):
        string += "Olti"
    elif(birlik == 7):
        string += "Yetti"
    elif(birlik == 8):
        string += "Sakkiz"
    elif(birlik == 9):
        string += "To'qqiz"
    return string

print(sozgaOgir(4))
    
# %%
def pifagor(s):
    for i in range(1,s):
        for t in range(1,i):
            print()
        print("")
pifagor(12)






























































