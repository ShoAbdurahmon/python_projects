from PyQt5.QtWidgets import *
import sys
import sqlite3
import time

'''

# 1
lst = list()
for i in range(1,6):
	a = input(f"Input{i}: ")
	lst.append(a)
	lst.sort()

print(lst)

# 2
while True:
	print("Chiqish 1 ")
	vaqt = input("Vaqtni kiriting: ")
	if(vaqt == "1"):
		break
	if(vaqt[1] == ":" or vaqt[1] == " " or vaqt[1] == ";"):
		vaqt_sonda == int(vaqt[0])
	else:
		vaqt_sonda = int(vaqt[:2])

	if(vaqt_sonda <= 12 and vaqt_sonda > 0):
		print("Kunning Birinchi Qismi")
	elif(vaqt_sonda < 23 and vaqt_sonda > 12):
		print("Kunning Ikkinchi Qismi")
	else:
		print("Vaqt Noto'g'ri Kiritilgan !!!")

# 3

songacha = int(input("Qaysi songacha: "))
jami_toqlar = 0
for i in range(songacha):
	while(True):
		try:
			b = int(input(f"Input{i}: "))
			if(b % 2 != 0):
				jami_toqlar += b
		except:
			print("Qaytadan urinib ko'ring !!!")
			continue
		break
print(jami_toqlar)

# 4

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.start_ui()
	def terminalga_yozish(self):
		y = self.yozuv.text()
		print("Text:",y)
		
	def faylga_yozish(self):
		with open("file.txt","a") as fayl:
			text = self.yozuv.text()
			fayl.write(text)
			fayl.write("\n")
			fayl.close()

	def delet_qil(self):
		self.yozuv.setText("")

	def start_ui(self):
		self.yozuv = QLineEdit()
		self.faylga = QPushButton("File")
		self.term = QPushButton("Terminal")
		self.delet = QPushButton("Delete")
		self.setWindowTitle("Text Copy Paster")
		self.setFixedSize(300,200)

		h_box = QHBoxLayout()
		h_box.addStretch()
		h_box.addWidget(self.term)
		h_box.addWidget(self.faylga)
		h_box.addWidget(self.delet)
		v_box = QVBoxLayout()
		v_box.addWidget(self.yozuv)
		v_box.addLayout(h_box)

		self.setLayout(v_box)
		self.show()

		self.term.clicked.connect(self.terminalga_yozish)
		self.faylga.clicked.connect(self.faylga_yozish)
		self.delet.clicked.connect(self.delet_qil)

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())



# 5
'''

username = "gulchapchap"
password = "1122"


print("""1. Barcha Malumotlarni Ko'rish
2. Musiqa Qidirish
3. Admin
4. Menyu
5. Exit""")
boglanish = sqlite3.connect("musiqiy.db")
kursor = boglanish.cursor()
while True:
	def create_table():
		boglanish = sqlite3.connect("musiqiy.db")
		kursor = boglanish.cursor()
		kursor.execute("CREATE TABLE IF NOT EXISTS musiqalar (nomi text, yil int, davlat text,vaqt text,bastakor text,turi text,olchami text)")
		boglanish.commit()
	def barchasini_korish():
		kursor.execute("SELECT * FROM musiqalar")
		malumotlar = kursor.fetchall()
		print("Malumotlar Kelmoqda....")
		time.sleep(2)
		for i in malumotlar:
			print(*i)
	def musiqa_qidirish():
		a = input("Qaysi Musiqani Qidiryapsiz: ")
		kursor.execute("SELECT * FROM musiqalar WHERE nomi = ?",(a,))
		malumotlar = kursor.fetchall()
		print("Malumotlar Kelmoqda....")
		time.sleep(2)
		for i in malumotlar:
			print(*i)
	def admin_panel():
		user = input("Username: ")
		pasw = input("Password: ")
		print("Tekshirilmoqda.....")
		time.sleep(3)
		print()
		if(password == pasw and user == username):
			print("Hush Kelibsiz !!!")
			print("""1. Musiqa Qo'shish
2. Musiqani o'chirish
3. Orqaga""")
			while(True):
				tanlash = input("Tanlang: ")
				if(tanlash == "1"):
					qoshish()
				elif(tanlash == "2"):
					delet_qil()
				elif(tanlash == "3"):
					print("--- Orqaga qaytildi ---")
					print("Menyuni ko'rish uchun 4")
					print()
					break


	def delet_qil():
		c = input("Qaysi Musiqani delete qilasiz: ")
		kursor.execute("DELETE FROM musiqalar WHERE nomi = ?",(c,))
		boglanish.commit()
		print("--- Musiqa Delete Qilindi ---")
		print()


	def menyu():
		print("""1. Barcha Malumotlarni Ko'rish
2. Musiqa Qidirish
3. Admin
4. Menyu
5. Exit""")
	def qoshish():
		print("--- Kiritish uchun Malumotlar ---")
		ism = input("Musiqa nomi: ")
		yili = input("Yili: ")
		davlati = input("Davlati: ")
		vaqti = input("Vaqti: ")
		autor = input("Basakori: ")
		turi = input("Turi: ")
		olcham = input("O'lchami: ")


		kursor.execute("INSERT INTO musiqalar VALUES (?,?,?,?,?,?,?)",(ism,yili,davlati,vaqti,autor,turi,olcham))
		boglanish.commit()
		print("--- Muvaffaqiyatli Qo'shildi ---")
		print()

	create_table()
	kursor.execute("INSERT INTO musiqalar VALUES ('I can fly',2017,'russia','22:10','Xcho','Jass','5.3 mb')")
	tanlov = input("Tanlang: ")
	if(tanlov == "1"):
		barchasini_korish()
	elif(tanlov == "2"):
		musiqa_qidirish()
	elif(tanlov == "3"):
		admin_panel()
	elif(tanlov == "4"):
		menyu()
	elif
		continue











	



