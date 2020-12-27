import openpyxl

# Create Object for workbook

wb = openpyxl.Workbook()

# grab the active sheet
sh = wb.active

# Set the sheetName
sh.title = "Validation"

sh['A1'] = "FirstName"
sh['B1'] = "LastName"
sh['C1'] = "Email"

sh['A2'] = "Divya"
sh['B2'] = "X"
sh['C2'] = "divya@gmail.com"

wb.save(r'C:\Python\Python_Dec\data\TC002.xlsx')



