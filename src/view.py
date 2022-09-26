import re
from datetime import datetime

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
        print(f'DATE: {data[0]} CATEGORY: {data[1]} AMOUNT: ${data[2]} DETAILS: {data[3]}\n')
      print(f"Total: ${totalAmt}")

  
  def viewSpendingCategories(self):
    print('-'*30)
    print("CATEGORIES\n")
    with open('src/data/spendingCategories.txt', 'r') as file:
      lines = file.read()
      lines = lines.split()
      for line in lines:
        print(line)


  def viewCategoryExpenses(self, category:str):
    print('-'*30)
    with open(f'src/Data/{category}.txt') as file:
      print(f"CATEGORY: {category}")
      lines = file.readlines()
      totalAmt = lines[0]
      for i in range(1,len(lines)):
        data = re.split('\||\n', lines[i])
        print(f'{i}) DATE: {data[0]} AMOUNT: ${data[1]} DETAILS: {data[2]}\n')
    return totalAmt


  def monthlySummary(self):
    with open('src/Data/allExpenses.txt', 'r') as file:
      lines = file.readlines()
      lines.reverse()
      currentMonth = datetime.now().strftime('%m')
      currentYear = datetime.now().strftime('%Y')
      total = 0
      catExpenses = {}
      print('-'*30)
      print(f"MONTHLY SUMMARY: {datetime.now().strftime('%B')}\n")
      for i in range(len(lines)-1):
        data = re.split('\||\n', lines[i])
        date = data[0]
        date = date.split('-')
        if date[0] == currentYear and date[1] == currentMonth:
          print(f'DATE: {data[0]} CATEGORY: {data[1]} AMOUNT: ${data[2]} DETAILS: {data[3]}\n')
          if data[1] not in catExpenses:
            catExpenses[data[1]] = float(data[2])
          else:
            catExpenses[data[1]] = float(catExpenses[data[1]]) + float(data[2])
          total = total + float(data[2])
      print("CATEGORIES:")
      for cat, amt in catExpenses.items():
        print(f'{cat}: ${amt}')
      print(f'\nTOTAL:\n${total}')  