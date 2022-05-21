print("Dardga Davo Klinikasi")
print("""
Tanlang: 
1. Kasallik
2. Dorilar
3. Doktorlar""")
tanlov = int(input("Tanlang: "))
if(tanlov == 1):
    print("""
Kasalliklar:
1. Covid 19
2. Shamollash
3. Grip
4. Sariq kasalligi""")

    dct = {1:"Covid 19 2020 yil Xitoydan chiqqan kasal bo'lib, butun dunyoni zararladi.\nCovid juda havfli kassalik bo'lib, insonda o'ta og'ir asoratlar boladi.",
           2:"Shamollash asosan bahor va kuz oylarida orttiriladi. U yuqumli kassalik bo'lib,uncahlik havfli emas. Lekin chorasini korish kerak.",
           3:"Grip ham mavsumli kasalliklar turiga kiradi.Immuniteti pastlarda juda og'ir o'tadi.",
           4:"Sariq kasalligi o'ta havfli bo'lib unga chalingan inson darhol kasalhonaga borishi kerak! Kasalga chalinganligingizni turli yollar bilan tekshirishingiz mumkin!"}
    print(dct[int(input("Kiriting: "))])