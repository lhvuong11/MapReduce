## Implement a MapReduce Simulation in Python

MapReduce is a programming model for processing large datasets in a distributed manner. It consists of two key functions:

    Map Function: Processes input data and emits key-value pairs.
    Reduce Function: Aggregates and processes the key-value pairs produced by the Map function.

### Why MapReduce Requires a Cluster

MapReduce is designed to process large-scale data across multiple machines in a distributed cluster. Typically, real-world implementations use frameworks like Hadoop or Spark, where data is divided into chunks and processed in parallel by different nodes in a cluster. The Map function runs on multiple machines to process data simultaneously, and the Reduce function aggregates the results efficiently. However, in this assignment, we will simulate MapReduce using Python on a single machine without requiring a cluster.

### Problem Statement

You are tasked with implementing a MapReduce simulation in Python. Your program should process a list of customer transactions and calculate the total amount spent by each customer.

### Task Requirements

    Implement a Map Function:
        Split each transaction string into CustomerID and Amount.
        Convert the Amount to a numerical value.
        Emit key-value pairs where key = CustomerID and value = Amount.

    Implement a Shuffle and Sort Function:
        Group transactions by CustomerID.

    Implement a Reduce Function:
        Sum up the amounts spent by each customer.

    Run the Simulation:
        Process a list of transactions and output the total amount spent by each customer.
