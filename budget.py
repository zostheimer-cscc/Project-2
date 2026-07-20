"""
Program Name: budget.py
Author: zachary ostheimer
Purpose: Defines the Budget class, which manages a collection of Transaction
         objects.
Starter Code: None
Date: 07/16/2026

"""
from transaction import Income, Expense

class Budget:
    """Manage a collection of transactions and report on them.
 
    A Budget holds a list of Transaction objects (composition). It does not
    inherit from Transaction because a budget is not itself a transaction;
    it is a container that organizes many of them.
    """
 
    def __init__(self):
        """Initialize a budget with an empty list of transactions."""
        self.transactions = []
 
    def add_transaction(self, transaction):
        """Add a Transaction object to the budget."""
        self.transactions.append(transaction)
 
    def remove_transaction(self, index):
        """Remove the transaction at the given index.
 
        Returns the removed transaction. Raises IndexError if the index is
        out of range, which the caller is expected to handle.
        """
        return self.transactions.pop(index)
