import pandas as pd
import datetime
import time

data = pd.read_csv("launches_data.csv")

data['date']=pd.to_datetime(data['timestamp']).dt.date

repo_list = []

for day in data.date.unique():
    temp = data.loc[data['date'] == day].spec.unique()
    to_add = []
    #print(f"elements in temp: {len(temp)}")
    for entry in temp:
        if not any(entry in i for i in repo_list):
            to_add.append(entry)
            #print(f"elements in to_add: {len(to_add)}")
    repo_list.append(to_add)
    #print(f"Finished day {day}")


cum_repo_list = []
for i, idx in zip(repo_list, range(0, len(repo_list))):
    count = len(i)
    if idx == 0:
        cum_repo_list.append(count)
    else: 
        cum_repo_list.append(cum_repo_list[idx - 1] + count)
