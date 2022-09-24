from src.spending import Expenses
from src.view import View

class Commands:

  def __init__(self) -> None:
    self.commands = ('Monthly Summary', 'Add Expense', 'Remove Expense', 'Add Category', 'Remove Category', 'View All', 'View Spending Categories', 'View Category Expenses', 'Exit')

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
      if command == 'monthly summary' or command == '1':
        monthlySum = View()
        monthlySum.monthlySummary()
      elif command == 'add expense' or command == '2':
        addEx = Expenses()
        addEx.addExpense()
      elif command == 'remove expense' or command == '3':
        rmEx = Expenses()
        rmEx.removeExpense()
      elif command == 'add category' or command == '4':
        addCat = Expenses()
        addCat.addCategory()
        addCat.printCategories()
      elif command == 'remove category' or command == '5':
        rmCat = Expenses()
        rmCat.removeCategory()
        rmCat.printCategories()
      elif command == 'view all' or command == '6':
        viewAll = View()
        viewAll.viewAll()
      elif command == 'view spending categories' or command == '7':
        viewSCat = View()
        viewSCat.viewSpendingCategories()
      elif command == 'view category expenses' or command == '8':
        getCat = Expenses()
        categoryIndex = getCat.getValidCategory()
        category = getCat.categories[categoryIndex-1]
        viewCatExpense = View()
        totalAmt = viewCatExpense.viewCategoryExpenses(category)
        print(f"Total: ${totalAmt}")
      elif command == 'exit' or command == '9':
        done = True
      else:
        print("Incorrect command")

    print("Have a Nice Day!")
    quit()
