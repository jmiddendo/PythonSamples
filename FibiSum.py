# Find the sum of all of the Fibi numbers below a user defined number.

def calcFibiSeq(n):
    retVal = 0
    currentNumber, previousNumber = 0, 1
    while (currentNumber < n):
        previousNumber, currentNumber = currentNumber, previousNumber + currentNumber
        if (currentNumber < n and currentNumber % 2 == 0):
            retVal += currentNumber
    return retVal
            
 
def main():

    queryLoop = True

    while(queryLoop):
        endNumber = input('Please enter a number: ')
    
        try:
            endNumber = int(endNumber)
        except:
            print('That was not a valid number!')
        else:
            queryLoop = False
            print(calcFibiSeq(endNumber))

if __name__ == '__main__':
    main()
