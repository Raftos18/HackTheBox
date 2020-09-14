import base64
from os import walk

with open('./decoded-data.txt', 'w') as dd:
    for (dirpath, dirnames, filenames) in walk('.'):
        for filename in filenames:
            with open(filename, 'r') as f:
                try:
                    decoded = base64.b64decode(f.read())                    
                    dd.write(str(decoded)+'\n')
                except Exception as ex:
                    print(ex)
                