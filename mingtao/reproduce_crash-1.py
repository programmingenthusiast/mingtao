#!/usr/bin/python
# Filename: reproduce_crash-1.py

import sched, time
import subprocess
from subprocess import call

s = sched.scheduler(time.time, time.sleep)

x = 1

def restart_smf():
	print "restarting smf ...", x
	subprocess.call("service smf stop && service smf start", shell=True)
	x += 1

def do_something(sc):
	print "Doing stuff..."
	#do your stuff
	restart_smf()
	sc.enter(600, 1, do_something, (sc,))

s.enter(600, 1, do_something, (s,))
s.run()
