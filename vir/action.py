from anyio import current_time
import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data= data.lower()


    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Liselkina")
        return "My name is Liselkina"

    elif "hello" in user_data or "Hey" in user_data:
        text_to_speech.text_to_speech("Hey! How can i help you")
        return "Hey! How can i help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning, How can I help you")
        return "Good morning, How can I help you"

    elif "time now" in user_data:
       current_time= datetime.datetime.now()
       Time= (str)(current_time)+"Hour:",(str)(current_time.minute)+"minute"
       text_to_speech.text_to_speech(Time)
       return Time

    elif "shutdown" in user_data:
       text_to_speech.text_to_speech("okay done")
       return "okay done"

    elif "youtube" in user_data:
       webbrowser.open("http://in.youtube.com/")
       text_to_speech.text_to_speech("Okay. The youtube is ready for you")
       return "Okay. The youtube is ready for you"

    elif "play music" in user_data:
       webbrowser.open("https://open.spotify.com/")
       text_to_speech.text_to_speech("Okay. The spotify is ready for you")
       return "Okay. The spotify is ready for you"

    elif "Open google" in user_data:
       webbrowser.open("https://www.google.com/")
       text_to_speech.text_to_speech("Okay. Google is ready for you")
       return "Okay. Google is ready for you"

    elif "weather" in user_data:
        ans=weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
    
    else:
        text_to_speech.text_to_speech("Sorry, Im not able to understand. Please try again")
        return "Sorry, Im not able to understand. Please try again"

