import pandas as pd

grocery = pd.read_csv("veg.csv")
grocery.head()


grocery["sales_amount"] = grocery["sales_quantity"].where(
                                             grocery["unit"] != "pcs",
                                             grocery["product_description"].str.split("-",expand=True)[1].astype("float") * \
                                             grocery["sales_quantity"]
                                          )

g = grocery.tail()

g

g.to_csv('main.csv')