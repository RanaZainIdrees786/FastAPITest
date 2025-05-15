import speech_recognition as sr
def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    while True:        
        # Use microphone as input
        with sr.Microphone() as source:
            print("🎤 Speak something...")
            recognizer.adjust_for_ambient_noise(source)  # Optional: better accuracy
            audio = recognizer.listen(source,phrase_time_limit=20)
            # audio = recognizer.record(source, duration=8)

            try:
                text = recognizer.recognize_google(audio)
                # Recognize speech using Google Speech Recognition
                print(f"📝 You said: {text}")
                if text == 'exit':
                    break
                return text
            except sr.UnknownValueError:
                print("❌ Sorry, I could not understand your speech.")
            except sr.RequestError:
                print("🚫 Speech Recognition service is unavailable.")

recognize_speech()