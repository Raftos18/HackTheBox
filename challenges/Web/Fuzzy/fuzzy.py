import wfuzz


available_directories = []

def props(cls):   
  return [i for i in cls.__dict__.keys() if i[:1] != '_']

# First look for available directories
for r in wfuzz.fuzz(url="http://docker.hackthebox.eu:32502/FUZZ", hc=[404], payloads=[("file",dict(fn="/usr/share/wordlists/wfuzz/general/common.txt"))]):
    available_directories.append(r.url)
    print("Found: ", r.url)    


#Look for files
for url in available_directories:
    for r in wfuzz.fuzz(url="{}" "http://docker.hackthebox.eu:32502/api/action.php?FUZZ", hs="Error: Parameter not set", payloads=[("file",dict(fn="/usr/share/wordlists/wfuzz/general/common.txt"))]):
        print(r)