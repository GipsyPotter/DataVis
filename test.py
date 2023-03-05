import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame(np.random.randint(0, 100, size=(1000, 5)), columns=['col1', 'col2', 'col3', 'col4', 'col5'])
print(df)
# add 1 row
rows = pd.DataFrame(np.random.randint(0, 100, size=(1, 5)), columns=['col1', 'col2', 'col3', 'col4', 'col5'])
df = df.append(rows, ignore_index=True)

# add 1 column
df['col6'] = np.random.randint(0, 100, size=(1001, 1))

print(df)
# save to csv
with open('test.csv', 'w') as f:
    df.to_csv(f, index=False)

# New dataframe with stats
df2 = pd.DataFrame(columns=['colums', 'mean', 'median', 'mode', 'std'])
for col in df.columns:
    df2 = df2.append({'colums': col, 'mean': df[col].mean(), 'median': df[col].median(), 'mode': df[col].mode()[0], 'std': df[col].std()}, ignore_index=True)
print(df2)
