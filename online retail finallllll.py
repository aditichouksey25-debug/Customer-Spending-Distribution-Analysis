import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest
df=pd.read_csv(r"C:\Users\aditi\Documents\Online Retail.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
df=df.dropna(subset=["CustomerID"])
print(df.isnull().sum())
print(df.info())
print(df.duplicated().sum())
df=df.drop_duplicates()
print(df.duplicated().sum())
print(df.info())
print(df["Quantity"].min())
print(df["UnitPrice"].min())
df=df[df["Quantity"]>0]
df=df[df["UnitPrice"]>0]
print(df.info())
df["Transaction Amount"]=df["Quantity"]*df["UnitPrice"]
print(df.head())
print(df["Transaction Amount"].min())
print(df["Transaction Amount"].max())
print(round((df["Transaction Amount"].mean()),2))
print(round(df["Transaction Amount"].std(),2))
plt.hist(df["Transaction Amount"],bins=50)
plt.title("Customer spending distribution With Outliers")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.xlim(0,200000)
plt.ylim(0,30)
plt.show()
df2=df[df["Transaction Amount"]<=500]
plt.hist(df2["Transaction Amount"])
plt.title("Customer spending WITHOUT Outliers")
plt.xlim(0,500)
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()
plt.boxplot(df["Transaction Amount"])
plt.title("Customer spending distribution with Outliers")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()
plt.boxplot(df2["Transaction Amount"])
plt.title("Customer spending distribution Without Outliers")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()
df["Z-Score"]=zscore(df["Transaction Amount"])
print(df.info())
print(df.head())
print(round(df["Z-Score"],2))
print((df["Z-Score"]>3).sum())
print((df["Z-Score"]<=3).sum())
print(df["Z-Score"].min())
print(df["Z-Score"].max())
Outliers=df[abs(df["Z-Score"]>3)]
print(len(Outliers))
Normal=df[abs(df["Z-Score"]<=3)]
print(len(Normal))
print(round((len(Outliers)/(len(Normal))*100),2))
model=IsolationForest(contamination=0.0009,random_state=42)
df["AI_Anomaly"]=model.fit_predict(df[["Transaction Amount"]])
print((df["AI_Anomaly"]==-1).sum())
ai_outliers=((df["AI_Anomaly"]==-1).sum())
print("Z_Score Outliers:",342)
print("AI Outliers:",ai_outliers)
ai_anomalies=df[df["AI_Anomaly"]==-1]
print(df.head(10))
print(df.info)
print(df.head())
plt.figure(figsize=(10,5))
plt.scatter(
    df[df["AI_Anomaly"]==1].index,
    df[df["AI_Anomaly"]==1]["Transaction Amount"],
    s=5,
    label="Normal")
plt.scatter(
    df[df["AI_Anomaly"]==-1].index,
    df[df["AI_Anomaly"]==-1]["Transaction Amount"],
    s=20,
    label="Anomaly")
plt.ylim(0,5000)
plt.title("AI-Based Anomaly Detection")
plt.xlabel("Transaction Index")
plt.ylabel("Transaction Amount")
plt.legend()
plt.show()