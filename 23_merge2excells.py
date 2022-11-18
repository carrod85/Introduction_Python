import os
import pandas as pd
from openpyxl import workbook

import glob

files = glob.glob("../venv/concatenation/*.xlsx")


all_data = pd.DataFrame()
for f in files:
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

print(all_data.head(10))
all_data.to_excel("../venv/concatenation/output.xlsx")# save output file.

