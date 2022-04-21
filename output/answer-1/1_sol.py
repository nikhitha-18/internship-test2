import pandas as pd
grocery = pd.read_csv("main.csv")
grocery["price_new"] = grocery["price"].fillna(
    grocery.groupby('product_description')['price'].transform("mean")
)
print (grocery[grocery["price"].isna()].head())
df = pd.DataFrame(grocery)
df.to_csv('solution.csv')