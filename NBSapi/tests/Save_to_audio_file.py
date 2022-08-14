import NBSapi
import time

#calling class
tts = NBSapi.NBSapi()
#call the speak function
tts.SpeakToFile("hello friends, this is  the new sapi 5 library", "audio.Wav", 0)