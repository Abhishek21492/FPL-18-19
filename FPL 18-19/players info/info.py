# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:11:32 2018

@author: Abhi
"""

import requests
import json
start_number = 1
for number in range(start_number, 566):
    res = requests.get('https://fantasy.premierleague.com/drf/element-summary/'+str(number))
    data = res.json()
    with open('data%s.json' %number, 'w') as f:
        json.dump(data, f)