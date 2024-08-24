
class Payment:
    def __init__(self, payment_id, amount, due_date):
        self.payment_id = payment_id
        self.amount = amount
        self.due_date = due_date
        self.paid = False

    def process_payment(self):
        self.paid = True
        print(f"Payment of {self.amount} has been processed.")

    def reminder(self):
        if not self.paid:
            print(f"Reminder: Payment of {self.amount} is due on {self.due_date}.")

    def apply_penalty(self, penalty_amount):
        if not self.paid:
            self.amount += penalty_amount
            print(f"A penalty of {penalty_amount} has been applied. Total due: {self.amount}.")
