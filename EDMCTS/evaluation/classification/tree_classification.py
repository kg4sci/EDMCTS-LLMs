import paramiko
from collections import defaultdict, OrderedDict
from scp import SCPClient
import json
import stat
import re
import random
import pandas as pd

with open('synthesis_data/gold_tree_data.json', 'r') as f:  
    gold_synthesis = json.load(f)
with open('tree_data.json', 'r') as f:
    silver_synthesis = json.load(f)
#print(len(gold_synthesis))
#print(len(silver_synthesis))
random.shuffle(gold_synthesis)
random.shuffle(silver_synthesis)
tree_list = []
for i in range(92):
    tree_list.append(gold_synthesis[i])
for i in range(8):
    tree_list.append(silver_synthesis[i])
random.shuffle(tree_list)
json_str = json.dumps(tree_list, indent=4, ensure_ascii=False)
with open('synthesis_data/test_tree_data.json', 'w') as json_file:
    json_file.write(json_str)
                
                

