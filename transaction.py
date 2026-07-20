"""
Program Name: transaction.py
Author: zachary ostheimer
Purpose: Defines the Transaction base class and its Income and Expense
         subclasses
Starter Code: None
Date: 07/16/2026

"""
class Transaction:
    """Represent a single financial transaction."""

    def __init__(self, amount, category, date):
        self.amount = float(amount)
        self.category = category
        self.date = date

    def get_effect(self):
        """Return how this transaction changes a running balance."""
        return 0.0

    def get_type(self):
        return "transaction"

    def to_dictionary(self):
        return {
            "type": self.get_type(),
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
        }

    def __str__(self):
        return f"{self.date} | {self.get_type().title()} | {self.category} | ${self.amount:.2f}"


class Income(Transaction):
    """Represent money coming in. Adds to the balance."""

    def get_effect(self):
        return self.amount
    def get_type(self):
        return "income"


class Expense(Transaction):
    """Represent money going out. Subtracts from the balance."""

    def get_effect(self):
        return -self.amount
    def get_type(self):
        return "expense"