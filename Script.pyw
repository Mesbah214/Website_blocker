# Website_blockr.py
#   by: Mesbah Uddin
#       A simple app that will block certain websites during a given time period to avoid distractions.

import time
from datetime import datetime as dt

hosts_temp = r"E:\Python WorkSpace\Website_blocker\hosts"
local_hosts = r"C:\Windows\System32\drivers\etc\hosts"
local_IP = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com",
            "www.youtube.com", "youtube.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Inside of working hours....")
        with open(local_hosts, "r+") as f:
            content = f.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    f.write(f'{local_IP} {website}\n')

    else:
        print("Fun hours!!!!")
        with open(local_hosts, "r+") as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    f.write(line)
            f.truncate()

    time.sleep(5)
