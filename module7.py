def main():
    #This input function allows the user to enter their name
    userName = input( "Please enter your name: " )

    #This function personalizes the information received above "user's name" returns a greeting and ask's the user a question
    flowerName = input( "Hello " + userName + ", Which flower would you like a price for?: " )


    flowerNameCapitalized = flowerName.capitalize()
    userFlowerNameLowerCase = flowerName.lower()

    #This is a dictionary.  readAllFlowers is defined below
    flowers = readAllFlowers()    
    
    #This is a conditional statement. 
    priceResponse = get_price(flowers, userFlowerNameLowerCase)
    if type(priceResponse)==float:
        print(f"The price of {flowerNameCapitalized} is: ${priceResponse:,.2f}")

    else: 
        print(priceResponse)

    writeLineToFile(userName, flowerNameCapitalized, priceResponse)
    
#This block of code is defining the function readAllFlowers and uses a test file.
def readAllFlowers():
    flowers ={}
    flowerDatabaseFile =open("flowerDatabase.txt", "r")
    line =flowerDatabaseFile.readline()

#This is a while loop that runs until there is nothing left in the text file.  It runs until it reaches the end or while it is not equal to empty space.
    while line != "":
#There is a space between the flower and the price in the dictionary or text file.  The split is used to ignore this space.        
        flowerAndPriceList =line.split()

#
        flowerName = flowerAndPriceList [0]
        flowerNameLowerCase = flowerName.lower()
        flowerPriceString  = flowerAndPriceList[1]

        flowerPriceFloat = float(flowerPriceString)
        flowers[flowerNameLowerCase] = flowerPriceFloat

        line =flowerDatabaseFile.readline()
    
    return flowers
        
def writeLineToFile(userName, flowerName, flowerPrice):
    userInquiriesFile =open("userInquiries.txt", "a")
    if type(flowerPrice)==float:
        userInquiriesFile.write(userName + " inquired about the " + str(flowerPrice) + " " + flowerName + " flower.\n")
    else:
        userInquiriesFile.write(userName + " inquired about the " + flowerName + " that is out of stock.\n")
    userInquiriesFile.close()
     


def get_price(flowers, flowerName):
    if flowerName in flowers:
        return flowers[flowerName]
    else:
        return "Sorry, we do not have that flower in stock."   


main()
