import sqlite3
from time import sleep

boglanish = sqlite3.connect("komp.db")
kursor = boglanish.cursor()

def add_table():
	kursor.execute("CREATE TABLE IF NOT EXISTS komputer (nom text, narx text, son text)")
	boglanish.commit()
def komp_korish():
	kursor.execute("SELECT * FROM komputer")
	malumotlar = kursor.fetchall()
	print("Malumotlar Kelmoqda....")
	sleep(2)
	for i in malumotlar:
		print(*i)
def faylga_yozish():
	kursor.execute("SELECT * FROM komputer")
	malumot = kursor.fetchall()
	with open("komputers.txt","a") as fayl:
		for i in malumot:
			string = str(i)
			fayl.write(string)
			fayl.write("\n")
			fayl.close()


def del_all():
	kursor.execute("DELETE FROM komputer")
	boglanish.commit()


def komp_qosh():
	k_ism = input("Komputer Nomi: ")
	k_narx = input("Narxi: ")
	k_son = input("Soni: ")
	kursor.execute("INSERT INTO komputer VALUES (?,?,?)",(k_ism,k_narx,k_son))
	boglanish.commit()

def komp_sotish():
	qaysi_komp = input("Qaysi komputerdan olmoqchisiz: ")
	print("Iltimos kuting....")
	sleep(2)
	kursor.execute("SELECT * FROM komputer WHERE nom = ?",(qaysi_komp,))
	malumotlar = kursor.fetchall()
	kursor.execute("SELECT son FROM komputer WHERE nom = ?",(qaysi_komp,))
	son_malumot = kursor.fetchall()
	if(malumotlar):
		print(*malumotlar)
		soni = input("Nechadona olasiz: ")
		if(int(soni) <= son_malumot[0][0]):
			qoldiq = son_malumot[0][0] - int(soni)
			print("Xaridingiz uchun Rahmat !!!")
			kursor.execute("UPDATE komputer SET son = ? WHERE nom = ?",(qoldiq,qaysi_komp))
			boglanish.commit()
		else:
			print(f"Bu Mahsulotdan {son_malumot[0][0]} ta Bor.")

	else:
		print("Komputer Nomi Noto'gri kiritilgan !!!")
		print("Qaytabdan Urinib Ko'ring.")

def komp_ochir():
	komp_nomi = input("Qaysi Komputerni O'chirmoqchisiz: ")
	kursor.execute("DELETE FROM komputer WHERE nom = ?",(komp_nomi,))
	boglanish.commit()

add_table()

print("""1. Komputerlarni ko'rish
2. Komputer Qo'shish
3. Sotib olish
4. Komputer Olib tashlash
5. Malumotlarni faylga Yozish
6. Barchasini O'chirish
7. Menu
0. Exit""")
while(True):
	

	tanlov = input("Tanlang: ")
	tanlov = str(tanlov)
	print()
	if(tanlov == "6"):
		break
	elif(tanlov == "5"):
		print("""1. Komputerlarni ko'rish
2. Komputer Qo'shish
3. Sotib olish
4. Komputer Olib tashlash
5. Malumotlarni faylga Yozish
6. Barchasini O'chirish
7. Menu
0. Exit""")


	if(tanlov == "1"):
		komp_korish()
	elif(tanlov == "2"):
		komp_qosh()
	elif(tanlov == "3"):
		komp_sotish()
	elif(tanlov == "4"):
		komp_ochir()
	elif(tanlov == "5"):
		faylga_yozish()
	elif(tanlov == "6"):
		del_all()







	











