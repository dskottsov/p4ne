import glob
import re

L = glob.glob('C:\\Users\\ds.kottsov\\Desktop\\test_config\\config_files\\*.txt')
s = ' ip address'

for name in L:
    with open(name) as f:
        for L in f:
            r = re.match("^ ip address ([0-9.]+) ([0-9.]+)$", L)
            if r:
                print(r.group(1), r.group(2))









