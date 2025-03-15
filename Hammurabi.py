import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
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

        land = int(land) + int(Hammurabi.askHowManyAcresToBuy(grain, bushelsPerAcre))
        grain = int(grain) - int(land) * int(bushelsPerAcre)
        printSummary()



    # other methods go here

    # def testPrint (x):
    #     print (x)
    #
    # def minusPeople (people):
    #     x = int(people) - 10
    #     people = x
    #     return people

    def askHowManyAcresToBuy(grain,bushelsPerAcre):
        howMany = input("How many acres would you like to buy? \n")
        while int(howMany) * int(bushelsPerAcre) > int(grain):
            print ("Hammurabi surely you jest, we cannot afford that with " + str(grain) + "bushels of grain.\n")
            howMany = input("How many acres would you like to buy? \n")
        return howMany

    def askHowManyAcresToSell (land):
        howMany = input("How many acres would you like to sell? \n")
        while int(howMany) > land:
            print("Hammurabi ease off the wine. You must be seeing double. Currently we own only " + str(land)
                  + " acres of land\n")
            howMany = input("How many acres would you like to sell? \n")
        return howMany


if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()

