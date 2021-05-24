#!/usr/bin/env python3

'''
Procstalker
Copyright (C) 2021 Paulo Matheus Vinhas (1000bbits)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import psutil
from datetime import datetime
import time
import os
import subprocess
from threading import Thread
import getopt

terminated_proc_pid = 0
path = []
pids = []

def get_processes_info():
    # the list the contain all process dictionaries
    processes = []
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            # get the process id
            pid = process.pid
            if pid == 0:
                # System Idle Process for Windows NT, useless to see anyways
                continue
            # get the name of the file executed
            name = process.name()
            processes.append({'pid': pid, 'name': name})
    return processes

def on_terminate(proc):
    now = datetime.now()
    print("process {} terminated on {} with exit code {}".format(proc, now.strftime("%d/%m/%Y %H:%M:%S"), proc.returncode))
    #proc.pid
    subprocess.run(path)
    #popen()
    #pids.pop()
    #thread = Thread(target = stalker_thread, args = (pids[terminated_proc_pid], ))
    #thread.start()

def stalker_thread(arg):
    print("Thread init'ed. Stalking...")
    print(arg)
    procs = psutil.Process(arg).children()
    gone, alive = psutil.wait_procs(procs, callback=on_terminate)

def popen():
    ret = subprocess.Popen(path)
    time.sleep(1)
    processes = get_processes_info()
    for proc in processes:
        vals = list(proc.values())
        keys = list(proc.keys())
        if 'sudo' == vals[1]:
            _pid = vals[0]
            if not _pid in pids:
                pids.append(_pid)

optlist, args = getopt.gnu_getopt( sys.argv[ 1: ], 'f:' )
for( opt, arg ) in optlist:
    if opt == '-f':
        f = arg
        name, extension = os.path.splitext(f)
        if extension == '.py':
            path = ["nohup", "sudo", "python3" ,"-u", os.path.abspath(f), "&"]
        else:
            path = ["nohup", "sudo", os.path.abspath(f), "&"]
        popen()
            
print(pids)
while(True):
    for pid in pids:
        procs = psutil.Process(pid).children()
        gone, alive = psutil.wait_procs(procs, callback=on_terminate)
        #thread = Thread(target = stalker_thread, args = (pid, ))
        #thread.start()
                                        
# if your keyboard is strange as mine and you have no idea where's the pipe char that's my kindness for you (:
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||