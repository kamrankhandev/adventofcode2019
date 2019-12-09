
def isInAssendingOrder(number):
    number = str(number)
    for i in range(len(number) - 1):
        if int(number[i + 1]) < int(number[i]):
            return False
    return True


def isRepeated(number):
    number = str(number)
    # https://stackoverflow.com/a/37867488
    return len(set(number)) < len(number)


def isRepeatedAndContainDouble1(number):
    number = str(number)

    isConsecutive = False
    if(isRepeated(number)):
        for i in range(len(number) - 1):
            if int(number[i + 1]) == int(number[i]):
                isConsecutive = True
                break

    return isConsecutive


def isRepeatedAndContainDouble2(number):
    number = str(number)

    consecutiveDigitsCount = 0
    if(isRepeated(number)):
        for i in range(len(number) - 1):
            if int(number[i + 1]) == int(number[i]):
                consecutiveDigitsCount += 1
            else:
                if(consecutiveDigitsCount == 1):
                    return True
                consecutiveDigitsCount = 0

    return consecutiveDigitsCount == 1
