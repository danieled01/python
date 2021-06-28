def def_argument(x,y=10):
    z = x+y
    return z

print (def_argument(10))

def def_argument_changed(x,y=10):
    z = x+y
    return z

print (def_argument(10,50))
