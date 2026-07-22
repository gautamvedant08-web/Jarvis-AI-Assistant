import speech_recognition as sr
import webbrowser 
import pyttsx3
import music_library



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "a1ece36fd0b4a9eafc9967139977bfd"

def speak(text): 
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower(): 
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower(): 
        webbrowser.open("https://youtube.com") 

    elif "open chrome" in c.lower(): 
        webbrowser.open("https://chrome.com")

    elif "open facebook" in c.lower(): 
        webbrowser.open("https://facebook.com") 

    elif "open hotstar" in c.lower(): 
        webbrowser.open("https://hotstar.com")
    
    elif c.lower().startswith("play"): 
        songs = c.lower().split(" ")[1]
        link = music_library.music[songs]
        webbrowser.open(link)       
    # elif "news"in c.lower(): 
        # r = requests.get(" https://newsapi.org/v2/top-headlines?country=us&apiKey=da1ece36fd0b4a9eafc9967139977bfd")




if __name__ == "__main__": 
    speak("Initializing jarvis...")  
    # Listien for the wake word jarvi
    while True:
        r = sr.Recognizer()
   
        print("recognizing")

        try:
            with sr.Microphone() as source:
                print("Listining....!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word= r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yaa") 
                with sr.Microphone() as source: 
                    print("JArvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
 
        except Exception as e:
            print("Could not understand")
       




