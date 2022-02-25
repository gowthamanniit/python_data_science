import pandas as pd
'''
s=[11,22,33,44,55,60,90]
m=['a','b','c','d','e','f','g']
#k=pd.Series(m)
k=pd.Series(s,m)   
print(k)
'''

#pip install openpyxl
'''
test_df=pd.read_excel('student.xlsx','mysheet')
print(test_df.tail(3)) # first 3 rows  head->top,tail->bottom
print(test_df)         # all rows
'''

# convert .xlsx to .csv
'''
test_df=pd.read_excel('student.xlsx','mysheet')
test_df.to_csv("myfile.csv")
print(test_df)
'''
#open csv file
'''
test_df=pd.read_csv('myfile.csv')
print(test_df)
print(test_df.head(2))
'''
# convert .csv to .xlsx

test_df=pd.read_csv('myfile.csv')
test_df.to_excel("myexcel.xlsx")
print(test_df)



