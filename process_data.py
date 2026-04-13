import pandas as pd

df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df0, df1, df2], ignore_index=True)

df = df[df["product"] == "pink morsel"]

df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)
df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv("formatted_data.csv", index=False)

print(df.head())
print("DONE")