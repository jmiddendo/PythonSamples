class Ebook(object):
    def __init__(self, newAuthor = 'Anon', newTitle = 'Unknown', newRating = 'child'):
        self.author = newAuthor
        self.title = newTitle
        self.rating = newRating

    def toString(self):
        return str(self.title) + ',' + str(self.author) + ',' + str(self.rating)
        

class BookList(object):
    def __init__(self):
        self.invBookList = list();

    def addBook(self, newBook):
        self.invBookList.append(newBook)

    def removeBook(self, oldBook):
        self.invBookList.remove(oldBook)

    def displayBookList(self):
        for book in self.invBookList:
            print(book.title + ',' + book.author + ',' + book.rating.strip())

    def filterListByName(self, filterCrit):
        retVal = list()
        for book in self.invBookList:
            if (book.title.find(filterCrit) != -1):
                retVal.append(book)
        return retVal

class BorrowerBookList(object):
    def __init__(self, newList = list()):
        self.borrowBookList = list(newList)

    def addBook(self, newBook):
        if newBook not in self.borrowBookList:
            self.borrowBookList.append(newBook)
        else:
            print('Book has already been rented!  Please try again!')

    def removeBook(self, oldBook):
        self.borrowBookList.remove(oldBook)

    def displayBookList(self):
        for book in self.borrowBookList:
            print(book.title + ',' + book.author + ',' + book.rating.strip())
    

class Borrower(object):

    def __init__(self, newID = -1, newName = "Generic Borrower", newAge =  33, newList = list()):
        self.borrowerIdentification = newID
        self.borrowerName = newName
        self.borrowerAge = newAge
        self.borrowerList = BorrowerBookList(newList)

    def displayBorrowerList(self):
        print('The borrower\'s booklist is: ')
        self.borrowerList.displayBookList()

    def toString(self):
        retVal = str(self.borrowerName) + ',' + str(self.borrowerIdentification) + ',' + str(self.borrowerAge)
        for book in self.borrowerList.borrowBookList:
            retVal += ',' + book.toString()
        return retVal

class BorrowerList(object):
    def __init__(self):
        self.borrowerList = list()
        self.borrowValidation = Validation()

    def addBorrower(self, newBorrower = None):

        if (newBorrower == None):
    
            runAgain = True
            tempID, tempAge = 0, 0
            tempName = ""

        
            while(runAgain):
                tempID = input('Please enter the user\'s identification number: ')

                if (not self.borrowValidation.isValidNumber(tempID,1,100)):
                    print('\nPlease enter a valid id number! Try again.\n')
                    continue
                else:
                    tempID = int(tempID)

                if (not self.borrowValidation.isAvailableIdentification(tempID,self.borrowerList)):
                    print('\nThe id you entered is already taken!  Please try again!\n')
                    continue

                runAgain = False

            runAgain = True

            while(runAgain):

                tempName = input('Please enter the user\'s name: ')

                if (not self.borrowValidation.isValidString(tempName)):
                    print('\nPlease enter a valid name! Try again.\n')
                    continue

                runAgain = False
        
            runAgain = True

            while(runAgain):
                tempAge = input('Please enter the user\'s age: ')

                if (not self.borrowValidation.isValidNumber(tempAge,6,109)):
                    print('\nPlease enter a valid age! Try again.\n')
                    continue
                else:
                    tempAge = int(tempAge)

                runAgain = False
            
            self.borrowerList.append(Borrower(tempID, tempName, tempAge))

            print('\nThe borrower has been added!')

        else:
            self.borrowerList.append(newBorrower)


    def countBorrower(self):
        return len(self.borrowerList)

    def displayBorrowers(self):
        for borrower in self.borrowerList:
            print('The borrower\'s ID is ' + str(borrower.borrowerIdentification))
            print('The borrower\'s name is ' + borrower.borrowerName)
            print('The borrower\'s age is ' + str(borrower.borrowerAge))
            borrower.displayBorrowerList()
            print('')
            

    def findBorrowerById(self, searchId):          
        for borrower in self.borrowerList:
            if(borrower.borrowerIdentification == searchId):
                return borrower

    def findBorrowerByName(self, searchName):
        retValue = list()
        for borrower in self.borrowerList:
            if (borrower.borrowerName.find(searchName) != -1):
                retValue.append(borrower)
        return retValue

    def getBorrowerList(self):
        return self.borrowerList
        

    def removeBorrower(self, oldBorrower):
        self.borrowerList.remove(oldBorrower)

