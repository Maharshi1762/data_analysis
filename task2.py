import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

#Reading CSV File
csv_name = input("Enter CSV file name==>")
FileName = csv_name + '.csv'
df = pd.read_csv(FileName)

#Removing duplicate
remove_duplicate = df.drop_duplicates(subset='NAME', keep="first")
print("Remove duplicat:==>",remove_duplicate)


#Mean,Median and Mode
a = list(remove_duplicate['SALES'])
print(a)
sales_mean = statistics.mean(a)
print('Mean:==>',sales_mean)
sales_med = statistics.median(a)
print('Median:==>',sales_med)
sales_mode = statistics.mode(a)
print('Mode:==>',sales_mode)

#Graph of sales
b = list(remove_duplicate['NAME'])
print(b)
x = np.array(b)
y = np.array(a)
#plt.bar(x,y)
plt.plot(x,y,color='green', linestyle='dashed', linewidth=3,marker='p', markerfacecolor='blue', markersize=10)
plt.show()

#Apply Query
high_sale = df.loc[df['SALES']>50000]
print('More than 50,000 sales:==>\n',high_sale)

#Exploratory Data Analysis
a=df.head()
print('Head of data:==>\n',a)
b=df.tail()
print('Tail of data:==>\n',b)
c=df.shape
print('Shape of data:==>',c)
d=df.describe()
print('Describe of data:==>\n',d)
e=df.columns
print('Columns of data:==>\n',e)
f=df.nunique()
#f=df['SALES'].nunique()
print('Unique data:==>\n',f)
print("\nInformation about data:==>\n")
df.info()
