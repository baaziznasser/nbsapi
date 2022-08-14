import NBSapi
import time

#calling class
tts = NBSapi.NBSapi()
#call the speak function
tts.Speak("hello friends, this is the new sapi 5 library", 1)
#pause 2 secs to be able to speak the test
time.sleep(2)