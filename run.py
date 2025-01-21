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
    os.system('gitdir ' + "https://github.com/Sharpfla/WillWare/tree/main/bin")
    pers_file = open(Path(pers), "w")
    pers_file.write("version:" + cur_version)
    print(cur_version)
    pers_file.close()
    print("updated")



### uses update.txt to track if there's a new 
def refresh_update():
    inst_version = (Path(pers).read_text()).split(":")[-1]
    cur_version = (Path("bin/var/update.txt").read_text()).split(":")[-1]
    if cur_version != inst_version:
        updater(cur_version)
        print('found update')



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
            refresh_update()
            print("updated reference at: " + my_time)
            time.sleep(interval*60-1)
