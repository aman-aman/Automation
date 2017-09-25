#/*
#aman kumar jha
#*/



from gtts import gTTS
import os


text ='You have a new Notification...!!!'
language = 'en'
obj=gTTS(text=text, lang=language, slow=False)
obj.save("hello.mp3")
os.system("hello.mp3")