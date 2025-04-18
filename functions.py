import argparse
import json
import os
import uuid
import datetime

EXPENSES_FILE = "expenses.json"

# Function to list expenses


def list_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []  # Retornar una lista vacía si el archivo no existe
    try:
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Si el archivo está vacío o tiene datos no válidos, retornar una lista vacía
        return []


# Function to save expenses
def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def validate_amount(amount):
    if amount <= 0:
        raise argparse.ArgumentTypeError("Amount must be a positive number.")

def validate_expense_id(expense_id, expenses):
    if not any(expense["id"] == expense_id for expense in expenses):
        raise argparse.ArgumentTypeError(
            f"Expense with ID {expense_id} does not exist.")

def add_expense(description, amount):
    try:
        validate_amount(amount)
        expenses = list_expenses()
        expenses_id = str(uuid.uuid4())
        expenses.append({"id": expenses_id, "name": description, "amount": amount,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d")})
        save_expenses(expenses)
        print(f"Added expense: {description} - ${amount} (ID: {expenses_id})")
    except ValueError as e:
        print(f"Error: {e}")

def display_expenses():
    expenses = list_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("Expenses:")
    for expense in expenses:
        print(
            f"ID: {expense['id']}, Description: {expense['name']}, Amount: ${expense['amount']} , Date: {expense['date']}")


def display_summary():
    expenses = list_expenses()
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ${total}")


def delete_expense(expense_id):
    try:
        expenses = list_expenses()
        validate_expense_id(expense_id, expenses)
        expenses = [expense for expense in expenses if expense["id"] != expense_id]
        save_expenses(expenses)
        print(f"Deleted expense with ID: {expense_id}")
    except ValueError as e:
        print(f"Error: {e}")
