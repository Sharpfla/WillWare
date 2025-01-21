import os
import sys
import urllib.request
from pathlib import Path
from datetime import datetime, time, timedelta, date
import time


upd = "./bin/var/update.txt"
pers = "persistent.txt"
interval = 1



### on startup apps
def run():
    #refresh_update()
    print("ran script")



### updates bin file
def updater(cur_version):
    pers_file = open(Path(pers), "w")
    upd_file = open(Path(upd), "r")
    upd_line = upd_file.readlines()
    upd_repos = upd_line[2].split(":")
    fail = False
    i = 0
    for item in upd_repos:
        try:
            if i >= 1:
                print(i)
                print("updating: https://github.com/Sharpfla/WillWare/tree/main/bin/apps/" + upd_repos[i])
                os.system('gitdir ' + "https://github.com/Sharpfla/WillWare/tree/main/bin/apps/" + upd_repos[i])
            i += 1
        except:
            print("failed to update: https://github.com/Sharpfla/WillWare/tree/main/bin/apps/" + upd_repos[i])
            fail = True
            i += 1
            return
    if fail != True:
        pers_file.write("version:" + cur_version)
        print("updated to version " + cur_version)
        upd_file.close()
        pers_file.close()
    else:
        print("update partially failed")
        upd_file.close()
        pers_file.close()

    



### uses update.txt to track if there's a new 
def refresh_update():
    inst_version = (Path("persistent.txt").read_text()).split(":")[-1]
    cur_version = (Path(upd).read_text()).split(":")[1]
    if cur_version != inst_version:
        print('found update')
        updater(cur_version)




#time delayed updater
def track_update():
    print("started auto updater")
    i = 0
    minut_to_run =[] 
    minutes = 59
    while minutes >= 0:
       minut_to_run.append(minutes)
       minutes -= interval

    while i <= 1:
       t = datetime.now()
       my_time = t.strftime("%H:%M:%S.%f")

       if t.second >= 50 and t.minute in minut_to_run:
            print("updated reference at: " + my_time)       
            refresh_update()
            time.sleep(interval*60-1)
