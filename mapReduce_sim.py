# INFM 203 Assignment 2: MapReduce Simulation

from itertools import groupby
from operator import itemgetter

#implment a map function
def mapper(transactions):
    for line in transactions:
        # split string into CustomerID and Amount
        line = line.strip()
        tokens = line.split(",")
        CustomerID = tokens[0]
        Amount = int(tokens[1])
        # emit CustomerID and Amount, writes output into a file
        with open(filename, "a") as f:
            f.write("%s %s\n" % (CustomerID, Amount))
    return filename #returns the file path as a string

def read_mapper():
    # read in mapper_output, remove whitespace
    for line in filename:
        yield line.strip().split(' ')

def shuffler():
    with open(filename, "r") as f:
        data = read_mapper()
        #for line in f:
            #CustomerID, Amount = line.strip().split(' ')
            #sortedID = " ".join(sorted([CustomerID]))
            #print(f"CustomerID: {sortedID}")
            #group transactions by each customer
        
        for key, keygroup in groupby(data, itemgetter(0)):
            values = ' '.join(sorted(v for k, v in keygroup))
            print("%s %s\n" % (key, values))




# string = "CustomerID, Amount
transactions = [
    "Alice, 20",
    "Bob, 50",
    "Alice, 30",
    "Bob, 20",
    "Charlie, 40"
]

filename = 'mapper_output.txt'

# processes the list of customer transactions
mapper(transactions)
shuffler()

