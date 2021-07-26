import xlrd

location = ("D:\\follower data\\9august.xlsx")
wb = xlrd.open_workbook(location)
sheet =  wb.sheet_by_index(0)
count = 0
for i in range(sheet.nrows):
    if count<200:
       print(f'"{sheet.cell_value(i,1)}" ,')
    count +=1



