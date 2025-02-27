def input_transaction():
  """Gets transaction details from the user."""
  date = input("Enter transaction date (YYYY-MM-DD): ")
  amount = float(input("Enter transaction amount: "))
  description = input("Enter transaction description: ")
  category = input("Enter transaction category: ")

  transaction = {
      "date": date,
      "amount": amount,
      "description": description,
      "category": category,
  }
  return transaction


def display_transactions(transactions):
  """Displays a list of transactions."""
  print("-" * 20)
  for transaction in transactions:
    print(f"Date: {transaction['date']}")
    print(f"Amount: {transaction['amount']}")
    print(f"Description: {transaction['description']}")
    print(f"Category: {transaction['category']}")
    print("-" * 20)


def main():
  """Main function to run the program."""
  transactions = []

  while True:
    print("\nOptions:")
    print("1. Add transaction")
    print("2. View transactions")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      new_transaction = input_transaction()
      transactions.append(new_transaction)
    elif choice == "2":
      display_transactions(transactions)
    elif choice == "3":
      break
    else:
      print("Invalid choice.")


if __name__ == "__main__":
  main()
