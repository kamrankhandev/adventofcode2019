import math
from index import getData, calculateFuel1

# Question 1
totalFuel1 = 0
for i in getData():
    totalFuel1 += calculateFuel1(i)

print(totalFuel1)
