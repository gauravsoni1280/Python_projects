def robosp():
    import pyttsx3
    synthesizer = pyttsx3.init()
    while(True):
        str=input("Enter what your want me to speak : ")
        if(str=='quit'):
            break
        synthesizer.say(str) 
        synthesizer.runAndWait() 
        synthesizer.stop()


if __name__=='__main__':
    robosp()