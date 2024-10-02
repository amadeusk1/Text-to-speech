from gtts import gTTS
import os

# Text to be converted to speech
text = input("Enter text that you want turned into speech: ")

# Language in which you want to convert
language = 'en'  # English

# Create a gTTS object
speech = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
speech.save("output.mp3")

#only works on some platforms)
os.system("start output.mp3")  # For Windows
# os.system("afplay output.mp3")  # For macOS
# os.system("mpg321 output.mp3")  # For Linux
