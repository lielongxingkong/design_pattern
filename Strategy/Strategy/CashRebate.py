from CashSuper import CashSuper

class CashRebate(CashSuper):
	def __init__(self, moneyRebate = 1):
		self.moneyRebate = moneyRebate 
	def acceptCash(self, money):
		return money * self.moneyRebate 
if __name__ == "__main__":
	cr = CashRebate(0.8)
	result = cr.acceptCash(100)
	print result 
