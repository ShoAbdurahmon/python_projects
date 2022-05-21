from math import *
# print("----- Calculator -----")

# print("""       Amallar: 
# 1: Qo'shish
# 2: Ayrish
# 3: Ko'paytirish
# 4: Bo'lish
# 5: Mod
# 6: Faktoriyal
# 7: Kvadrat
# 8: Kub
# 9: Ildiz
# 10: Ekub""")
# amal = int(input("Amalni kiriting: "))
# if(amal == 1):
#     a = int(input("Birinchi son: "))
#     b = int(input("Ikkinchi son: "))
    


def qosh(son1,son2):
    return son1 + son2
def ayrish(son1,son2):
    return son1 - son2
def bolish(son1,son2):
    return son1 / son2
def kopaytirish(s1,s2):
    return s1 * s2
def mod(son,son1):
    return son % son1
def faktoriyal(son):
    return factorial(son)
def kvadrat(son):
    return son * son
def kub(son):
    return son * son * son
def ildiz(son):
    return sqrt(son)
def ekub(son,son1):
    return gcd(son, son1)
