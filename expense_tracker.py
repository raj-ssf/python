class ExpenseTracker:
    def __init__(self):
        self.expenses = []     # list of dicts: {"category", "amount", "description"}
        self.budget = 0

    def add_expense(self, category, amount, description):
        tracker = {"category":  category, "amount" : amount, "description": description}
        self.expenses.append(tracker)
        print(f" Expense {category} for amount {amount:.2f} by description {description}")

    def view_all(self):
        if not self.expenses:
            print("No expenses yet")
            return
        for i, item in enumerate(self.expenses, 1):
            print(f"{i}. {item['category']}  | {item['amount']:.2f} | {item['description']}")
        total = sum(item['amount'] for item in self.expenses)
        print(f"Total: ${total:.2f}")
        
    def view_summary(self):
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount
        
        print("----------Summary of Everything---------")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
            
            
        total = self.get_total()
        print(f"Total: ${total:.2f}")

        if self.budget > 0:
            remaining = self.budget - total
            percent = (remaining / self.budget) * 100
            print(f"Budget: ${total:.2f} / ${self.budget:.2f} ({percent:.1f}% remaining)")
                   
    def set_budget(self, amount):
        self.budget = amount
        print(f"Budget has been set to {self.budget:.2f}")
    
    def get_total(self):
        return sum(item['amount'] for item in self.expenses)


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View summary by category")
        print("4. Set budget")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == "1":
            category = input("Category: ")
            amount = float(input("Amount: "))
            description = input("Description: ")
            tracker.add_expense(category, amount, description)
        elif choice == "2":
            tracker.view_all()
        elif choice == "3":
            tracker.view_summary()
        elif choice == "4":
            amount = float(input("Enter budget: "))
            tracker.set_budget(amount)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

main()