class InputOutput(object):

    def importBookList(self, bookList):
        fStream = open('ebooks.txt','r+')
        for row in fStream.readlines():
            rowArray = row.split(',')
            bookList.addBook(Ebook(rowArray[1],rowArray[0],rowArray[2]))
        fStream.close()
            
            
    def importBorrowerList(self, borrowerList, borrowerAttributes, bookAttibutes):

        tempArray = list()
        x, endValue = borrowerAttributes, 0
        
        fStream = open('borrowers.txt','r+')
        for row in fStream.readlines():
            x = borrowerAttributes
            rowArray = row.split(',')
            endValue = len(rowArray) - borrowerAttributes
            tempArray.clear()
            if(endValue != 0):
                while(x < endValue + 1):
                    tempArray.append(Ebook(newTitle=rowArray[x], newAuthor=rowArray[x + 1], newRating=rowArray[x + 2]))
                    x += bookAttibutes
            borrowerList.addBorrower(Borrower(int(rowArray[1]), rowArray[0].strip(), int(rowArray[2].strip()), tempArray))
        fStream.close()

    def exportBookList(self, bookList):
        fStream = open('ebooks.txt','w+')
        for book in bookList.invBookList:
            fStream.write(book.toString().strip() + '\n')
        fStream.close()

    def exportBorrowerList(self, borrowerList):
        fStream = open('borrowers.txt','w+')
        for borrower in borrowerList.borrowerList:
            fStream.write(borrower.toString().strip() + '\n')
        fStream.close()

class MenuManager(object):

    def __init__(self):
        self.dataValidator = Validation()      

    def displayMainMenu(self):

        runAgain = True

        while (runAgain):
            print('\nWelcome to the Library system')
            print('=============================')
            print('(1) Reqister New Borrower')
            print('(2) Perform a Library Transaction')
            print('(3) List All Borrowers')
            print('(4) Display Help')
            print('(5) Exit Library')
            userChoice = input('Please enter a choice: ')

            print('\n')

            if self.dataValidator.isValidNumber(userChoice,1,5):
                return int(userChoice)
            else:
                print('Please make a valid selection!')
                continue

    def displaySearchType(self, searchType):

        runAgain = True
            
        while (runAgain):
            print('\n     Search ' + searchType + 's By')
            print('=============================')
            print('(1) ' + searchType + '\'s Identification Number')
            print('(2) ' + searchType + '\'s Name')
            print('(3) Return to main menu')
            userChoice = input('Please choose an option: ')

            print('\n')

            if self.dataValidator.isValidNumber(userChoice,1,3):
                return int(userChoice)
            else:
                print('Please make a valid selection!')
                continue

    def displayBorrowerOptions(self):
 
        runAgain = True
            
        while (runAgain):
            print('\n     Manage Borrower')
            print('=========================')
            print('(1) Borrow a book')
            print('(2) Return a Book')
            print('(3) List borrowed books')
            print('(4) Return to main menu')
            userChoice = input('Please choose an option: ')

            print('\n')

            if (self.dataValidator.isValidNumber(userChoice,1,4)):
                return int(userChoice)
            else:
                print('Please make a valid selection!')
                continue

    def displayBorrowerMenu(self, borrowerList):

        x, retValue = 1, 0
        runAgain = True

        while(runAgain):
            
            print('\n     Choose a borrower')
            print('==========================')
            
            for borrower in borrowerList:
                print('(' + str(x) + ') ' + borrower.borrowerName)
                x += 1

            print('(' + str(x) + ') Return to previous menu')

            retValue = input('Please choose an option: ')

            if(len(borrowerList) == 0):
                retValue = 1
            elif(not self.dataValidator.isValidNumber(retValue, 1, len(borrowerList))):
                print('Please choose a valid option.  Try again!')
                continue
            else:
                retValue = int(retValue)

            runAgain = False

        return retValue

    def displayBookMenu(self, bookList):

        x, retValue = 1, 0
        runAgain = True

        while(runAgain):
            print('\n     Book Menu')
            print('===================')
            for book in bookList:
                print('(' + str(x) + ') ' + book.title)
                x += 1

            print('(' + str(x) + ') Return to previous menu')
              
            retValue = input('Please choose an option: ')

            if(len(bookList) == 0):
                retValue = 1
            elif(not self.dataValidator.isValidNumber(retValue, 1, len(bookList))):
                print('Please choose a valid option.  Try again!')
                continue
            else:
                retValue = int(retValue)

            runAgain = False

        return retValue

