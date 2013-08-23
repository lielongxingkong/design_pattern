from CashSuper import CashSuper 

class CashContext:
	def __init__(self, CashSuper):
		self.cashSuper = CashSuper
	def getResult(self, money):
		return self.cashSuper.acceptCash(money)
