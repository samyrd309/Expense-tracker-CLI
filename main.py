import argparse
from functions import add_expense, display_expenses, display_summary, delete_expense
# Parser configuration
parser = argparse.ArgumentParser(
    description="A simple command-line expense tracker."
)

subparsers = parser.add_subparsers(dest="command", required=True)

# Subparser for adding an expense
add_parser = subparsers.add_parser("add", help="Add a new expense")
add_parser.add_argument("-d", "--description", type=str,
                        help="Description of the expense")
add_parser.add_argument("-a", "--amount", type=float,
                        help="Amount of the expense")

list_parser = subparsers.add_parser("list", help="List all expenses")

summary_parser = subparsers.add_parser(
    "summary", help="Display total expenses")

delete_parser = subparsers.add_parser("delete", help="Delete an expense")
delete_parser.add_argument("-i", "--id", type=str,
                           help="ID of the expense to delete")


args = parser.parse_args()

if args.command == "add":
    add_expense(args.description, args.amount)
elif args.command == "list":
    display_expenses()
elif args.command == "summary":
    display_summary()
elif args.command == "delete":
    delete_expense(args.id)
