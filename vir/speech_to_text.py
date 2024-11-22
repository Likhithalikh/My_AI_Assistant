import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    try:
        voice_data= ""
        voice_data = r.recognize_google(audio)
        return voice_data

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("Sorry, there was a problem with the request.")

 