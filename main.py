import sys
import datetime

#convert a deal from a string into a key value dictionary
def parseQuery(line):
    searchParams = {}
    searchParams["dealFile"] = line[1]
    searchParams["hotel"] = line[2]
    try: 
        searchParams["startDate"] = parseDate(line[3])
    except:
        print "Error: Invalid Start Date"
        return {}
    try: 
        searchParams["duration"] = int(line[4])
    except:
        print "Error: Invalid Duration"
        return {}
    return searchParams

#convert a search query into a key value dictionary
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

#apply a given discount to a given initial cost
def applyDiscount(discountType, initialCost, value):
    if discountType == "rebate" or discountType == "rebate_3plus":
        return initialCost - value
    elif discountType == "pct":
        return int(initialCost * (100 - abs(value))/100.0)

#convert a date string into a datetime object
def parseDate(date):
    splitDate = date.split("-")
    return datetime.date(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]))

#return True if date falls between startDate and endDate, and False otherwise
def inDateRange(date, startDate, endDate):
    return date - startDate > datetime.timedelta(seconds = 0) and endDate - date > datetime.timedelta(seconds = 0)


def findBestDeal(query):
    searchParams = parseQuery(query)
    if searchParams == {}:
        return 

    bestDeal = {}
    bestCost = 9999999999

    try: 
        f = open(searchParams["dealFile"])
    except: 
        return "Error: Unable to open given file"
    for line in f:
        dealParams = parseDeal(line)
        #test if we are looking at the correct hotel
        if not (dealParams["hotel"] == searchParams["hotel"]): 
            continue
        #test if the start of our reservation falls within the booking period
        elif not inDateRange(searchParams["startDate"], parseDate(dealParams["startDate"]), parseDate(dealParams["endDate"])):
            continue
        #test if the deal is a rebate_3plus and we are staying for fewew than three days
        elif dealParams["type"] == "rebate_3plus" and searchParams["duration"] < 3:
            continue
        else: 
            #find the cose of the stay before the deal
            baseCost = int(searchParams["duration"]) * int(dealParams["price"])

            #find the cost of the stay after the deal
            baseCost = applyDiscount(dealParams["type"], baseCost, int(dealParams["value"]))

            #update the best deal
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
        res = findBestDeal(args)
        if res:
            print res



