import datetime
import random
import os

hotelPrices = {"Hotel Apple": 200, "Hotel Banana": 300, "Hotel Grapefruit": 400, "Hotel Orange" : 600, "Hotel Pineapple": 800}
dealTypes = ["rebate", "rebate_3plus", "pct"]


#generate a random date between startdate and endate
def randomDate(startDate, endDate):
    datedelta = (endDate - startDate).total_seconds()
    rand = random.random()
    return datetime.timedelta(seconds = rand * datedelta) + startDate


#returns a list of two days in 2015 that are the given duration apart
def randomDateRange(duration):
    day1 = datetime.date(2015, 1, 1)
    day2 = datetime.date(2015, 12, 31) - datetime.timedelta(days = duration)

    firstDate = randomDate(day1, day2)
    return [firstDate, firstDate + datetime.timedelta(days = duration) ]

#generate a deal for a given hotel
def generateDeal(hotel):
    dealType = random.choice(dealTypes)
    dateRange = randomDateRange(random.randrange(1,15))
    price = hotelPrices[hotel] + int(random.random() * 10) * 10 - 50 

    amount = 0 
    dealText = ""

    if dealType == "rebate": 
        amount = -1 * int(random.random() * 10) * int(int(price)/10.0 + 10)
        dealText = "$" + str(amount) + " off your stay"
    elif dealType == "pct":
        amount = -1 * (int(random.random() * 5) * 5 + 5)
        dealText =  str(abs(amount)) + "% off your stay"
        pass
    elif dealType == "rebate_3plus":
        amount = -1 * int(random.random() * 10) * 10 + 5
        dealText =  "$" + str(abs(amount)) + " off your stay 3 nights or more"
    return hotel + "," + str(price) + "," + dealText + "," + str(amount) + "," + dealType + "," + str(dateRange[0]) + "," +  str(dateRange[1])


#generate 500 random deals for each hotel
if __name__ == "__main__":
    f = open(os.getcwd() + "/data/deals.txt", 'w')
    for key,dealType in hotelPrices.iteritems():
        for x in range(500):
            f.write(generateDeal(key) + "\n")
    f.close()