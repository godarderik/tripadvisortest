import datetime
import random

hotels = ["Hotel Apple", "Hotel Banana", "Hotel Grapefruit", "Hotel Orange", "Hotel Pineapple"]
dealTypes = ["rebtate", "rebate_3plus", "pct"]


#generate a random date between startdate and endate
def randomDate(startDate, endDate):
    datedelta = (endDate - startDate).total_seconds()
    rand = random.random()
    return datetime.timedelta(seconds = rand * datedelta) + startDate

def generatePercentDeal():
    return "percent deal"

def generateRebateDeal():
    return "rebate deal"

def generateRebatePlusDeal():
    return "rebate plus deal"


def generateDeal():
    dealList = []
    deals = [generateRebateDeal, generatePercentDeal, generateRebatePlusDeal]
    dealList.append(random.choice(deals)())
    return dealList






if __name__ == "__main__":
    print generateDeal()