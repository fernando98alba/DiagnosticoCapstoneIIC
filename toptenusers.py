import re
import json
import pandas as pd
from collections import defaultdict
import datetime

def feature2(file):
    more_tweets = defaultdict(lambda: 0)
    with open(file) as f:
        for line in f:
            line_json = json.loads(line)
            
            more_tweets[line_json["user"]["username"]] +=1
    
    df_tweet = pd.json_normalize(more_tweets).transpose().sort_values(by=[0], ascending=False)
    return df_tweet.head(10)
