import json
from pathlib import Path
from datetime import datetime

FILE = Path("expenses.json")


def load_data():
    if FILE.exists():
        try:
            return json.loads(FILE.read_text())
        except json.JSONDecodeError:
            pass

    return {
        "income": [],
        "expenses": []
    }


def save_data(data):
    FILE.write_text(
        json.dumps(data, indent=4, ensure_ascii=False)
    )


def add_income(data):
    try:
        amount = float(input("Income amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    source = input("Source: ")

    data["income"].append({
        "amount": amount,
        "source": source,
        "date": datetime.now().strftime("%Y-%m-%d")
    })

    save_data(data)
    print("Income added!")


def add_expense(data):
    try:
        amount = float(input("Expense amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Category: ")
    description = input("Description: ")

    data["expenses"].append({
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    })

    save_data(data)
    print("Expense added!")


def show_report(data):
    income = sum(
        item["amount"]
        for item in data["income"]
    )

    expenses = sum(
        item["amount"]
        for item in data["expenses"]
    )

    balance = income - expenses

    print("\n===== FINANCIAL REPORT =====")
    print(f"Income:   ${income:.2f}")
    print(f"Expenses: ${expenses:.2f}")
    print(f"Balance:  ${balance:.2f}")


def show_expenses(data):
    if not data["expenses"]:
        print("No expenses.")
        return

    for i, expense in enumerate(
        data["expenses"], 1
    ):
        print(
            f"{i}. "
            f"${expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['date']}"
        )


def main():
    data = load_data()

    while True:
        print("""
===== EXPENSE TRACKER =====

1. Add Income
2. Add Expense
3. Show Expenses
4. Financial Report
5. Exit
""")

        choice = input("> ")

        if choice == "1":
            add_income(data)

        elif choice == "2":
            add_expense(data)

        elif choice == "3":
            show_expenses(data)

        elif choice == "4":
            show_report(data)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
