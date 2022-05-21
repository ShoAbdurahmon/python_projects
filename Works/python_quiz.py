print(not(True and False or True) or (True or not True and False))

print("asd" in "dfasdflk" and "a" < "A")


a = 10
b = 15
c = 1
while(a > 5):
    b += 2
    c += 1
    if(b % c == 0):
        break
    a -= 1
# 5 25 6

tpl = (1,2,3,4)
print(tpl.index(3))