import re
import json
import pandas as pd
from collections import defaultdict
import datetime

def feature4(file):
    more_hash = defaultdict(lambda: 0)
    with open(file) as f:
        for line in f:
            line_json = json.loads(line)
            x = re.findall("#.*? ", line_json["content"])
            #print(x)
            #print(line_json["content"])
            if x:
                for element in x:
                    more_hash[element] += 1
            
    
    df_hash = pd.json_normalize(more_hash).transpose().sort_values(by=[0], ascending=False)
    return df_hash.head(10)
