from metapub import pubmedcentral as pcm
import pandas as pd

df=pd.read_csv("/content/drive/MyDrive/data4scrap.csv",dtype=object)
df=df.drop(['Unnamed: 0'],axis=1)

f=open("citations.txt",'a')
for i in range(df.shape[0]): 
  f.write(pcm.get_pmid_for_otherid(df.iat[i,1]))
f.close()
