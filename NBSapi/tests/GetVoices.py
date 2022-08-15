import NBSapi
import time
#calling class
tts = NBSapi.NBSapi()
#get the voices list
voices = tts.GetVoices()
for voice in voices:
	print(voice["Name"])
time.sleep(5)
#get all english voices only
voices = tts.GetVoices("Language=409")
for voice in voices:
	print(voice["Name"])
time.sleep(5)
