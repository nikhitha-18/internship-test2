import pandas as pd
grocery = pd.read_csv("main.csv")
grocery.head()
grocery["sales_amount"] = grocery["sales_quantity"].where(
    grocery["unit"] != "pcs",
    grocery["product_description"].str.split("-",expand=True)[1].astype("float") * \
    grocery["sales_quantity"]
)
df = pd.DataFrame(grocery)
df.to_csv('solution.csv')