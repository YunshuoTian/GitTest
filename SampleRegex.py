*new file to the repository*
import numpy as np
import pandas as pd
import re
import nltk

df = pd.read_excel(io='SN Not Found.xlsx', sheet_name='Search No Result',header=0)
df.dtypes
df["SearchTerms"]=df["SearchTerms"].astype(str)

df_1 = pd.DataFrame(df, columns=["SearchTerms"])
df_1["Regex"]=df_1.SearchTerms.str.match("([A-Za-z]+[\d]+[\w]*|[\d]+[A-Za-z]+[\w]*){2,9}")
df_1["Char_Count"]=df_1.SearchTerms.str.len()
df_1.to_csv('out.csv',index=False)