import re
import json
import pandas as pd
from collections import defaultdict
import datetime

def feature3(file):
    more_days = defaultdict(lambda: 0)
    with open(file) as f:
        for line in f:
            line_json = json.loads(line)
            date = datetime.datetime.strptime(line_json["date"].split("T")[0], "%Y-%m-%d").date()
            more_days[date] +=1
            
    
    df_days = pd.json_normalize(more_days).transpose().sort_values(by=[0], ascending=False)
    return df_days.head(10)
