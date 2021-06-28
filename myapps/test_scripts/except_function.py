def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return ("You are dividing by zero")
print (divide(1,0))
