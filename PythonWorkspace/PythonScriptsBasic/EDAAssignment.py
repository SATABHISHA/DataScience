import pandas as pd
from tabula import read_pdf

#df = pd.read_excel(r'C:\Users\user\Downloads\PythonWorkspace\iPythonNotebook\demo.xlsx', sheet_name='Sheet1')
df = read_pdf(r'C:\Users\user\Downloads\git\DataScience\PythonWorkspace\Assignment\EdaAssignment\Dataset.pdf')
print(df)