from logging import info
from gtts import gTTS


info("Initializing Application")
print("Initializing")
text = " welcome to buy me dot lk. Im your AI shopping assistant"

info("Initializing text to speech conversion")
print("Initializing text to speech conversion")
tts = gTTS(text, lang='en')
tts.save("converted_audio.mp3")
info("Successful text to speech conversion")
print("Successful text to speech conversion")
