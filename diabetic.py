import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df= pd.read_csv("diabetes.csv")
print(df.head())
# df.info() #to print the full summary

#Task 1 compute mean values and variance for all values 
# THE MEAN , Variance , standard deviation per AGE

mean= df['AGE'].mean()
var=df['AGE'].var()
std=df['AGE'].std()
print(f"\n\nMean={mean} \nVariance={var} \nStandard Deviation ={std}\n")

# THE Mean , Variance and standard deviation per SEX 

mean= df['SEX'].mean()
var=df['SEX'].var()
std=df['SEX'].std()
print(f"\n\nMean={mean} \nVariance={var} \nStandard Deviation ={std}\n")

#Task 2: Plot boxplots for BMI, BP and Y depending on gender

plt.figure(figsize=(10,2))
plt.boxplot(df['BMI'],vert=False,showmeans=True)
plt.grid(color='green',linestyle='dotted')
plt.show()

plt.figure(figsize=(10,2))
plt.boxplot(df['BP'],vert=False,showmeans=True)
plt.grid(color='yellow',linestyle='dotted')
plt.show()


plt.figure(figsize=(10,2))
plt.boxplot(df['Y'],vert=False,showmeans=True)
plt.grid(color='blue',linestyle='dotted')
plt.show()

#Task 3: What is the distribution of Age, Sex, BMI and Y variables?

df['AGE'].hist(bins=15)
plt.suptitle('AGE distribution of diabetes patient')
plt.xlabel('AGE')
plt.ylabel('Count')
plt.show()

#Task 4: Test the correlation between different variables and disease progression (Y)

plt.scatter(df['BMI'], df['Y'])
plt.show()



