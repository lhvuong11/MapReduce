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
        # emit CustomerID and Amount
        # writes output into a file
        with open("mapper_output.txt", "a") as f:
            f.write("%s %s\n" % (CustomerID, Amount))

def mapper_output(file):
    # read in mapper_output, remove whitespace
    for line in file:
        yield line.strip().split(' ')

def shuffler(file):
    data = mapper_output(file)

    #sort by CustomerID, 
    for key, keygroup in groupby(data, itemgetter(0)):
        #print([(k,v) for k,v in keygroup])
        values = sorted(v for k,v in keygroup)
    #key_sort = sorted(data, key=lambda x: x[0])


# string = "CustomerID, Amount
transactions = [
    "Alice, 20",
    "Bob, 50",
    "Alice, 30",
    "Bob, 20",
    "Charlie, 40"
]

# processes the list of customer transactions
mapper(transactions)
shuffler('mapper_output.txt')

