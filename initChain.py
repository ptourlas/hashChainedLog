#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os

if os.path.getsize('./textfile'):
    print("\n Non-empty file!\n")
else:
    entry = {'date':'1/1/2020','partID':'12938329','tested':'fail'}

    finprint_input = entry['date']+entry['partID']+entry['tested']

    fingerprint = hashlib.md5(finprint_input.encode())

    entry.update({'fingerprint':fingerprint.hexdigest()})

    txt = open('./textfile','a')

    txt.write(str(entry)+'\n')

    txt.close()