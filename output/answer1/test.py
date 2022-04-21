import pandas as pd

grocery = pd.read_csv("veg.csv")
grocery.head()

grocery.groupby('product_description')['price'].mean()

grocery[grocery["price"].isna()].head()

grocery.to_csv('main.csv')