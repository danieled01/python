#have to write a function that will return the value of a string backwards:

def solution(string):
    return string[::-1]

#string[::1] works by specifying which elements you want as [begin:end:step].  So by specifying -1 for the step you are telling Python to use -1 as a step which in turn starts
#from the end.  This works both with strings and lists
