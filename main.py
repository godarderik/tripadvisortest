import sys
import datetime

#todo - implement more error checking here
def parseQuery(line):
    searchParams = {}
    searchParams["dealFile"] = line[1]
    searchParams["hotel"] = line[2]
    searchParams["startDate"] = line[3]
    searchParams["duration"] = line[4]
    return searchParams

def parseDeal(line):
    splitLine = line.split(',')
    dealParams = {}
    dealParams["hotel"] = splitLine[0]
    dealParams["price"] = splitLine[1]
    dealParams["text"] = splitLine[2]
    dealParams["value"] = splitLine[3]
    dealParams["type"] = splitLine[4]
    dealParams["startDate"] = splitLine[5]
    dealParams["endDate"] = splitLine[6]
    return dealParams

def applyDiscount(discountType, initialCost, value):
    if discountType == "rebate" or discountType == "rebate_3plus":
        return initialCost - value
    elif discountType == "pct":
        return int(initialCost * (100 - abs(value))/100.0)


def parseDate(date):
    splitDate = date.split("-")
    return datetime.date(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]))

def inDateRange(date, startDate, endDate):
    return date - startDate > datetime.timedelta(seconds = 0) and endDate - date > datetime.timedelta(seconds = 0)


def findBestDeal(query):
    searchParams = parseQuery(query)
    bestDeal = {}
    bestCost = 9999999999

    f = open(searchParams["dealFile"])
    for line in f:
        dealParams = parseDeal(line)
        if not (dealParams["hotel"] == searchParams["hotel"]): #if we are not looking at the correct hotel 
            continue
        elif not inDateRange(parseDate(searchParams["startDate"]), parseDate(dealParams["startDate"]), parseDate(dealParams["endDate"])): #test date here
            continue
        elif dealParams["type"] == "rebate_3plus" and searchParams["duration"] < 3:
            continue
        else: 
            baseCost = int(searchParams["duration"]) * int(dealParams["price"])
            baseCost = applyDiscount(dealParams["type"], baseCost, int(dealParams["value"]))
            if baseCost < bestCost:
                bestCost = baseCost
                bestDeal = dealParams
    if bestDeal == {}:
        return "no deals available"
    return bestDeal["text"]



if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) < 5:
        print "Error: Not enough arguments supplied"
    elif len(sys.argv) > 5: 
        print "Error: Too many arguments supplied"
    else:
        print findBestDeal(args)



