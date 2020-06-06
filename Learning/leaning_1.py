a = 1
n = 1
import math
while n <= 100:
   a = (-math.sqrt(2)) ** a
   if a == (-math.sqrt(2)) ** a:
      print("They are equal ")
   print(a)
   n += 1