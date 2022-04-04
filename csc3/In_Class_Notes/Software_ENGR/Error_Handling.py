try:
    print ("Hello!")
    print ("How")
    print ("are")
    print ("you")
    print ("doing?")
except NameError:
    print ("A name error occured.")
except TypeError:
    print ("A type error occured.")
except:
    print ("An error occured.")