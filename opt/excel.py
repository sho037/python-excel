import pandas as pd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

df = pd.read_excel('sales.xlsx')

print(df) # df内にあるsales.xlsxのデータを出力

for row in df.values:
    ws.append([row[0],row[1]])

wb.save('test.xlsx')