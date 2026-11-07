# ==========================================
# BUDGETWISE - MAIN PROGRAM
# ==========================================

from budget_pkg import (
    set_budget,
    add_expense,
    remaining_budget,
    overspending_alert,
    category_analysis,
    calculate_savings,
    monthly_report
)


def display_banner():

    print("\n")
    print("=" * 55)
    print("              BUDGETWISE")
    print("       SMART PERSONAL BUDGET PLANNER")
    print("=" * 55)


def main():

    display_banner()

    expenses = []

    try:

        income = float(input("\nEnter your monthly income: ₹"))

        budget = float(input("Enter your monthly budget: ₹"))

        budget = set_budget(budget)

        if income < 0:
            raise ValueError("Income cannot be negative.")

    except ValueError as error:

        print("Invalid input:", error)
        return

    while True:

        print("\n")
        print("1. Add Expense")
        print("2. View Remaining Budget")
        print("3. Category-wise Analysis")
        print("4. Overspending Alert")
        print("5. Calculate Savings")
        print("6. Monthly Report")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            category = input("Enter expense category: ")

            try:

                amount = float(input("Enter expense amount: ₹"))

                add_expense(expenses, category, amount)

                print("\nExpense added successfully!")

            except ValueError as error:

                print("Error:", error)

        elif choice == "2":

            remaining = remaining_budget(budget, expenses)

            print("\nRemaining Budget: ₹", round(remaining, 2))

        elif choice == "3":

            analysis = category_analysis(expenses)

            print("\nCATEGORY-WISE EXPENSES")

            if not analysis:
                print("No expenses recorded.")

            for category, amount in analysis.items():

                print(category, ": ₹", round(amount, 2))

        elif choice == "4":

            print("\n", overspending_alert(budget, expenses))

        elif choice == "5":

            savings = calculate_savings(income, expenses)

            print("\nYour Current Savings: ₹", round(savings, 2))

        elif choice == "6":

            report = monthly_report(budget, expenses)

            print("\n")
            print("=" * 45)
            print("           MONTHLY REPORT")
            print("=" * 45)

            print("Monthly Budget : ₹", report["budget"])

            print("Total Expenses: ₹", report["total_expenses"])

            print("Remaining     : ₹", report["remaining"])

            print("\nCategory Analysis:")

            if not report["categories"]:
                print("No expenses recorded.")

            for category, amount in report["categories"].items():

                print(category, ": ₹", amount)

            print("\nBudget Status:", report["status"])

            print("=" * 45)

        elif choice == "7":

            print("\nThank you for using BudgetWise!")
            print("Track Smart. Spend Wise. Save More.")
            break

        else:

            print("\nInvalid choice! Please select 1-7.")


if __name__ == "__main__":
    main()
