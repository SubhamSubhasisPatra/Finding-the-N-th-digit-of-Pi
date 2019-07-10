'''
Pi  = SUMk=0 to infinity 16-k [ 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6) ]
Refer this page for Pi calculation = https://www.math.hmc.edu/funfacts/ffiles/20010.5.shtml
https://github.com/SubhamSubhasisPatra/Finding-the-N-th-digit-of-Pi

'''

from __future__ import division
import math
from decimal import Decimal as D
from decimal import getcontext

precision = int(input("Enter precision : "))
getcontext().prec = precision
pi = D(0)
for k in range(precision+1):
	pi += D(math.pow(16, -k)) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))
print('PI :' , pi)
