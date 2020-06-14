#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import unittest
import os

class impl:

    def initChain(self):
        if os.path.exists('./textfile'):
            if os.path.getsize('./textfile'):
                print("\n Non-empty file!\n")
                return 1
        else:
            entry = {'date':'1/1/2020','partID':'12938329','tested':'fail'}

            finprint_input = entry['date']+entry['partID']+entry['tested']

            fingerprint = hashlib.md5(finprint_input.encode())

            entry.update({'fingerprint':fingerprint.hexdigest()})

            txt = open('./textfile','a')
            txt.write(str(entry)+'\n')
            txt.close()

            return entry

if __name__ == '__main__':
    x = impl()
    x.initChain()
    print("?????????")

class Test(unittest.TestCase):

    default_value = "{'date': '1/1/200', 'partID': '12938329', 'tested': 'fail', 'fingerprint': 'f957352772e787a9b15a262247d6c641'}\n"

    def test_cmp_defaultValue_with_file(self):
        if os.path.exists('./textfile'):
            with open('./textfile') as f:
                first_line = f.readline()
                self.assertEqual(first_line, self.default_value)
        
    def test_initChain_return_code(self):
        y = impl()
        x = y.initChain()
        self.assertEqual(x, self.default_value)

# if __name__ == '__main__':
#     unittest.main()