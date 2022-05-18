import pyttsx3

def generate_audio_from_os():
    engine = pyttsx3.init()
    text = "Welcome to the MedicalHub Fysical Score Screening. Which region of your body would you like to assess today? Squat down"
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        if index == 7 or index == 17 or index == 28 or index == 33 or index == 37:
            print(index)  # 7, 17, 28, 33, 37
            engine.setProperty("voice", voice.id)
            engine.say(text)
            engine.runAndWait()
            # engine.stop()
            engine.save_to_file(text, f"voice{index}.mp3")

