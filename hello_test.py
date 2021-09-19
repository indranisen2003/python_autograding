import pandas as pd;

try:
  hello()
except Exception, error:
  print "An exception was thrown!"
  print str(error)
  assert False, f"raised an exception {error}"
