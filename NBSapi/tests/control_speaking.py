import NBSapi
import time
text = """
	hello friends, this is the new sapi 5 library.
	it may help you to make your python programs speaking texts and create audio books, by using the text to speech feature.
	this library can works only on windows, because it work with the sapi5 functions.
"""

#calling class
tts = NBSapi.NBSapi()
#call the speak function
tts.Speak(text, 1)
#wait 500 MS
time.sleep(0.5)
#pause the speech
tts.Pause()
#wait 1s
time.sleep(1)
#resume the speech
tts.Resume()
#wait 500 MS
time.sleep(0.5)
#stop the speech
tts.Stop()
#change Voice
tts.SetVoice(2)
#change Rate
tts.SetRate(9)
#change volume
tts.SetVolume(50)
#respeek text
tts.Speak(text, 1)
#wait some time
time.sleep(1)
#check if is Speaking
if tts.GetStatus() == 2:
	print(f"yes it is speaking now using the sapi5 voice {tts.GetAttribute('Name')}")
time.sleep(10)