from PyQt5.QtWidgets import *
import sys
from random import randint
from time import sleep



class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Son Top O'yini")

		self.start_ui()
		self.setFixedSize(300,150)
		self.show()
	def start_ui(self):
		self.text = QLineEdit()
		self.oyin = QLabel("Son Top O'yini")
		self.send = QPushButton("Send")
		self.yozuv = QLabel()
		self.restart = QPushButton("Restart")
		self.text.setFixedSize(180,20)
		h_box = QHBoxLayout()
		h_box1 = QHBoxLayout()
		v_box = QVBoxLayout()
		h_box.addWidget(self.text)
		h_box.addWidget(self.send)
		h_box1.addWidget(self.yozuv)
		h_box1.addWidget(self.restart)
		v_box.addWidget(self.oyin)
		v_box.addStretch()
		v_box.addLayout(h_box)
		v_box.addLayout(h_box1)
		v_box.addStretch()
		self.setLayout(v_box)
		self.send.clicked.connect(self.send_funk)
		self.restart.clicked.connect(self.restart_funk)
	def restart_funk(self):
		self.tahmin_haqqi = 3
		self.randSon = randint(1,10)
	def send_funk(self):
		self.tahmin_haqqi -= 1
		text = self.text.text()
		tahmin = int(text)

	    if(tahmin < self.randSon):
			self.yozuv.setText("Loading.....")
	        sleep(2)
	        self.yozuv.setText("Ozgina qosh NIGGA")
	    elif(tahmin > self.randSon):
	        self.yozuv.setText("Loading.....")
	        sleep(2)
	        self.yozuv.setText("Ozgina tushir NIGGA")
	    else:
	        self.yozuv.setText("Loading.....")
	        sleep(2)
	        self.yozuv.setText("Tabriklaymiz NIGGA topdingiz !!!")
        	
	    if(tahmin_haqqi == 0):
	        self.yozuv.setText("Game over NIGGA !!!")
	        self.yozuv.setText("Aniq javob: {}".format(self.tahmin_haqqi))
	        


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())


