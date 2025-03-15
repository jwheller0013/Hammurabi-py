import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        # declare local variables here: grain, population, etc.
        # statements go after the declarations

        current_stats = [100, 2800, 1000, 19, 1, 0]
        #current_stats = [people, grain, land, land_value, year, starved]
        more_stats = [5, 3000, 3, 200]
        #more_stats = [immigrants, harvest, bushelsPerAcre, ratsDestroyed]

        return Hammurabi.printSummary(self)

    # other methods go here
    def printSummary(self):
        print ("O great Hammurabi!\n" +
               "You are in year " + current_stats[4] + " of your ten year rule.\n" +
               "In the previous year " + current_stats[5] + " people starved to death.\n" +
               "In the previous year " + more_stats[0] + " people entered the kingdom.\n" +
               "The population is now " + current_stats[0] + ".\n" +
               "We harvested " + more_stats[1] + " bushels at " + more_stats[2] + " bushels per acre.\n" +
               "Rats destroyed " + more_stats[3] + " bushels, leaving " + current_stats[1] + " bushels in storage.\n" +
               "The city owns " + current_stats[2] + " acres of land.\n" +
               "Land is currently worth " + current_stats[3] + " bushels per acre.")



if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()

