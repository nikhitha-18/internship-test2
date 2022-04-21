import pandas as pd
csvData = pd.read_csv("main.csv")
csvData.sort_values(["Red Cards"],
axis=0,
ascending=[False],
inplace=True)
csvData.sort_values(["Yellow Cards"],
axis=0,
ascending=[False],
inplace=True)
df=pd.DataFrame(csvData)
df.to_csv('solution_3.csv')