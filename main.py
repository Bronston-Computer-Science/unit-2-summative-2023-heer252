print('for basic  math, choose option 1')
print('for trig calculations, choose option 2')
print('for unit conversion, choose option 3')
print('to exit   choose option 4')
opt = float(input())

if opt==1:
 import basic_math
elif opt==2:
 import trig_calculator

elif opt==3:
 import unit_conversion
elif opt==4:
 print ("exiting the code") 
