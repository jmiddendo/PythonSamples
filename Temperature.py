### Convert Celsius into Fahrenheit
### The formula for the conversion is (temp * 9)/5+32 

maxLimit = 50000;
midLimit = 10;
minLimit = 0;

def queryMinValue():
    checkValue = True

    while (checkValue):
        lowerAmount = input('Please give in a lower limit, limit >= {} and <= {}: '.format(minLimit, midLimit));

        try:
            lowerAmount = int(lowerAmount)
        except:
            print('Please enter a valid number!\n');
            continue;

        if (lowerAmount < minLimit or lowerAmount > midLimit):
            print('Please enter a number within the valid range\n'.format(minLimit));
            continue;

        checkValue = False;

        return lowerAmount

def queryMaxValue():
    checkValue = True

    while (checkValue):
        higherAmount = input('Please give in a higher limit, {} > limit <= {}: '.format(midLimit, maxLimit));

        try:
            higherAmount = int(higherAmount)
        except:
            print('Please enter a valid number!\n');
            continue;

        if (higherAmount <= midLimit or higherAmount > maxLimit):
            print('Please enter a number within the valid range\n'.format(minLimit));
            continue;

        checkValue = False;

        return higherAmount

def queryStepValue():
    checkValue = True

    while (checkValue):
        stepAmount = input('Please give in a step, {} < step <= {}: '.format(minLimit, midLimit));

        try:
            stepAmount = int(stepAmount)
        except:
            print('Please enter a valid number!\n');
            continue;

        if (stepAmount <= minLimit or stepAmount > midLimit):
            print('Please enter a number within the valid range\n'.format(minLimit));
            continue;

        checkValue = False;

        return stepAmount
    
def displayConversion(start, end, step):
    print('Celsius         Fahrenheit')
    print('-------         ----------')

    x = float(start)

    while(x <= end):
        x = round(x, 6)
        y = round(((x * 9) / 5) + 32, 6)
        print('{0:.6f}       {0:.6f}   '.format(x, y))
        x += step

def main():
    
    lowerAmount = queryMinValue();   
    higherAmount = queryMaxValue();
    stepAmount = queryStepValue();
    print('\n')
    displayConversion(lowerAmount, higherAmount, stepAmount)

    

if __name__ == '__main__':
    main();
