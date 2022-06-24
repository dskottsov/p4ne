import glob
import re

L = glob.glob('C:\\Users\\ds.kottsov\\Desktop\\test_config\\config_files\\*.txt')
s = ' ip address'


with glob.glob('C:\\Users\\ds.kottsov\\Desktop\\test_config\\config_files\\*.txt') as f:
    for L in f:
        if s in L:
            print(L.replace(s, ''))