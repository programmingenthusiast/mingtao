#!/usr/bin/python
# Filename: reproduce_crash-1.py

import sched, time
import subprocess
from subprocess import call

s = sched.scheduler(time.time, time.sleep)

x = 1

def restart_smf():
	global x
	print "restarting smf ...%d... times" % x
	subprocess.call("service smf stop && service smf start", shell=True)
	x += 1

def do_something(sc):
	print "Doing stuff..."
	#do your stuff
	restart_smf()
	sc.enter(600, 1, do_something, (sc,))

# restart smf every 10 minutes
s.enter(600, 1, do_something, (s,))
s.run()
