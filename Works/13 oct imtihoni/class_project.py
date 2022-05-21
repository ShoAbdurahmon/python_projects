class Uy():
	def __init__(self,joylashuv, xonalari, narxi):
		self.joylashuv = joylashuv
		self.xonalari = xonalari
		self.narxi = narxi
	def __str__(self):
		return f"""Joylashuv: {self.joylashuv}
Xonalari: {self.xonalari}
Narxi: {self.narxi}"""

meningUyim = Uy("Chorsu",5,300)
print(meningUyim)

class Dom(Uy):
	def 