import pandas as pd;

try:
  hello()
except:
  print "An exception was thrown!"
  print str(error)
  assert False, f"raised an exception"
