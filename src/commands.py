from src.spending import Expenses
from src.view import View

class Commands:

  def __init__(self) -> None:
    self.commands = ('Add Expense', 'Remove Expense', 'Add Category', 'View All', 'View Spending Categories', 'View Category Expenses', 'Exit')

  def listCommands(self):
    print('-'*30)
    for i,command in enumerate(self.commands):
      print(f"{i+1}: {command}")
    print()

  def getValidCommand(self):
    print("Hello!")
    print("Welcome to your Expense Tracker!")
    done = False
    while not done:
      self.listCommands()
      command = input("Enter Command: ")
      print()
      if command.isalpha():
        command = command.lower()
      if command == 'add expense' or command == '1':
        addEx = Expenses()
        addEx.addExpense()
      elif command == 'remove expense' or command == '2':
        pass
      elif command == 'add category' or command == '3':
        addCat = Expenses()
        addCat.addCategory()
        addCat.printCategories()
      elif command == 'view all' or command == '4':
        view = View()
        view.viewAll()
      elif command == 'view spending categories' or command == '5':
        view = View()
        view.viewSpendingCategories()
      elif command == 'view category expenses' or command == '6':
        view = View()
        view.viewCategory()
      elif command == 'exit' or command == '7':
        done = True
      else:
        print("Incorrect command")

    print("Have a Nice Day!")
    quit()
