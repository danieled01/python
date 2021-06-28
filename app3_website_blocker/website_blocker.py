import time
import os
from datetime import datetime as dt
from pathlib import Path
from time import strftime
import shutil

hosts_file='/etc/hosts'
redirect_ip='127.0.0.1'
website_list=['www.bbc.com','www.yahoo.com']
timestamp=strftime("%Y-%m-%d")

while True:
    time_now = dt.now()
    if dt(time_now.year, time_now.month, time_now.day, 8, 0, 0) < dt.now() < dt(time_now.year, time_now.month, time_now.day, 17, 0, 0):
        with open(hosts_file, "r") as myfile:
            contents=myfile.read()
            if os.path.isfile('tmp/etc_hosts.tmp'):
                with open('/tmp/etc_hosts.tmp', 'r+') as outf:
                    outf.write(contents)
                    for i in website_list:
                        if i in contents:
                            pass
                        else:
                            outf.write(redirect_ip+' '+i+'\n')
                            shutil.copy2('/etc/hosts', '/tmp/hosts'+'_'+timestamp)
                            shutil.copy2('/tmp/etc_hosts.tmp', '/etc/hosts')
            else:
                Path('/tmp/etc_hosts.tmp').touch()
                with open('/tmp/etc_hosts.tmp', 'r+') as outf:
                    outf.write(contents)
                    for i in website_list:
                        if i in contents:
                            pass
                        else:
                            outf.write(redirect_ip+' '+i+'\n')
                            shutil.copy2('/etc/hosts', '/tmp/hosts'+'_'+timestamp)
                            shutil.copy2('/tmp/etc_hosts.tmp', '/etc/hosts')
    else:
        with open(hosts_file, "r") as myfile:
            contents=myfile.read()
            if os.path.isfile('tmp/etc_hosts.tmp'):
                with open('/tmp/etc_hosts.tmp', 'r+') as outf:
                    outf.write(contents)
                    d = outf.readlines()
                    outf.seek(0)
                    for i in d:
                        if not any(website in i for website in website_list):
                            outf.write(i)
                        outf.truncate()
                    shutil.copy2('/etc/hosts', '/tmp/hosts'+'_'+timestamp)
                    shutil.copy2('/tmp/etc_hosts.tmp', '/etc/hosts')
            else:
                Path('/tmp/etc_hosts.tmp').touch()
                with open("/tmp/etc_hosts.tmp", "r+") as outf:
                    outf.write(contents)
                    d = outf.readlines()
                    outf.seek(0)
                    for i in d:
                        if not any(website in i for website in website_list):
                            outf.write(i)
                        outf.truncate()
                    shutil.copy2('/etc/hosts', '/tmp/hosts'+'_'+timestamp)
                    shutil.copy2('/tmp/etc_hosts.tmp', '/etc/hosts')
    time.sleep(5)
