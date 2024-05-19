import pandas as pd
df = pd.read_csv('nj58.csv')
df = df.drop_duplicates('标题', keep='first')
df = df[df['大小'].notna()]
df['单价'] = df['单价'].str.replace('元/㎡', '')
df['大小'] = df['大小'].str.replace('㎡', '')
df['建造时间'] = df['建造时间'].str.replace('年建造', '')
df.to_csv('clean.csv', index=0)
print(df.shape)

