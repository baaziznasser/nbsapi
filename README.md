# NBSapi
## what is NBSapi
the NBSapi is a python library that can help you to convert your text to speech, where you can hear it directly or save it to an audio file.\
it currently working only on windows with sapi5
## requirements
to use the NBSapi you just need to install the pywin32 library by using\
pip install pywin32
## usage
to use the library you need to import it
	from NBSapi import NBSapi\
	tts = NBSapi()\
	TTS.Speak("hello")

## whats new
* added examples within the tests folder
* updated setup file and requirements

## class functions
this library has a lot of functions that make the sapi 5 tts easy

### Speak
Speak(text (string), flag (int))\
this is the function that will speek text\
you can use the flags that exists on the lib file\

### SpeakToFile
SpeakToFile(text (string), file (string), flags (int))\
create an audio file with the giving text and path

### Pause
Pause()\
pause the speech

### Resume
Resume()\
resume the speech

### Stop
Stop()\
Stop the Speech

### GetVoice
GetVoice()\
get the current voice information as a dict

### SetVoice
SetVoice(voice (index or object), byindex (int))\
Set the current voice, even by object or by index starting from 0

### GetVolume
GetVolume()\
Get the Current volume

### SetVolume
SetVolume(vol (int))\
set the Current volume

### GetRate
GetRate()\
Get the Current Rate

### SetRate
SetRate(Rate (int))\
Set the Rate of the voice Between -10 and 10

### GetVoices
GetVoices()\
Get a list of dicts, each item has a voice information\
so, you can use this list indexes to set the voice, it has the same order.

### GetAttribute
GetAttribute(attr (string))\
get an attribute of the selected voice such as Name, Age, Language, and Gender.

### GetStatus(
GetStatus(Property (string))\
Get a state of any thing you want, you can use the declared variable that start with STS_

### GetObject
get the current SPVoice object


## notes:
this library is new, so i will add a features to it as i can.\
if you have any idea about this library please help with it.