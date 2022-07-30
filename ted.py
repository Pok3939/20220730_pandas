import pandas as pd
import numpy as np
ted = pd.read_csv("ted.csv")
print(ted)

print(ted.head(10))


print(ted.dtypes)
print(ted.sort_values('views').tail())
ted['comments_per_view'] = ted.comments/ted.views
print(ted.sort_values('comments_per_view').tail())
print(ted.isna())
print(ted.isna().sum())