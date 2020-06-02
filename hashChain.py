#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 00:45:15 2020

@author: bionic
"""

import hashlib

arr = []

entry1 = {
        'date'  :'1/1/2020',
        'partID':'12938329',
        'tested':'pass'
        }

arr.append(entry1)

finprint_input = entry1['date']+entry1['partID']+entry1['tested']

fingerprint = hashlib.md5(finprint_input.encode())
entry1.update({'fingerprint':fingerprint.hexdigest()})

entry2 = {
        'date'  :'2/1/2020',
        'partID':'92461239',
        'tested':'fail'
        }

arr.append(entry2)

finprint_input = entry1['date']+entry1['partID']+entry1['tested']\
+arr[0]['fingerprint']

fingerprint = hashlib.md5(finprint_input.encode())
entry2.update({'fingerprint':fingerprint.hexdigest()})

print(arr)