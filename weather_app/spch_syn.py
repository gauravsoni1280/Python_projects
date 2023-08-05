def robosp(str):
    import pyttsx3
    synthesizer = pyttsx3.init()
    synthesizer.say(str) 
    synthesizer.runAndWait() 
    synthesizer.stop()