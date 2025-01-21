import os
import sys
import urllib.request
from pathlib import Path

upd = "./bin/var/update.txt"
pers = "persistent.txt"



##updt = Path("bin/var/update.txt").read_text()
##pers = open("bin/var/persistent.txt", "w")

### on startup apps
def run():
    track_update()
    print("ran script")
    pass

### updates bin file
def updater(cur_version):
    os.system('gitdir ' + "https://github.com/Sharpfla/WillWare/tree/main/bin")
    pers_file = open(Path(pers), "w")
    pers_file.write("version:" + cur_version)
    print(cur_version)
    pers_file.close()
    print("updated")
    pass
### uses update.txt to track if there's a new 
def track_update():
    inst_version = (Path(pers).read_text()).split(":")[-1]
    cur_version = (Path("bin/var/update.txt").read_text()).split(":")[-1]
    if cur_version != inst_version:
        updater(cur_version)
        print('found update')
    pass