from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QApplication, QLineEdit, QPushButton
import sys
import sqlite3
from time import sleep

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.ui()
		self.connecting()
	def connecting(self):
		boglanish = sqlite3.connect("accounts.db")
		self.kursor = boglanish.cursor()
		self.kursor.execute("CREATE TABLE IF NOT EXISTS gmails (user text, pass text)")
		boglanish.commit()
	def tizimga_kirit(self):
		user = self.username.text()
		passw = self.password.text()
		self.username.setText("")
		self.password.setText("")
		a = "SELECT * FROM gmails WHERE user = ? And pass = ?"
		self.kursor.execute(a,(user,passw))
		data = self.kursor.fetchall() 
		if len(data) == 0:
			self.yozuv.setText("Boshqatdan urinib ko'ring")
		else:
			self.yozuv.setText("Hush Kelibsiz !!!")

	def royhatdan_ot(self):
		if(len(self.password.text()) != 0 or len(self.username.text()) != 0):
			a = self.password.text()
			b = self.username.text()
			self.username.setText("")
			self.password.setText("")
			self.kursor.execute("INSERT INTO gmails VALUES (?,?)",(b,a))
			self.yozuv.setText("Yangi Account Muvaffaqiyatli o'rnatildi !!!")
		else:
			self.yozuv.setText("Username va Parolni kiriting bro !!")
			

	def ui(self):
		self.setWindowTitle("Accounts Google")
		self.username = QLineEdit()
		self.password = QLineEdit()
		self.password.setEchoMode(QLineEdit.Password)
		self.google = QLabel("                    GOOGLE")
		self.kirish = QPushButton("Kirish")
		self.royhat = QPushButton("Yangi Account")
		self.username.setFixedSize(150,20)
		self.password.setFixedSize(150,20)
		self.yozuv = QLabel("Username va Parolni kiriting !!!")
		
	
		h_box1 = QHBoxLayout()
		h_box = QHBoxLayout()
		h_box.addWidget(self.kirish)
		h_box.addWidget(self.royhat)
		v_box = QVBoxLayout()
		v_box.addWidget(self.google)
		v_box.addStretch()
		v_box.addWidget(self.username)
		v_box.addWidget(self.password)
		v_box.addWidget(self.yozuv)
		v_box.addStretch()
		v_box.addLayout(h_box)
		v_box.addStretch()
		h_box1.addStretch()
		h_box1.addLayout(v_box)
		h_box1.addStretch()

		self.setLayout(h_box1)
		self.royhat.clicked.connect(self.royhatdan_ot)
		self.kirish.clicked.connect(self.tizimga_kirit)
		self.setFixedSize(200,200)
		self.show()


app = QApplication(sys.argv)
oyna = Window()
sys.exit(app.exec_())



























