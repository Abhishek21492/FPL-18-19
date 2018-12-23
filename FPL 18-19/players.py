# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:59:29 2018

@author: Abhi
"""

import pandas as pd
import json
df = pd.read_json('player_data.json')
df1=df[['id','first_name','second_name']].sort_values(by=['id'])
df1.to_csv('info.csv', index=False, sep='\t')
