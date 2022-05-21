# PyQt5

import sys
from PyQt5 import QtWidgets


def Window():
	app = QtWidgets.QApplication(sys.argv)

	oyna = QtWidgets.QWidget()
	oyna.setText("My Calculator")

	yozuv = QtWidgets.QLabel(oyna)
	yozuv = setText("Men hali o'zgarmadim")
	yozuv.move(0,0)

	tugma = QtWidgets.QPushButton(oyna)
	tugma.setText("Buttonni bos !!")

	
	oyna.setFixedSize(200,200)
	oyna.show()
	sys.exit(app.exex_())

Oyna()



