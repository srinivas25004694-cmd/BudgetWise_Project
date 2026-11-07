# ==========================================
# BUDGETWISE - PERSONAL BUDGET PLANNER
# ==========================================

# Function 1: Set Monthly Budget

def set_budget(amount):

    if amount <= 0:
        raise ValueError("Budget must be greater than zero.")

    return amount


# Function 2: Add Expenses

def add_expense(expenses, category, amount):

    if not category.strip():
        raise ValueError("Category cannot be empty.")

    if amount <= 0:
        raise ValueError("Expense must be greater than zero.")

    expenses.append({
        "category": category.title(),
        "amount": amount
    })

    return expenses


# Function 3: Calculate Total Expenses

def total_expenses(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# Function 4: Calculate Remaining Budget

def remaining_budget(budget, expenses):

    if budget <= 0:
        raise ValueError("Invalid budget.")

    return budget - total_expenses(expenses)


# Function 5: Overspending Alert

def overspending_alert(budget, expenses):

    spent = total_expenses(expenses)

    if spent > budget:
        return "WARNING! You have exceeded your budget."

    elif spent == budget:
        return "Your entire budget has been used."

    else:
        return "Good! You are within your budget."


# Function 6: Category-wise Analysis

def category_analysis(expenses):

    analysis = {}

    for expense in expenses:

        category = expense["category"]

        if category in analysis:
            analysis[category] += expense["amount"]

        else:
            analysis[category] = expense["amount"]

    return analysis


# Function 7: Calculate Savings

def calculate_savings(income, expenses):

    if income < 0:
        raise ValueError("Income cannot be negative.")

    return income - total_expenses(expenses)


# Function 8: Generate Monthly Report

def monthly_report(budget, expenses):

    spent = total_expenses(expenses)

    remaining = remaining_budget(budget, expenses)

    analysis = category_analysis(expenses)

    return {
        "budget": budget,
        "total_expenses": spent,
        "remaining": remaining,
        "categories": analysis,
        "status": overspending_alert(budget, expenses)
    }
