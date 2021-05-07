from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import datetime

class App:

    def __init__(self):
        '''self.__mongoConnector = MongoConnector('mongodb://ec2-54-85-131-49.compute-1.amazonaws.com:27021')

        #Connect to each collection
        self.__business = self.__mongoConnector.db.business
        self.__checkin = self.__mongoConnector.db.checkin
        self.__reviews = self.__mongoConnector.db.reviews
        self.__tips = self.__mongoConnector.db.tips
        self.__users = self.__mongoConnector.db.users'''

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
                self.__discoverBusiness()
            elif(choice == '2'):
                self.__reviewBusiness()
            elif(choice == '3'):
                self.__checkInBusiness()
            elif (choice == '4'):
                self.__closeBusiness()
            elif (choice == '5'):
                self.__getReviews()
            elif (choice == '6'):
                self.__sendInTip()
            elif (choice == '7'):
                self.__viewBusinessLeaderBoard()
            elif (choice == '8'):
                self.__otherSearchBusiness()
            elif (choice == '9'):
                self.__top10Tips()
            elif (choice == '10'):
                self.__deleteReview()
            elif (choice == '11'):
                self.__getAverageElite()
            elif (choice == '12'):
                self.__getAverageCompliment()
            elif (choice == '13'):
                self.__getNumberOfEliteUsers()
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
        print('{:50}{:}'.format('7 - View the Business Leaderboards', '15 - View the list of 10 users who joined yelp in a certain year'))
        print('{:50}{:}'.format('8 - Discover a business based on other criterias', '0 - Exit'))



    #Use Case 1 todo
    def __discoverBusiness(self):
        state = input("Enter the state abbreviation that you would like to find the business in:\n")
        city = input("Enter the city that you would like the find the businesss in:\n")
        category = input("Enter the category of the business you would:\n")
        #preform query here
        print("Search Results:")

        print("Enter to return to the main menu.")
        input()

    #Use Case 2 todo
    def __reviewBusiness(self):
        try:
            userId = input("Enter your user id:\n")
            businessId = input("Enter the business id of the business you would like to review:\n")
            stars = int(input("How many stars would you give this business?\n"))
            if(stars >5 or stars <0 ):
                raise ValueError
            print("Input your review. Finish by entering an empty line.")
            buffer = input()
            review = ""
            while buffer != "":
                review = review+"\n"+ buffer
                buffer = input()
            print("Thank you for sending in the review! Press enter to return to the main menu")
            input()
        except ValueError:
            print("Invalid star count. Press Enter to return to the menu and Try Again.")
            input()

    #Use Case 3
    def __checkInBusiness(self):
        businessID = input('\033[0;34mEnter the id of the business you would like to check into:\n\033[0m')
        date = datetime.datetime.now()
        date = date.replace(microsecond=0)
        result = self.__checkin.update_one({'business_id': businessID}, {'$push':{"date": str(date)}})
        if(result.modified_count >0):
            print("\033[0;34mSuccessfully checked into the business! Press Enter to return to the menu.\033[0m")
        else:
            print("No businesses found to check in. Press Enter to return to the menu and Try Again.")

    #Use Case 4 todo
    def __closeBusiness(self):
        zipcode = input("Enter the zipcode of the business that is closing\n")
        businessID = input("Enter the id of the business that is closing\n")


        print("Success. The business has been reported closed. Press Enter to return to the main menu.")
        input()

    #Use Case 5 todo
    def __getReviews(self):
        businessID = input("Enter the id of the business you would like to find reviews about:\n")

        print("Top 10 Reviews:")

        print("Press Enter to return to the main menu.")
        input()
    #Use Case 6
    def __sendInTip(self):
        userID = input("\033[0;34mEnter your user id:\n\033[0m")
        businessID = input("\033[0;34mEnter the business id you would like to provide a tip to:\n\033[0m")
        tip = input("\033[0;34mPlease provide a tip in one line:\n\033[0m")
        date = datetime.datetime.now()
        date = date.replace(microsecond=0)
        result = self.__tips.insert_one({"text": tip, "date": date, "compliment_count": 0, "user_id": userID, "business_id": businessID})
        print("\033[0;34mThanks for helping the community. Your tip id is" + str(result.inserted_id) + ". Press Enter to return to the menu.\033[0m")
        input()

    #Use Case 7 todo
    def __viewBusinessLeaderBoard(self):
        print("Top 10 Businesses:")


        print("Press enter to return to the main menu.")
        input()
    #Use Case 8 todo
    def __otherSearchBusiness(self):
        try:
            reviewCount = int(input("At least how many reviews should this business have:\n"))
            happyHourResponse = input("Does this business have happy hour? (Y/N)\n")
            dogsAllowedResponse = input("Does this business have dogs? (Y/N)\n")

            happyHour = None
            dogsAllowed = None
            if(happyHourResponse == 'Y'):
                happyHour = True
            elif(happyHourResponse == 'N'):
                happyHour = False
            else:
                raise IOError
            if(dogsAllowedResponse == 'Y'):
                dogsAllowed = True
            elif(dogsAllowedResponse == 'N'):
                dogsAllowed = False
            else:
                raise IOError
            print("Top Businesses")
            print("Press Enter to the Return to the Main Menu")
            input()
        except (IOError, ValueError) as error:
            print("Invalid response. Press Enter to Return to the Main Menu and Try Again.")
            input()


    #Use Case 9 todo
    def __top10Tips(self):
        businessID = input("Enter the business id of the business\n")

        print("Top 10 Tips of Business")

        print("Press Enter to return to the Main Menu")
        input()
    #Use Case 10
    def __deleteReview(self):
        businessID = input('\033[0;34mEnter the id of the business you would like to delete the review from:\n\033[0m')
        reviewID = input("\033[0;34mEnter the id of the review you would like to delete:\n\033[0m")
        result = self.__reviews.delete_one({"review_id": reviewID, "business_id": businessID})
        if(result.deleted_count >0):
            print("\033[0;34mReview has been deleted. Feel free to make another one! Press Enter to return to the menu.\033[0m")
        else:
            print("No Reviews found to delete. Press Enter to return to the menu and Try Again.")
        input()

    #Use Case 11 todo
    def __getAverageElite(self):
        print("Average Review Counts and Number of Friends of Elite Users:")

        print("Press Enter to return to the Main Menu.")
        input()
    #Use Case 12 todo
    def __getAverageCompliment(self):
        print("Average Number of Complements Received Per User:")

        print("Press Enter to return the Main Menu.")
        input()
    #Use Case 13 todo
    def __getNumberOfEliteUsers(self):
        try:
            year = int(input("\033[0;34mEnter a year you would like to get the analytics from:\n\033[0m"))
            print("Number of elite users in" + str(year) +":")
            print("Press Enter to return to the main menu.")
            input()
        except ValueError:
            print("\033[0;91mInvalid Year. Press Enter to return to menu and Try Again.\033[0m")
            input()
    #Use Case 14 todo

    #Use Case 15
    def __getUserJoinedByYear(self):
        try:
            year = int(input("\033[0;34mEnter a year you would like to find the user who have joined then:\n\033[0m"))
            cursor = self.__users.find({ "yelping_since": {"$type": "date"},"$expr": {"$eq": [{"$year": "$yelping_since"}, year]}}).limit(10)
            print("Users who have joined in "+ str(year) +":")
            count = 1
            for document in cursor:
                print(str(count)+ ". "+str(document['name'])+ " UserId:"+ str(document['user_id']))
                count+=1
            print("\033[0;34mPress Enter to return to the menu.\033[0;34m")
            input()
        except ValueError:
            print("\033[0;91mInvalid Year. Press Enter to return to menu and Try Again.\033[0m")
            input()


class MongoConnector:

    def __init__(self, connectionString):
        client = MongoClient(connectionString)
        try:
            client.admin.command('ismaster')
            print("Successfully Connected to MongoDB Client")
            self.db = client.yelp
        except ConnectionFailure:
            print("Server not available")

#Run App
app = App()
app.start()