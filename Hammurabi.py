import random
from random import randrange


class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        Hammurabi.intro()
        play_game = True
        play_game = Hammurabi.start_game(play_game)

        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        if play_game == False:
            print("Goodbye.")
        while play_game == True:

            game_mode = Hammurabi.game_mode(self)

            people = 100
            grain = 2800
            land = 1000
            land_value = 19
            starved = 0
            immigrants = 5
            harvest = 3000
            bushelsPerAcre = 3
            ratsDestroyed = 200
            planted_acres = 0
            bought_land = 0
            sold_land = 0
            buy = True
            feed = 0
            fed = 0
            total_starved = 0
            plagueDeaths = 0
            revolt = False
            total_ratsDestroyed = 0
            plague_counter = 0

            for i in range(10, 11, 1):

                print("O great Hammurabi!\n" +
                "You are in year " + str(i) + " of your ten year rule.\n" +
                "In the previous year " + str(starved) + " people starved to death.\n" +
                "In the previous year " + str(immigrants) + " people entered the kingdom.\n" +
                "The population is now " + str(people) + ".\n" +
                "We harvested " + str(harvest) + " bushels at " + str(bushelsPerAcre) + " bushels per acre.\n" +
                "Rats destroyed " + str(ratsDestroyed) + " bushels, leaving " + str(grain) + " bushels in storage.\n" +
                "The city owns " + str(land) + " acres of land.\n" +
                "Land is currently worth " + str(land_value) + " bushels per acre.")

                buy = Hammurabi.askBuyOrSell(buy)
                if buy == True:
                    bought_land = Hammurabi.askHowManyAcresToBuy(grain,land_value)
                    sold_land = 0
                if buy == False:
                    sold_land = Hammurabi.askHowManyAcresToSell(land)
                    bought_land = 0
                land = int(land) - int(sold_land) + int(bought_land)
                grain = int(grain) + (int(sold_land) - int(bought_land)) * int(land_value)
                #this handles buying and selling

                feed = int(Hammurabi.askHowMuchGrainToFeedPeople(grain))
                fed = feed/20
                grain = int(grain) - int(feed)
                starved = int(Hammurabi.starvationDeaths(fed, people))
                total_starved = total_starved + starved
                people = people - starved
                #should the people die at end of each year or before can plant?
                #this handles feeding/starving

                planted_acres = int(Hammurabi.askHowManyAcresToPlant(land, people, grain))
                grain = int(grain) - (int(planted_acres)*2)
                #this handles bushels_planted

                bushelsPerAcre = int(Hammurabi.bushels_per_acre())
                harvest = int(Hammurabi.harvest(bushelsPerAcre, planted_acres))
                grain = int(grain) + int(harvest)

                if game_mode == "All":
                    plagueDeaths = people - int(Hammurabi.plagueDeaths(people))
                    people = people - plagueDeaths
                    if plagueDeaths > 0:
                        print("Dreadful news a plague struck our lands. " + str(plagueDeaths) + " died.\n")
                        plague_counter = plague_counter+1
                    #covers plague hitting town

                    revolt = Hammurabi.uprising(people, starved)
                    if revolt == True:
                        print("So yeahhhh been great serving you but that angry mob is coming " +
                              "to kill you for starving them. I'd advise maybe wiping your mouth of crumbs " +
                              "before they get here......bye.\n")
                        return
                    #covers uprising

                    if starved == 0:
                        immigrants = Hammurabi.immigrants(people, land, grain)
                        people = int(people) + int(immigrants)
                    elif starved != 0:
                        immigrants = 0
                    #covers immigration

                    ratsDestroyed = int(Hammurabi.grainEatenByRats(grain))
                    total_ratsDestroyed = total_ratsDestroyed + ratsDestroyed
                    grain = int(grain) - int(ratsDestroyed)
                    #covers rats

                    land_value = int(Hammurabi.newCostOfLand(land_value))


                if i == 10:
                    Hammurabi.end_results(total_starved, land, total_ratsDestroyed, plague_counter)
                    return




    # other methods go here

    def start_game(x):
        z =input("Are you ready to see if you can live up to being the great\n" + "Hammurabi?\n")
        if z == "No":
            print("So be it.")
            x = False
        if z == "Yes":
            x = True
        else:
            print("Nah you opened me to play a game not make Jim error code all your mistakes.")
            x = False
        return x


    def intro():
        print ("Congratulations, you are the newest ruler of ancient Sumer, elected for a ten year term of " +
               "office. Your \nduties are to dispense food, direct farming, and buy and sell land as " +
               "needed to support your people.\n" + "Watch out for rat infestiations and the plague! " +
               "Grain is the general currency, measured in bushels. The \n" + "following will help you in " +
               "your decisions:\n\n" + "Each person needs at least 20 bushels of grain per year to survive\n" +
               "Each person can farm at most 10 acres of land\n" +
               "It takes 2 bushels of grain to farm an acre of land\n" +
               "The market price for land fluctuates yearly\n\n" + "Rule wisely and you will be showered " +
               "with appreciation at the end of your term.\n" + "Rule poorly and you will be kicked out of office! \n")

    def askHowManyAcresToBuy(grain,land_value):
        howMany = input("How many acres would you like to buy? \n")
        while int(howMany) * int(land_value) > int(grain):
            print ("Hammurabi surely you jest, we cannot afford that with " + str(grain) + " bushels of grain.\n")
            howMany = input("How many acres would you like to buy? \n")
        return howMany

    def askHowManyAcresToSell (land):
        howMany = input("How many acres would you like to sell? \n")
        while int(howMany) > int(land):
            print("Hammurabi ease off the wine. You must be seeing double. Currently we own only " + str(land)
                  + " acres of land\n")
            howMany = input("How many acres would you like to sell? \n")
        return howMany

    def askBuyOrSell (buy):
        buyOrSell = input("So my lord are we buying or selling land?\n")
        if buyOrSell == "buying":
            buy = True
        elif buyOrSell == "selling":
            buy = False
        return buy

    def askHowMuchGrainToFeedPeople (grain):
        howMany = input("How much grain shall we provide the people with? \n")
        while int(howMany) > int(grain):
            print("Hammurabi, I know you are grateful for our people but we only have " +
                  str(grain) + " grain in our storage.")
            howMany = input("How much grain shall we provide the people with? \n")
        grain = int(howMany)
        return grain

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
        while int(howMany)*2 > int(grain):
            print("Hammurabi just cause you plant the grain over a larger area does not mean" +
            " it will grow to fill it. We have only " + str(grain) + " bushels of grain. \n")
            howMany = input("How many acres of grain shall we plant? \n")
        return int(howMany)

    def starvationDeaths (fed, people):
        starved = 0
        if int(people) > int(fed):
            starved = int(people) - int(fed)
        if int(people) <= int(fed):
            starved = 0
        return starved

    def bushels_per_acre ():
        luck = randrange(1, 7)
        return luck

    def harvest (bushelsPerAcre, planted_acres):
        harvest = int(planted_acres) * int(bushelsPerAcre)
        return harvest

    def end_results(total_starved, land, total_ratsDestroyed, plague_counter):
        print("O great Hammurabi you have made it to the end of your ten year rule.")

        if total_starved == 0:
            print("You are quite a humanitarian somehow no one starved under your rule.")
        elif total_starved <= 50:
            print("Of your subjects only " + str(total_starved) + " starved to death.")
        elif total_starved > 50:
            print("Surprised you made it out alive considering " + str(total_starved) + " starved to death.")

        if plague_counter == 0:
            print("Not a single plague during your rule!\n"
                  "It was a hard sell but that concept of washing hands worked wonders.")
        elif plague_counter > 1 and plague_counter < 5:
            print("A few plagues could not stop you O Great Hammurabi\n" +
                  "We survied " + str(plague_counter) + " plagues in total.")
        elif plague_counter > 5:
            print("Surprised we have any people left after " + str(plague_counter) +
                  " plagues hit our land.\n" + "Perhaps killing all those healers " +
                  "in the kingdom for calling you fat was a mistake.")

        if total_ratsDestroyed == 0:
            print("Praise be our luck or the barn cats as rats ate none of our grain")
        elif total_ratsDestroyed <= 1000:
            print("We lost our fair share of grain to rats over the years " + str(total_ratsDestroyed)
                  + " bushels in total.")
        elif total_ratsDestroyed > 1000 and total_ratsDestroyed < 3000:
            print("Seems we spent those years feeding rats as much as people " + str(total_ratsDestroyed)
                  + " bushels in total.")
        elif total_ratsDestroyed > 3000:
            print("Granted should call you the king of rats with how much they ate" + str(total_ratsDestroyed) +
                  " bushels in total.\n" + "I mean really sire I told you your decree banning cats was bad.")

        if land < 1000:
            print("During your rule we lost land though, roughly " + str(1000-int(land)) + " acres.\n" +
            "Probably be a good idea to work on how to spin that to sound good to the next ruler.")
        elif land == 1000:
            print("During your rule we did not loose or gain land. I mean not bad....\n" +
                  "not great...but hey we all can't be as good as your brother.")
        elif land > 1000:
            print("Nice job increasing our kingdom O Great Hammurabi. Our kingdom grew by\n" +
                  str(int(land) - 1000) +".")


    def game_mode(self):
        self = input("Looking to play a 'Basic' game or ready for 'All' the challenges of rule?\n")
        return self

    def plagueDeaths(self):
        chance = randrange(1,101)
        if chance <= 15:
            self = self/2
        return self

    def uprising(people, starved):
        revolt = False
        if int(starved) > (int(people)*0.45):
            revolt = True
        return revolt

    def immigrants(people, land, grain):
        immigrants = int((20 * int(land) + int(grain))/(100*int(people))+1)
        return immigrants

    def grainEatenByRats(self):
        chance = randrange(1,101)
        eaten = 0
        if chance <= 40:
            eaten_percent = randrange(10, 31)
            eaten = int(eaten) + ((int(self) * int(eaten_percent)) / 100)
            return eaten
        return eaten

    def newCostOfLand(self):
        self = randrange(17,24)
        return self

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()

