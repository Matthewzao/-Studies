import sys  
import time
test = 'this is just a test'
for char in test:
          time.sleep(0.08)
          sys.stdout.write(char)
          sys.stdout.flush()