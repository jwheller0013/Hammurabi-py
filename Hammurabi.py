import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        print ("Congratulations, you are the newest ruler of ancient Sumer, elected for a ten year term of " +
               "office. Your \nduties are to dispense food, direct farming, and buy and sell land as " +
               "needed to support your people.\n" + "Watch out for rat infestiations and the plague! " +
               "Grain is the general currency, measured in bushels. The \n" + "following will help you in " +
               "your decisions:\n\n" + "Each person needs at least 20 bushels of grain per year to survive\n" +
               "Each person can farm at most 10 acres of land\n" +
               "It takes 2 bushels of grain to farm an acre of land\n" +
               "The market price for land fluctuates yearly\n\n" + "Rule wisely and you will be showered " +
               "with appreciation at the end of your term.\n" + "Rule poorly and you will be kicked out of office! \n")

        play_game =input("Are you ready to see if you can live up to being the great\n" + "Hammurabi?\n")
        if play_game == "No":
            print("So be it.")
            play_game = False
        if play_game == "Yes":
            play_game = True
            return play_game
        else:
            print("Nah you opened me to play a game not make Jim error code all your mistakes.")
            play_game = False
        while play_game == True:

        # declare local variables here: grain, population, etc.
        # statements go after the declarations
            people = 100
            grain = 2800
            land = 19
            land_value = 1
            starved = 0
            immigrants = 5
            harvest = 3000
            bushelsPerAcre = 3
            ratsDestroyed = 200
            year = 1
            planted_land = 0

            def printSummary():
                print("O great Hammurabi!\n" +
                    "You are in year " + str(year) + " of your ten year rule.\n" +
                    "In the previous year " + str(starved) + " people starved to death.\n" +
                    "In the previous year " + str(immigrants) + " people entered the kingdom.\n" +
                    "The population is now " + str(people) + ".\n" +
                    "We harvested " + str(harvest) + " bushels at " + str(bushelsPerAcre) + " bushels per acre.\n" +
                    "Rats destroyed " + str(ratsDestroyed) + " bushels, leaving " + str(grain) + " bushels in storage.\n" +
                    "The city owns " + str(land) + " acres of land.\n" +
                    "Land is currently worth " + str(land_value) + " bushels per acre.")

            printSummary()
            land = int(land) + int(Hammurabi.askHowManyAcresToBuy(grain, land_value))
            grain = int(grain) - int(land) * int(land_value)
            land = int(land) - int(Hammurabi.askHowManyAcresToSell(land))
            grain = int(grain) + int(land) * int(land_value)
            grain = int(grain) - int(Hammurabi.askHowMuchGrainToFeedPeople(grain))
            planted_land = int(Hammurabi.askHowManyAcresToPlant(land, people, grain))
            printSummary()
            print (planted_land)



    # other methods go here

    # def testPrint (x):
    #     print (x)
    #
    # def minusPeople (people):
    #     x = int(people) - 10
    #     people = x
    #     return people

    def askHowManyAcresToBuy(grain,land_value):
        howMany = input("How many acres would you like to buy? \n")
        while int(howMany) * int(land_value) > int(grain):
            print ("Hammurabi surely you jest, we cannot afford that with " + str(grain) + "bushels of grain.\n")
            howMany = input("How many acres would you like to buy? \n")
        return howMany

    def askHowManyAcresToSell (land):
        howMany = input("How many acres would you like to sell? \n")
        while int(howMany) > int(land):
            print("Hammurabi ease off the wine. You must be seeing double. Currently we own only " + str(land)
                  + " acres of land\n")
            howMany = input("How many acres would you like to sell? \n")
        return howMany

    #need to combine these

    def askHowMuchGrainToFeedPeople (grain):
        howMany = input("How much grain shall we provide the people with? \n")
        return howMany

    def askHowManyAcresToPlant (land, people, grain):
        howMany = input("How many acres of grain shall we plant? \n")
        while int(howMany) > int(land):
            print("Hammurabi you need to count with more than your fingers and toes. We only have " +
            str(land) + " acres of land. \n")
            howMany = input("How many acres of grain shall we plant? \n")
        while int(howMany) > int(people)*10:
            print("Hammurabi I know you are a great leader but the people would rather kill you than" +
            " work overtime. We have only " + str(people) + " people. \n")
            howMany = input("How many acres of grain shall we plant? \n")
        while int(howMany) > int(grain)*2:
            print("Hammurabi just cause you plant the grain over a larger area does not mean" +
            " it will grow to fill it. We have only " + str(grain) + "bushels of grain. \n")
            howMany = input("How many acres of grain shall we plant? \n")
        return howMany

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()

