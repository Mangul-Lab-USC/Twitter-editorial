#Initial Data Preprocessing of PubMed Data
#by Aditya Sarkar
import pandas as pd

file1 = open('drive/MyDrive/out.txt', 'r') 
Lines = file1.readlines()

file2 = open('drive/MyDrive/outch.txt', 'w')

c=0
for line in Lines:
  t=line
  if(len(t.split(','))==4):
    file2.writelines(line)

df = pd.read_csv('drive/MyDrive/outch.txt', sep=",", header=None)
df.columns = ["Journal", "PMC_ID", "Lastname", "Firstname"]

df.head(10)

df=df.drop([0])
df.head(10)

df.to_csv("pubmed_data.csv")

a=[]
for i in range(df.shape[0]):
  a.append(df.iat[i,2])
a=list(set(a))
print(len(a))

a=[]
for i in range(df.shape[0]):
  a.append(df.iat[i,3])
a=list(set(a))
print(len(a))