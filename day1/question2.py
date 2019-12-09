import math
from index import getData, calculateFuel2

# Question 2
totalFuel2 = 0
for i in getData():
    totalFuel2 += calculateFuel2(i)

print(totalFuel2)
