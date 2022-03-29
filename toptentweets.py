import re
import json
import pandas as pd
from collections import defaultdict
import datetime

def feature1(file):
    data = []
    with open(file) as f:
        for line in f:
            line_json = json.loads(line)
            line_aux = dict()
            for key in line_json.keys():
                if "url" not in key.lower():
                    if line_json[key] != None:
                        line_aux[key] = line_json[key]
                if  key == "quotedTweet":
                    if line_json[key] != None:
                        line_aux[key] = line_json[key]['id']
            #print(line_aux)
            data.append(line_aux)

    df = pd.json_normalize(data).sort_values(by=['retweetCount'], ascending=False)
    #print(df.head(10))
    return df.head(10)
