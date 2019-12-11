from index import isInAssendingOrder,  isRepeatedAndContainDouble2

machedPasswords = 0
for n in range(178416, 676461):
    n = str(n)
    if isInAssendingOrder(n) and isRepeatedAndContainDouble2(n):
        machedPasswords += 1

print(machedPasswords)
