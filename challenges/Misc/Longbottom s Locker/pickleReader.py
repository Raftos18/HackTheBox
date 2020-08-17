import pickle

data = pickle.load(open( "./socute/donotshare", "rb" ) )
msg1 = ""
msg2 = ""
for i in data:
    for char, j in i:
        msg1 += char * j
    msg1 += '\n'

print(msg1) # ======> Gu1d0-v4N-R055Um