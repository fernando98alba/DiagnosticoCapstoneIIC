import re
import json
import pandas as pd
from collections import defaultdict
import datetime
file = "dataset.json"
data = []
def feature1(file):
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
    print(df.head(10))
