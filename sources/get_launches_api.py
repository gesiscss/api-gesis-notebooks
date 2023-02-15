import datetime
import math
import pandas as pd
import requests
import time

from_dt = datetime.datetime(2019,6,1).isoformat()
to_dt = datetime.datetime(2020,9,30).isoformat()
url = f'https://notebooks.gesis.org/gallery/api/v1.0/launches/{from_dt}/{to_dt}'

launches = []
# because of pagination the api gives 100 results per page so for analysis you have to take data in all pages
next_page = 1
start = datetime.datetime.now()
while next_page is not None:
    params = {'origin': 'notebooks.gesis.org',
             'page': next_page}
    r = requests.get(url, params=params)
    response = r.json()
    # check the limit of queries per second/minute,
    message = response.get("message", "")
    if message not in ["2 per 1 second", "100 per 1 minute"]:
        launches.extend(response['launches'])
        if next_page % 50 == 0:
            timesnap = datetime.datetime.now() - start
            print(f"finished page {next_page}. Loop going for {math.floor(timesnap.seconds / 3600)}:{math.floor(timesnap.seconds % 3600 / 60)}:{timesnap.seconds % 3600 % 60}. Average time per page: {round(timesnap.seconds / next_page,3)} seconds")
        next_page = response['next_page']

    else:
        time.sleep(1)
        
data = pd.DataFrame.from_dict(launches)
data.to_csv("launches_data.csv")