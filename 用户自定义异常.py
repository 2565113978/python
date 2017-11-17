def functionName(level):
    if level < 1:
        raise Exception("Invalild level!",level)
    print "OK"




try :
    functionName(0)
except "Invalild level!":
    print "user defined exception"
else:
    print "else......"
finally:
    print"finally alway run......"
