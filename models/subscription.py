from abc import ABC, abstractmethod

class Subscription(ABC):
    def __init__(self, member_email, amount, date):
        self.member_email = member_email
        self.amount = amount
        self.date = date

    @abstractmethod
    def process_payment(self):
        pass

class MonthlySubscription(Subscription):
    def process_payment(self):
        print(f"Processing monthly subscription of {self.amount} for {self.member_email}")

class AnnualSubscription(Subscription):
    def process_payment(self):
        print(f"Processing annual subscription of {self.amount} for {self.member_email}")

class Donation(Subscription):
    def process_payment(self):
        print(f"Processing donation of {self.amount} for {self.member_email}")
