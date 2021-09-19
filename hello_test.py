import hello
try:
    hello.hello_world()
except:
    print ("An exception was thrown!")
    assert False, f"raised an exception"
