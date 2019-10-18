#pruner_pd.py

import pandas as pd
import json


data = {}
with open("baby_names.txt","r") as infile:
    data = json.load(infile)

df=pd.DataFrame(list(data["top"].items()), columns=['Names', 'Count'])

df= df[~df.Names.str.contains("v")]
df = (df[df["Names"] != "Aaron"])
df= (df[df["Names"] != "Luke"])
df= (df[df["Names"] != "Winston"])
df= (df[df["Names"] != "Gary"])
df= (df[df["Names"] != "Avery"])
df=(df[df["Count"] != "28"])
df2 = {'Names': "Ron", 'Count': '5'}
df = df.append(df2, ignore_index=True)
print(df)