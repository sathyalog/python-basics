#Modules

import time
print(time.asctime())
print(time.timezone)


from time import asctime,sleep
print(asctime())
sleep(3) # like a setTimeout() in JS
print(asctime())

#Module search using path. This will search for python installation
import sys
for path in sys.path:
    print(path)
