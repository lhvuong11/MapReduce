import re

#implment a map function
def mapper(transactions):
    for line in transactions:
        # split string into CustomerID and Amount
        line = line.strip()
        tokens = line.split(",")
        # convert Amount to numerical value
        Amount = float(tokens[1].strip())
        for token in tokens:
            # emit each token with a count of 1
            print(f"{token}\t1")

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
