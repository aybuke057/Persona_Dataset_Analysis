import pandas as pd


df = pd.read_csv('datasets/persona.csv')
df.head()
df.shape
df.columns
df.dtypes
df.value_counts()
df.describe()
df.isnull().sum()

df['SOURCE'].nunique()
df['SOURCE'].value_counts()

df['PRICE'].nunique()

df['PRICE'].value_counts()

df['COUNTRY'].value_counts()

df.groupby("COUNTRY")["PRICE"].sum()

df['SOURCE'].value_counts()

df.groupby("COUNTRY")["PRICE"].mean()

df.groupby("SOURCE")["PRICE"].mean()

df.groupby(["COUNTRY","SOURCE"])["PRICE"].mean()

df.groupby(["COUNTRY","SOURCE", "SEX", "AGE"])["PRICE"].mean()

agg_df = df.groupby(["COUNTRY","SOURCE", "SEX", "AGE"])["PRICE"].mean().sort_values(ascending=False)

agg_df.reset_index()

df["AGE_CAT"] =pd.cut(df["AGE"], bins=[0, 18, 23, 30, 40, 70], labels=['0_18', '19_23', '24_30', '31_40', '41_70'])


df["COUNTRY"] = df["COUNTRY"].astype(str)
df["SOURCE"] = df["SOURCE"].astype(str)
df["SEX"] = df["SEX"].astype(str)
df["AGE_CAT"] = df["AGE_CAT"].astype(str)
df["customers_level_based"] = df["COUNTRY"] + "_" + df['SOURCE'] + "_" + df["SEX"] + "_" + df["AGE_CAT"]
agg_df = df.drop(["COUNTRY","SOURCE", "SEX", "AGE","AGE_CAT" ],axis=1)
agg_df = df.groupby('customers_level_based')['PRICE'].mean().reset_index()

df["SEGMENT"] = pd.qcut(df["PRICE"], 4, labels =['d', 'c', 'b', 'a'])
df.groupby("SEGMENT").agg({"PRICE":["mean", "sum", "max"]})

new_user= "tur_android_female_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

new_user2= "fra_ios_female_31_40"
agg_df[agg_df["customers_level_based"] == new_user2]

