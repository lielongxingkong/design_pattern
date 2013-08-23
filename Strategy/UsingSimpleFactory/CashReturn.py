from CashSuper import CashSuper
from math import floor
class CashReturn(CashSuper):
	def __init__(self, moneyCondition, moneyReturn):
		self.moneyReturn = moneyReturn 
		self.moneyCondition = moneyCondition
	def acceptCash(self, money):
		result = money
		if money >= self.moneyCondition:
			result = money - floor(money / self.moneyCondition) * self.moneyReturn
		return result

if __name__ == "__main__":
	cr = CashReturn(300, 100)
	result = cr.acceptCash(700)
	print result
	
