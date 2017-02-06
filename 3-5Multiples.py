# Sum of multiples of 3 and 5

def main():
    endInteger = input('Enter a number that you want to sum to: ')
    retVal = 0

    try:
        endInteger = int(endInteger)
    except:
        print('That is not a valid number.')
    else:
        for x in range(endInteger):
            if (x % 3 == 0 or x % 5 == 0):
                retVal += x
        print(retVal)
                
        
if __name__ == '__main__':
    main()
