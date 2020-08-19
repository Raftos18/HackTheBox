import zipfile
import os

filename = "37366.zip"
extract_dir = "./"
oldfilename = ""

while True:
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        try:
            new_file = next(iter(zip_ref.NameToInfo))
            print('Fileinfo', zip_ref.namelist())
            if(all(['.zip' not in i for i in zip_ref.namelist()])):
                print('not all files contain zip')
                break
            password = new_file.split('.')[0]
            res = zip_ref.extractall(extract_dir, pwd=bytes(password, 'utf-8'))
            oldfilename = filename            
            filename = new_file
        except Exception as e:
            print(e)
            break
    
    if (oldfilename != '37366'):
        os.unlink(oldfilename)