from CashNormal import CashNormal
from CashRebate import CashRebate
from CashReturn import CashReturn
from CashContext import CashContext

type = 'return'

if type == 'normal':
	context = CashContext(CashNormal())
elif type == 'rebate':
	context = CashContext(CashRebate(0.8))
elif type == 'return':
	context = CashContext(CashReturn(300, 100))

print context.getResult(1000)
