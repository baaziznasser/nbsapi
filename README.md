# NBSapi
## what is NBSapi
the NBSapi is a python library that can help you to convert your text to speech, where you can hear it directly or save it to an audio file.  return
it currently working only on windows with sapi5  return
## requirements
to use the NBSapi you just need to install the pywin32 library by using  return
pip install pywin32  return
## usage
to use the library you need to import it
	from NBSapi import NBSapi  return
	tts = NBSapi()  return
	TTS.Speak("hello")  return

## whats new
*added examples within the tests folder
*updated setup file and requirements

## class functions
this library has a lot of functions that make the sapi 5 tts easy

### Speak  return
Speak(text (string), flag (int))  return
this is the function that will speek text  return
you can use the flags that exists on the lib file  return

### SpeakToFile  return
SpeakToFile(text (string), file (string), flags (int))  return
create an audio file with the giving text and path  return

### Pause  return
Pause()  return
pause the speech  return

### Resume
Resume()  return
resume the speech  return

### Stop
Stop()  return
Stop the Speech  return

### GetVoice
GetVoice()  return
get the current voice information as a dict  return

### SetVoice
SetVoice(voice (index or object), byindex (int))  return
Set the current voice, even by object or by index starting from 0  return

### GetVolume
GetVolume()  return
Get the Current volume  return

### SetVolume
SetVolume(vol (int))  return
set the Current volume  return

### GetRate
GetRate()  return
Get the Current Rate  return

### SetRate
SetRate(Rate (int))  return
Set the Rate of the voice Between -10 and 10  return

### GetVoices
GetVoices()  return
Get a list of dicts, each item has a voice information  return
so, you can use this list indexes to set the voice, it has the same order.

### GetAttribute
GetAttribute(attr (string))  return
get an attribute of the selected voice such as Name, Age, Language, and Gender.  return

### GetStatus(
GetStatus(Property (string))  return
Get a state of any thing you want, you can use the declared variable that start with STS_  return

### GetObject
get the current SPVoice object  return


## notes:
this library is new, so i will add a features to it as i can.  return
if you have any idea about this library please help with it.  return