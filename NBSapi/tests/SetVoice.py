
#note please change voices name and description to the voices you have to be able to test the feature

import NBSapi
import time
#calling class
tts = NBSapi.NBSapi()
#set the first arabic Voice as the Default voice
tts.SetVoice("Language=401", "by_attribute")
#check the voice
print(tts.GetVoice())
#Set Voice By Name
tts.SetVoice("Name=heather22k_hq", "by_attribute")
#check the voice
print(tts.GetVoice())

#Set the second voice as default voice
tts.SetVoice(1, "by_index")
#check the voice
print(tts.GetVoice())

#set the Voice By description
tts.SetVoice("Leila (Arabic) SAPI5 -", "by_description")

#check the voice
print(tts.GetVoice())
