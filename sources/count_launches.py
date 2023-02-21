import pandas as pd
import datetime
import time

data = pd.read_csv("launches_data.csv")

data['date'] = pd.to_datetime(data['timestamp']).dt.date

launches_per_day = (data.groupby(["date"])
 .size())

day_cum = [launches_per_day[0]]
i = 1
while i < len(launches_per_day):
    temp = launches_per_day[i] + day_cum[i-1]
    day_cum.append(temp)
    i = i + 1
    