import sqlite3


def create_database():
  """Creates the database and table if they don't exist."""
  conn = sqlite3.connect('finance_tracker.db')
  cursor = conn.cursor()

  cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            description TEXT,
            category TEXT
        )
    ''')
  conn.commit()
  conn.close()


def get_db_connection():
  """Returns a database connection and cursor."""
  conn = sqlite3.connect('finance_tracker.db')
  cursor = conn.cursor()
  return conn, cursor


def input_transaction():
  """Gets transaction details from the user and saves to the database."""
  date = input("Enter transaction date (YYYY-MM-DD): ")
  amount = float(input("Enter transaction amount: "))
  description = input("Enter transaction description: ")
  category = input("Enter transaction category: ")

  conn, cursor = get_db_connection()
  cursor.execute(
      '''
        INSERT INTO transactions (date, amount, description, category)
        VALUES (?, ?, ?, ?)
    ''', (date, amount, description, category))
  conn.commit()
  conn.close()
  print("Transaction added successfully!")


def display_transactions():
  """Displays all transactions from the database."""
  conn, cursor = get_db_connection()
  cursor.execute("SELECT * FROM transactions")
  transactions = cursor.fetchall()
  conn.close()

  print("-" * 20)
  if transactions:
    for transaction in transactions:
      print(f"ID: {transaction[0]}")
      print(f"Date: {transaction[1]}")
      print(f"Amount: {transaction[2]}")
      print(f"Description: {transaction[3]}")
      print(f"Category: {transaction[4]}")
      print("-" * 20)
  else:
    print("No transactions found.")


def input_transaction_from_csv(date, amount, description, category):
  """Add transaction details from the csv to the database."""

  conn, cursor = get_db_connection()
  cursor.execute(
      '''
        INSERT INTO transactions (date, amount, description, category)
        VALUES (?, ?, ?, ?)
    ''', (date, amount, description, category))
  conn.commit()
  conn.close()
  print("Transaction from csv added successfully!")


def main():
  """Main function to run the program."""
  create_database()
  while True:
    print("\nOptions:")
    print("1. Add transaction")
    print("2. View transactions")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      new_transaction = input_transaction()
    elif choice == "2":
      display_transactions()
    elif choice == "3":
      break
    else:
      print("Invalid choice.")


if __name__ == "__main__":
  main()
