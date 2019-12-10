from pip._vendor.distlib.compat import raw_input
from xlrd import open_workbook
from os import system, name
import configparser as cp
import random

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()
config = cp.RawConfigParser()
config.read('app.properties')

wb = open_workbook(config.get('FileProperties','filepath'))

SHEET_PREFIX="Wordlist"
selected_sheet_index=-1

# for sheet in wb.sheets():
#     if sheet.name.startswith(SHEET_PREFIX):
#         number_of_rows = sheet.nrows
#         print(sheet.name+"("+str(number_of_rows)+")")

sheet=wb.sheet_by_index(int(config.get('FileProperties','sheetindex'))-1)
# while True:
#     selected_sheet=raw_input("Select the sheet: ")
#     if selected_sheet is not None and len(selected_sheet.strip())>0:
#         selected_sheet_index = int(selected_sheet.strip())
#         selected_sheet_name=SHEET_PREFIX+"-"+str(selected_sheet_index)
#         if (selected_sheet_index>0 and selected_sheet_index<len(wb.sheets())):
#             sheet=wb.sheet_by_index(selected_sheet_index)
#             print(selected_sheet_name+" is selected.")
#             break
quiz_size=int(config.get('FileProperties','quizsize'))
list=random.sample(range(sheet.nrows-2), quiz_size)
list=[x + 2 for x in list]

# print(list)

print("=================================================================================")
print()
for i in list:
    print("     "+sheet.cell(i,1).value)
print()
print("=================================================================================")
# print(list)

raw_input()

print("=====================================ANSWERS=====================================")
print()
for i in list:
    print("     "+str(sheet.cell(i,1).value).ljust(20,'-')+"----> "+sheet.cell(i, 2).value.replace("\n","; "))
print()
print("=================================================================================")