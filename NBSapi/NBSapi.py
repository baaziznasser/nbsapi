"""
this library is created by nacer baaziz from algeria
notes:
1. if you find any problems with this library please contact me at
nacerbaaziz@ng-space.com
or 
nacersttile@gmail.com
2. you can use this library freely, but without removing this header
"""

### starting code

#import needed libraries
import comtypes.client as c_c

## consts
#speak flags
SVSFDefault = 0
SVSFlagsAsync = 1
SVSFPurgeBeforeSpeak = 2
SVSFIsFilename = 4
SVSFIsXML = 8
SVSFIsNotXML = 16
SVSFPersistXML = 32

#Normalizer Flags
SVSFNLPSpeakPunc = 64

#TTS Format
SVSFParseSapi = None
SVSFParseSsml = None
SVSFParseAutoDetect = None

#Masks
SVSFNLPMask = 64
SVSFParseMask = None
SVSFVoiceMask = 127
SVSFUnusedFlags = -128

#status
STS_CurrentStreamNumber = "CurrentStreamNumber"
STS_InputSentenceLength = "InputSentenceLength"
STS_InputSentencePosition = "InputSentencePosition"
STS_InputWordLength = "InputWordLength"
STS_InputWordPosition = "InputWordPosition"
STS_LastBookmark = "LastBookmark"
STS_LastBookmarkId = "LastBookmarkId"
STS_LastHResult = "LastHResult"
STS_LastStreamNumberQueued = "LastStreamNumberQueued"
STS_PhonemeId = "PhonemeId"
STS_RunningState = "RunningState"
STS_VisemeId = "VisemeId"

#speech runing state
SRSEWaiting = 0
SRSEDone = 1
SRSEIsSpeaking = 2



#function to check if is sapi installed and it contains voices
def is_sapi():
	try:
		tts = c_c.CreateObject("Sapi.SpVoice")
		tts.GetVoices()
		return True
	except:
		return False

#creating main class
class NBSapi():
	## call the __init__ function and load the sapi class
	def __init__(self):
		#check if sapi is avalable
		if not is_sapi():
			return None

		#load tts
		try:
			self.tts = c_c.CreateObject("Sapi.SpVoice")
			self.tts.AlertBoundary = 32
		except:
			self.tts = None
			return None

	#function to get the main sapi class as an object
	def GetObject(self):
		return self.tts

	#get all the sapi5 registered voices as a list of dicts
	def GetVoices(self, attrs = ""):
		if self.tts == None:
			return []
		self.res = list()
		self.thisres = dict()
		#loop through voices
		for voice in self.tts.GetVoices(attrs):
			self.thisres = dict()

			#get voice info
			try:
				self.thisres["Name"] = voice.GetAttribute("Name")
				self.thisres["Age"] = voice.GetAttribute("Age")
				self.thisres["Gender"] = voice.GetAttribute("Gender")
				self.thisres["Language"] = voice.GetAttribute("Language")
				self.thisres["Description"] = voice.GetDescription()
				self.thisres["Id"] = voice.Id
				self.thisres["Vendor"] = voice.GetAttribute("Vendor")
				self.thisres["Version"] = voice.GetAttribute("Version")
			except:
				pass
			self.res.append(self.thisres)
		return self.res

	#get the current voice information as dict
	def GetVoice(self):
		if self.tts == None:
			return {}
		self.thisvoice = self.tts.Voice
		self.thisres = dict()
		try:
			self.thisres["Name"] = self.thisvoice.GetAttribute("Name")
			self.thisres["Age"] = self.thisvoice.GetAttribute("Age")
			self.thisres["Gender"] = self.thisvoice.GetAttribute("Gender")
			self.thisres["Language"] = self.thisvoice.GetAttribute("Language")
			self.thisres["Description"] = self.thisvoice.GetDescription()
			self.thisres["Id"] = self.thisvoice.Id
			self.thisres["Vendor"] = self.thisvoice.GetAttribute("Vendor")
			self.thisres["Version"] = self.thisvoice.GetAttribute("Version")
		except:
			pass
		return self.thisres

	#set the current voice even by (object, index, attribute, description, or id)
	def SetVoice(self, voice, key = "by_index"):
		if self.tts == None:
			return None

		#check the method that will use
		if key == "by_index":
			voice = int(voice)
			if voice < 0:
				voice = 0
			self.v_count =  self.tts.GetVoices().Count-1
			if voice > self.v_count:
				voice = self.v_count
			self.tts.Voice = self.tts.GetVoices().Item(voice)

		elif key == "by_attribute":
			self.gt_voice = self.tts.GetVoices(voice)
			if self.gt_voice.Count == 0:
				return 0
			self.tts.Voice = self.gt_voice.Item(0)

		elif key == "by_description":
			self.gt_voice = self.tts.GetVoices()
			for vd in self.gt_voice:
				if vd.GetDescription() == voice:
					self.tts.Voice = vd
					break
		else:
			self.tts.Voice = voice
		return self.GetVoice()

	#get an attribute of the current voice
	def GetAttribute(self, attr):
		if self.tts == None:
			return None

		return self.tts.Voice.GetAttribute(attr)

	#get the volume of the sapi object
	def GetVolume(self):
		if self.tts == None:
			return None

		return self.tts.Volume

	#set the volume
	def SetVolume(self, volume):
		if self.tts == None:
			return None

		volume = int(volume)
		if volume < 0:
			volume = 0
		if volume > 100:
			volume = 100
		self.tts.Volume = volume
		return self.tts.Volume

	#get the voice rate
	def GetRate(self):
		if self.tts == None:
			return None

		return self.tts.Rate

	#change the rate of the voice
	def SetRate(self, rate):
		if self.tts == None:
			return None

		rate = int(rate)
		if rate < -10:
			rate = -10
		if rate > 10:
			rate = 10
		self.tts.Rate = rate
		return self.tts.Rate

	#speak a text
	def Speak(self, text, flags = SVSFDefault):
		if self.tts == None:
			return None

		self.tts.Speak(text, flags)
		return 1

	#save the text as wave file
	def SpeakToFile(self, text, filepath, flags = SVSFlagsAsync):
		if self.tts == None:
			return None

		self.ObjFile = c_c.CreateObject("SAPI.SPFileStream")
		self.ObjFile.Format.Type = 39
		self.crntout = self.tts.AudioOutputStream
		outobj = self.ObjFile.Open(filepath, 3)
		self.tts.AudioOutputStream = self.ObjFile
		self.tts.Speak(text, flags)
		self.ObjFile.Close()
		self.tts.AudioOutputStream = self.crntout
		return 1

	#pause speech
	def Pause(self):
		if self.tts == None:
			return None

		return self.tts.Pause()

	#resume speech
	def Resume(self):
		if self.tts == None:
			return None

		return self.tts.Resume()

	#stop the speech
	def Stop(self):
		if self.tts == None:
			return None

		#get current voice settings
		crnt_vc = self.tts.Voice
		crnt_vlm = self.tts.Volume
		crnt_rt = self.tts.Rate

		#unload the spVoice object
		self.tts = None

		#recreate the SPVoice object
		self.tts = c_c.CreateObject("Sapi.SpVoice")

		#restore the old voice settings
		self.tts.Voice = crnt_vc
		self.tts.Volume = crnt_vlm
		self.tts.Rate = crnt_rt
		self.tts.AlertBoundary = 32

#get status
	def GetStatus(self, Property = STS_RunningState):
		if self.tts == None:
			return None

		return eval("self.tts.Status." + Property)

