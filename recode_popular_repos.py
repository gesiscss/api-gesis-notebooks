import pandas as pd

data = pd.read_csv("launches_data.csv")

totals_per_repo = (data.groupby(["spec"])
 .size()
 .reset_index(name='repo_counts')
                   .sort_values(by='repo_counts', ascending=False))
top = totals_per_repo.head(10)["spec"]
data_others = data
data_others.loc[~data_others['spec'].isin(list(top)), 'spec']  = 'others'
totals_per_repo = (data_others.groupby(["spec"])
 .size()
 .reset_index(name='repo_counts')
                   .sort_values(by='repo_counts', ascending=False))

others_row = totals_per_repo.loc[totals_per_repo["spec"] == "others"]
totals_per_repo = totals_per_repo.loc[totals_per_repo["spec"] != "others"]
totals_per_repo = pd.concat([totals_per_repo, others_row])