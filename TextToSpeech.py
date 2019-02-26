
#1st thing 1st you should get Google Text to Speech module with pip install gtts
#After that you can create following *.mp3 files for authentication
#Do this in IDLE

############################################################################################

>>> from gtts import gTTS
>>> import os
>>> tts = gTTS(text = "Say the Holly word!", lang="en-uk")
>>> tts.save("question.mp3")
>>> tts = gTTS(text = "Okay. You can pass now!", lang="en-uk")
>>> tts.save("success.mp3")
>>> tts = gTTS(text = "Oops, Sorry. You shall not pass. Try again later!", lang="en-uk")
>>> tts.save("fail.mp3") 