class Validation(object):
    
    def isValidNumber(self, testNumber, minCheck, maxCheck):
        try:
            testNumber = int(testNumber)
        except:
            return False

        if (testNumber < minCheck or testNumber > maxCheck):
            return False

        return True

    def isValidString(self, testString):
        if (len(testString.strip()) == 0):
            return False
        else:
            return True

    def isAvailableIdentification(self, testNumber, custList):

        for borrower in custList:
            if (borrower.borrowerIdentification == testNumber):
                return False

        return True
    

class MyLibrary(object):

    def __init__(self):
        self.userInterface = MenuManager()
        self.customerList = BorrowerList()
        self.inventoryList =  BookList()
        self.libraryValidator = Validation()
        self.databaseManagement = InputOutput()
        self.databaseManagement.importBookList(self.inventoryList)
        self.databaseManagement.importBorrowerList(self.customerList,3,3)


    def manageAcount(self, loggedAccount):
        
        menuOption = 0

        while (menuOption != 4):
            print('\nLogged in as: ' + loggedAccount.borrowerName)
            menuOption = self.userInterface.displayBorrowerOptions()

            if(menuOption == 1):             

                bookOption = 0
                userBook = None

                if(len(loggedAccount.borrowerList.borrowBookList) == 2 ):
                    print('You have borrowed your limit.  Please try again!')
                    continue
                
                while(bookOption != 3):
                    
                    bookOption = self.userInterface.displaySearchType('Book')

                    if(len(loggedAccount.borrowerList.borrowBookList) == 2 ):
                        print('You have borrowed your limit.  Please try again!')
                        break

                    if(bookOption == 1):
                        
                        bookIndex = self.userInterface.displayBookMenu(self.inventoryList.invBookList)

                        try:
                            bookOption = self.inventoryList.invBookList[bookIndex - 1]
                        except:
                            continue

                        if (loggedAccount.borrowerAge < 18 and bookOption.rating.strip() == 'adult'):
                            print('Sorry young \'un.  Maybe when you\'re older.')
                            continue

                        loggedAccount.borrowerList.addBook(bookOption)

                        
                    if(bookOption == 2):
                        
                        runAgain = True

                        while(runAgain):
                        
                            searchParam = input('Please enter a name or part of a name to search for: ')

                            if(not self.libraryValidator.isValidString(searchParam)):
                                print('Please enter valid search string!  Please try again.')
                                continue

                            runAgain = False
                        
                        searchBookList = self.inventoryList.filterListByName(searchParam)

            
                        bookIndex = self.userInterface.displayBookMenu(searchBookList)

                        try:
                            bookOption = searchBookList[bookIndex - 1]
                        except:
                            continue

                        if (loggedAccount.borrowerAge < 18 and bookOption.rating.strip() == 'adult'):
                            print('Sorry young \'un.  Maybe when you\'re older.')
                            continue

                        loggedAccount.borrowerList.addBook(bookOption)
                    
                
            elif(menuOption == 2):

                bookIndexNumber = self.userInterface.displayBookMenu(loggedAccount.borrowerList.borrowBookList)

                try:
                    returnBook = loggedAccount.borrowerList.borrowBookList[bookIndexNumber - 1]
                except:
                    continue

                loggedAccount.borrowerList.removeBook(returnBook)
                
            elif(menuOption == 3):
                loggedAccount.displayBorrowerList()
            elif(menuOption == 4):
                continue
            else:
                print('I did not recognize this choice.  Please try again!')
                

    def registerBorrower(self):
        self.customerList.addBorrower()

    def performTransaction(self):

        menuOption = 0
        userAccount = None

        while (menuOption != 3):
            menuOption = self.userInterface.displaySearchType('Borrower')
            userAccount = None

            if(menuOption == 1):

                runAgain = True

                while(runAgain):
                    searchParam = input('Please input a borrower id: ')

                    if(self.libraryValidator.isValidNumber(searchParam,1,100)):
                        searchParam = int(searchParam)
                    else:
                        print('Please make a valid selection!')
                        continue

                    if(self.libraryValidator.isAvailableIdentification(searchParam, self.customerList.getBorrowerList())):
                        print('ID not found.  Please try again!')
                        continue

                    runAgain = False

                userAccount = self.customerList.findBorrowerById(searchParam)
                        
            elif(menuOption == 2):

                runAgain = True

                while(runAgain):
                    searchParam = input('Please enter a name or part of a name to search for: ')

                    if(not self.libraryValidator.isValidString(searchParam)):
                        print('Please enter valid search string!  Please try again.')
                        continue

                    runAgain = False

               
                filteredList = self.customerList.findBorrowerByName(searchParam)
                borrowerChoice = self.userInterface.displayBorrowerMenu(filteredList)

                try:
                   userAccount = filteredList[borrowerChoice - 1]
                except:
                   continue
                
            elif(menuOption == 3):
                continue
            else:
                print('I did not recognize this choice.  Please try again!')

            
            self.manageAcount(userAccount)

    def listBorrowers(self):
        self.customerList.displayBorrowers()

    def displayHelp(self):
        print('Welcome to the library system!')
        print('==============================')
        print('Enter option one to enter a new user.  You will be prompted to enter their name')
        print('and age.\n')

        print('Enter option two to manage a borrower.  You will be able to chose to borrow')
        print('a book, return a book, or view your book list.\n')
              
        print('To borrow or return a book, you will be asked for your borrower ID and the book')
        print('you wish to borrow or return.\n')

        print('Enter option three to view a list of all borrowers and the books')
        print('they have borrowed.\n')

        print('Enter option four to view this help menu, again.\n')

        print('Enter option five to exit the system.')


    def runLibrary(self):
        userChoice = 0
        runAgain = True
        
        while (runAgain):

            userChoice = self.userInterface.displayMainMenu();
        
            if (userChoice == 1):
                self.registerBorrower()
            elif (userChoice == 2):
                self.performTransaction()
            elif (userChoice == 3):
                self.listBorrowers()
            elif (userChoice == 4):
                self.displayHelp()
            elif (userChoice == 5):
                self.databaseManagement.exportBookList(self.inventoryList)
                self.databaseManagement.exportBorrowerList(self.customerList)
                print('Thank you for using the library!  Have a pleasant day!')
                runAgain = False
            else:
                print('I did not expect that.  Please try again!')
                
            
def main():
    currentSystem = MyLibrary()
    currentSystem.runLibrary()

if __name__ == '__main__':
    main()
