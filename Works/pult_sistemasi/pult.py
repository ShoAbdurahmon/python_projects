import time
from random import randint
class Pult():
    def __init__(self,tv_holat='Off',tv_ovoz = 0,kanal_listi= ["bbc","my5"],kanal="bbc"):
        print("Pult Kiritilmoqda .......")
        self.tv_holat = tv_holat
        self.tv_ovoz = tv_ovoz
        self.kanal_listi = kanal_listi
        self.kanal = kanal
    def __str__(self):
        return "Pult Holati: {}".format(self.tv_holat)
    
    def ovoz_ozgartir(self):
        while True:
            soniya = 5
            belgi = input("+ | - : ")
            if(belgi == '+'):
                if(self.tv_ovoz < 5):
                    self.tv_ovoz += 1
                    print("Ovoz +: {}".format(self.tv_ovoz))
                    soniya = 5
                    continue
            elif(belgi == '-'):
                if(self.tv_ovoz > 0):
                    self.tv_ovoz -= 1
                    print("Ovoz -: {}".format(self.tv_ovoz))
                    soniya = 5
                    continue
            else:
                print("Ovoz Yangilanish Tugatildi...")
                break
            for i in range(5):
                time.sleep(1)
                soniya -= 1
                print(".",end='')
            if(soniya <= 0):
                
                break
    def tv_power(self):
        if(self.tv_holat == 'On'):
            print("Tv ochirilmoqda...")
            self.tv_holat = "Off"
        else:
            print("Tv yoqilmoqda...")
            self.tv_holat = "On"
    def random_kanal(self):
        random_kanal = randint(0,len(self.kanal_listi)-1)
        self.kanal = self.kanal_listi[random_kanal]
    def kanal_qosh(self,yangi_kanal):
        self.kanal_listi.append(yangi_kanal)
        print("Yangi kanal qoshildi.....")







