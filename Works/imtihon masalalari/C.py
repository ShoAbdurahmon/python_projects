from time import sleep

string = input("So'z: ")
for i in string:
    print(i,end='')
    sleep(1)
    
print("")

teskari = string[::-1]
for j in teskari:
    print(j,end='')
    sleep(1)
