# INFM 203 Assignment 2: MapReduce Simulation

from itertools import groupby
from operator import itemgetter

#implment a map function
def mapper(transactions, filename="mapper_output.txt"):
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

def read_mapper(file):
    # read in mapper_output, remove whitespace
    for line in file:
        yield line.strip().split(' ')

def shuffler(file):
    #data = read_mapper(file)
    with open(file, "r") as f:
        for line in f:
            CustomerID, Amount = line.strip().split(' ')
            sortedID = " ".join(sorted([CustomerID]))
            print(f"CustomerID: {sortedID}, Amount: {Amount}")
            
            #group transactions by each customer
            #for key, keygroup in groupby(tokens, itemgetter(0)):
                #with open("shuffler_output.txt", "a") as f:
            #values = ' '.join(sorted(v for k, v in keygroup))
            #f.write("%s %s\n" % (key, values))



# string = "CustomerID, Amount
transactions = [
    "Alice, 20",
    "Bob, 50",
    "Alice, 30",
    "Bob, 20",
    "Charlie, 40"
]

# processes the list of customer transactions
shuffler(mapper(transactions))

