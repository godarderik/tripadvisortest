import sys

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


def findBestDeal(query):
    searchParams = parseQuery(query)
    bestDeal = {}

    f = open(searchParams["dealFile"])
    for line in f:
        dealParams = parseDeal(line)
    return searchParams


if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) < 5:
        print "Error: Not enough arguments supplied"
    elif len(sys.argv) > 5: 
        print "Error: Too many arguments supplied"
    else:
        print findBestDeal(args)



