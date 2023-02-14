#%matplotlib inline
import matplotlib.pyplot as plt
import datetime
import math
import pandas as pd
import requests
import time

data = pd.read_csv("launches_data.csv")

totals_per_repo = (data.groupby(["spec"])
 .size()
 .reset_index(name='repo_counts')
                   .sort_values(by='repo_counts', ascending=False))
top10 = totals_per_repo.head(10)["spec"]
data_others = data
data_others.loc[~data_others['spec'].isin(list(top10)), 'spec']  = 'others'
totals_per_repo = (data_others.groupby(["spec"])
 .size()
 .reset_index(name='repo_counts')
                   .sort_values(by='repo_counts', ascending=False))

others_row = totals_per_repo.loc[totals_per_repo["spec"] == "others"]
totals_per_repo = totals_per_repo.loc[totals_per_repo["spec"] != "others"]
totals_per_repo = pd.concat([totals_per_repo, others_row])
totals_per_repo


data['date']=pd.to_datetime(data['timestamp']).dt.date
totals_per_day = data.groupby(["date"], as_index=False).size()


repo_list = []

for day, idx in zip(data['date'], totals_per_day.index):
    temp = data.loc[data['date'] == day].spec.unique()
    repo_list.append(repo_list)
    to_add = []
    for entry in temp:
        if entry not in repo_list[idx]:
            to_add.append(entry)
    repo_list.append(entry)
    if idx % 20 == 0:
        print(len(repo_list[idx]))