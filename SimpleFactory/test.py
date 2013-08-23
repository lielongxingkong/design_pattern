from OperationFactory import OperationFactory
from Operation import Operation
from OperationAdd import OperationAdd
from OperationSub import OperationSub

if __name__ == '__main__':
	factory = OperationFactory()
	
	oper1 = factory.createOperation("+")
	oper1.numberA = 1
	oper1.numberB = 3
	result1 = oper1.getResult()
	print result1

	oper2 = factory.createOperation("-")
	oper2.numberA = 2
	oper2.numberB = 3
	result2 = oper2.getResult()
	print result2
	

	oper3 = factory.createOperation("*")
	oper3.numberA = 3
	oper3.numberB = 3
	result3 = oper3.getResult()
	print result3
	
	oper4 = factory.createOperation("/")
	oper4.numberA = 4
	oper4.numberB = 0
	result4 = oper4.getResult()
	print result4
