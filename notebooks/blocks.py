import re
import pandas as pd
from collections import OrderedDict

block_info = OrderedDict()
index = 1

with open("HDFS.log") as infile:
    for line in infile:
        block_ids_in_row = re.findall(r'(blk_-?\d+)', line)
        block_info[index] = block_ids_in_row[0]
        index += 1

df = pd.DataFrame.from_dict(block_info, orient = 'index', columns=['block_id'])
df.to_csv("blocks.csv")
