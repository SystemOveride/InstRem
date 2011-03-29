import os
import pynotify

def maxs():
	if pynotify.init("Installed"):
		n = pynotify.Notification("Installed", "New application installed")
		n.show()

			
def mins():
	if pynotify.init("Removed"):
		n = pynotify.Notification("Removed", "Application successfull removed")
		n.show()

l = len(os.listdir('/usr/share/'))

while True:
    f = len(os.listdir('/usr/share/'))
    if f>l:
	    maxs()
    elif f<l:
		mins()
    elif l==f:
		pass
    else:
		print "Pynotify problem"

    l = len(os.listdir('/usr/share/'))
