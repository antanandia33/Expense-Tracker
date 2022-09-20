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

      