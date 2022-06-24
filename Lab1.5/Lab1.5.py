import glob

L = glob.glob('C:\\Users\\ds.kottsov\\Desktop\\test_config\\config_files\\*.txt')
s = ' ip address'

for name in L:
    with open(name) as f:
        for L in f:
            if s in L:
                print(L.replace(s, ''))










