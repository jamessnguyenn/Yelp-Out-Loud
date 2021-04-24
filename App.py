from MongoConnector import MongoConnector

class App:

    def __init__(self):
        self.__mongoConnector = MongoConnector()
        print('\u001B[34m----------------------------------------------------------')
        print('Welcome to Yelp Out Loud!\u001B[0m')
        self.__terminated = False


    def start(self):
        while(self.__terminated is False):
            print('\u001B[34m----------------------------------------------------------\u001B[0m')
            print("\033[1;34mChoose an option you would like to do:\n\u001B[0m")
            self.__displayMenu()
            choice = input()
            if(choice == '1'):
                print('You inputted 1!')
            elif(choice == '2'):
                print('You inputted 2!')
            elif(choice == '3'):
                self.__checkInBusiness()
            elif (choice == '4'):
                print('You inputted 4!')
            elif (choice == '5'):
                print('You inputted 5!')
            elif (choice == '6'):
                self.__sendInTip()
            elif (choice == '7'):
                print('You inputted 7!')
            elif (choice == '8'):
                print('You inputted 8!')
            elif (choice == '9'):
                print('You inputted 9!')
            elif (choice == '10'):
                self.__deleteReview()
            elif (choice == '11'):
                print('You inputted 11!')
            elif (choice == '12'):
                print('You inputted 12!')
            elif (choice == '13'):
                print('You inputted 13!')
            elif (choice == '14'):
                print('You inputted 14!')
            elif (choice == '15'):
                self.__getUserJoinedByYear()
            elif(choice=='0'):
                self.__terminated =True
                print('Goodbye!')
            else:
                print("\033[0;91mInvalid entry. Try Again\033[0m")

    def __displayMenu(self):
        print('{:50}{:}'.format('1 - Discover a business', '9 - View tips About a Business'))
        print('{:50}{:}'.format('2 - Review a business', '10 - Delete a review'))
        print('{:50}{:}'.format('3 - Check into a business', "11 - View average review count and friends of elite users"))
        print('{:50}{:}'.format('4 - Close a business', '12 - View the average number of complements recieved by a user'))
        print('{:50}{:}'.format('5 - View Reviews of a business', '13 - View the number of elite users in a specific year'))
        print('{:50}{:}'.format('6 - Send a Tip about a business', '14 - View the total number of reviews posted by a user'))
        print('{:50}{:}'.format('7 - View the Business Leaderboards', '15 - View the list of users who joined yelp in a certain year'))
        print('{:50}{:}'.format('8 - Discover a business based on other criterias', '0 - Exit'))

    def __checkInBusiness(self):
        businesID = input('\033[0;34mEnter the id of the business you would like to check into:\n\033[0m')
        #todo perform UPDATE
        print("\033[0;34mSuccessfully checked into the business! Press Enter to return to the menu.\033[0m")

    def __sendInTip(self):
        userID = input("\033[0;34mEnter your user id:\n\033[0m")
        businesID = input("\033[0;34mEnter the business id you would like to provide a tip to:\n\033[0m")
        tip = input("\033[0;34mPlease provide a tip in one line:\n\033[0m")
        #todo perform INSERT
        print("\033[0;34mThanks for submitting the tip and helping the community! Press Enter to return to the menu.\033[0m")
        input()

    def __deleteReview(self):
        reviewID = input("\033[0;34mEnter the id of the review you would like to delete:\n\033[0m")
        #todo perform DELETION
        print("\033[0;34mReview has been deleted. Feel free to make another one! Press Enter to return to the menu.\033[0m")
        input()

    def __getUserJoinedByYear(self):
        try:
            year = int(input("\033[0;34mEnter a year you would like to find the user who have joined then:\n\033[0m"))
            #todo perform FIND
            print("Users who have joined in "+ str(year) +":")
            print("\033[0;34mPress Enter to return to the menu.\033[0;34m")
            input()
        except ValueError:
            print("\033[0;91mInvalid Year. Press Enter to return to menu and Try Again.\033[0m")
            input()






#Run App
app = App()
app.start()