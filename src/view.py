from src.spending import Expenses
import re

class View:

  def __init__(self) -> None:
    pass

  def viewAll(self):
    print('-'*30)
    print("ALL EXPENSES")
    with open('src/data/allExpenses.txt', 'r') as file:
      lines = file.readlines()
      totalAmt = lines[0]
      for i in range(1,len(lines)):
        data = re.split('\||\n', lines[i])
        print(f'{data[0]} {data[1]} {data[2]} {data[3]}\n')
      print(f"Total: ${totalAmt}")

  
  def viewSpendingCategories(self):
    print('-'*30)
    print("CATEGORIES\n")
    with open('src/data/spendingCategories.txt', 'r') as file:
      lines = file.read()
      lines = lines.split()
      for line in lines:
        print(line)

  def viewCategory(self): 
    print('-'*30)
    print("Enter category number")
    expenses = Expenses()
    expenses.printCategories()
    validResponse = False
    index = 0
    while not validResponse:
      try:
        index = int(input("Enter the category number: "))
        validResponse = expenses.checkCategoryNum(index-1)
        print()
      except ValueError:
        print("Enter the number corresponding to the categories stated above")
    category = expenses.categories[index-1]
    with open(f'src/Data/{category}.txt') as file:
      print('-'*30)
      print(f"CATEGORY: {category}")
      lines = file.readlines()
      totalAmt = lines[0]
      for i in range(1,len(lines)):
        data = re.split('\||\n', lines[i])
        print(f'{data[0]} {data[1]} {data[2]}\n')
      print(f"Total: ${totalAmt}")