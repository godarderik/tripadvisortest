# Find the Best Hotel Deal

## Running the Code

I used Python 2.7.9 and its standard libraries. The data I generated is found in the data folder. The code can be run by calling “python BestHotelDea.py” followed by the required parameters. 


## Assumptions

In generating test data and writing the code to search for the best deals, I had to make a number of assumptions about the structure of the problem. The first was about the exact meaning of the best deal. I took “best deal” to mean the deal that, when applied, would minimize the overall cost of the trip. Also, I assume a deal is valid for a given trip if the start date of the trip falls between the start and end date of the deal. A deal that is valid using this definition will still be valid even if the user’s trip continues after the deal has ended. In addition, when generating the data, I generated entries of the following form. My code, however, is compatible with any valid input. 
*	Deals last between 1 and 14 days. 
*	The dates for deals are randomly selected from dates in the year 2015, subject to the above constraint. 
*	Five hotels offer deals. 
*	Each hotel has a fixed price for rooms. 
*	Rebate and rebate plus three deals offer a rebate selected uniformly at random from between $10 and the cost of one night at the hotel. They are in intervals of $10. 
*	Percent deals offer discounts selected uniformly at random between 5% and 25%, in intervals of 5%.

## Overview

At a high level, my program reads in input from the given file line by line. It parses each line and determines if the user’s check-in date falls within the dates of the deal. If it is, the program calculates the value of that deal by finding the total cost of the user’s trip with that deal applied. The program keeps track of the best deal as it goes along and return it when it is finished. If there are no relevant deals, the program returns the appropriate error message along the way. The running time of this algorithm is linear in the number of possible deals, since it looks at each deal once and do constant work per deal. 

## Installation

If I were to have more time to work on this project, there are a number of improvements I could make to my approach. 
* First, my algorithm is “embarrassingly parallel,” since it is immediately clear how to extend it to multiple processors. By having each process find the best deal in a given section of the data and then comparing the solutions to find the best one, this problem can be solved much quicker and more efficiently using parallelization. 
* In addition, I am somewhat limited when writing this program in that the deals to consider could change each time the program is run, and the user inputs also have no discernible pattern. In real life, however, it is likely that certain trends would emerge among the user searches. I could use this information to cache the results of the searches to make the most common searches significantly faster. 
* In addition, the fact that I must read from a .csv file each time the program runs slows it down significantly. It would be very helpful if I could store the deals in a way that made it easy for me to get only the deals for a given hotel. Currently, I must search through all of the possible lines in the input file, since I know nothing about their order. 
* Finally, if I had more time, I would like to write tests for the code that I have currently written. The code is currently small enough that it is not too difficult to reason about without tests, but if I were ever to want to extend this code in any way, the first thing that I would do would be to write tests for my existing code. 

