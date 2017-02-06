# Accept a file name and count the number of line in the said file

def queryFileName():
    getName = True
    while(getName):
        fileName = input('Please enter a file name: ')
        
        try:
            retValue = open(fileName,'r')

        except:
            print('There was an issue opening the file.  Please try again!')
            print('')
            continue
            
        if (retValue.mode == 'read'):
            print('The file failed to open.')
            print('')
            continue
        
        getName = False
        
    return retValue

def main():
    testFile = queryFileName()

    i = 0

    for line in enumerate(testFile):
        i += 1
    print('There are {} lines in the file!'.format(i))
        
    
    
    testFile.close()
        
    

if __name__ == '__main__':
    main()
