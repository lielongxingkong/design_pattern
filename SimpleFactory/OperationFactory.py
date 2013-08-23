from OperationAdd import OperationAdd
from OperationSub import OperationSub
from OperationMul import OperationMul
from OperationDiv import OperationDiv
class OperationFactory():
	def __init__(self):
		pass
	def createOperation(self, operate):
		oper = self.getOperation(operate)
		return oper
	def getOperation(self, operate):
		if operate == "+":
			oper = OperationAdd()
		elif operate == "-":
			oper = OperationSub()
		elif operate == "*":
			oper = OperationMul()
		elif operate == "/":
			oper = OperationDiv()
		else:
			oper = None
		return oper 

