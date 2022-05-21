rng = int(input("Range: "))
for i in range(rng + 1):
    print(i)

# %% Methodlar
lst1 = []
lst1.append(10)

tpl = (1,2,3)
print(tpl.index(2))

# %% Functons

print("Hello world")
a = list()
input()
range()
type()

# %% user defined
def qosh():
    print(10+10)
qosh()
def sayHello(ism):
    print(f"Salom {ism}")
sayHello("John")
def topla(a,b,c):
    print(f"{a} + {b} + {c} = {a+b+c}")
topla(1,2,3)
def faktoriyal(son):
    f = 1
    if(son == 1 or son == 0):
        print("son faktoriyali 1 !!!")
    else:
        while(son >= 1):
            f *= son
            son -= 1
        print(f"son faktoriyali: {f}")
faktoriyal(6)

# %%
def qosh(a,b):
    return a + b
a = qosh(10,20)
print(a)

def a1(b1):
    return b1 + 10
def c1(d1):
    return d1 + 10

print(a1(c1(10)))

def a(b):
    return b + 1
def b(c):
    return c + 2
def c(d):
    return d + 3
print(a(b(c(19))) + b(a(c(31)))

      

# %%
b = 23
while(True):
    a = 132
    break

print(a)

# local

def a():
    bb = 23
    print("Hello a",bb)

a()

# %%
def kvOl(a):
    return a * a

print(kvOl(10))

kvOllambda = lambda x : x * x
print(kvOllambda(10))

funk1 = lambda soz : soz[::-1]
print(funk1("assalom"))

jami = lambda a,b,c : a+b+c
print(jami(11, 12, 32))


juftMi = lambda son : son % 2 == 0
if(juftMi(45)):
    print("Juft:")
else:
    print("Toq!!!")
# %%
print("Prime number")

def prime_n(son):
    for i in range(2,son):
        if(son % 2 == 0):
            return False
    return True

while True:
    son = input("sonni kiriting: ")
    if(son == 'q'):
        break
    son = int(son)
    if(son == 1):
        print("Tub son")
    elif(son == 2):
        print("Son Tub !!!")
    else:
        if(prime_n(son)):
            print("Son Tub Ekan")
        else:
            print("Son Tub Emas Ekan !!!")










