# INFM 203 Assignment 2: MapReduce Simulation

from itertools import groupby
from operator import itemgetter

#implment a map function
def mapper(transactions, filename="mapper_output.txt"):
    with open(filename, "w") as f:
        for line in transactions:
            # split string into CustomerID and Amount
            line = line.strip()
            tokens = line.split(",")
            CustomerID = tokens[0]
            Amount = int(tokens[1])
            # emit CustomerID and Amount
            # writes output into a file that stores the key, value pairs
            f.write("%s %s\n" % (CustomerID, Amount))
    return filename #returns the file path as a string

def read_mapper(filename):
    # read in mapper_output, remove whitespace
    with open(filename, "r") as f:
        for line in f:
            yield line.strip().split(' ')

def shuffler(filename):
    data = read_mapper(filename)

    #sorting data by CustomerID key
    pairs = sorted(data, key=itemgetter(0))

    #grouping the data by CustomerID key 
    for key, keygroup in groupby(pairs, itemgetter(0)):
        #values = ' '.join(v for k, v in keygroup)
        values = [int(v) for k, v in keygroup]
        yield key, values
        #print("%s %s" % (key, values))

def reducer(shuffled_file):
    #sum the amounts for each CustomerID
    for key, value in shuffled_file:
        #total = sum(int(v) for k, v in value)
        #total = sum(int(v) for v in key[1:])
        yield key, sum(value)

# string = CustomerID, Amount
transactions = [
    "Alice, 20",
    "Bob, 50",
    "Alice, 30",
    "Bob, 20",
    "Charlie, 40"
]

# processes the list of customer transactions
mapped_file = mapper(transactions)
shuffled_file = shuffler(mapped_file)

print("\nGiven transactions of:")
for transaction in transactions:
    print(transaction)

print("\nThe total amount spent by each customer is:")
for key, value in reducer(shuffled_file):
    #prints the customer's name as capitalized even if originally lowercase
    print("%s: %s" % (key.capitalize(), value))
print("\n")

"""
tested successfully with the following transactions:
transactions = [
    "Dylan, 100",
    "Alice, 20",
    "Bob, 50",
    "Alice, 50",
    "Charlie, 100"
]

transactions = [
    "dylan, 1",
    "Alice,  20",
    "dylan, 5",
    "Alice, 50",
    "Charlie,  100"
]

"""