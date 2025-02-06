import csv

class ExpenseTracker:
    def __init__(self, file_name="expenses.csv"):
        self.file_name = file_name
        self.load_data()

    def load_data(self):
        # Initialize the file and read data
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.reader(file)
                self.data = [row for row in reader]
        except FileNotFoundError:
            self.data = []
            with open(self.file_name, mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(["Type", "Category", "Amount", "Description"])

    def add_transaction(self, trans_type, category, amount, description):
        # Add a transaction
        with open(self.file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([trans_type, category, amount, description])
        print("Transaction added successfully.")

    def show_summary(self):
        # Display summary of transactions
        print("\nSummary of Transactions:")
        income = 0
        expense = 0
        for row in self.data[1:]:
            if row[0] == "Income":
                income += float(row[2])
            elif row[0] == "Expense":
                expense += float(row[2])
        print(f"Total Income: ${income}")
        print(f"Total Expenses: ${expense}")
        print(f"Net Balance: ${income - expense}")

    def view_transactions(self):
        # Display all transactions
        print("\nTransactions:")
        if len(self.data) > 1:
            for row in self.data[1:]:
                print(f"{row[0]} | {row[1]} | ${row[2]} | {row[3]}")
        else:
            print("No transactions found.")

    def run(self):
        while True:
            print("\n--- Personal Expense Tracker ---")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Show Summary")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                trans_type = input("Enter type (Income/Expense): ").capitalize()
                category = input("Enter category (e.g., Food, Rent, Salary): ")
                amount = input("Enter amount: ")
                description = input("Enter a short description: ")
                self.add_transaction(trans_type, category, amount, description)

            elif choice == "2":
                self.view_transactions()

            elif choice == "3":
                self.show_summary()

            elif choice == "4":
                print("Exiting Expense Tracker. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

# Run the Expense Tracker
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
