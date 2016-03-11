#Help received from stackoverflow.com user "10flow" http://stackoverflow.com/questions/2953462/pinging-servers-in-python
import os
import time

os.system("clear") #Clear terminal on execution

print "\nThis script was made originally to make my cellular wifi hotspot remain open by keeping internet activity active."
print "This script has been tested on OS X El Capitan, but not on Windows. This script should work on most UNIX based operating systems."

hostname = "google.com" #since google seems to be a fairly reliable site when we look at uptime
counter = 0
success = 0
failed = 0
seconds = 60

print "This script sends a packet once every %s seconds.\n" % (seconds)

while True: #loop indefinitely and execute the clear command after the first pass
        if counter > 0:
            os.system("clear")
        response = os.system("ping -c 1 " + hostname)
        counter += 1
        if counter > 1:
            print "\nPing sent. We have sent %s packets from this program since we have started it.\n" % (counter)
        else:
            print "\nPing sent. We have sent %s packet from this program since we have started it. \n" % (counter)
        #and then check the response... 
        if response == 0:
            print hostname, 'is up! It seems that you are connected.\n'
            success += 1
        else:
            print hostname, 'is down! It seems that you are not connected.\n'
            failed += 1
        print "%s / %s pings successful            %s / %s pings failed" % (success, counter, failed, counter)
        time.sleep(seconds) #delay for one minute (60 seconds)
