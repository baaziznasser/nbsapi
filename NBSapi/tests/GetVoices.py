import NBSapi
import time
#calling class
tts = NBSapi.NBSapi()
#get the voices list
voices = tts.GetVoices()
for voice in voices:
	print(voice["Name"])
time.sleep(10)