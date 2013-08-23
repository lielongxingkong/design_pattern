from CashNormal import CashNormal
from CashRebate import CashRebate
from CashReturn import CashReturn

class CashFactory:
	def __init__(self):
		pass
	def getCash(self, type):
		if type == 'normal':
			cash = CashNormal()
		elif type == 'rebate':
			cash = CashRebate(0.8)
		elif type == 'return':
			cash = CashReturn(300, 100)
		else:
			cash =  None
		return cash

	def createCash(self, type):
		cash = self.getCash(type)
		return cash

if __name__ == "__main__":
	factory = CashFactory()
	cash = factory.createCash("return")
	result = cash.acceptCash(700)
        print result
	
	cash = factory.createCash("rebate")
	result = cash.acceptCash(700)
        print result
