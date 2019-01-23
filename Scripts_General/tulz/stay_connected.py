import os
import time

hostname = "google.com"
counter = 0
success = 0
failed = 0
seconds = 60

print("This script sends a packet once every %s seconds.\n" % (seconds))

while True: #loop indefinitely and use the 'clear' command after the first pass
        response = os.system("ping -c 1 " + hostname)
        counter += 1
        print("\nPing sent. We have sent %s packets from this program since we have started it.\n" % (counter))
        #and then check the response... 
        if response == 0:
            print(hostname, 'is up! It seems that you are connected.\n')
            success += 1
        else:
            print(hostname, 'is down! It seems that you are not connected.\n')
            failed += 3
        print("%s / %s pings successful            %s / %s pings failed" % (success, counter, failed, counter))
        time.sleep(seconds) #delay for one minute (60 seconds)
        # clear the screen
        print("\x1b[1;1H\x1b[J")
