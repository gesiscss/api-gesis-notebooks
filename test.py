#%matplotlib inline
import matplotlib.pyplot as plt
import datetime
import math
import pandas as pd
import requests
import time

data = pd.read_csv("launches_data.csv")


data['date']=pd.to_datetime(data['timestamp']).dt.date
totals_per_day = data.groupby(["date"], as_index=False).size()



repo_list = []

for day, idx in zip(data['date'], totals_per_day.index):
    temp = data.loc[data['date'] == day].spec.unique()
    # repo_list.append(repo_list)
    to_add = []
    for entry in temp:
        if not any(entry in i for i in repo_list):
            to_add.append(entry)
    repo_list.append(to_add)


cum_repo_list = []
for i, idx in zip(repo_list, range(0, len(repo_list))):
    count = len(i)
    if idx == 0:
        cum_repo_list.append(count)
    else: 
        cum_repo_list.append(cum_repo_list[idx - 1] + count)


plt.plot(data.date.unique(), cum_repo_list)

    

    