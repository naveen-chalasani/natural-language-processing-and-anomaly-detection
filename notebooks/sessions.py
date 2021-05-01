import os 
import re
import numpy as np 
import pandas as pd
from collections import OrderedDict

# extract session info from log file and save the output in sessions.csv

def hdfs_sessions(log_file):
    
    session = 0
    sequence_in_session = 0
    block_id_list = list()
    session_info = OrderedDict()
    
    log_data = pd.read_csv(log_file, engine='c', na_filter=False, memory_map=True, header=None, error_bad_lines=False)
    
    for index, row in log_data.iterrows():
        print(index)
        
        block_ids_in_row = re.findall(r'(blk_-?\d+)', row[0])
        #block_ids = '; '.join(sorted(set(block_ids_in_row)))
        block_id = block_ids_in_row[0]
        
        if block_id not in block_id_list:
            block_id_list.append(block_id)
            session += 1
            sequence_in_session = 1
        else:
            sequence_in_session += 1
        
        temp_list = [None] * 3
        temp_list[0] = block_id
        temp_list[1] = session
        temp_list[2] = sequence_in_session
        session_info[index + 1] = temp_list
            
    df = pd.DataFrame.from_dict(session_info, orient = 'index', columns=['block_id', 'session', 'sequence_in_session'])
    df.to_csv("sessions.csv")

# , error_bad_lines=False
# hdfs_sessions('HDFS_2k.log')
# hdfs_sessions('HDFS.log')
hdfs_sessions('content.txt')
