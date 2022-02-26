from pandas import *

xls = ExcelFile('results.xls')
df = xls.parse(xls.sheet_names[0])
# print (df.to_dict())

for x in df:
    # combine 