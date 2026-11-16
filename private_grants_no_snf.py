import pandas as pd

path_private_grants = "FY27_10_Private_Grants_Foundation.xlsx"

df = pd.read_excel(path_private_grants, sheet_name="data")


print(df.info())