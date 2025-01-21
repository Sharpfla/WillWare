import os
import run
import urllib.request
from threading import Thread


t1 = Thread(target=run.run)
t1.daemon = True
t1.start()

run.track_update()